(function () {
  'use strict';

  /* Language switching for the legal pages (Privacy Policy / Terms of Use).
     Unlike the rest of the site — which translates text in place from a
     dictionary — each legal document exists as its own full-page file per
     language (e.g. privacy.html / privacy-pl.html / privacy-uk.html).
     So here the EN/UK/PL buttons NAVIGATE between those files, and we keep
     the choice in sync with the site-wide language stored in localStorage. */

  var STORAGE_KEY = 'alfaLang';
  var SUPPORTED = ['en', 'uk', 'pl'];

  /* Hosts with "pretty URLs" (Netlify, Cloudflare Pages…) serve these pages
     extensionless (/terms instead of /terms.html), so the .html suffix and a
     trailing slash are both optional. Generated URLs keep the same style. */
  var m = location.pathname.match(/^(.*\/)(privacy|terms)(?:-(pl|uk))?(\.html)?\/?$/i);
  if (!m) return;                       // not a localized legal page — do nothing

  var dir = m[1];                       // path up to the file name
  var base = m[2].toLowerCase();        // "privacy" or "terms"
  var current = (m[3] || 'en').toLowerCase(); // language of THIS file
  var ext = m[4] || '';                 // ".html" locally, "" on pretty-URL hosts

  function urlFor(lang) {
    return dir + (lang === 'en' ? base : base + '-' + lang) + ext;
  }

  /* If the visitor already chose a language elsewhere on the site, keep the
     legal page in the same language by redirecting to the matching file. */
  var saved = null;
  try { saved = localStorage.getItem(STORAGE_KEY); } catch (e) {}
  if (saved && SUPPORTED.indexOf(saved) !== -1 && saved !== current) {
    location.replace(urlFor(saved));
    return;
  }

  /* Reflect the current file's language in the button state. */
  function markActive() {
    document.querySelectorAll('.lang-btn').forEach(function (b) {
      var on = b.getAttribute('data-lang') === current;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }

  /* Capture-phase handler runs before i18n.js's own click listener, so we can
     take over the button and navigate instead of translating in place. */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest ? e.target.closest('.lang-btn') : null;
    if (!btn) return;
    var lang = btn.getAttribute('data-lang');
    if (!lang || SUPPORTED.indexOf(lang) === -1) return;
    e.stopPropagation();
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e2) {}
    if (lang !== current) location.href = urlFor(lang);
  }, true);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', markActive);
  } else {
    markActive();
  }
}());
