import { createHash, timingSafeEqual } from "node:crypto";

// No credentials belong in this public source file.
// Forwarding is OFF unless REDDIT_FORWARDING_ENABLED is exactly "true".
const reply = (status, data) => new Response(JSON.stringify(data), {
  status,
  headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
});

function matchesSecret(received, expected) {
  if (!received || !expected) return false;
  const a = Buffer.from(received);
  const b = Buffer.from(expected);
  return a.length === b.length && timingSafeEqual(a, b);
}

export function createHandler(env, fetcher = fetch) {
return async function handler(request) {
  if (request.method !== "GET") return reply(405, { error: "Use GET" });
  const params = new URL(request.url).searchParams;

  // Safe deployment check: never sends an event or returns credentials.
  if (params.size === 0) return reply(200, { status: "receiver_ready" });

  const secret = env("EVERFLOW_POSTBACK_SECRET");
  if (!secret) return reply(503, { error: "Postback secret is not configured" });
  if (!matchesSecret(params.get("key"), secret)) {
    return reply(401, { error: "Unauthorized" });
  }

  // Static test marker only; no real conversion information is returned or logged.
  if (params.get("test") === "1") {
    return reply(200, { status: "test_received", forwarded_to_reddit: false });
  }

  const redditTest = params.get("test") === "reddit";
  if (!redditTest && env("REDDIT_FORWARDING_ENABLED") !== "true") {
    return reply(503, { error: "Live forwarding is disabled" });
  }
  // Set these only after verifying the offer and the event represent a paid sale.
  const expectedOffer = env("EVERFLOW_RO_OFFER_ID");
  const expectedEvent = env("EVERFLOW_RO_SALE_EVENT_ID");
  if (!expectedOffer || !expectedEvent) {
    return reply(503, { error: "Verified sale mapping is not configured" });
  }
  if (params.get("offer_id") !== expectedOffer || params.get("event_id") !== expectedEvent) {
    return reply(422, { error: "Offer or event does not match the verified sale mapping" });
  }

  const conversionId = params.get("conversion_id") || "";
  const clickId = params.get("click_id") || "";
  const time = params.get("event_at_ms") || "";
  if (redditTest && clickId !== "rs_test_001") {
    return reply(422, { error: "Reddit testing accepts only rs_test_001" });
  }
  if (!redditTest && !clickId) {
    return reply(200, { status: "skipped_no_reddit_click", forwarded_to_reddit: false });
  }
  if (!redditTest && /^(rs_test_|reddit_test_)/i.test(clickId)) {
    return reply(200, { status: "skipped_test_marker", forwarded_to_reddit: false });
  }
  if (!/^[a-zA-Z0-9_-]{1,128}$/.test(conversionId) ||
      !clickId || clickId.length > 1024 || /[\s{}]/.test(clickId) ||
      !/^\d{13}$/.test(time)) {
    return reply(422, { error: "Valid conversion ID, Reddit click ID and Unix millisecond time are required" });
  }
  const eventAt = Number(time);
  const age = Date.now() - eventAt;
  if (age < -300000 || age > 7 * 86400000) {
    return reply(422, { error: "Conversion time is outside the accepted window" });
  }
  const pixel = env("REDDIT_PIXEL_ID") || "";
  const token = env("REDDIT_CAPI_TOKEN") || "";
  if (!/^a2_[a-zA-Z0-9]+$/.test(pixel) || !token) {
    return reply(503, { error: "Reddit credentials are not configured" });
  }
  const testId = env("REDDIT_TEST_ID") || "";
  if (redditTest && !testId) {
    return reply(503, { error: "Reddit Event Testing ID is not configured" });
  }
  const dedupId = createHash("sha256")
    .update(`everflow:${redditTest ? "test" : "live"}:${expectedOffer}:${expectedEvent}:${conversionId}`)
    .digest("hex");
  const event = {
    event_at: eventAt,
    action_source: "WEBSITE",
    type: { tracking_type: "PURCHASE" },
    metadata: { conversion_id: redditTest ? `rs_test_001_${dedupId}` : dedupId },
  };
  // The synthetic marker is not a real Reddit click ID and cannot attribute a sale.
  // In Event Testing it is identified in conversion_id instead of a match key.
  if (!redditTest) event.click_id = clickId;
  const data = { events: [event] };
  if (redditTest) data.test_id = testId;
  try {
    const result = await fetcher(`https://ads-api.reddit.com/api/v3/pixels/${pixel}/conversion_events`, {
      method: "POST",
      headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
      signal: AbortSignal.timeout(8000),
      body: JSON.stringify({ data }),
    });
    const body = await result.json().catch(() => null);
    if (!result.ok || !body?.data?.message?.includes("Successfully processed 1 conversion events")) {
      return reply(502, { error: "Reddit did not confirm acceptance", reddit_http_status: result.status });
    }
    return reply(200, { status: redditTest ? "accepted_by_reddit_test" : "accepted_by_reddit" });
  } catch {
    // Never log request URLs, secrets, click IDs, or upstream response bodies.
    return reply(502, { error: "Reddit request failed or timed out" });
  }
}
;
}

export default createHandler((name) => {
  if (typeof Netlify !== "undefined") return Netlify.env.get(name);
  if (typeof process !== "undefined") return process.env[name];
  return undefined;
});
