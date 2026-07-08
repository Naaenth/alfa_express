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

  /* ---------- Contact form (EmailJS delivery) ----------------------------- */
  var form = document.getElementById('contact-form');
  if (form) {
    var statusEl = document.getElementById('form-status');
    var EMAIL = 'central.alfa.express@gmail.com';

    function fieldValid(field) {
      return field.type === 'checkbox' ? field.checked : !!field.value.trim();
    }
    function markField(field, ok) {
      var wrap  = field.closest('.form-field');
      var errEl = wrap && wrap.querySelector('.field-error');
      if (wrap)  wrap.classList.toggle('invalid', !ok);
      if (errEl) errEl.textContent = ok ? '' : 'This field is required.';
    }
    function setStatus(kind, msg) {
      if (!statusEl) return;
      statusEl.className = 'form-status' + (kind ? ' ' + kind : '');
      statusEl.textContent = msg;
    }
    /* Config is live only once all three placeholders have been replaced. */
    function emailjsReady() {
      var c = window.EMAILJS_CONFIG;
      return !!(window.emailjs && c &&
        c.publicKey.indexOf('YOUR_')  !== 0 &&
        c.serviceId.indexOf('YOUR_')  !== 0 &&
        c.templateId.indexOf('YOUR_') !== 0);
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      /* Honeypot: a ticked hidden field means a bot — drop silently. */
      if (form.botcheck && form.botcheck.checked) return;

      /* Required-field validation */
      var valid = true;
      form.querySelectorAll('[required]').forEach(function (field) {
        var ok = fieldValid(field);
        if (!ok) valid = false;
        markField(field, ok);
      });
      if (!valid) return;

      var submitBtn = form.querySelector('[type="submit"]');
      var origText  = submitBtn.textContent;

      function reset() {
        submitBtn.classList.remove('is-loading');
        submitBtn.disabled = false;
        submitBtn.textContent = origText;
      }

      submitBtn.classList.add('is-loading');
      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending…';
      setStatus('', '');

      if (!emailjsReady()) {
        reset();
        setStatus('is-error', 'The form is not connected yet. Please email us directly at ' + EMAIL + '.');
        return;
      }

      emailjs.sendForm(window.EMAILJS_CONFIG.serviceId, window.EMAILJS_CONFIG.templateId, form)
        .then(function () {
          reset();
          setStatus('is-success', 'Thank you! Your message has been sent. Our team will get back to you within one business day.');
          form.reset();
        })
        .catch(function () {
          reset();
          setStatus('is-error', 'Sorry, something went wrong. Please try again or email ' + EMAIL + '.');
        });
    });

    /* Live validation — clear the error as soon as the field becomes valid */
    form.querySelectorAll('[required]').forEach(function (field) {
      var evt = (field.tagName === 'SELECT' || field.type === 'checkbox') ? 'change' : 'input';
      field.addEventListener(evt, function () {
        if (fieldValid(field)) markField(field, true);
      });
    });
  }

}());
