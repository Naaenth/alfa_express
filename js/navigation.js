(function () {
  'use strict';

  var toggle   = document.getElementById('nav-toggle');
  var mobileNav = document.getElementById('mobile-nav');
  var overlay  = document.getElementById('nav-overlay');
  var closeBtn = document.getElementById('mobile-nav-close');
  var header   = document.getElementById('site-header');

  /* ---------- Mobile nav open / close ------------------------------------ */
  function openNav() {
    mobileNav.classList.add('is-open');
    overlay.removeAttribute('hidden');
    requestAnimationFrame(function () {
      overlay.classList.add('is-visible');
    });
    if (toggle)    toggle.setAttribute('aria-expanded', 'true');
    if (mobileNav) mobileNav.setAttribute('aria-hidden', 'false');
    document.body.classList.add('no-scroll');
  }

  function closeNav() {
    mobileNav.classList.remove('is-open');
    overlay.classList.remove('is-visible');
    if (toggle)    toggle.setAttribute('aria-expanded', 'false');
    if (mobileNav) mobileNav.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('no-scroll');
    setTimeout(function () {
      if (overlay) overlay.setAttribute('hidden', '');
    }, 250);
  }

  if (toggle)   toggle.addEventListener('click', openNav);
  if (closeBtn) closeBtn.addEventListener('click', closeNav);
  if (overlay)  overlay.addEventListener('click', closeNav);

  /* Close on Escape key */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && mobileNav && mobileNav.classList.contains('is-open')) {
      closeNav();
    }
  });

  /* ---------- Scroll shadow on header ------------------------------------ */
  if (header) {
    window.addEventListener('scroll', function () {
      header.classList.toggle('scrolled', window.scrollY > 10);
    }, { passive: true });
  }

  /* ---------- Accordion (contact/FAQ page) ------------------------------- */
  /* Panels ship with a [hidden] attribute (display:none !important) which would
     block the max-height animation — strip it so CSS max-height:0 controls them. */
  document.querySelectorAll('.accordion-panel').forEach(function (panel) {
    panel.removeAttribute('hidden');
  });

  document.querySelectorAll('.accordion-trigger').forEach(function (trigger) {
    trigger.addEventListener('click', function () {
      var isExpanded = this.getAttribute('aria-expanded') === 'true';

      /* Close all panels first */
      document.querySelectorAll('.accordion-trigger').forEach(function (t) {
        t.setAttribute('aria-expanded', 'false');
        var panel = t.closest('.accordion-item').querySelector('.accordion-panel');
        if (panel) panel.style.maxHeight = null;
      });

      /* Open the clicked one if it was closed */
      if (!isExpanded) {
        this.setAttribute('aria-expanded', 'true');
        var panel = this.closest('.accordion-item').querySelector('.accordion-panel');
        if (panel) panel.style.maxHeight = panel.scrollHeight + 'px';
      }
    });
  });

  /* ---------- Active nav link highlight ---------------------------------- */
  /* Pretty-URL hosts drop the .html suffix, so compare extension-agnostic keys. */
  function pageKey(path) {
    var p = (path.split(/[?#]/)[0].split('/').pop() || '').toLowerCase().replace(/\.html$/, '');
    return p || 'index';
  }
  var currentPage = pageKey(window.location.pathname);
  document.querySelectorAll('.nav-list a, .mobile-nav-list a').forEach(function (link) {
    var href = link.getAttribute('href');
    if (pageKey(href) === currentPage) {
      link.setAttribute('aria-current', 'page');
    } else {
      link.removeAttribute('aria-current');
    }
  });

}());
