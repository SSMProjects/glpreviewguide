#!/usr/bin/env python3
"""SEO check for glp1reviewguide.com (report-only; never edits files).

Rules (see claude/robots-sitemap-notes.md in the project):
  * Indexed pages = /reviews/*, the homepage, /about and /disclosure. Everything else
    must be `noindex` (ad landers, templates, legal pages).
  * Every indexed page has a canonical equal to the URL Netlify serves:
    https://glp1reviewguide.com/<path lowercased, no .html>  ("/" for index.html).
  * sitemap.xml lists exactly the indexed pages, each with a YYYY-MM-DD <lastmod>.
  * Any page that has a canonical must point it at itself (lowercase, no .html).
  * robots.txt exists, has no Disallow rules, and points at the sitemap.

Exit code 1 if any error is found. Warnings don't fail the check.
Run locally from the repo root:  python3 .github/scripts/seo_check.py
"""
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

SITE = "https://glp1reviewguide.com"
INDEXED_EXACT = {"index.html", "about.html", "disclosure.html"}
INDEXED_PREFIX = ("reviews/",)
SKIP = re.compile(r"^google[0-9a-f]{16}\.html$")  # Search Console verification file
SM_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

errors, warnings = [], []
GH = os.environ.get("GITHUB_ACTIONS") == "true"


def err(msg, file=None):
    errors.append((file, msg))


def warn(msg, file=None):
    warnings.append((file, msg))


def html_files():
    try:
        out = subprocess.check_output(["git", "ls-files", "*.html"], text=True)
        files = out.split()
    except Exception:
        files = []
        for root, dirs, names in os.walk("."):
            dirs[:] = [d for d in dirs if not d.startswith(".") and d != "node_modules"]
            files += [os.path.relpath(os.path.join(root, n), ".") for n in names if n.endswith(".html")]
    return sorted(f for f in files if not SKIP.match(os.path.basename(f)) and not f.startswith("vendor/"))


def served_url(f):
    p = f[:-5]
    if p == "index":
        return SITE + "/"
    if p.endswith("/index"):
        p = p[: -len("index")]
    return SITE + "/" + p.lower()


def should_index(f):
    return f in INDEXED_EXACT or f.startswith(INDEXED_PREFIX)


def meta(html, name):
    for tag in re.findall(r"<meta\b[^>]*>", html, re.I):
        if re.search(r'\bname\s*=\s*["\']%s["\']' % name, tag, re.I):
            m = re.search(r'\bcontent\s*=\s*["\']([^"\']*)', tag, re.I)
            return m.group(1).strip() if m else ""
    return None


def canonicals(html):
    out = []
    for tag in re.findall(r"<link\b[^>]*>", html, re.I):
        if re.search(r'\brel\s*=\s*["\']canonical["\']', tag, re.I):
            m = re.search(r'\bhref\s*=\s*["\']([^"\']*)', tag, re.I)
            out.append(m.group(1).strip() if m else "")
    return out


# ---------------------------------------------------------------- pages
pages = {}  # served url -> file, for indexable pages
for f in html_files():
    try:
        s = open(f, encoding="utf-8", errors="replace").read()
    except OSError as e:
        err(f"can't read file: {e}", f)
        continue
    robots = meta(s, "robots")
    indexable = robots is None or "noindex" not in robots.lower()
    cans = canonicals(s)
    url = served_url(f)

    if len(cans) > 1:
        err(f"has {len(cans)} canonical tags; keep exactly one", f)
    if cans and cans[0] != url:
        err(f'canonical is "{cans[0]}" but this page is served at "{url}" (use the lowercase URL without .html)', f)

    if should_index(f):
        if not indexable:
            err(f'is an SEO page but robots is "{robots}"; SEO pages must be "index, follow"', f)
        if not cans:
            err(f'SEO page has no canonical; add <link rel="canonical" href="{url}">', f)
    else:
        if indexable:
            shown = "missing" if robots is None else f'"{robots}"'
            err(f'robots tag is {shown}; pages outside /reviews/ (except home, about, disclosure) must be '
                f'<meta name="robots" content="noindex, follow">. If this should be an SEO page, put it in /reviews/.', f)
        elif "nofollow" in robots.lower():
            warn(f'robots is "{robots}"; the site standard is "noindex, follow"', f)
    if indexable:
        pages[url] = f

# ---------------------------------------------------------------- sitemap
locs = []
if not os.path.exists("sitemap.xml"):
    err("sitemap.xml is missing", "sitemap.xml")
else:
    try:
        root = ET.parse("sitemap.xml").getroot()
        if root.tag != SM_NS + "urlset":
            err("sitemap root must be <urlset> in the sitemaps.org namespace", "sitemap.xml")
        for u in root.findall(SM_NS + "url"):
            loc = (u.findtext(SM_NS + "loc") or "").strip()
            lastmod = (u.findtext(SM_NS + "lastmod") or "").strip()
            locs.append(loc)
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", lastmod):
                err(f'<lastmod> for {loc} should be YYYY-MM-DD (got "{lastmod}")', "sitemap.xml")
    except ET.ParseError as e:
        err(f"sitemap.xml is not valid XML: {e}", "sitemap.xml")

dupes = {l for l in locs if locs.count(l) > 1}
for l in sorted(dupes):
    err(f"{l} is listed more than once", "sitemap.xml")
for l in locs:
    if l not in pages:
        err(f"{l} is in the sitemap but isn't an indexable page in the repo "
            f"(noindex, missing, or a non-canonical URL such as .html or uppercase)", "sitemap.xml")
for url, f in sorted(pages.items()):
    # Only SEO pages belong in the sitemap; an ad page that's missing noindex already got its own error above.
    if should_index(f) and url not in locs:
        err(f"indexable page {url} is missing from sitemap.xml; add a <url> with <loc>{url}</loc> and a <lastmod>", f)

# ---------------------------------------------------------------- robots.txt
if not os.path.exists("robots.txt"):
    err("robots.txt is missing", "robots.txt")
else:
    r = open("robots.txt", encoding="utf-8").read()
    if not re.search(r"^Sitemap:\s*%s/sitemap\.xml\s*$" % re.escape(SITE), r, re.M | re.I):
        err(f"robots.txt should contain: Sitemap: {SITE}/sitemap.xml", "robots.txt")
    if re.search(r"^Disallow:\s*\S", r, re.M | re.I):
        err("robots.txt has a Disallow rule; Google must be able to crawl noindex pages to see the tag", "robots.txt")

# ---------------------------------------------------------------- report
def emit(kind, items):
    for f, msg in items:
        if GH:
            loc = f" file={f}" if f else ""
            print(f"::{kind}{loc}::{msg}")
        else:
            print(f"{kind.upper()}: {f + ': ' if f else ''}{msg}")

emit("warning", warnings)
emit("error", errors)
print(f"\nSEO check: {len(html_files())} HTML pages, {len(pages)} indexable, {len(locs)} sitemap URLs, "
      f"{len(errors)} error(s), {len(warnings)} warning(s).")
if not errors:
    print("Indexed pages: " + ", ".join(u.replace(SITE, "") or "/" for u in sorted(pages)))
sys.exit(1 if errors else 0)
