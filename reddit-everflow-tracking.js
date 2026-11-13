(function () {
  'use strict';

  // Applies only to the Ro affiliate links on a page that loads this script.
  // Does not send conversion events or change any Google Sub ID fields.
  var STORAGE_KEY = 'reddit_ro_click_v1';
  var originalSources = new WeakMap();

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
    try { sessionStorage.removeItem(STORAGE_KEY); } catch (e) {}
  }

  function currentClick() {
    if (!consented()) { forget(); return ''; }
    var params = new URL(window.location.href).searchParams;
    var id = clean(params.get('ler_cid')) || clean(params.get('rdt_cid'));
    // A new Google click must not inherit a previous Reddit click ID.
    if (params.has('gclid') || params.has('wbraid') || params.has('gbraid')) {
      forget();
      return '';
    }
    if (id) {
      try { sessionStorage.setItem(STORAGE_KEY, id); } catch (e) {}
      return id;
    }
    try { return clean(sessionStorage.getItem(STORAGE_KEY)); } catch (e) { return ''; }
  }

  function isRoLink(anchor) {
    try {
      var u = new URL(anchor.getAttribute('href'), window.location.href);
      return u.protocol === 'https:' && u.hostname === 'go.glp1reviewguide.com' &&
        u.pathname === '/ZZ2GX/711W2G/';
    } catch (e) { return false; }
  }

  function update() {
    var id = currentClick();
    document.querySelectorAll('a[href]').forEach(function (a) {
      if (!isRoLink(a)) return;
      var u = new URL(a.getAttribute('href'), window.location.href);
      if (!originalSources.has(a)) originalSources.set(a, u.searchParams.get('source_id'));
      if (id) {
        u.searchParams.set('source_id', id);
      } else {
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
