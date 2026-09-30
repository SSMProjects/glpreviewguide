SITE = "GLP1ReviewGuide.com"
DOMAIN = "glp1reviewguide.com"
EMAIL = "hello@glp1reviewguide.com"
UPDATED = "September 2026"

def page(fname, title, desc, body, canonical=""):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://{DOMAIN}/{canonical or fname}">
<link rel="icon" href="images/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<!-- Consent: Google Consent Mode v2 defaults (keep ABOVE any Google tag), banner styles + script -->
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',functionality_storage:'granted',security_storage:'granted',wait_for_update:500}});
gtag('set','ads_data_redaction',true);gtag('set','url_passthrough',true);
</script>
<link rel="stylesheet" href="consent.css">
<script src="consent.js" defer></script>
<!-- Non-essential tags must be blocked until consent, e.g.:
<script type="text/plain" data-gr-consent="analytics" data-src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
<script type="text/plain" data-gr-consent="advertising">/* Taboola / Outbrain / Google Ads pixel */</script> -->
</head>
<body>
<div class="adbar">Advertising disclosure: we may earn a commission when you visit providers from this page. This does not affect our scores. <a href="disclosure.html">Learn more</a></div>
<header class="site"><div class="wrap">
  <a class="brand" href="index.html"><img src="images/logo.svg" alt="" width="32" height="32"><span>GLP1Review<b style="color:#0000FF">Guide</b><small style="font-size:13px;font-weight:500;color:#615B6B">.com</small></span></a>
  <nav class="main" aria-label="Main">
    <a href="index.html">Best GLP-1 programs</a>
    <a href="review-pallas-health.html">Reviews</a>
    <a href="about.html">About</a>
  </nav>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap">
  <div class="cols">
    <div><h4>{SITE}</h4><p>Independent comparisons of online weight-care programs that offer GLP-1 medications, so you can arrive at your doctor's appointment with better questions.</p></div>
    <div><h4>Site</h4><ul><li><a href="index.html">Best GLP-1 programs</a></li><li><a href="index.html#method">How we score</a></li><li><a href="about.html">About us</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
    <div><h4>Legal</h4><ul><li><a href="disclosure.html">Advertising disclosure</a></li><li><a href="disclosure.html#medical">Medical disclaimer</a></li><li><a href="privacy.html">Privacy policy</a></li><li><a href="consumer-health-data-privacy.html">Consumer health data privacy</a></li><li><a href="cookie-policy.html">Cookie policy</a></li><li><a href="terms.html">Terms of use</a></li><li><a class="pc" href="your-privacy-choices.html"><img src="images/privacy-choices.svg" alt="" width="30" height="14">Your Privacy Choices / Do Not Sell or Share My Personal Information</a></li><li><button type="button" class="linklike" data-gr-open-consent>Cookie settings</button></li></ul></div>
  </div>
  <div class="legal">
    <p>The content on this site is for general information only and is not medical advice. GLP-1 medications are available by prescription only and are not right for everyone. Talk to a licensed healthcare provider about the benefits and risks, including serious side effects, before starting any medication. Individual results vary.</p>
    <p>{SITE} is an independent publisher. We are not a healthcare provider or pharmacy and do not sell, prescribe or dispense medications. Product names and trademarks belong to their respective owners and are used for identification only.</p>
    <p>&copy; 2026 {SITE}. All rights reserved.</p>
  </div>
