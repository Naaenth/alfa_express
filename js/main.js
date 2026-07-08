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

  /* ---------- Contact form (EmailJS) -------------------------------------- */
  /* 1. Create a free account at https://www.emailjs.com
     2. Add an Email Service (e.g. Gmail) -> copy its SERVICE ID
     3. Create an Email Template using {{name}} {{email}} {{phone}}
        {{subject_line}} {{message}} -> copy its TEMPLATE ID
     4. Account > General -> copy your PUBLIC KEY
     5. Paste all three below. Until then the form runs in demo mode. */
  var EMAILJS = {
    publicKey:  'mxU1MTRL9WN6OQLwm',
    serviceId:  'service_ogqtr0w',
    templateId: 'template_3ran6mq'
  };
  var emailjsReady =
    typeof emailjs !== 'undefined' &&
    EMAILJS.publicKey.indexOf('YOUR_') !== 0 &&
    EMAILJS.serviceId.indexOf('YOUR_') !== 0 &&
    EMAILJS.templateId.indexOf('YOUR_') !== 0;

  if (emailjsReady) emailjs.init({ publicKey: EMAILJS.publicKey });

  var form = document.getElementById('contact-form');
  if (form) {

    function fieldFilled(field) {
      return field.type === 'checkbox' ? field.checked : !!field.value.trim();
    }
    function errorElFor(field) {
      return form.querySelector('.field-error[data-error-for="' + field.id + '"]') ||
             (field.closest('.form-field') || {}).querySelector &&
             field.closest('.form-field').querySelector('.field-error');
    }
    function setFieldState(field, ok) {
      var wrap  = field.closest('.form-field');
      var errEl = errorElFor(field);
      if (wrap) wrap.classList.toggle('invalid', !ok);
      if (errEl) errEl.textContent = ok ? '' : 'This field is required.';
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      /* Required-field validation (checkbox-aware) */
      var valid = true;
      form.querySelectorAll('[required]').forEach(function (field) {
        var ok = fieldFilled(field);
        if (!ok) valid = false;
        setFieldState(field, ok);
      });
      if (!valid) return;

      /* Honeypot: bots tick the hidden checkbox — pretend success, send nothing */
      var honeypot = form.querySelector('input[name="botcheck"]');

      var submitBtn = form.querySelector('[type="submit"]');
      var statusEl  = document.getElementById('form-status');
      var origText  = submitBtn.textContent;

      submitBtn.classList.add('is-loading');
      submitBtn.textContent = 'Sending…';

      function finish(ok, msg) {
        submitBtn.classList.remove('is-loading');
        submitBtn.textContent = origText;
        if (statusEl) {
          statusEl.className  = 'form-status ' + (ok ? 'is-success' : 'is-error');
          statusEl.textContent = msg;
        }
        if (ok) form.reset();
      }

      var SUCCESS_MSG = 'Thank you! Your message has been received. Our team will get back to you within one business day.';
      var ERROR_MSG   = 'Something went wrong sending your message. Please email us directly at oleksii.maryniuk@alfaexpresseu.com.';

      if (honeypot && honeypot.checked) {
        setTimeout(function () { finish(true, SUCCESS_MSG); }, 800);
        return;
      }

      if (emailjsReady) {
        /* Real submission via EmailJS — field names map to template variables */
        emailjs.sendForm(EMAILJS.serviceId, EMAILJS.templateId, form)
          .then(function () {
            finish(true, SUCCESS_MSG);
          })
          .catch(function () {
            finish(false, ERROR_MSG);
          });
      } else {
        /* EmailJS not configured yet — demo success so the site works locally */
        setTimeout(function () { finish(true, SUCCESS_MSG); }, 1200);
      }
    });

    /* Live validation — clear error as soon as the field is corrected */
    form.querySelectorAll('[required]').forEach(function (field) {
      field.addEventListener(field.type === 'checkbox' ? 'change' : 'input', function () {
        if (fieldFilled(field)) setFieldState(field, true);
      });
    });

    /* Deep link support: e.g. Careers "Apply now" -> contact.html?subject=driver
       preselects the matching subject and scrolls the form into view. */
    (function preselectSubject() {
      var subj = new URLSearchParams(location.search).get('subject');
      if (!subj) return;
      var select = form.querySelector('#subject-line');
      if (!select) return;
      var opt = subj === 'driver'
        ? select.querySelector('option[data-subject="driver"]')
        : null;
      if (!opt) {
        Array.prototype.forEach.call(select.options, function (o) {
          if (!opt && o.textContent.trim().toLowerCase() === subj.trim().toLowerCase()) opt = o;
        });
      }
      if (!opt) return;
      opt.selected = true;
      var wrap = select.closest('.form-field');
      if (wrap) wrap.classList.remove('invalid');
      if (form.scrollIntoView) form.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }());
  }

}());
