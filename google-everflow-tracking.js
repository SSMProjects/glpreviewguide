(function () {
  'use strict';

  var CLICK_ID_KEYS = ['gclid', 'wbraid', 'gbraid'];
  var ATTR_KEYS = ['campaignid', 'adgroupid', 'creative', 'keyword', 'matchtype', 'device', 'network', 'placement', 'targetid'];
  var ALL_ATTR_KEYS = ['gclid', 'wbraid', 'gbraid'].concat(ATTR_KEYS);

  var KEYS = ['gclid', 'campaignid', 'adgroupid', 'creative', 'keyword', 'matchtype', 'device', 'network', 'placement', 'targetid'];
  var SUBS = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9', 'sub10'];

  function isMacro(v) {
    if (!v || typeof v !== 'string') return true;
    var s = v.trim();
    if (!s) return true;
    return s.indexOf('{') !== -1 || s.indexOf('}') !== -1 ||
           s.indexOf('%7B') !== -1 || s.indexOf('%7D') !== -1 ||
           s.indexOf('%7b') !== -1 || s.indexOf('%7d') !== -1;
  }

  function cleanValue(v) {
    if (!v || typeof v !== 'string') return '';
    var s = v.trim();
    if (isMacro(s)) return '';
    return s;
  }

  // Affirmative advertising consent check:
  // Requires explicit decision, advertising enabled, no sale opt-out, and no Global Privacy Control (GPC).
  function hasAdvertisingConsent() {
    if (navigator.globalPrivacyControl === true) return false;
    if (window.GRConsent && typeof window.GRConsent.get === 'function') {
      var c = window.GRConsent.get();
      return !!(c && c.decided === true && c.advertising === true && !c.saleOptOut && !c.gpc);
    }
    try {
      var m = document.cookie.match(/(?:^|; )gr_consent=([^;]*)/);
      if (m) {
        var p = JSON.parse(decodeURIComponent(m[1]));
        return !!(p && p.advertising === true && !p.saleOptOut && !p.gpc);
      }
    } catch (e) {}
    return false;
  }

  // Remove all persisted advertising attribution across current and legacy keys.
  // Preserves functional and security storage (e.g. gr_consent).
  function clearAttributionStorage() {
    try {
      ALL_ATTR_KEYS.forEach(function (k) {
        sessionStorage.removeItem('glp1_' + k);
        sessionStorage.removeItem('gads.' + k);
        sessionStorage.removeItem('gads_' + k);
        localStorage.removeItem('glp1_' + k);
        localStorage.removeItem('gads.' + k);
        localStorage.removeItem('gads_' + k);
      });
      for (var i = sessionStorage.length - 1; i >= 0; i--) {
        var sk = sessionStorage.key(i);
        if (sk && /^(gads[._]|glp1_)/.test(sk)) {
          sessionStorage.removeItem(sk);
        }
      }
      for (var j = localStorage.length - 1; j >= 0; j--) {
        var lk = localStorage.key(j);
        if (lk && /^(gads[._]|glp1_)/.test(lk)) {
          localStorage.removeItem(lk);
        }
      }
    } catch (e) {}
  }

  function getUrlParam(k) {
    try {
      var params = new URLSearchParams(window.location.search);
      var raw = params.get(k);
      if (!raw) return '';
      return cleanValue(raw);
    } catch (e) {
      return '';
    }
  }

  function getStoredParam(k) {
    try {
      var v = sessionStorage.getItem('glp1_' + k);
      return cleanValue(v);
    } catch (e) {
      return '';
    }
  }

  function getIncomingClick() {
    for (var i = 0; i < CLICK_ID_KEYS.length; i++) {
      var key = CLICK_ID_KEYS[i];
      var val = getUrlParam(key);
      if (val) return { key: key, value: val };
    }
    return null;
  }

  function getStoredClick() {
    for (var i = 0; i < CLICK_ID_KEYS.length; i++) {
      var key = CLICK_ID_KEYS[i];
      var val = getStoredParam(key);
      if (val) return { key: key, value: val };
    }
    return null;
  }

  // Priority: current URL parameter -> valid consented stored value -> blank.
  // For Sub1 (click ID): prefers gclid, falls back to wbraid/gbraid if gclid is absent.
  function getAttributionValue(k) {
    var fromUrl = getUrlParam(k);
    if (fromUrl) return fromUrl;
    if (k === 'gclid') {
      var altFromUrl = getUrlParam('wbraid') || getUrlParam('gbraid');
      if (altFromUrl) return altFromUrl;
    }
    if (hasAdvertisingConsent()) {
      var stored = getStoredParam(k);
      if (stored) return stored;
      if (k === 'gclid') {
        return getStoredParam('wbraid') || getStoredParam('gbraid');
      }
    }
    return '';
  }

  function storeAttribution() {
    var incomingClick = getIncomingClick();
    if (incomingClick) {
      var storedClick = getStoredClick();
      // When a new Google ad click identifier arrives, clear the previous attribution record
      // before saving the new click's values so missing fields remain empty and stale values
      // from older clicks are never inherited.
      if (!storedClick || storedClick.key !== incomingClick.key || storedClick.value !== incomingClick.value) {
        clearAttributionStorage();
      }
      try {
        sessionStorage.setItem('glp1_' + incomingClick.key, incomingClick.value);
      } catch (e) {}
    }

    ATTR_KEYS.forEach(function (k) {
      var v = getUrlParam(k);
      if (v) {
        try {
          sessionStorage.setItem('glp1_' + k, v);
        } catch (e) {}
      }
    });
  }

  function updateLinks() {
    var consented = hasAdvertisingConsent();

    if (consented) {
      storeAttribution();
    } else {
      clearAttributionStorage();
    }

    var anchors = document.querySelectorAll('a[href*="go.glp1reviewguide.com"]');
    anchors.forEach(function (a) {
      try {
        var href = a.getAttribute('href');
        if (!href) return;
        var u = new URL(href, window.location.origin);
        SUBS.forEach(function (sub, idx) {
          var key = KEYS[idx];
          var val = consented ? getAttributionValue(key) : '';
          if (val) {
            u.searchParams.set(sub, val);
          } else {
            u.searchParams.delete(sub);
          }
        });
        a.href = u.toString();
      } catch (e) {}
    });
  }

  // Developer/QA test hook (no sensitive data exposed)
  window.__GLP1_TRACKING__ = {
    hasConsent: hasAdvertisingConsent,
    clearStorage: clearAttributionStorage,
    update: updateLinks,
    getIncomingClick: getIncomingClick,
    getStoredClick: getStoredClick,
    getStoredKeys: function () {
      var active = [];
      ALL_ATTR_KEYS.forEach(function (k) {
        try {
          if (sessionStorage.getItem('glp1_' + k)) active.push(k);
        } catch (e) {}
      });
      return active;
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateLinks);
  } else {
    updateLinks();
  }

  document.addEventListener('gr:consent', updateLinks);

  // Re-verify upon CTA click in case consent or parameters changed
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a[href*="go.glp1reviewguide.com"]');
    if (a) {
      updateLinks();
    }
  }, true);
})();