</div></footer>
</body>
</html>'''
    open(fname, "w").write(html)

# ---------- Provider data (checked September 2026; re-verify before publishing) ----------
P = [
 dict(k="a", name="WeightWatchers Med+", short="WW Med+", flag="Best overall", total="9.5",
  summary="Obesity medicine specialists, one-on-one dietitian support and a full nutrition and activity app, with brand-name GLP-1s for people who qualify.",
  price="Membership $74/mo (12-month plan) or $149/mo month to month; medication from $199/mo",
  price_short="$74/mo + medication", meds="Wegovy (pill and pen), Zepbound, Foundayo, Saxenda", ins="HSA/FSA accepted", visit="Obesity medicine specialists",
  compounded="No", cancel="12-month plans are billed for the remaining months if you cancel early",
  scores=[("Clinical care",97),("Medication access",95),("Price transparency",86),("Ongoing support",98)],
  pros=["Care from obesity medicine specialists","One-on-one registered dietitian and a GLP-1 member community","App includes meal tracking, recipes, sleep tracking and strength-training videos","Accepts HSA/FSA","Brand-name, FDA-approved medications only"],
  cons=["Cancelling a 12-month plan early still bills the remaining months","Medication pricing is harder to find on the website"],
  care="Prescribing clinicians specialize in obesity medicine. Members who qualify for medication also get one-on-one sessions with a registered dietitian and access to a support community for people taking GLP-1s.",
  pricing="Med+ membership is $74 a month on a 12-month commitment, or $149 a month billed month to month. Medication is billed separately, starting around $199 a month for the starting dose of an oral GLP-1 and rising with dose.",
  bestfor="People who want medication paired with structured nutrition coaching and long-term habit support. If you want to avoid a long commitment, compare the month-to-month price first."),
 dict(k="b", name="Ro", short="Ro", flag="Best for insurance help", total="9.2",
  summary="Brand-name GLP-1s only, unlimited messaging with a provider, and an insurance concierge that checks your coverage for you.",
  price="Membership $149/mo ($39 first month; about $74/mo if prepaid annually); medication from $149/mo",
  price_short="$149/mo + medication", meds="Zepbound, Wegovy (pill and pen), Foundayo, Saxenda", ins="Insurance concierge checks coverage", visit="Chat-based, unlimited messaging",
  compounded="No", cancel="Cancel up to 48 hours before renewal; no long-term contract required",
  scores=[("Clinical care",90),("Medication access",95),("Price transparency",91),("Ongoing support",88)],
  pros=["Insurance concierge checks your GLP-1 coverage","Unlimited messaging with your provider","Cancel up to 48 hours before renewal, with no long-term contract","Brand-name, FDA-approved medications only"],
  cons=["Wegovy pill, Foundayo and the Zepbound KwikPen are cash-pay only","Care is mostly by chat rather than video","Doesn't accept HSA/FSA"],
  care="Care runs through a chat-based system with unlimited messaging to a licensed provider. There's no required video visit, which is convenient but less personal than a face-to-face appointment.",
  pricing="The Ro Body membership costs $39 for the first month and $149 a month after that, or roughly $74 a month when prepaid annually. Medication is billed separately, starting around $149 a month for the starting dose of an oral GLP-1.",
  bestfor="People with insurance who want help finding out whether their plan covers a GLP-1, and who are comfortable handling care by message."),
 dict(k="c", name="PlushCare", short="PlushCare", flag="Best for doctor visits", total="8.9",
  summary="Video visits with board-certified physicians licensed in all 50 states, with an optional low-cost membership and prescriptions sent to your pharmacy.",
  price="Visits $129 each; optional membership $19.99/mo; Wegovy from $199/mo",
  price_short="$129/visit", meds="Wegovy (pen), Zepbound, Saxenda; also Contrave and Xenical", ins="Takes insurance; HSA/FSA for visits", visit="Video visits with physicians",
  compounded="Only during FDA drug shortages", cancel="Membership is optional",
  scores=[("Clinical care",95),("Medication access",86),("Price transparency",88),("Ongoing support",82)],
  pros=["Board-certified physicians licensed in all 50 states","Real video appointments, not just a questionnaire","Membership is optional and low cost","Offers non-GLP-1 weight-loss medications too"],
  cons=["Each visit costs $129 before insurance","Prescriptions go to a pharmacy instead of shipping to your home","Less built-in coaching than dedicated weight-loss programs"],
  care="PlushCare is a general telehealth practice. You book a video visit with a board-certified physician, who can prescribe weight-loss medication if it's appropriate and send it to your pharmacy.",
  pricing="Visits cost $129 each, and insurance may cover them. The optional membership is $19.99 a month. Medication is paid separately at the pharmacy; Wegovy starts around $199 a month.",
  bestfor="People who want a real doctor's appointment and plan to use insurance, and who don't need an app or coaching program."),
 dict(k="d", name="Hims & Hers", short="Hims & Hers", flag="Best for medication choice", total="8.5",
  summary="A familiar wellness brand offering several brand-name oral and injectable GLP-1s, with unlimited provider messaging and lifestyle guidance.",
  price="Membership $149/mo ($39 first month); medication from $149/mo",
  price_short="$149/mo + medication", meds="Wegovy (pill and pen), Foundayo, Zepbound (vial and pen)", ins="No HSA/FSA", visit="Online intake + unlimited messaging",
  compounded="No (stopped in 2026)", cancel="Monthly membership",
  scores=[("Clinical care",86),("Medication access",94),("Price transparency",82),("Ongoing support",85)],
  pros=["Wide choice of brand-name oral and injectable GLP-1s","Unlimited messaging with a provider","Membership includes exercise, nutrition and meditation guidance"],
  cons=["GLP-1s aren't available in a few states","Some users report trouble cancelling recurring shipments","In July 2026 the FTC sued the company over billing and data-sharing practices; the company denies the claims"],
  care="You complete an online intake form, and a medical provider decides whether a prescription is appropriate. Members get unlimited messaging with a provider after that.",
  pricing="The weight-loss membership costs $39 for the first month, then $149 a month. Medication is billed separately, starting around $149 a month for an oral GLP-1 starting dose.",
  bestfor="People who want to choose between several brand-name pills and pens. Read the cancellation steps before you sign up."),
 dict(k="e", name="Mochi Health", short="Mochi", flag="Best website experience", total="8.1",
  summary="An easy-to-use platform with 24/7 support that offers both brand-name and lower-cost compounded GLP-1s.",
  price="Membership $79/mo; compounded semaglutide from $60 (starting dose); brand-name costs more",
  price_short="$79/mo + medication", meds="Wegovy, Zepbound, Foundayo; compounded semaglutide and tirzepatide", ins="HSA/FSA accepted", visit="Online + provider messaging",
  compounded="Yes (not FDA-approved)", cancel="Monthly membership",
  scores=[("Clinical care",84),("Medication access",86),("Price transparency",84),("Ongoing support",88)],
  pros=["Easy-to-use website with 24/7 patient support","Direct messaging with your provider","Accepts HSA/FSA","Has published safety test results for recent compounded batches"],
  cons=["Compounded medications are not FDA-approved","A relatively high number of Better Business Bureau complaints","Extra services require a Wellness Plus plan and qualifying insurance"],
  care="Membership is required for a prescription and includes 24/7 patient support and direct messaging with your provider.",
  pricing="Membership is $79 a month. Compounded semaglutide starts at $60 and compounded tirzepatide at $90 for the starting dose, rising with dose. Brand-name medications cost more.",
  bestfor="Budget-focused patients who understand the trade-offs of compounded medication, or who want brand-name options with a lower membership fee."),
]

# ----- Offers keyed by original key; final order is set below -----
OFFERS={'a': ('$74/mo', '$25', 'first month of membership', 'Then $74/mo on a 12-month plan. Medication from $199/mo.', 'Brand-name GLP-1s only'), 'b': ('$149/mo', '$39', 'first month of membership', 'Then $149/mo. Medication from $149/mo.', 'Insurance concierge included'), 'c': ('', '$129', 'per video visit', 'Optional membership $19.99/mo. Wegovy from $199/mo.', 'Prescription sent to your pharmacy'), 'd': ('$149/mo', '$39', 'first month of membership', 'Then $149/mo. Medication from $149/mo.', 'Unlimited provider messaging'), 'e': ('', '$79', 'per month membership', 'Compounded semaglutide from $60. Brand-name costs more.', '24/7 patient support')}
for _p in P: _p["was"],_p["now"],_p["now_note"],_p["then"],_p["perk"]=OFFERS[_p["k"]]

PALLAS = dict(name="Pallas Health", short="Pallas", flag="Best overall value",
  summary="All-in GLP-1 pricing with no membership fee, the same price at every dose, and both compounded and FDA-approved brand-name options.",
  price="Compounded semaglutide $139 first month, then $597 every 12 weeks (about $199/mo) or $159/mo on the annual plan; compounded tirzepatide from $179",
  price_short="From $139 first month", meds="Compounded semaglutide and tirzepatide; Wegovy, Zepbound, Ozempic, Mounjaro (cash-pay)",
  ins="HSA/FSA eligible; no insurance", visit="100% online; 1 video visit required in 7 states + DC",
  compounded="Yes (not FDA-approved), plus brand-name options", cancel="Cancel or pause anytime with no cancellation fees",
  scores=[("Clinical care",92),("Medication access",97),("Price transparency",97),("Ongoing support",93)],
  pros=["No membership fee: clinician visits, follow-ups and messaging are included in the price",
        "Compounded plans cost the same at every dose, including step-ups",
        "Full refund if a clinician decides treatment isn't right for you",
        "Offers both compounded GLP-1s and FDA-approved brand-name medications",
        "LegitScript certified; medication ships free from US-licensed pharmacies",
        "HSA/FSA eligible, and you can cancel or pause anytime with no fees"],
  cons=["Compounded medications are not FDA-approved",
        "Brand-name medications are cash-pay only and expensive (Wegovy $1,349/mo)",
        "Launched in 2026, so there's little independent customer feedback yet",
        "Doesn't accept insurance"],
  care="Intake, clinician review, check-ins and refills all happen online, and review is often same-day. Prescriptions are written by US-licensed clinicians through an affiliated medical group, and the medical team is led by a physician board-certified in obesity medicine. Most states need no video visit; 7 states plus Washington, D.C. require one to start.",
  pricing="There's no membership fee. Compounded semaglutide is $139 for the first month, then $597 every 12 weeks (about $199 a month) or about $159 a month on the annual plan. Compounded tirzepatide is $179 for the first month, then about $299 a month, or $259 a month on the annual plan. Nothing is charged until a clinician prescribes, and you're refunded in full if they decide treatment isn't right for you. Brand-name medications are cash-pay and billed monthly.",
  bestfor="People paying out of pocket who want one predictable monthly price, including dose increases, and the choice between compounded and brand-name medication. If you want to use insurance, or prefer a company with a longer track record, look at #2 and #3.",
  was="$199/mo", now="$139", now_note="first month (compounded semaglutide)",
  then="Then about $199/mo, or $159/mo on the annual plan. Refunded if not prescribed.", perk="No membership fee + free shipping")

DIRECTMEDS = dict(name="DirectMeds", short="DirectMeds", flag="Best all-inclusive monthly price",
  url="https://directmeds.com/dm-offers-stc/?oid=12&amp;uid=61&amp;affid=1020&amp;sub1={affiliate_id}&amp;sub2={transaction_id}&amp;sub3={sub1}&amp;sub4={sub2}&amp;sub5={sub3}",
  summary="One monthly price that includes the medication, doctor visits, supplies and shipping, with compounded semaglutide or tirzepatide as an injection or under-the-tongue drops.",
  price="Compounded semaglutide $147 first month ($150 off), then $297/mo; compounded tirzepatide $399/mo. Medication, doctor visits, supplies and shipping included.",
  price_short="From $147 first month", meds="Compounded semaglutide and tirzepatide (injection or sublingual drops)",
  ins="No insurance needed (cash-pay)", visit="Online intake; doctor review within 24 hours",
  compounded="Yes (not FDA-approved)", cancel="Confirm cancellation terms at checkout",
  scores=[("Clinical care",92),("Medication access",90),("Price transparency",97),("Ongoing support",90)],
  pros=["One monthly price covers medication, doctor visits, supplies and shipping, with no membership fee",
        "$150 off the first month: compounded semaglutide is $147 to start",
        "Choose injections or sublingual (under-the-tongue) drops",
        "A licensed doctor reviews your intake within 24 hours",
        "Full refund if your prescription isn't approved",
        "LegitScript certified; ships from U.S.-based 503A compounding pharmacies in 1–2 days"],
  cons=["Compounded medications are not FDA-approved",
        "No brand-name options such as Wegovy or Zepbound",
        "After the first month, semaglutide is $297/mo and tirzepatide $399/mo, more than some programs on this list",
        "There's less research on sublingual drops than on injections",
        "Not available in Mississippi or Louisiana; doesn't take insurance"],
  care="You complete a 5-minute health qualifier, choose a medication and pay for the first month, then finish a medical intake in the patient portal. A licensed doctor reviews it within 24 hours and decides whether a prescription is appropriate. Doctor visits are included in the price, and support is available by phone (888-696-7176) and email.",
  pricing="Compounded semaglutide is $297 a month and compounded tirzepatide $399 a month. That price includes the medication, doctor visits, supplies and shipping, with no separate membership fee. New patients get $150 off the first month, so semaglutide starts at $147. If your prescription isn't approved, you get a full refund.",
  bestfor="People paying out of pocket who want one all-inclusive price, fast doctor review and quick delivery, and who are comfortable with compounded medication. If you want brand-name drugs or to use insurance, compare Ro, WeightWatchers Med+ or PlushCare.",
  was="$297/mo", now="$147", now_note="first month (compounded semaglutide, $150 off)",
  then="Then $297/mo; tirzepatide $399/mo. Full refund if not approved.", perk="Doctor visits, supplies + shipping included")

# DirectMeds is a paid featured placement at #1 (disclosed on the page). Its score is calculated the same way as everyone else's.
P = [DIRECTMEDS, PALLAS] + [p for p in P if p["name"] not in ("Mochi Health", "Hims & Hers")]
W=[.30,.25,.25,.20]
for idx,_p in enumerate(P):
    _p["k"]="abcde"[idx]
    _p["total"]=f'{sum(w*s for w,(_,s) in zip(W,_p["scores"]))/10:.1f}'
SLUGS={"DirectMeds":"directmeds","Pallas Health":"pallas-health","WeightWatchers Med+":"weightwatchers-med-plus","Ro":"ro","PlushCare":"plushcare","Hims & Hers":"hims-and-hers"}
for _p in P: _p["slug"]=SLUGS[_p["name"]]
P[2]["flag"]="Best for nutrition coaching"

def bars(s):
    return "".join(f'<div class="bar"><span>{n}<em>{v/10:.1f}</em></span><i><b style="width:{v}%"></b></i></div>' for n,v in s)

def pick(i,p):
    top = " top" if i==1 else ""
    return f'''
