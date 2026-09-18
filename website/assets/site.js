/* THREADBORN site.js — art peek overlay + chapters dropdown (progressive enhancement:
   without JS the .artpeek anchor simply opens the page art in a new tab). */
(function () {
  function close() { document.body.classList.remove("artopen"); }
  document.addEventListener("click", function (e) {
    var peek = e.target.closest ? e.target.closest(".artpeek") : null;
    if (peek) { e.preventDefault(); document.body.classList.toggle("artopen"); return; }
    if (e.target.closest && e.target.closest(".artoverlay")) { close(); }
    // chapters dropdown
    var chBtn = e.target.closest ? e.target.closest(".nav-ch-btn") : null;
    if (chBtn) {
      var dd = chBtn.nextElementSibling;
      var open = dd.hasAttribute("hidden");
      dd.toggleAttribute("hidden");
      chBtn.setAttribute("aria-expanded", open);
      return;
    }
    // close dropdown when clicking outside
    if (e.target.closest && !e.target.closest(".nav-chapters")) {
      var dds = document.querySelectorAll(".nav-ch-dropdown");
      for (var i = 0; i < dds.length; i++) { dds[i].setAttribute("hidden", ""); }
      var btns = document.querySelectorAll(".nav-ch-btn");
      for (var j = 0; j < btns.length; j++) { btns[j].setAttribute("aria-expanded", "false"); }
    }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { close(); }
  });
})();
