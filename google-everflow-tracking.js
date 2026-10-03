(function () {
  'use strict';

  var keys = [
    'gclid',
    'campaignid',
    'adgroupid',
    'creative',
    'keyword',
    'matchtype',
    'device',
    'network',
    'placement',
    'targetid'
  ];

  var params = new URLSearchParams(window.location.search);

  keys.forEach(function (key) {
    var value = params.get(key);
    if (value) {
      sessionStorage.setItem('glp1_' + key, value);
    }
  });

  function getValue(key) {
    return params.get(key) ||
           sessionStorage.getItem('glp1_' + key) ||
           '';
  }

  var mapping = {
    sub1: getValue('gclid'),
    sub2: getValue('campaignid'),
    sub3: getValue('adgroupid'),
    sub4: getValue('creative'),
    sub5: getValue('keyword'),
    sub6: getValue('matchtype'),
    sub7: getValue('device'),
    sub8: getValue('network'),
    sub9: getValue('placement'),
    sub10: getValue('targetid')
  };

  function updateEverflowLinks() {
    document.querySelectorAll('a[href*="go.glp1reviewguide.com"]').forEach(function (link) {
      try {
        var url = new URL(link.href, window.location.origin);

        Object.keys(mapping).forEach(function (sub) {
          if (mapping[sub]) {
            url.searchParams.set(sub, mapping[sub]);
          }
        });

        link.href = url.toString();
      } catch (e) {
        console.error('Everflow tracking URL error:', e);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateEverflowLinks);
  } else {
    updateEverflowLinks();
  }
})();
