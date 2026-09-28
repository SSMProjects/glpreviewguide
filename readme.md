# GLP1ReviewGuide.com: GLP-1 comparison site

Static HTML. Upload the whole folder (keep `images/` and `styles.css`) to any host: Netlify, Cloudflare Pages, cPanel, S3.

## Before you launch (find & replace)
- Brand, domain and email are set at the top of build.py (GLP1ReviewGuide.com / glp1reviewguide.com / hello@glp1reviewguide.com). Run `python3 build.py` to regenerate the homepage, reviews, About, Contact, Disclosure, How we review and Terms.
- NOT generated (edit directly): privacy.html, consumer-health-data-privacy.html, your-privacy-choices.html, cookie-policy.html, accessibility.html, team.html, lp/*.html. See SETUP-NOTES.md.
- Providers (in rank order): Pallas Health, WeightWatchers Med+, Ro, PlushCare, Hims & Hers. Pallas details come from pallashealth.co (checked September 2026). Facts and prices were checked in September 2026 (Forbes Health, Sept 2026 update; provider sites). Re-verify every price on each provider's site before launch and every 60–90 days after.
- Overall scores are calculated automatically from the four criteria scores using the weights on the How We Review page (30/25/25/20). Edit the criteria scores in build.py, not the totals.
- Scores are editorial starting points. Adjust them to your own evaluation so you can stand behind them.
- `https://AFFILIATE-LINK-A` … `-E` → your tracking links (keep rel="sponsored nofollow"). A = Pallas Health, B = WW Med+, C = Ro, D = PlushCare, E = Hims & Hers.
- `[Author Name]`, `[Reviewer Name, MD]`, company address, `[State]` → real people and details
- `images/provider-*.svg` → official logos from each affiliate program's brand-asset kit
- Dashed "Image slot" boxes → your own screenshots or photos
- Have a lawyer review privacy.html and terms.html

## Ad-policy essentials already built in
Advertising disclosure bar on every page, medical disclaimer and safety info, no guaranteed results,
no before/after photos, no fake testimonials or urgency timers, named author + medical reviewer,
methodology page, full contact/company page, privacy + terms, FAQ schema markup.

## Files
- index.html + main.css: the ranked comparison page (split hero with top-pick card, top-5 tiles, ranked program cards with score rings, Find-your-fit quiz, scoring method, editor's-pick feature, FAQ, author box).
- Quiz logic lives in the <script> at the bottom of index.html (function pick). Update it if you change the lineup.
- Review, about, legal pages use styles.css.
- vendor/fontawesome: icons are bundled locally, so no CDN is needed.
