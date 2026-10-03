(function () {
  'use strict';
  var KEYS = ['gclid','campaignid','adgroupid','creative','keyword','matchtype','device','network','placement','targetid'];
  var SUBS = ['sub1','sub2','sub3','sub4','sub5','sub6','sub7','sub8','sub9','sub10'];
  var params = new URLSearchParams(window.location.search);

  // Ad click attribution runs unless the visitor has opted out:
  // "Reject non-essential", advertising turned off in Cookie settings,
  // the opt-out toggle on Your Privacy Choices, or a Global Privacy Control signal.
  function allowed() {
    if (navigator.globalPrivacyControl === true) return false;
    if (!window.GRConsent) return false;
    return !window.GRConsent.get().saleOptOut;
  }
  function clearStored() {
    try { KEYS.forEach(function (k) { sessionStorage.removeItem('glp1_' + k); }); } catch (e) {}
  }
  function store() {
    try { KEYS.forEach(function (k) { var v = params.get(k); if (v) sessionStorage.setItem('glp1_' + k, v); }); } catch (e) {}
  }
  function val(k) {
    var v = params.get(k); if (v) return v;
    try { return sessionStorage.getItem('glp1_' + k) || ''; } catch (e) { return ''; }
  }
  function update() {
    var ok = allowed();
    if (ok) store(); else clearStored();
    document.querySelectorAll('a[href*="go.glp1reviewguide.com"]').forEach(function (a) {
      try {
        var u = new URL(a.getAttribute('href'), window.location.origin);
        SUBS.forEach(function (s, i) {
          var v = ok ? val(KEYS[i]) : '';
          if (v) u.searchParams.set(s, v); else u.searchParams.delete(s);   // never send literal {macros}
        });
        a.href = u.toString();
      } catch (e) {}
    });
  }
  // consent.js loads with "defer", so wait for DOMContentLoaded before reading GRConsent.
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', update); else update();
  document.addEventListener('gr:consent', update);
})();
