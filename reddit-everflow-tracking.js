(function () {
  'use strict';

  // Applies only to the Ro affiliate links on a page that loads this script.
  // Sends no conversion events. For consented Reddit visits only, Sub2 is
  // campaign, Sub3 is creative, Sub5 is channel; Google retains its mapping.
  var STORAGE_KEY = 'reddit_ro_attribution_v2';
  var originalSources = new WeakMap();
  var decorated = new WeakSet();

  function clean(value) {
    if (typeof value !== 'string') return '';
    value = value.trim();
    return value && value.length <= 1024 && !/[\s{}]/.test(value) ? value : '';
  }

  function consented() {
    if (navigator.globalPrivacyControl === true) return false;
    try {
      if (!window.GRConsent || typeof window.GRConsent.get !== 'function') return false;
      var c = window.GRConsent.get();
      return !!(c && c.decided === true && c.advertising === true && !c.saleOptOut && !c.gpc);
    } catch (e) { return false; }
  }

  function forget() {
    try { sessionStorage.removeItem(STORAGE_KEY); sessionStorage.removeItem('reddit_ro_click_v1'); } catch (e) {}
  }

  function currentClick() {
    if (!consented()) { forget(); return null; }
    var params = new URL(window.location.href).searchParams;
    var source = (params.get('utm_source') || '').toLowerCase();
    var id = clean(params.get('ler_cid')) || clean(params.get('rdt_cid'));
    if (params.has('gclid') || params.has('wbraid') || params.has('gbraid') ||
        (source && source !== 'reddit')) {
      forget();
      return null;
    }
    if (id || source === 'reddit') {
      // Replace the entire record so a new creative never inherits an old click.
      var record = { click: id, campaign: tag(params.get('utm_campaign')),
        creative: tag(params.get('utm_content')) };
      try { sessionStorage.setItem(STORAGE_KEY, JSON.stringify(record)); } catch (e) {}
      return record;
    }
    try {
      var stored = JSON.parse(sessionStorage.getItem(STORAGE_KEY));
      return stored && { click: clean(stored.click), campaign: tag(stored.campaign),
        creative: tag(stored.creative) };
    } catch (e) { return null; }
  }

  function tag(value) {
    return typeof value === 'string' && /^[a-zA-Z0-9_-]{1,100}$/.test(value) ? value : '';
  }

  function isRoLink(anchor) {
    try {
      var u = new URL(anchor.getAttribute('href'), window.location.href);
      return u.protocol === 'https:' && u.hostname === 'go.glp1reviewguide.com' &&
        u.pathname === '/ZZ2GX/711W2G/';
    } catch (e) { return false; }
  }

  function update() {
    var record = currentClick();
    document.querySelectorAll('a[href]').forEach(function (a) {
      if (!isRoLink(a)) return;
      var u = new URL(a.getAttribute('href'), window.location.href);
      if (!originalSources.has(a)) originalSources.set(a, u.searchParams.get('source_id'));
      if (record) {
        // Google runs first; discard stale Google slots for this Reddit click.
        for (var i = 1; i <= 10; i++) u.searchParams.delete('sub' + i);
        u.searchParams.delete('wbraid');
        u.searchParams.delete('gbraid');
        if (record.click) {
          u.searchParams.set('source_id', record.click);
          u.searchParams.set('sub1', record.click);
        } else u.searchParams.delete('source_id');
        if (record.campaign) u.searchParams.set('sub2', record.campaign);
        if (record.creative) u.searchParams.set('sub3', record.creative);
        u.searchParams.set('sub5', 'reddit');
        decorated.add(a);
      } else {
        // Google's earlier listener owns Sub IDs when its click is present.
        var p = new URL(window.location.href).searchParams;
        if (decorated.has(a) && !p.has('gclid') && !p.has('wbraid') && !p.has('gbraid')) {
          for (var j = 1; j <= 10; j++) u.searchParams.delete('sub' + j);
        }
        decorated.delete(a);
        var original = originalSources.get(a);
        if (original === null) u.searchParams.delete('source_id');
        else u.searchParams.set('source_id', original);
      }
      a.href = u.toString();
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', update);
  else update();
  document.addEventListener('gr:consent', update);
  // Loaded AFTER the Google script so its Google-field updates run first.
  document.addEventListener('click', function (event) {
    var anchor = event.target && event.target.closest && event.target.closest('a[href]');
    if (anchor && isRoLink(anchor)) update();
  }, true);
  document.addEventListener('auxclick', function (event) {
    var anchor = event.target && event.target.closest && event.target.closest('a[href]');
    if (anchor && isRoLink(anchor)) update();
  }, true);
})();
