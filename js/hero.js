/* ============================================================
   HERO ANIMATION
   The typing effect and the scroll-reveal entrance, carried over
   from the original single-page site and made reusable.

   A page opts in by putting these in its HTML:

     <span class="typedText" data-strings="one|two|three"></span>
       -> types through the strings, looping

     <div data-reveal>                     -> fades in on scroll
     <div data-reveal data-reveal-group>   -> children fade in in sequence

   Both libraries are optional. If a CDN fails to load, the page
   still renders correctly with everything visible.
   ============================================================ */

(function () {
  'use strict';

  var reduceMotion = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ----- TYPING EFFECT ----- */
  var typedEl = document.querySelector('.typedText');

  if (typedEl) {
    var strings = (typedEl.getAttribute('data-strings') || '')
      .split('|')
      .map(function (s) { return s.trim(); })
      .filter(Boolean);

    if (strings.length === 0) {
      /* Nothing to type. Leave whatever is already in the HTML. */
    } else if (reduceMotion || typeof window.Typed === 'undefined') {
      /* No animation: show the first string so the sentence still reads. */
      typedEl.textContent = strings[0];
    } else {
      new window.Typed(typedEl, {
        strings: strings,
        loop: true,
        typeSpeed: 100,
        backSpeed: 80,
        backDelay: 2000,
        smartBackspace: false,
        showCursor: false
      });
    }
  }

  /* ----- SCROLL REVEAL ----- */
  if (reduceMotion || typeof window.ScrollReveal === 'undefined') return;

  var sr = window.ScrollReveal({
    origin: 'top',
    distance: '40px',
    duration: 900,
    easing: 'cubic-bezier(0.4, 0, 0.2, 1)',
    /* reset:false so elements animate once. The original site used
       reset:true, which re-ran the animation on every scroll up. That
       reads as a glitch when moving between pages. */
    reset: false,
    mobile: true
  });

  sr.reveal('[data-reveal]', { interval: 90 });
  sr.reveal('[data-reveal-group] > *', { interval: 90 });
})();
