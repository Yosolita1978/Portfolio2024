/* ============================================================
   NAVIGATION
   Mobile menu toggle. The "current page" highlight is done in
   the HTML with aria-current, so it works without JavaScript.
   ============================================================ */

(function () {
  'use strict';

  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('nav-menu');

  if (!toggle || !menu) return;

  function setOpen(open) {
    menu.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  toggle.addEventListener('click', function () {
    var isOpen = toggle.getAttribute('aria-expanded') === 'true';
    setOpen(!isOpen);
  });

  /* Close the menu when a link is tapped. */
  menu.addEventListener('click', function (event) {
    if (event.target.closest('a')) setOpen(false);
  });

  /* Close on Escape, and return focus to the button. */
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });

  /* If the window grows past the mobile breakpoint while the menu is
     open, clear the open state so the desktop layout is not affected. */
  window.addEventListener('resize', function () {
    if (window.innerWidth > 980) setOpen(false);
  });
})();
