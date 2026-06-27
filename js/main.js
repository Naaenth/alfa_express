(function () {
  'use strict';

  /* ---------- AOS (Animate On Scroll) ------------------------------------ */
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 650,
      once: true,
      offset: 60,
      easing: 'ease-out-cubic'
    });
  }

  /* ---------- Swiper carousels ------------------------------------------- */
  if (typeof Swiper !== 'undefined') {

    /* Testimonials */
    if (document.querySelector('.testimonials-swiper')) {
      new Swiper('.testimonials-swiper', {
        slidesPerView: 1,
        spaceBetween: 24,
        loop: true,
        autoplay: { delay: 5500, disableOnInteraction: false },
        pagination: { el: '.testimonials-swiper .swiper-pagination', clickable: true },
        navigation: {
          nextEl: '.testimonials-swiper .swiper-button-next',
          prevEl: '.testimonials-swiper .swiper-button-prev'
        },
        breakpoints: {
          720: { slidesPerView: 2 },
          1024: { slidesPerView: 3 }
        }
      });
    }

    /* Fleet slider */
    if (document.querySelector('.fleet-swiper')) {
      new Swiper('.fleet-swiper', {
        slidesPerView: 1,
        spaceBetween: 24,
        loop: true,
        pagination: { el: '.fleet-swiper .swiper-pagination', clickable: true },
        navigation: {
          nextEl: '.fleet-swiper .swiper-button-next',
          prevEl: '.fleet-swiper .swiper-button-prev'
        },
        breakpoints: {
          640:  { slidesPerView: 2 },
          1024: { slidesPerView: 3 }
        }
      });
    }
  }

  /* ---------- Animated stat counters ------------------------------------- */
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

  function animateCounters() {
    document.querySelectorAll('.stat-number[data-count]').forEach(function (el) {
      var target   = parseInt(el.getAttribute('data-count'), 10);
      var suffix   = el.getAttribute('data-suffix') || '';
      var duration = 1800;
      var start    = null;

      function step(ts) {
        if (!start) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        var value    = Math.floor(easeOut(progress) * target);
        el.textContent = value.toLocaleString() + suffix;
        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          el.textContent = target.toLocaleString() + suffix;
        }
      }
      requestAnimationFrame(step);
    });
  }

  var statsSection = document.querySelector('.stats');
  if (statsSection) {
    var counted = false;
    var io = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting && !counted) {
        counted = true;
        animateCounters();
      }
    }, { threshold: 0.3 });
    io.observe(statsSection);
  }

  /* ---------- Footer copyright year -------------------------------------- */
  var yearEl = document.getElementById('current-year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- Contact form (demo handler) --------------------------------- */
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      /* Basic required-field validation */
      var valid = true;
      form.querySelectorAll('[required]').forEach(function (field) {
        var wrap = field.closest('.form-field');
        var errEl = wrap && wrap.querySelector('.field-error');
        if (!field.value.trim()) {
          valid = false;
          if (wrap) wrap.classList.add('invalid');
          if (errEl) errEl.textContent = 'This field is required.';
        } else {
          if (wrap) wrap.classList.remove('invalid');
          if (errEl) errEl.textContent = '';
        }
      });
      if (!valid) return;

      var submitBtn = form.querySelector('[type="submit"]');
      var statusEl  = document.getElementById('form-status');
      var origText  = submitBtn.textContent;

      submitBtn.classList.add('is-loading');
      submitBtn.textContent = 'Sending…';

      /* Simulate submission */
      setTimeout(function () {
        submitBtn.classList.remove('is-loading');
        submitBtn.textContent = origText;
        if (statusEl) {
          statusEl.className  = 'form-status is-success';
          statusEl.textContent = 'Thank you! Your message has been received. Our team will get back to you within one business day.';
        }
        form.reset();
      }, 1600);
    });

    /* Live validation — clear error on re-input */
    form.querySelectorAll('[required]').forEach(function (field) {
      field.addEventListener('input', function () {
        var wrap  = field.closest('.form-field');
        var errEl = wrap && wrap.querySelector('.field-error');
        if (field.value.trim()) {
          if (wrap)  wrap.classList.remove('invalid');
          if (errEl) errEl.textContent = '';
        }
      });
    });
  }

}());
