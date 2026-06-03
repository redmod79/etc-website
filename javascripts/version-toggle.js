(function () {
  var STORAGE_KEY = 'study-version';
  var DEFAULT_VERSION = 'v1';
  var LABELS = { v1: 'Original', v2: 'v2 (BS8)' };

  function getVersion() {
    try { return localStorage.getItem(STORAGE_KEY) || DEFAULT_VERSION; }
    catch (e) { return DEFAULT_VERSION; }
  }

  function setVersion(v) {
    try { localStorage.setItem(STORAGE_KEY, v); } catch (e) {}
    applyVersion(v);
  }

  function applyVersion(v) {
    var blocks = document.querySelectorAll('.version-content');
    blocks.forEach(function (el) {
      el.style.display = el.getAttribute('data-version') === v ? '' : 'none';
    });

    var btn = document.getElementById('version-toggle-btn');
    if (btn) {
      btn.textContent = LABELS[v] || v;
      btn.title = 'Viewing ' + (LABELS[v] || v) + ' — click to switch';
      btn.setAttribute('data-current', v);
    }
  }

  function initToggle() {
    var blocks = document.querySelectorAll('.version-content');
    var container = document.getElementById('version-toggle-container');

    if (blocks.length === 0) {
      if (container) container.style.display = 'none';
      return;
    }

    if (container) container.style.display = '';

    var btn = document.getElementById('version-toggle-btn');
    if (btn && !btn.hasAttribute('data-bound')) {
      btn.setAttribute('data-bound', '1');
      btn.addEventListener('click', function () {
        var current = getVersion();
        setVersion(current === 'v1' ? 'v2' : 'v1');
      });
    }

    applyVersion(getVersion());
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initToggle);
  } else {
    initToggle();
  }

  // MkDocs Material instant loading support
  if (typeof document$ !== 'undefined') {
    document$.subscribe(function () { initToggle(); });
  } else {
    // Fallback: observe body for MkDocs instant navigation
    var observer = new MutationObserver(function (mutations) {
      for (var i = 0; i < mutations.length; i++) {
        if (mutations[i].type === 'childList' &&
            mutations[i].target.classList &&
            mutations[i].target.classList.contains('md-content')) {
          initToggle();
          break;
        }
      }
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }
})();
