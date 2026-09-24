/* THREADBORN site.js — art peek overlay, chapters dropdown, and the model-sheet zoom viewer.
   Progressive enhancement: without JS the .artpeek anchor opens the page art in a new tab and
   every model sheet is a plain image. */
(function () {
  function close() { document.body.classList.remove("artopen"); }
  document.addEventListener("click", function (e) {
    if (!e.target.closest) { return; }
    /* --- zoom viewer: any .zoomable art opens full screen --- */
    var z = e.target.closest(".zoomable");
    if (z && window.TBZoom) { e.preventDefault(); window.TBZoom.open(z); return; }

    /* --- art peek overlay (reader pages) --- */
    var peek = e.target.closest(".artpeek");
    if (peek) { e.preventDefault(); document.body.classList.toggle("artopen"); return; }
    if (e.target.closest(".artoverlay")) { close(); }

    /* --- chapters dropdown --- */
    var chBtn = e.target.closest(".nav-ch-btn");
    if (chBtn) {
      var dd = chBtn.nextElementSibling;
      var open = dd.hasAttribute("hidden");
      dd.toggleAttribute("hidden");
      chBtn.setAttribute("aria-expanded", open);
      return;
    }
    if (!e.target.closest(".nav-chapters")) {
      var dds = document.querySelectorAll(".nav-ch-dropdown");
      for (var i = 0; i < dds.length; i++) { dds[i].setAttribute("hidden", ""); }
      var btns = document.querySelectorAll(".nav-ch-btn");
      for (var j = 0; j < btns.length; j++) { btns[j].setAttribute("aria-expanded", "false"); }
    }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { close(); }
    /* keyboard: open a focused sheet */
    if ((e.key === "Enter" || e.key === " ") && e.target && e.target.classList &&
        e.target.classList.contains("zoomable") && window.TBZoom) {
      e.preventDefault();
      window.TBZoom.open(e.target);
    }
  });

  /* ------------------------------------------------------------------ zoom viewer
     Fit-to-screen on open; wheel / +- / double-click to zoom; drag or one-finger pan;
     two-finger pinch on touch. Esc, the close button or a click on the backdrop exits. */
  var MINF = 0.5, MAXF = 8;
  function Zoom() {
    var lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML =
      '<div class="lbtitle"></div><img alt="" draggable="false">' +
      '<div class="lbbar">' +
      '<button type="button" data-act="out" title="Zoom out (−)">−</button>' +
      '<button type="button" data-act="fit" title="Fit to screen (0)">Fit</button>' +
      '<button type="button" data-act="in" title="Zoom in (+)">+</button>' +
      '<button type="button" data-act="actual" title="Actual pixels (1)">100%</button>' +
      '<button type="button" data-act="close" title="Close (Esc)">✕ Close</button>' +
      '</div>';
    document.body.appendChild(lb);
    var img = lb.querySelector("img"), title = lb.querySelector(".lbtitle");
    var scale = 1, x = 0, y = 0, fit = 1, natural = { w: 0, h: 0 }, pointers = {}, pinch = null;

    function layout() {
      var w = natural.w, h = natural.h;
      if (!w || !h) { return; }
      img.style.width = w + "px";
      img.style.height = h + "px";
      fit = Math.min((window.innerWidth * 0.96) / w, (window.innerHeight * 0.9) / h);
      img.style.transform = "translate(" + x + "px," + y + "px) scale(" + scale + ")";
    }
    function setScale(s, cx, cy) {
      var lo = fit * MINF, hi = fit * MAXF;
      s = Math.max(lo, Math.min(hi, s));
      if (cx === undefined) { cx = window.innerWidth / 2; cy = window.innerHeight / 2; }
      x = cx - (cx - x) * (s / scale);
      y = cy - (cy - y) * (s / scale);
      scale = s;
      layout();
    }
    function fitView() {
      scale = fit;
      x = (window.innerWidth - natural.w * fit) / 2;
      y = (window.innerHeight - natural.h * fit) / 2 - 10;
      layout();
    }
    function open(src) {
      img.src = src.currentSrc || src.src;
      title.textContent = src.alt || "Model sheet";
      var go = function () {
        natural = { w: img.naturalWidth, h: img.naturalHeight };
        scale = 1; x = 0; y = 0;
        layout();
        fitView();
        document.body.classList.add("lightboxopen");
      };
      if (img.complete && img.naturalWidth) { go(); } else { img.onload = go; }
    }
    function shut() {
      document.body.classList.remove("lightboxopen");
      pointers = {}; pinch = null;
      if (img.getAttribute("src")) { img.removeAttribute("src"); }
    }
    lb.addEventListener("click", function (e) {
      var act = e.target.closest("button") && e.target.closest("button").dataset.act;
      if (act === "close") { shut(); return; }
      if (act === "in") { setScale(scale * 1.3); return; }
      if (act === "out") { setScale(scale / 1.3); return; }
      if (act === "fit") { fitView(); return; }
      if (act === "actual") { setScale(1, window.innerWidth / 2, window.innerHeight / 2); return; }
      if (e.target === lb) { shut(); }
    });
    lb.addEventListener("dblclick", function (e) {
      if (e.target.closest("button")) { return; }
      if (scale > fit * 1.05) { fitView(); } else { setScale(1, e.clientX, e.clientY); }
    });
    lb.addEventListener("wheel", function (e) {
      e.preventDefault();
      setScale(scale * (e.deltaY < 0 ? 1.12 : 1 / 1.12), e.clientX, e.clientY);
    }, { passive: false });
    /* one-finger drag, two-finger pinch */
    lb.addEventListener("pointerdown", function (e) {
      if (e.target.closest("button")) { return; }
      pointers[e.pointerId] = { x: e.clientX, y: e.clientY };
      img.classList.add("dragging");
      if (Object.keys(pointers).length === 2) {
        var p = Object.values(pointers);
        pinch = { d: Math.hypot(p[0].x - p[1].x, p[0].y - p[1].y), s: scale };
      }
      if (lb.setPointerCapture) { try { lb.setPointerCapture(e.pointerId); } catch (err) {} }
    });
    lb.addEventListener("pointermove", function (e) {
      var prev = pointers[e.pointerId];
      if (!prev) { return; }
      var dx = e.clientX - prev.x, dy = e.clientY - prev.y;
      pointers[e.pointerId] = { x: e.clientX, y: e.clientY };
      if (pinch && Object.keys(pointers).length === 2) {
        var p = Object.values(pointers);
        var d = Math.hypot(p[0].x - p[1].x, p[0].y - p[1].y);
        var mid = { x: (p[0].x + p[1].x) / 2, y: (p[0].y + p[1].y) / 2 };
        setScale(pinch.s * (d / pinch.d), mid.x, mid.y);
        return;
      }
      x += dx; y += dy;
      layout();
    });
    function lift(e) {
      delete pointers[e.pointerId];
      if (Object.keys(pointers).length < 2) { pinch = null; }
      if (!Object.keys(pointers).length) { img.classList.remove("dragging"); }
    }
    lb.addEventListener("pointerup", lift);
    lb.addEventListener("pointercancel", lift);
    lb.addEventListener("pointerleave", lift);
    window.addEventListener("resize", function () {
      if (!document.body.classList.contains("lightboxopen")) { return; }
      var wasFit = Math.abs(scale - fit) < 0.001;
      layout();
      if (wasFit) { fitView(); }
    });
    document.addEventListener("keydown", function (e) {
      if (!document.body.classList.contains("lightboxopen")) { return; }
      if (e.key === "Escape") { shut(); }
      else if (e.key === "+" || e.key === "=") { setScale(scale * 1.3); }
      else if (e.key === "-" || e.key === "_") { setScale(scale / 1.3); }
      else if (e.key === "0") { fitView(); }
      else if (e.key === "1") { setScale(1, window.innerWidth / 2, window.innerHeight / 2); }
    });
    return { open: open, close: shut };
  }
  window.TBZoom = Zoom();
})();
