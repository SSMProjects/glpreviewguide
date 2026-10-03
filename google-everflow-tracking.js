(function () {
  'use strict';
  var KEYS = ['gclid','campaignid','adgroupid','creative','keyword','matchtype','device','network','placement','targetid'];
  var SUBS = ['sub1','sub2','sub3','sub4','sub5','sub6','sub7','sub8','sub9','sub10'];
  var params = new URLSearchParams(window.location.search);
  // Bing click ID goes into sub1 when there is no gclid
  if (!params.get('gclid') && params.get('msclkid')) params.set('gclid', params.get('msclkid'));
  function canTrack() {
    return !!(window.GRConsent && window.GRConsent.get().advertising);
  }
  function save() {
    if (!canTrack()) return;
    KEYS.forEach(function (k) { var v = params.get(k); if (v) { try { sessionStorage.setItem('glp1_' + k, v); } catch (e) {} } });
  }
  function val(k) {
    if (!canTrack()) return '';
    var v = params.get(k); if (v) return v;
    try { return sessionStorage.getItem('glp1_' + k) || ''; } catch (e) { return ''; }
  }
  function update() {
    save();
    document.querySelectorAll('a[href*="go.glp1reviewguide.com"]').forEach(function (a) {
      try {
        var u = new URL(a.getAttribute('href'), window.location.origin);
        SUBS.forEach(function (s, i) {
          var v = val(KEYS[i]);
          if (v) u.searchParams.set(s, v); else u.searchParams.delete(s);
        });
        a.href = u.toString();
      } catch (e) {}
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', update); else update();
  document.addEventListener('gr:consent', update);
})();
