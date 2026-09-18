/* THREADBORN site.js — art peek overlay on reader pages (progressive enhancement:
   without JS the .artpeek anchor simply opens the page art in a new tab). */
(function () {
  function close() { document.body.classList.remove("artopen"); }
  document.addEventListener("click", function (e) {
    var peek = e.target.closest ? e.target.closest(".artpeek") : null;
    if (peek) { e.preventDefault(); document.body.classList.toggle("artopen"); return; }
    if (e.target.closest && e.target.closest(".artoverlay")) { close(); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { close(); }
  });
})();
