# GLP1ReviewGuide.com: privacy pages, consent banner and pre-landers

## What's in this package

| File | Goes to | What it is |
|---|---|---|
| `gr.css` | `/gr.css` | Shared styles (same colors and fonts as main.css) |
| `consent.js` | `/consent.js` | Cookie banner, Google Consent Mode v2, GPC support, script blocking |
| `images/logo.svg` | `/images/logo.svg` | New GLP1ReviewGuide.com logo mark (replaces the old one) |
| `images/privacy-choices.svg` | `/images/privacy-choices.svg` | California "Your Privacy Choices" toggle icon |
| `your-privacy-choices.html` | `/your-privacy-choices` | **Do Not Sell/Share** page: toggle, GPC notice, request form |
| `consumer-health-data-privacy.html` | `/consumer-health-data-privacy` | **Consumer Health Data Privacy Policy** (WA MHMDA, NV, CT) |
| `cookie-policy.html` | `/cookie-policy` | Cookie policy with cookie table |
| `privacy.html` | `/privacy` | **Replaces** the current privacy policy (new brand, GPC, CA notice) |
| `accessibility.html` | `/accessibility` | Accessibility statement |
| `team.html` | `/team` | Editor and medical reviewer bio page (fill in with REAL people) |
| `lp/online-glp1-programs.html` | `/lp/online-glp1-programs` | Pre-lander A: advertorial |
| `lp/7-things-glp1-online.html` | `/lp/7-things-glp1-online` | Pre-lander B: listicle |

## 1. Add the banner to EVERY existing page (homepage, reviews, about, terms…)

Paste this into `<head>` **above** any Google tag or GTM code:

```html
<script>
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',functionality_storage:'granted',security_storage:'granted',wait_for_update:500});
gtag('set','ads_data_redaction',true);gtag('set','url_passthrough',true);
</script>
<link rel="stylesheet" href="/gr.css" media="print" onload="this.media='all'"> <!-- only if the page doesn't already use gr.css; the banner styles live here -->
<script src="/consent.js" defer></script>
```

> On the homepage, main.css and gr.css share the same color tokens, so loading both is safe. If you'd rather not load all of gr.css there, copy the `/* ===== Consent banner ===== */` and `.switch` blocks into main.css.

Then **block every non-essential tag until consent** by changing its script type:

```html
<!-- before -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXX"></script>
<!-- after -->
<script type="text/plain" data-gr-consent="analytics" data-src="https://www.googletagmanager.com/gtag/js?id=G-XXXX"></script>
<script type="text/plain" data-gr-consent="analytics">gtag('js',new Date());gtag('config','G-XXXX');</script>

<!-- Taboola / Outbrain / Google Ads conversion pixels -->
<script type="text/plain" data-gr-consent="advertising"> ...pixel code... </script>
```

If you use Google Tag Manager instead, load GTM normally after the consent-default snippet. In GTM, set each tag's built-in consent checks (analytics_storage / ad_storage), and make Taboola/Outbrain tags fire only on a `gr:consent` custom event where `advertising` is true.

## 2. Replace the footer's Legal column on every page

```html
<div><h4>Legal</h4><ul>
 <li><a href="/disclosure">Advertising disclosure</a></li>
 <li><a href="/disclosure#medical">Medical disclaimer</a></li>
 <li><a href="/privacy">Privacy policy</a></li>
 <li><a href="/consumer-health-data-privacy">Consumer health data privacy</a></li>
 <li><a href="/cookie-policy">Cookie policy</a></li>
 <li><a href="/terms">Terms of use</a></li>
 <li><a class="pc" href="/your-privacy-choices"><img src="/images/privacy-choices.svg" alt="" width="30" height="14">Your Privacy Choices / Do Not Sell or Share My Personal Information</a></li>
 <li><button type="button" class="linklike" data-gr-open-consent>Cookie settings</button></li>
</ul></div>
```
Washington's MHMDA requires a **prominent link to the Consumer Health Data Privacy Policy on the homepage**. The footer link covers this as long as the homepage footer is updated too.

## 3. Brand rename checklist (WeightCare Compare → GLP1ReviewGuide.com)

- [ ] Logo text in the header and footer on every page: `GLP1Review<b>Guide</b><small>.com</small>`. Replace `images/logo.svg`.
- [ ] `<title>` tags: "| WeightCare Compare" → "| GLP1ReviewGuide.com"
- [ ] **Canonical tags currently point to weightcarecompare.com** (seen on /privacy). Change every one to `https://glp1reviewguide.com/...`. Leaving these as-is is a misrepresentation and SEO risk.
- [ ] Emails: hello@ / privacy@ / accessibility@ / corrections@ / editor@glp1reviewguide.com. Set these mailboxes up.
- [ ] Footer legal line, About page, Terms, Disclosure: replace every "WeightCare Compare"
- [ ] Search the whole site for "weightcare" before launch

## 4. Placeholders to fill (highlighted yellow on the pages)

- `[Legal entity name]` and `[street address]`: privacy, CHD policy
- Editor and medical reviewer names, bios, photos, license links: team, both landers. **These must be real people who agreed to be listed.**
- Ad platforms and affiliate partner names in the CHD policy sharing table
- Hosting/CDN cookie row and analytics retention period (cookie policy)
- Form handler: `your-privacy-choices.html` posts to `/api/privacy-request`. Point it at your form service.
- Real affiliate links on the homepage (it still has `AFFILIATE-LINK-A`…)

## 5. Pre-landers: test setup (6-cell test)

Each lander has two angles, switched by URL (the homepage cells are the control, with the angle coming from the ad creative), with no duplicate pages to maintain:

| Cell | URL |
|---|---|
| Advertorial · cost | `/lp/online-glp1-programs?angle=cost` |
| Advertorial · convenience | `/lp/online-glp1-programs?angle=convenience` |
| Listicle · cost | `/lp/7-things-glp1-online?angle=cost` |
| Listicle · convenience | `/lp/7-things-glp1-online?angle=convenience` |
| Direct to comparison · cost ad | `/?utm_content=cost` (homepage, no pre-lander) |
| Direct to comparison · convenience ad | `/?utm_content=convenience` |

- The CTAs send readers to `/#top5` and automatically forward `utm_*`, `gclid`, `tblci` (Taboola), `obclid`/`dicbo` (Outbrain), `lp` and `angle`. You can see which lander and angle produced each affiliate click.
- Landers are `noindex` (paid-traffic pages).
- The image boxes on the landers describe exactly what photo to use and at what size. Replace each `.img-slot` div with `<img src="..." alt="..." width="1600" height="900">`.
- A mobile sticky CTA appears after the reader scrolls past the first CTA.

## 6. Before launch

- [ ] Privacy counsel reviews: privacy, CHD policy, cookie policy, Do Not Sell page
- [ ] Healthcare-advertising review of both landers (claims, ISI, disclosures)
- [ ] Check that the homepage quiz really doesn't send answers anywhere (DevTools > Network while answering). The CHD policy says it doesn't.
- [ ] Run a cookie scan with everything accepted, then update the cookie table
- [ ] Re-verify prices monthly. The landers say "about $20–$200 a month" in program fees, based on the September 2026 comparison.
