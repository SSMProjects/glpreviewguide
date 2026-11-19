/* =====================================================================
   GLP1ReviewGuide — engagement layer for the sa/ standalones.
   Loaded with `defer`. No cookies, no storage, no network calls.

   What it does
   1. Reading-progress line at the top of the page.
   2. Sticky bottom button: shows after the first screen, hides next to the
      main button box, the footer, the consent banner and while typing.
   3. Desktop side rail (>=1300px): contents with the current section marked.
   4. Engagement events pushed to window.dataLayer, ready for GA4 / GTM:
        { event:'nr_engagement', nr_action, nr_label, nr_page }
        nr_action: engaged_time (5s,15s,30s,60s) · scroll_depth (25,50,75,100)
                   cta_click (which button) · toc_click · tool_use (bmi, cost)
      Nothing is sent anywhere by this file. A tag you add later decides that,
      and Google Consent Mode on the page still applies to it.
   Add ?nrdebug=1 to a page URL to see the events in the browser console.
   ===================================================================== */
(function () {
  'use strict';
  var d = document, w = window, body = d.body;
  if (!body || body.getAttribute('data-nr-ready')) return;
  body.setAttribute('data-nr-ready', '1');

  var PAGE = body.getAttribute('data-page') || location.pathname.split('/').pop().replace(/\.html$/, '');
  var DEBUG = /[?&]nrdebug=1/.test(location.search);
  var isB = body.classList.contains('nr-b');

  function ev(action, label) {
    var o = { event: 'nr_engagement', nr_action: action, nr_label: String(label == null ? '' : label), nr_page: PAGE };
    try { (w.dataLayer = w.dataLayer || []).push(o); } catch (e) {}
    if (DEBUG && w.console) console.log('[nr]', action, o.nr_label);
    try { d.dispatchEvent(new CustomEvent('nr:event', { detail: o })); } catch (e) {}
  }
  function $all(sel, root) { return Array.prototype.slice.call((root || d).querySelectorAll(sel)); }

  /* ---------- 1. label every offer button so clicks can be told apart ---------- */
  var n = 0;
  $all('a.offerlink, a[data-offer]').forEach(function (a) {
    if (a.getAttribute('data-cta')) return;
    var label;
    if (a.closest('.sticky-bar')) label = 'sticky';
    else if (a.closest('.col-side')) label = 'sidebar';
    else if (a.closest('.rec-mobile')) label = 'rec-card';
    else if (a.closest('.final')) label = 'final';
    else if (a.closest('.tablet-box')) label = 'needle-free-box';
    else if (a.closest('#start')) label = 'main-box';
    else label = 'inline-' + (++n);
    a.setAttribute('data-cta', label);
  });
  d.addEventListener('click', function (e) {
    var t = e.target;
    if (!t || !t.closest) return;
    var a = t.closest('a.offerlink, a[data-offer]');
    if (a) { ev('cta_click', a.getAttribute('data-cta') || 'unlabeled'); return; }
    var toc = t.closest('.nr-chips a, .nr-rail ol a');
    if (toc) ev('toc_click', (toc.getAttribute('href') || '').replace('#', ''));
  }, true);

  /* ---------- 2. time on page (only counts while the tab is visible) ---------- */
  var secs = 0, marks = [5, 15, 30, 60];
  var timer = setInterval(function () {
    if (d.visibilityState && d.visibilityState !== 'visible') return;
    secs++;
    if (secs === marks[0]) { ev('engaged_time', marks.shift() + 's'); if (!marks.length) clearInterval(timer); }
  }, 1000);

  /* ---------- 3. progress line, scroll depth, sticky button, rail ---------- */
  var bar = d.createElement('div');
  bar.className = 'nr-progress';
  bar.setAttribute('aria-hidden', 'true');
  bar.innerHTML = '<i></i>';
  body.appendChild(bar);
  var fill = bar.firstChild;

  var sticky = d.getElementById('nrSticky') || d.getElementById('stickyBar');
  var rail = d.getElementById('nrRail');
  var head = d.querySelector('.nr-head') || d.querySelector('h1');
  var depths = [25, 50, 75, 100];
  var nearCta = 0, typing = false, ticking = false;
  var tocLinks = $all('.nr-rail ol a'), tocCur = -1;
  var tocTargets = tocLinks.map(function (a) { return d.getElementById((a.getAttribute('href') || '').slice(1)); });

  function setSticky(on) {
    if (!sticky) return;
    if (isB) { sticky.classList.toggle('nr-hide', !on); return; }   /* the page's own script handles "show" */
    sticky.classList.toggle('show', on);
    sticky.setAttribute('aria-hidden', on ? 'false' : 'true');
    var a = sticky.querySelector('a');
    if (a) { if (on) a.removeAttribute('tabindex'); else a.setAttribute('tabindex', '-1'); }
  }
  function onScroll() {
    ticking = false;
    var y = w.pageYOffset || 0, vh = w.innerHeight, full = d.documentElement.scrollHeight;
    var max = Math.max(1, full - vh), p = Math.min(1, y / max);
    fill.style.transform = 'scaleX(' + p + ')';
    var pct = Math.min(100, Math.round((y + vh) / full * 100));
    while (depths.length && y > 10 && pct >= (depths[0] === 100 ? 98 : depths[0])) ev('scroll_depth', depths.shift());
    var pastHead = head ? head.getBoundingClientRect().bottom < vh * 0.35 : y > vh * 0.6;
    setSticky((isB ? true : pastHead) && nearCta === 0 && !typing);
    if (rail) {
      rail.classList.toggle('show', pastHead && nearCta < 2);
      if (w.innerWidth >= 1300) {                       /* mark the section being read */
        var cur = -1;
        for (var i = 0; i < tocTargets.length; i++) if (tocTargets[i] && tocTargets[i].getBoundingClientRect().top <= 140) cur = i;
        if (cur !== tocCur) {
          if (tocLinks[tocCur]) tocLinks[tocCur].removeAttribute('aria-current');
          if (tocLinks[cur]) tocLinks[cur].setAttribute('aria-current', 'true');
          tocCur = cur;
        }
      }
    }
  }
  function req() { if (!ticking) { ticking = true; (w.requestAnimationFrame || setTimeout)(onScroll); } }
  w.addEventListener('scroll', req, { passive: true });
  w.addEventListener('resize', req, { passive: true });

  /* hide the sticky button when a full-size button box or the footer is on screen */
  if ('IntersectionObserver' in w) {
    var seen = new Map();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { seen.set(en.target, en.isIntersecting ? (en.target.getAttribute('data-nr-zone') === 'end' ? 2 : 1) : 0); });
      nearCta = 0; seen.forEach(function (v) { if (v > nearCta) nearCta = v; });
      req();
    }, { rootMargin: '0px 0px -60px 0px' });
    $all('.nr-a .cta, .nr-b .final').forEach(function (el) { io.observe(el); });
    $all('.legal, .sitefoot, .site-footer, .disclaimer').forEach(function (el) { el.setAttribute('data-nr-zone', 'end'); io.observe(el); });

  }
  /* keep the sticky button out of the way of the on-screen keyboard */
  d.addEventListener('focusin', function (e) { if (e.target && /^(INPUT|SELECT|TEXTAREA)$/.test(e.target.tagName) && e.target.type !== 'radio') { typing = true; req(); } });
  d.addEventListener('focusout', function () { if (typing) { typing = false; req(); } });

  /* ---------- 4. on-page tools ---------- */
  var bmi = d.getElementById('bmi-form');
  if (bmi) bmi.addEventListener('submit', function () { ev('tool_use', 'bmi'); });
  var cc = d.getElementById('costcalc'), ccUsed = false;
  if (cc) cc.addEventListener('change', function () { if (!ccUsed) { ccUsed = true; ev('tool_use', 'cost'); } });

  onScroll();
})();
