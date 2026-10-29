// That Foodie Lawyer — site behaviour
(function () {
  var header = document.querySelector('.site-header');
  var onScroll = function () { header && header.classList.toggle('scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); });
    });
  }

  // Fade-in on scroll
  var fades = document.querySelectorAll('.fade');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    fades.forEach(function (el) { io.observe(el); });
  } else { fades.forEach(function (el) { el.classList.add('in'); }); }

  // Contact form (Netlify Forms)
  var form = document.getElementById('contact-form');
  if (form) {
    var params = new URLSearchParams(location.search);
    var sel = form.querySelector('select[name="topic"]');
    var topic = params.get('topic'), service = params.get('service');
    if (topic && sel) Array.prototype.forEach.call(sel.options, function (o) { if (o.value === topic) sel.value = topic; });
    if (service) {
      var msg = form.querySelector('textarea[name="message"]');
      if (msg && !msg.value) msg.value = 'I would like to ask about: ' + service + '\n\n';
      if (sel) sel.value = 'Advisory';
    }
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var status = form.querySelector('.form-status');
      var btn = form.querySelector('button[type="submit"]');
      status.className = 'form-status'; status.textContent = 'Sending...'; btn.disabled = true;
      fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(new FormData(form)).toString() })
        .then(function (r) { if (!r.ok) throw new Error(); })
        .then(function () { form.reset(); status.className = 'form-status ok'; status.textContent = 'Thank you. Your message is on its way and I will be in touch soon.'; })
        .catch(function () { status.className = 'form-status err'; status.innerHTML = 'Something went wrong. Please email me directly at <a href="mailto:foodie@thatfoodielawyer.com">foodie@thatfoodielawyer.com</a>.'; })
        .finally(function () { btn.disabled = false; });
    });
  }

  // Calendly booking embed
  var cal = document.querySelector('.calendly-inline-widget');
  if (cal) {
    var url = cal.getAttribute('data-url') || '';
    if (url.indexOf('REPLACE_WITH') !== -1) {
      cal.outerHTML = '<div class="fallback"><h3>Booking calendar coming soon</h3><p>Online booking is being set up. In the meantime, email <a href="mailto:foodie@thatfoodielawyer.com">foodie@thatfoodielawyer.com</a> to arrange your Strategy Call.</p></div>';
    } else {
      var s = document.createElement('script');
      s.src = 'https://assets.calendly.com/assets/external/widget.js'; s.async = true;
      document.body.appendChild(s);
      window.addEventListener('message', function (e) {
        if (e.origin === 'https://calendly.com' && e.data && e.data.event === 'calendly.event_scheduled') {
          var c = document.querySelector('.confirm'); if (c) c.classList.add('show');
        }
      });
    }
  }
})();

// Newsletter signup (Kit): submit in place, fall back to a normal form post if anything fails
document.querySelectorAll('form[data-kit]').forEach(function (form) {
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var status = form.querySelector('.nl-status');
    var btn = form.querySelector('button');
    btn.disabled = true; status.className = 'nl-status'; status.textContent = 'Subscribing...';
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
      .then(function () {
        form.reset(); status.className = 'nl-status ok';
        status.textContent = 'Thank you! Check your inbox to confirm your subscription.';
      })
      .catch(function () { form.removeAttribute('data-kit'); form.submit(); })
      .finally(function () { btn.disabled = false; });
  });
});