<article class="pick{top}" id="provider-{p["k"]}">
  <div class="pick-flag">{p["flag"]}</div>
  <div class="pick-body">
    <div class="pick-logo">
      <span class="num" aria-label="Rank {i}">{i}</span>
      <img src="images/provider-{p["slug"]}.svg" alt="{p["name"]} logo" width="160" height="80">
      <a href="review-{p["slug"]}.html">Read full review</a>
    </div>
    <div>
      <h3>{p["name"]}</h3>
      <p class="summary">{p["summary"]}</p>
      <div class="proscons">
        <div><h4>What we like</h4><ul>{"".join(f"<li>{x}</li>" for x in p["pros"])}</ul></div>
        <div><h4>Things to know</h4><ul>{"".join(f"<li>{x}</li>" for x in p["cons"])}</ul></div>
      </div>
    </div>
    <div class="score">
      <div class="score-total">{p["total"]}<small> / 10 our score</small></div>
      {bars(p["scores"])}
      <a class="btn" href="{link(p)}" rel="sponsored nofollow noopener" target="_blank">Visit {p["name"]}</a>
      <p class="fine">{p["price"]}. Prescription requires a medical consultation.</p>
    </div>
  </div>
</article>'''

rows = "".join(f'<tr><td class="rank">{i}</td><td><strong>{p["name"]}</strong><br><span class="fine">{p["flag"]}</span></td><td>{p["price_short"]}</td><td>{p["meds"]}</td><td>{p["ins"]}</td><td>{p["visit"]}</td><td><strong>{p["total"]}</strong></td><td><a href="#provider-{p["k"]}">Details</a></td></tr>' for i,p in enumerate(P,1))

AUTHOR = f'''<div class="byline"><span class="avatar" aria-hidden="true"></span>
<span>Written by <strong>[Author Name]</strong>, health editor. Medically reviewed by <strong>[Reviewer Name, MD]</strong>. Updated {UPDATED}.</span></div>'''

FAQ = [
("What are GLP-1 medications?","GLP-1 receptor agonists are prescription medications that mimic a hormone involved in appetite and blood sugar regulation. Some are FDA-approved for chronic weight management in adults who meet specific criteria, and others are approved for type 2 diabetes. Only a licensed clinician can decide whether one is appropriate for you."),
("Do these programs guarantee a prescription?","No. Every provider on this list requires a medical evaluation, and a clinician may decide a GLP-1 medication is not right for you. Reputable programs will tell you that up front."),
("What side effects should I know about?","Commonly reported side effects include nausea, vomiting, diarrhea and constipation. Serious risks can include pancreatitis, gallbladder problems and, in animal studies, thyroid C-cell tumors. Review the full prescribing information and discuss your health history with a clinician."),
("Are compounded versions the same as brand-name medications?","No. Compounded drugs are not FDA-approved, and the FDA has restricted routine compounding of semaglutide and tirzepatide now that the brand-name versions are no longer in shortage. Ask any provider exactly what medication and pharmacy they use."),
("Will insurance cover a GLP-1 medication?","Coverage varies widely by plan and diagnosis. Some programs help check your benefits or file prior authorization requests, but approval is never guaranteed."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in FAQ)
faq_ld = ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q,a) for q,a in FAQ)

# ---------- index.html (homepage layout) ----------
import math
def ring(score, size=96, stroke=9, color="#0000FF"):
    r=(size-stroke)/2; c=2*math.pi*r; off=c*(1-float(score)/10)
    return f"""<svg class="ring" viewBox="0 0 {size} {size}" width="{size}" height="{size}" role="img" aria-label="Score {score} out of 10">
<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="#E6E6FF" stroke-width="{stroke}"/>
<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-dasharray="{c:.1f}" stroke-dashoffset="{off:.1f}" transform="rotate(-90 {size/2} {size/2})"/>
<text x="50%" y="50%" dominant-baseline="central" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-size="{size*0.3:.0f}" font-weight="700" fill="#1F1B2E">{score}</text></svg>"""

REL='rel="sponsored nofollow noopener" target="_blank"'
def link(p): return p.get("url") or f'https://AFFILIATE-LINK-{p["k"].upper()}'

def card(i,p):
    top=i==1
    crit="".join(f'<li><span>{n}</span><i><b style="width:{v}%"></b></i><em>{v/10:.1f}</em></li>' for n,v in p["scores"])
    was=f'<s>{p["was"]}</s>' if p["was"] else ""
    return f"""
<article class="pick{' pick_top' if top else ''}" id="pick-{i}">
 <header class="pick_head">
  <span class="pick_rank">{'<i class="fa-solid fa-crown"></i>' if top else ''}#{i}</span>
  <div class="pick_id">
   <p class="pick_flag">{'Featured partner · ' if top else ''}{p["flag"]}</p>
   <h2>{p["name"]}</h2>
   <p class="pick_sum">{p["summary"]}</p>
  </div>
  <div class="pick_ring">{ring(p["total"], 96, 9, "#0000FF" if top else "#0000FF")}<span>overall</span></div>
 </header>
 <div class="pick_body">
  <a class="pick_logo" href="{link(p)}" {REL}><img src="images/provider-{p["slug"]}.svg" alt="{p["name"]}" width="160" height="80"></a>
  <div class="pick_lists">
   <div><h3>Why it stands out</h3><ul class="plus">{"".join(f"<li>{x}</li>" for x in p["pros"])}</ul></div>
   <div><h3>Worth knowing</h3><ul class="minus">{"".join(f"<li>{x}</li>" for x in p["cons"])}</ul></div>
  </div>
  <ul class="pick_crit" aria-label="Score breakdown">{crit}</ul>
 </div>
 <footer class="pick_foot">
  <div class="pick_price"><span class="pp_label">Starting price</span><span class="pp_now">{was}{p["now"]}</span><span class="pp_note">{p["now_note"]}</span></div>
  <p class="pick_then">{p["then"]}<br><strong>{p["perk"]}</strong></p>
  <div class="pick_cta"><a class="cta" href="{link(p)}" {REL}>See if I qualify</a><a class="more" href="review-{p["slug"]}.html">Full review</a></div>
 </footer>
</article>"""

top=P[0]
by={p["name"]:p for p in P}
quiz_targets = {name:{"rank":i+1,"id":f"pick-{i+1}","name":name} for i,(name) in enumerate([p["name"] for p in P])}
import json
QT=json.dumps(quiz_targets)

index_html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="robots" content="index, follow">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Best Online GLP-1 Weight-Loss Programs (2026): Top 5 Compared | {SITE}</title>
<meta name="description" content="We compared popular online GLP-1 weight-loss programs on medical care, medications, true monthly cost and support. See the top 5 and find the one that fits you.">
<link rel="canonical" href="https://{DOMAIN}/">
<link rel="icon" href="images/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="vendor/fontawesome/css/all.min.css">
<link rel="stylesheet" href="main.css">
<!-- Consent: Google Consent Mode v2 defaults (keep ABOVE any Google tag), banner styles + script -->
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',functionality_storage:'granted',security_storage:'granted',wait_for_update:500}});
gtag('set','ads_data_redaction',true);gtag('set','url_passthrough',true);
</script>
<link rel="stylesheet" href="consent.css">
<script src="consent.js" defer></script>
<!-- Non-essential tags must be blocked until consent, e.g.:
<script type="text/plain" data-gr-consent="analytics" data-src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
<script type="text/plain" data-gr-consent="advertising">/* Taboola / Outbrain / Google Ads pixel */</script> -->
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"Best Online GLP-1 Weight-Loss Programs (2026): Top 5 Compared","author":{{"@type":"Person","name":"[Author Name]"}},"publisher":{{"@type":"Organization","name":"{SITE}"}},"dateModified":"2026-09-24"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_ld}]}}</script>
</head>
<body>

<p class="adnote">Advertising disclosure: we may earn a commission when you visit providers from this page. It never changes our scores. <a href="disclosure.html">How we make money</a></p>

<header class="nav"><div class="w">
 <a class="brand" href="index.html"><img src="images/logo.svg" alt="" width="32" height="32"><span>GLP1Review<b>Guide</b><small style="font-size:13px;font-weight:500;color:#615B6B">.com</small></span></a>
 <nav aria-label="Main"><a href="#pick-1">Top 5</a><a href="#fit">Find your fit</a><a href="index.html#method">How we score</a><a href="about.html">About</a></nav>
</div></header>

<main>
<section class="hero"><div class="w hero_grid">
 <div class="hero_copy">
  <p class="kicker"><i class="fa-solid fa-scale-balanced"></i> Independent comparison · Updated {UPDATED}</p>
  <h1>Online GLP-1 programs, <em>compared honestly (2026). How ONE Program fixed everything&nbsp;&nbsp;</em></h1>
  <div class="hero_actions"><a class="btn_dark" href="#pick-1">See the top 5</a><a class="btn_line" href="#fit">Find my fit in 3 questions</a></div>
  <div class="disc_row">
   <details><summary>Editorial disclosure</summary><p>We research programs independently. If you sign up through our links we may earn a commission at no cost to you. Brands can't pay to change our scores.</p></details>
  </div>
 </div>
</div></section>

<section class="intro"><div class="w narrow">
 <div class="dek">
  <p>We started by comparing <strong>15 GLP-1 and medical weight-management programs</strong> available online. We looked beyond the headline price and compared what people actually get for their money: the medical consultation process, medication options, ongoing provider support, recurring fees, shipping costs, cancellation policies, and what happens if a patient isn't prescribed treatment.</p>
  <p>The differences were bigger than we expected. <strong>One&nbsp;stood out for their combination of transparent pricing, access to licensed medical providers, ongoing support, and overall simplicity.</strong></p>
  <p style="font-size:17px">We've narrowed the field to five programs below and explain how each compares. Our rankings consider factors such as clinical care, medication access, price transparency, and ongoing support—not promises of a particular weight-loss result. Eligibility and treatment are determined by a licensed healthcare provider, and results vary from person to person.</p>
  <p><strong>Scroll down to compare the five programs</strong>, see what each includes, and decide which options are worth discussing with a healthcare professional.</p>
 </div>
</div></section>

<div class="w">
 <div class="safety"><i class="fa-solid fa-circle-info"></i><p><strong>Before you compare:</strong> GLP-1 medications require a prescription and a medical evaluation, and they aren't right for everyone, including people with a personal or family history of medullary thyroid carcinoma or MEN 2. Common side effects include nausea, vomiting and diarrhea. Results vary. We're not endorsed by any brand here; trademarks belong to their owners. <a href="disclosure.html#medical">Medical disclaimer</a></p></div>
</div>

<section class="picks"><div class="w">
 {"".join(card(i,p) for i,p in enumerate(P,1))}
</div></section>

<section class="fit" id="fit"><div class="w fit_grid">
 <div class="fit_intro">
  <p class="kicker light"><i class="fa-solid fa-compass"></i> Find your fit</p>
  <h2>Not sure which one? Answer three questions.</h2>
  <p>Every program above suits a different kind of person. Tell us what matters to you and we'll point you to a good place to start. This isn't medical advice; a clinician makes the final call.</p>
 </div>
 <div class="quiz" id="quiz">
  <fieldset><legend>1. Do you plan to use health insurance?</legend>
   <label><input type="radio" name="ins" value="yes"> Yes</label><label><input type="radio" name="ins" value="no"> No, I'll pay myself</label><label><input type="radio" name="ins" value="unsure"> Not sure</label></fieldset>
  <fieldset><legend>2. Which medications are you open to?</legend>
   <label><input type="radio" name="med" value="brand"> FDA-approved brand-name only</label><label><input type="radio" name="med" value="any"> Open to compounded</label><label><input type="radio" name="med" value="unsure"> Not sure yet</label></fieldset>
  <fieldset><legend>3. What matters most to you?</legend>
   <label><input type="radio" name="pri" value="price"> Lowest, predictable price</label><label><input type="radio" name="pri" value="coach"> Nutrition coaching</label><label><input type="radio" name="pri" value="doctor"> A video visit with a doctor</label></fieldset>
  <button type="button" id="quiz_go" class="btn_dark">Show my match</button>
  <div class="quiz_out" id="quiz_out" aria-live="polite"></div>
 </div>
</div></section>

<section class="method" id="method"><div class="w">
 <h2 class="sec">How we scored them</h2>
 <p class="sec_dek">Every program is scored on the same four criteria. We don't take medications ourselves or publish personal weight-loss results; we compare programs as services, using public pricing and each program's own sign-up flow.</p>
 <div class="weights" role="img" aria-label="Clinical care 30 percent, medication access 25 percent, price transparency 25 percent, ongoing support 20 percent">
  <div style="flex:30"><b>30%</b><span>Clinical care</span></div>
  <div style="flex:25"><b>25%</b><span>Medication access</span></div>
  <div style="flex:25"><b>25%</b><span>Price transparency</span></div>
  <div style="flex:20"><b>20%</b><span>Ongoing support</span></div>
 </div>
 <div class="wdesc">
  <p><i class="fa-solid fa-user-doctor"></i><span><strong>Clinical care.</strong> Clinician credentials, depth of review, labs and how fast you can reach someone about side effects.</span></p>
  <p><i class="fa-solid fa-prescription-bottle-medical"></i><span><strong>Medication access.</strong> Which FDA-approved GLP-1s are available, and whether compounded options are clearly labeled.</span></p>
  <p><i class="fa-solid fa-receipt"></i><span><strong>Price transparency.</strong> Total monthly cost shown up front, price changes with dose, and cancellation terms.</span></p>
  <p><i class="fa-solid fa-comments"></i><span><strong>Ongoing support.</strong> Coaching, nutrition help, check-ins and app quality.</span></p>
 </div>
</div></section>

<section class="feature"><div class="w feature_grid">
 <aside class="feat_panel">
  <p class="hc_label"><i class="fa-solid fa-crown"></i> Featured partner</p>
  {ring(top["total"],120,11,"#fff")}
  <h2>{top["name"]}</h2>
  <dl>
   <div><dt>First month</dt><dd>{top["now"]}</dd></div>
   <div><dt>After that</dt><dd>$297/mo</dd></div>
   <div><dt>Tirzepatide</dt><dd>$399/mo</dd></div>
   <div><dt>Membership fee</dt><dd>None</dd></div>
  </dl>
  <a class="cta light" href="{link(top)}" {REL}>See if I qualify</a>
  <p class="feat_fine">Refunded in full if your prescription isn't approved. Paid placement.</p>
 </aside>
 <div class="feat_copy">
  <h2 class="sec">Why we feature {top["name"]}</h2>
   <p>{top["name"]} is our featured partner, which means it pays for its position at the top of this page. Its score is calculated with the same method as every other program. What stands out is how simple the pricing is: one monthly price covers the medication, doctor visits, supplies and shipping.</p>
   <h3>All-inclusive pricing</h3>
   <p>Most programs charge a membership and bill medication separately. {top["pricing"]}</p>
   <h3>Fast review and delivery</h3>
   <p>{top["care"]} Approved prescriptions ship from U.S.-based 503A compounding pharmacies, usually within 1–2 days.</p>
   <h3>Medication choice</h3>
   <p>Doctors can prescribe compounded semaglutide or tirzepatide, as a weekly injection or as sublingual (under-the-tongue) drops. Compounded medications are not FDA-approved and are not generic versions of brand-name drugs. There's less research on sublingual forms than on injections, so ask your doctor which is right for you.</p>
   <h3>Things to weigh</h3>
   <p>{top["name"]} doesn't offer brand-name medications or take insurance, and it isn't available in Mississippi or Louisiana. After the first month its price is higher than some programs on this list, including our highest-scoring program, {P[1]["name"]}. It is LegitScript certified, which means its pharmacy and prescribing practices have been independently reviewed.</p>
   <p>A licensed clinician decides whether a GLP-1 medication is right for you.</p>
 </div>
</div></section>

<section class="faq"><div class="w narrow">
 <h2 class="sec">Questions people ask</h2>
 {faq_html}
</div></section>

<section class="byline_sec"><div class="w narrow byline_card">
 <div class="photo_slot">Author<br>photo</div>
 <div><p class="by_label">Written by</p><h3>[Author Name], Health &amp; Consumer Products Editor</h3>
 <p>[Real, verifiable bio: years covering health, relevant education, where their work has appeared.]</p>
 <p class="by_rev"><i class="fa-solid fa-stethoscope"></i> Medically reviewed by <strong>[Reviewer Name, MD]</strong>, [specialty]. Prices checked {UPDATED}.</p></div>
</div></section>
</main>

<footer class="foot"><div class="w foot_grid">
 <div><a class="brand" href="index.html"><img src="images/logo.svg" alt="" width="28" height="28"><span>GLP1Review<b>Guide</b><small style="font-size:13px;font-weight:500;color:#615B6B">.com</small></span></a>
  <p>Independent comparisons of online GLP-1 programs, so you can walk into your consultation with better questions.</p>
  <p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
 <div><h4>Explore</h4><ul><li><a href="#top5">Top 5 programs</a></li><li><a href="#fit">Find your fit</a></li><li><a href="#method">How we score</a></li><li><a href="about.html">About us</a></li></ul></div>
 <div><h4>Legal</h4><ul><li><a href="disclosure.html">Advertising disclosure</a></li><li><a href="disclosure.html#medical">Medical disclaimer</a></li><li><a href="privacy.html">Privacy policy</a></li><li><a href="consumer-health-data-privacy.html">Consumer health data privacy</a></li><li><a href="cookie-policy.html">Cookie policy</a></li><li><a href="terms.html">Terms of use</a></li><li><a class="pc" href="your-privacy-choices.html"><img src="images/privacy-choices.svg" alt="" width="30" height="14">Your Privacy Choices / Do Not Sell or Share My Personal Information</a></li><li><button type="button" class="linklike" data-gr-open-consent>Cookie settings</button></li></ul></div>
 <p class="foot_legal">Content is for information only and is not medical advice. GLP-1 medications require a prescription; talk to a licensed clinician about benefits and risks. {SITE} is an independent publisher, not a healthcare provider or pharmacy. We may earn commissions from links on this page, which may affect where programs appear. &copy; 2026 {SITE}.</p>
</div></footer>

<script>
(function(){{
  var T={QT};
  function pick(ins,med,pri){{
    if(ins==='yes') return pri==='doctor' ? ['PlushCare','Takes insurance and gives you a real video visit with a board-certified physician.'] : ['Ro','Its insurance concierge checks whether your plan covers a GLP-1 before you commit.'];
    if(pri==='coach') return ['WeightWatchers Med+','Pairs obesity medicine specialists with one-on-one dietitian support and a full nutrition app.'];
    if(pri==='doctor') return ['PlushCare','Video visits with board-certified physicians licensed in all 50 states.'];
    if(med==='brand') return ['Ro','Brand-name GLP-1s only, with a low intro month and no long-term contract.'];
    if(med==='any') return ['DirectMeds','One monthly price that includes medication, doctor visits and shipping, with $150 off your first month.'];
    return ['Pallas Health','Offers both compounded and brand-name options, with no membership fee and one price at every dose.'];
  }}
  document.getElementById('quiz_go').addEventListener('click',function(){{
    var q=document.getElementById('quiz'), out=document.getElementById('quiz_out');
    var v=function(n){{var el=q.querySelector('input[name="'+n+'"]:checked');return el?el.value:null;}};
    var ins=v('ins'),med=v('med'),pri=v('pri');
    if(!ins||!med||!pri){{out.innerHTML='<p class="q_warn">Please answer all three questions.</p>';return;}}
    var r=pick(ins,med,pri), t=T[r[0]];
    out.innerHTML='<div class="q_card"><span class="q_rank">#'+t.rank+'</span><div><p class="q_lbl">A good place to start</p><h3>'+t.name+'</h3><p>'+r[1]+'</p><a href="#'+t.id+'">See the full breakdown</a></div></div>';
  }});
}})();
</script>
</body>
</html>"""
open("index.html","w").write(index_html)

# ---------- review pages ----------
for i,p in enumerate(P,1):
    body = f'''
