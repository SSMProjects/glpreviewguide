/*!
 * GLP1ReviewGuide.com consent manager (no dependencies)
 * - Opt-in for all non-essential cookies (health-related site: WA MHMDA / CT / NV / CPRA "sensitive" data)
 * - Honors Global Privacy Control (GPC) as an opt-out of sale/sharing/targeted ads
 * - Google Consent Mode v2 updates (pair with the "consent default" snippet in <head>)
 * - Blocks tagged scripts until the matching category is granted:
 *     <script type="text/plain" data-gr-consent="analytics" data-src="https://..."></script>
 *     <script type="text/plain" data-gr-consent="advertising"> ...inline pixel code... </script>
 * - Any element with [data-gr-open-consent] reopens the settings panel.
 * Public API: window.GRConsent.get() / .set({analytics:bool, advertising:bool}) / .open() / .optOutOfSale()
 */
(function () {
  "use strict";
  var COOKIE = "gr_consent";
  var VERSION = 1;               // bump to re-ask everyone after a policy change
  var DAYS = 365;
  var POLICY_URL = "/cookie-policy";
  var CHOICES_URL = "/your-privacy-choices";

  var gpc = navigator.globalPrivacyControl === true;

  function readCookie() {
    try {
      var m = document.cookie.match(new RegExp("(?:^|; )" + COOKIE + "=([^;]*)"));
      if (!m) return null;
      var v = JSON.parse(decodeURIComponent(m[1]));
      return v && v.v === VERSION ? v : null;
    } catch (e) { return null; }
  }
  function writeCookie(state) {
    try {
      var exp = new Date(Date.now() + DAYS * 864e5).toUTCString();
      document.cookie = COOKIE + "=" + encodeURIComponent(JSON.stringify(state)) +
        "; expires=" + exp + "; path=/; SameSite=Lax" + (location.protocol === "https:" ? "; Secure" : "");
    } catch (e) { /* storage blocked: banner will show again next visit */ }
  }

  var state = readCookie();
  var loaded = { analytics: false, advertising: false };

  function current() {
    var s = state || { analytics: false, advertising: false };
    // GPC always wins for advertising (sale/sharing/targeted ads)
    return { analytics: !!s.analytics, advertising: gpc ? false : !!s.advertising, decided: !!state, gpc: gpc, saleOptOut: gpc || !!(state && state.saleOptOut) };
  }

  function gtagUpdate(c) {
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    gtag("consent", "update", {
      analytics_storage: c.analytics ? "granted" : "denied",
      ad_storage: c.advertising ? "granted" : "denied",
      ad_user_data: c.advertising ? "granted" : "denied",
      ad_personalization: c.advertising ? "granted" : "denied"
    });
  }

  function activate(category) {
    if (loaded[category]) return;
    loaded[category] = true;
    var nodes = document.querySelectorAll('script[type="text/plain"][data-gr-consent="' + category + '"]');
    Array.prototype.forEach.call(nodes, function (old) {
      var s = document.createElement("script");
      for (var i = 0; i < old.attributes.length; i++) {
        var a = old.attributes[i];
        if (a.name !== "type" && a.name !== "data-src" && a.name !== "data-gr-consent") s.setAttribute(a.name, a.value);
      }
      if (old.getAttribute("data-src")) { s.src = old.getAttribute("data-src"); s.async = true; }
      else s.text = old.text;
      old.parentNode.replaceChild(s, old);
    });
  }

  function apply(prev) {
    var c = current();
    gtagUpdate(c);
    if (c.analytics) activate("analytics");
    if (c.advertising) activate("advertising");
    // If something was revoked after its scripts already ran, reload so they stop.
    if (prev && ((prev.analytics && !c.analytics && loaded.analytics) || (prev.advertising && !c.advertising && loaded.advertising))) {
      setTimeout(function () { location.reload(); }, 300);
    }
    try { document.dispatchEvent(new CustomEvent("gr:consent", { detail: c })); } catch (e) {}
    syncUI();
  }

  function save(choice) {
    var prev = current();
    state = {
      v: VERSION,
      analytics: !!choice.analytics,
      advertising: gpc ? false : !!choice.advertising,
      saleOptOut: gpc || !choice.advertising || !!choice.saleOptOut,
      gpc: gpc,
      ts: new Date().toISOString()
    };
    writeCookie(state);
    hide();
    apply(prev);
  }

  /* ---------- UI ---------- */
  var el, prefs, aBox, adBox;
  function build() {
    el = document.createElement("section");
    el.className = "gr-cc";
    el.setAttribute("role", "dialog");
    el.setAttribute("aria-modal", "false");
    el.setAttribute("aria-labelledby", "gr-cc-title");
    el.hidden = true;
    el.innerHTML =
      '<h2 id="gr-cc-title">Your privacy choices</h2>' +
      '<p>We use essential cookies to run this site. With your permission we also use analytics cookies to see which pages help people, and advertising cookies to measure our ads. ' +
      'Because this site covers a health topic, we keep these <strong>off unless you turn them on</strong>. See our <a href="' + POLICY_URL + '">Cookie Policy</a> and <a href="/consumer-health-data-privacy">Consumer Health Data Privacy Policy</a>.</p>' +
      (gpc ? '<p class="gr-note">We detected a Global Privacy Control signal from your browser, so advertising cookies and any sale or sharing of your data are turned off.</p>' : '') +
      '<div class="gr-cc-prefs" hidden>' +
        '<div class="switch_row"><div><b>Essential</b><p>Needed for security, load balancing and remembering these choices. Always on.</p></div><label class="switch"><input type="checkbox" checked disabled aria-label="Essential cookies, always on"><span></span></label></div>' +
        '<div class="switch_row"><div><b>Analytics</b><p>Aggregate traffic measurement (for example Google Analytics). Never used to build a health profile.</p></div><label class="switch"><input type="checkbox" data-k="analytics" aria-label="Analytics cookies"><span></span></label></div>' +
        '<div class="switch_row"><div><b>Advertising</b><p>Lets ad partners (Google Ads, Taboola, Outbrain) measure which ads led to a visit. Turning this on may count as "sharing" under some state laws.</p></div><label class="switch"><input type="checkbox" data-k="advertising" aria-label="Advertising cookies"' + (gpc ? " disabled" : "") + '><span></span></label></div>' +
      '</div>' +
      '<div class="gr-cc-actions">' +
        '<button type="button" class="gr-primary" data-act="reject">Reject non-essential</button>' +
        '<button type="button" class="gr-primary" data-act="accept">Accept all</button>' +
        '<button type="button" data-act="custom">Customize</button>' +
      '</div>';
    document.body.appendChild(el);
    prefs = el.querySelector(".gr-cc-prefs");
    aBox = el.querySelector('[data-k="analytics"]');
    adBox = el.querySelector('[data-k="advertising"]');
    el.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-act]");
      if (!b) return;
      var act = b.getAttribute("data-act");
      if (act === "accept") save({ analytics: true, advertising: true });
      else if (act === "reject") save({ analytics: false, advertising: false });
      else if (act === "custom") { prefs.hidden = false; b.setAttribute("data-act", "save"); b.textContent = "Save my choices"; b.classList.add("gr-primary"); aBox.focus(); }
      else if (act === "save") save({ analytics: aBox.checked, advertising: adBox.checked });
    });
    el.addEventListener("keydown", function (e) { if (e.key === "Escape" && state) hide(); });
  }
  function syncUI() {
    var c = current();
    if (aBox) { aBox.checked = c.analytics; adBox.checked = c.advertising; }
    // Keep any on-page controls (e.g. /your-privacy-choices) in sync
    Array.prototype.forEach.call(document.querySelectorAll("[data-gr-bind]"), function (i) {
      var k = i.getAttribute("data-gr-bind");
      if (k === "saleOptOut") i.checked = c.saleOptOut;
      else i.checked = !!c[k];
      if (k !== "analytics" && gpc) i.disabled = true;
    });
  }
  function show(expand) {
    if (!el) build();
    syncUI();
    el.hidden = false;
    document.body.classList.add("has-banner");
    if (expand) { prefs.hidden = false; var b = el.querySelector('[data-act="custom"]'); if (b) { b.setAttribute("data-act", "save"); b.textContent = "Save my choices"; b.classList.add("gr-primary"); } }
    var first = el.querySelector("button"); if (first && expand) first.focus();
  }
  function hide() { if (el) el.hidden = true; document.body.classList.remove("has-banner"); }

  function init() {
    // GPC visitors with no saved choice: record the opt-out silently but still ask about analytics
    apply(null);
    if (!state) show(false);
    document.addEventListener("click", function (e) {
      var t = e.target.closest("[data-gr-open-consent]");
      if (t) { e.preventDefault(); show(true); }
    });
  }

  window.GRConsent = {
    get: current,
    set: function (c) { save({ analytics: c.analytics, advertising: c.advertising, saleOptOut: c.saleOptOut }); },
    open: function () { show(true); },
    optOutOfSale: function () { var c = current(); save({ analytics: c.analytics, advertising: false, saleOptOut: true }); },
    gpc: gpc,
    choicesUrl: CHOICES_URL
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
