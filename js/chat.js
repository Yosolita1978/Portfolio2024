/* ============================================================
   CHATBOT IFRAME
   The Hugging Face embed grabs focus the moment it loads, which
   scrolls the page down on its own. On the old site the iframe sat
   far down a long page so it rarely showed; here it is the main
   content, so it fired on every visit.

   The fix is to load it only when the visitor asks for it. That
   removes the scroll jump entirely, and nothing is requested from
   Hugging Face until the button is clicked.
   ============================================================ */

(function () {
  'use strict';

  var frame = document.querySelector('.chat-frame');
  var button = document.getElementById('chat-start');
  if (!frame || !button) return;

  var src = frame.getAttribute('data-src');
  if (!src) return;

  button.addEventListener('click', function () {
    var placeholder = document.getElementById('chat-placeholder');

    var iframe = document.createElement('iframe');
    iframe.src = src;
    iframe.title = 'Career chatbot: ask anything about Cristina Rodriguez';
    iframe.setAttribute('frameborder', '0');
    iframe.setAttribute('scrolling', 'no');

    /* Hold the scroll position while the embed initialises, but stop
       the moment the visitor scrolls themselves, so we never fight
       them for control of the page. */
    var y = window.scrollY;
    var userScrolled = false;

    function release() { userScrolled = true; }
    ['wheel', 'touchstart', 'keydown'].forEach(function (evt) {
      window.addEventListener(evt, release, { passive: true, once: true });
    });

    var guard = setInterval(function () {
      if (userScrolled) { clearInterval(guard); return; }
      if (window.scrollY !== y) window.scrollTo(0, y);
    }, 50);

    setTimeout(function () {
      clearInterval(guard);
      ['wheel', 'touchstart', 'keydown'].forEach(function (evt) {
        window.removeEventListener(evt, release);
      });
    }, 3000);

    if (placeholder) placeholder.remove();
    frame.appendChild(iframe);
  });
})();
