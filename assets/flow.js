// Bandeau : les mots du verset apparaissent l'un après l'autre, comme sur
// l'accueil de l'app. Sans JavaScript ou avec « réduire les animations »,
// le verset est affiché d'emblée.
(function () {
  var verse = document.querySelector(".verse");
  if (!verse) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var words = verse.querySelectorAll(".w");
  verse.classList.add("pending");
  var i = 0;
  function next() {
    if (i >= words.length) return;
    words[i].classList.add("on");
    i += 1;
    setTimeout(next, 420);
  }
  // Laisse la police se charger avant le premier mot.
  var start = function () {
    setTimeout(next, 300);
  };
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(start);
  } else {
    start();
  }
})();