<section class="hero"><div class="wrap">
  <div>
    <h1>{p["name"]} review: pricing, medications and what to expect</h1>
    <p class="dek">{p["summary"]}</p>
    {AUTHOR}
  </div>
  <div class="hero-art"><img src="images/provider-{p["slug"]}.svg" alt="{p["name"]} logo" width="320" height="160"></div>
</div></section>
<div class="wrap"><div class="notice"><strong>Prescription required</strong>A licensed clinician decides whether a GLP-1 medication is appropriate. This review is not medical advice. <a href="disclosure.html#medical">Medical disclaimer</a>.</div></div>
<section class="section"><div class="wrap">
  <article class="pick top"><div class="pick-flag">Ranked #{i}: {p["flag"]}</div><div class="pick-body">
    <div class="pick-logo"><img src="images/provider-{p["slug"]}.svg" alt="" width="160" height="80"></div>
    <div><div class="proscons">
      <div><h4>What we like</h4><ul>{"".join(f"<li>{x}</li>" for x in p["pros"])}</ul></div>
      <div><h4>Things to know</h4><ul>{"".join(f"<li>{x}</li>" for x in p["cons"])}</ul></div></div></div>
    <div class="score"><div class="score-total">{p["total"]}<small> / 10</small></div>{bars(p["scores"])}
      <a class="btn" href="{link(p)}" rel="sponsored nofollow noopener" target="_blank">Visit {p["name"]}</a>
      <p class="fine">{p["price"]}. Prescription not guaranteed.</p></div>
  </div></article>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap prose">
  <h2>At a glance</h2>
  <div class="table-scroll"><table class="compare" style="min-width:0">
    <tbody>
      <tr><th>Price</th><td>{p["price"]}</td></tr>
      <tr><th>Medications offered</th><td>{p["meds"]}</td></tr>
      <tr><th>Compounded medications</th><td>{p["compounded"]}</td></tr>
      <tr><th>Insurance / HSA</th><td>{p["ins"]}</td></tr>
      <tr><th>Visit type</th><td>{p["visit"]}</td></tr>
            <tr><th>Cancellation</th><td>{p["cancel"]}</td></tr>
    </tbody></table></div>
  <h2>Medical care</h2>
  <p>{p["care"]}</p>
  <h2>Pricing</h2>
  <p>{p["pricing"]} Prices were checked in {UPDATED}; confirm current pricing on the provider's site.</p>
  <h2>Who it's best for</h2>
  <p>{p["bestfor"]}</p>
  <h2>Our verdict</h2>
  <p>{p["summary"]} A licensed clinician decides whether a GLP-1 medication is appropriate, and results vary from person to person.</p>
  <p><a class="btn ghost" href="index.html#provider-{p["k"]}">Back to the full comparison</a></p>
