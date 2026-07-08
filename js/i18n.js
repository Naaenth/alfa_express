(function () {
  'use strict';

  var STORAGE_KEY = 'alfaLang';
  var SUPPORTED = ['en', 'uk', 'pl'];

  /* Dictionaries are keyed by the normalised English source text and supplied
     by js/i18n-data.js (loaded first). Anything without an entry stays in its
     original language. */
  var DATA = window.ALFA_DICT || {};
  var T = { pl: DATA.pl || {}, uk: DATA.uk || {} };
  var TITLES = DATA.titles || {};

  /* Helpers ---------------------------------------------------------------- */
  function norm(s) { return s.replace(/\s+/g, ' ').trim(); }
  function pick(dict, key) {
    return (dict && Object.prototype.hasOwnProperty.call(dict, key)) ? dict[key] : null;
  }

  /* Snapshot translatable text nodes once (originals preserved) ------------ */
  var nodes = [];
  (function collect() {
    if (!document.body) return;
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue || !norm(n.nodeValue)) return NodeFilter.FILTER_REJECT;
        var p = n.parentNode;
        if (!p) return NodeFilter.FILTER_REJECT;
        var tag = (p.nodeName || '').toLowerCase();
        if (tag === 'script' || tag === 'style' || tag === 'noscript') return NodeFilter.FILTER_REJECT;
        if (p.classList && p.classList.contains('lang-btn')) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var n;
    while ((n = walker.nextNode())) {
      nodes.push({ node: n, raw: n.nodeValue, key: norm(n.nodeValue) });
    }
  })();

  /* Snapshot translatable attributes -------------------------------------- */
  var attrs = [];
  (function collectAttrs() {
    document.querySelectorAll('[placeholder]').forEach(function (el) {
      var v = el.getAttribute('placeholder');
      if (v && norm(v)) attrs.push({ el: el, attr: 'placeholder', raw: v, key: norm(v) });
    });
  })();

  var baseTitle = document.title;

  /* Apply ------------------------------------------------------------------ */
  function applyText(item, dict) {
    if (!dict) { item.node.nodeValue = item.raw; return; }
    var t = pick(dict, item.key);
    if (t == null) { item.node.nodeValue = item.raw; return; }
    var lead = item.raw.match(/^\s*/)[0];
    var trail = item.raw.match(/\s*$/)[0];
    item.node.nodeValue = lead + t + trail;
  }
  function applyAttr(item, dict) {
    if (!dict) { item.el.setAttribute(item.attr, item.raw); return; }
    var t = pick(dict, item.key);
    item.el.setAttribute(item.attr, t == null ? item.raw : t);
  }
  function setActive(lang) {
    document.querySelectorAll('.lang-btn').forEach(function (b) {
      var on = b.getAttribute('data-lang') === lang;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }
  /* Point footer legal links (Privacy / Terms) at the current language's file
     variant, so they open the matching translation directly. */
  function rewriteLegalLinks(lang) {
    document.querySelectorAll('.footer-legal a[href]').forEach(function (a) {
      var mm = (a.getAttribute('href') || '').match(/(privacy|terms)(?:-(?:pl|uk))?\.html$/);
      if (!mm) return;
      var base = mm[1];
      a.setAttribute('href', lang === 'en' ? base + '.html' : base + '-' + lang + '.html');
    });
  }
  function apply(lang) {
    if (SUPPORTED.indexOf(lang) === -1) lang = 'en';
    var dict = (lang === 'en') ? null : T[lang];
    nodes.forEach(function (it) { applyText(it, dict); });
    attrs.forEach(function (it) { applyAttr(it, dict); });
    var tt = TITLES[baseTitle];
    document.title = (dict && tt && tt[lang]) ? tt[lang] : baseTitle;
    document.documentElement.setAttribute('lang', lang);
    setActive(lang);
    rewriteLegalLinks(lang);
  }

  /* Init + wire-up --------------------------------------------------------- */
  var saved = 'en';
  try { saved = localStorage.getItem(STORAGE_KEY) || 'en'; } catch (e) {}
  apply(saved);

  document.addEventListener('click', function (e) {
    var btn = e.target.closest ? e.target.closest('.lang-btn') : null;
    if (!btn) return;
    var lang = btn.getAttribute('data-lang');
    if (!lang) return;
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e2) {}
    apply(lang);
  });

}());