</div></section>'''
    page(f"review-{p['slug']}.html", f"{p['name']} Review ({UPDATED}): Pricing, Medications & Support | {SITE}",
         f"Our independent review of {p['name']}: pricing, medication options, clinical care and support.", body)

# ---------- simple pages ----------
def simple(fname, title, desc, h1, inner):
    page(fname, f"{title} | {SITE}", desc, f'<section class="section"><div class="wrap prose"><h1 style="font:600 clamp(30px,8vw,40px)/1.15 var(--serif);margin:0 0 18px;overflow-wrap:anywhere">{h1}</h1>{inner}</div></section>')

ic = lambda d: f'<svg viewBox="0 0 24 24" fill="none" stroke="#2F7D6D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
# how-we-review.html removed (methodology lives in the homepage #method section).

simple("about.html","About Us","Who we are and why we compare online weight-care programs.","About "+SITE,f'''
<p>{SITE} helps people understand their options for online weight care before they talk to a clinician. The number of telehealth programs offering GLP-1 medications has grown quickly, and their pricing, medications and level of care vary a lot. We lay those differences out side by side.</p>
<h2 id="team">Our team</h2>
<p><strong>[Author Name]</strong>, health editor. [Short bio with relevant experience.]</p>
<p><strong>[Reviewer Name, MD]</strong>, medical reviewer. [Specialty, board certification, and what they review.]</p>
<div class="img-slot" style="aspect-ratio:3/1">Image slot: add real team headshots (square, at least 400 × 400px).</div>
<h2>Our editorial standards</h2>
<p>We base health information on FDA prescribing information and peer-reviewed research, link to sources, and never promise specific results. Commercial relationships don't influence our rankings. See <a href="index.html#method">how we score programs</a>.</p>
<h2 id="contact">Contact us</h2>
<p>Questions, corrections or partnership inquiries: email <a href="mailto:{EMAIL}">{EMAIL}</a>. We reply within two business days. We can't give medical advice or help with prescriptions or orders; contact your provider directly. In a medical emergency, call 911.</p>
<p>[Legal company name]<br>[Street address]<br>[City, State ZIP]</p>''')

# contact.html removed (contact details live on about.html#contact and in every footer).

simple("disclosure.html","Advertising Disclosure & Medical Disclaimer","How we earn money and important medical information.","Advertising disclosure",f'''
<p>{SITE} is a free, independent comparison site. To keep it free, we may receive compensation from some companies listed when you click a link and sign up. Links that may earn us a commission are marked as sponsored in our code.</p>
<p>Compensation may affect which companies we feature and where they appear on the page, but it does not affect our scores, which follow our <a href="index.html#method">published methodology</a>. We don't list every program available.</p>
<h2 id="medical">Medical disclaimer</h2>
<p>Content on this site is for informational purposes only and is not a substitute for professional medical advice, diagnosis or treatment. Always consult a qualified healthcare provider before starting, stopping or changing any medication.</p>
<p>GLP-1 medications are available by prescription only. They carry risks including gastrointestinal side effects, pancreatitis, gallbladder disease and a boxed warning about thyroid C-cell tumors. They are not appropriate for everyone. Results vary between individuals.</p>
<p>{SITE} does not prescribe, sell or dispense medication and is not a pharmacy or healthcare provider.</p>''')

# privacy.html is now a standalone page (with consumer-health-data, cookie and Do Not Sell pages).
# Edit privacy.html directly. It is intentionally NOT generated here any more.

simple("terms.html","Terms of Use","Terms governing use of "+SITE+".","Terms of use",f'''
<p><em>Last updated: {UPDATED}. Template text: have a lawyer review before publishing.</em></p>
<h2>Acceptance</h2><p>By using this site you agree to these terms. If you don't agree, please don't use the site.</p>
<h2>No medical advice</h2><p>Content is informational only. See our <a href="disclosure.html#medical">medical disclaimer</a>.</p>
<h2>Third-party sites</h2><p>We link to third-party providers. We aren't responsible for their content, products, services, pricing or privacy practices. Any transaction is between you and that provider.</p>
<h2>Accuracy</h2><p>We work to keep information current, but prices and availability change. Confirm details directly with each provider.</p>
<h2>Intellectual property</h2><p>Site content is owned by {SITE} unless otherwise stated. Third-party trademarks belong to their owners.</p>
<h2>Limitation of liability</h2><p>To the extent permitted by law, {SITE} is not liable for any damages arising from use of this site.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of [State], United States.</p>
<h2>Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>''')
print("built")
