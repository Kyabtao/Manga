#!/usr/bin/env python3
"""
THREADBORN — static reading-site generator (dependency-free, Python 3 stdlib only).

Reads the markdown canon in the repo (series-bible/, chapters/, README.md) and emits a
clean static website under website/ with page-wise reading navigation (EN + Hindi).

Usage (from anywhere):   python3 website/build.py
Then serve the repo root, e.g.:   python3 -m http.server 8000
and open  http://localhost:8000/website/index.html

Generated HTML is committed so the site can be read without building anything.
Images are NOT copied: pages link to the originals under chapters/ via relative paths,
so there is exactly one copy of every asset in the repo.
"""
import os
import re
import glob
import shutil
import posixpath

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # repo root
SITE = os.path.join(ROOT, "website")

# --------------------------------------------------------------------------- helpers
def p(*parts):
    return posixpath.join(*parts)

def repo_rel(abs_path):
    return os.path.relpath(abs_path, ROOT).replace(os.sep, "/")

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# --------------------------------------------------------------------------- inline md
_CODE = re.compile(r"`([^`]+)`")
_IMG = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
_LNK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_EM = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")

class Resolver:
    """Rewrites relative hrefs inside a source markdown file to site URLs.

    `as_image=True` (used for inline images) keeps a raw file raw: a link to a character's
    -ref.png becomes that character's art page, but an *embedded* -ref.png stays the image.
    """
    def __init__(self, src_repo, site_rel):
        self.src_dir = posixpath.dirname(src_repo)
        self.site_dir = posixpath.dirname(site_rel)
    def __call__(self, href, as_image=False):
        if href.startswith(("http://", "https://", "#", "mailto:")):
            return href
        path, _, frag = href.partition("#")
        if not path:
            return href
        target = posixpath.normpath(posixpath.join(self.src_dir, path))
        if target in SRC2SITE and not (as_image and target in REF_REPO_PATHS):
            new = SRC2SITE[target]
        elif os.path.exists(os.path.join(ROOT, target)) and not target.endswith(".md"):
            new = "../" + target          # repo files are served one level above website/
        else:
            return href
        out = posixpath.relpath(new, self.site_dir or ".")
        return out + ("#" + frag if frag else "")

def inline(md, res=None):
    codes = []
    def stash(m):
        codes.append(m.group(1))
        return "\x00%d\x00" % (len(codes) - 1)
    s = _CODE.sub(stash, md)
    s = esc(s)
    if res:
        s = _IMG.sub(lambda m: '<img src="%s" alt="%s" loading="lazy">'
                     % (res(m.group(2), as_image=True), m.group(1)), s)
        s = _LNK.sub(lambda m: '<a href="%s">%s</a>' % (res(m.group(2)), m.group(1)), s)
    else:
        s = _IMG.sub(lambda m: '<img src="%s" alt="%s" loading="lazy">' % (m.group(2), m.group(1)), s)
        s = _LNK.sub(lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), s)
    s = _BOLD.sub(r"<strong>\1</strong>", s)
    s = _EM.sub(r"<em>\1</em>", s)
    def unstash(m):
        return "<code>%s</code>" % esc(codes[int(m.group(1))])
    return re.sub(r"\x00(\d+)\x00", unstash, s)

# --------------------------------------------------------------------------- block md
_SEP = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
_LIST = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")
_STOP = re.compile(r"^(#{1,6}\s|\||>|```|\s*([-*]|\d+\.)\s|\s*(-{3,}|\*{3,})\s*$)")

def table_html(rows, res):
    def cells(row):
        row = row.strip()
        if row.startswith("|"):
            row = row[1:]
        if row.endswith("|"):
            row = row[:-1]
        return [c.strip() for c in row.split("|")]
    head = cells(rows[0])
    body = [cells(r) for r in rows[2:]]
    h = "<div class=\"tw\"><table><thead><tr>" + "".join(
        "<th>%s</th>" % inline(c, res) for c in head) + "</tr></thead><tbody>"
    for r in body:
        h += "<tr>" + "".join("<td>%s</td>" % inline(c, res) for c in r) + "</tr>"
    return h + "</tbody></table></div>"

def blocks(lines, res=None):
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            buf, i = [], i + 1
            while i < n and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append("<pre><code>%s</code></pre>" % esc("\n".join(buf)))
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lv = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lv, inline(m.group(2), res), lv))
            i += 1
            continue
        if re.match(r"^\s*(-{3,}|\*{3,})\s*$", line):
            out.append("<hr>"); i += 1
            continue
        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append("<blockquote>%s</blockquote>" % blocks(buf, res))
            continue
        if line.startswith("|"):
            tbl = []
            while i < n and lines[i].startswith("|"):
                tbl.append(lines[i]); i += 1
            if len(tbl) >= 2 and _SEP.match(tbl[1]):
                out.append(table_html(tbl, res))
            else:
                out.append("<p>" + "<br>".join(inline(t, res) for t in tbl) + "</p>")
            continue
        m = _LIST.match(line)
        if m:
            ordered = m.group(2)[0].isdigit()
            tag = "ol" if ordered else "ul"
            items, cur = [], m.group(3)
            i += 1
            while i < n:
                mm = _LIST.match(lines[i])
                if mm:
                    items.append(cur)
                    cur = mm.group(3); i += 1
                elif lines[i].strip() and not _STOP.match(lines[i]) and cur is not None:
                    cur += " " + lines[i].strip(); i += 1
                else:
                    break
            items.append(cur)
            items = [inline(t, res) for t in items]
            out.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % t for t in items), tag))
            continue
        buf = [line.strip()]; i += 1
        while i < n and lines[i].strip() and not _STOP.match(lines[i]):
            buf.append(lines[i].strip()); i += 1
        out.append("<p>%s</p>" % inline(" ".join(buf), res))
    return "\n".join(out)

def render_md(repo_path, site_rel):
    with open(os.path.join(ROOT, repo_path), encoding="utf-8") as f:
        text = f.read()
    return blocks(text.split("\n"), Resolver(repo_path, site_rel))

# --------------------------------------------------------------------------- source map
SRC2SITE = {}
CHAPTERS = sorted(posixpath.basename(d) for d in glob.glob(os.path.join(ROOT, "chapters", "chapter-*"))
                  if os.path.isdir(d))

SRC2SITE["README.md"] = "about.html"
SRC2SITE["ringbound-era-analysis.md"] = "legacy.html"
for f in sorted(glob.glob(os.path.join(ROOT, "series-bible", "*.md"))):
    SRC2SITE["series-bible/" + posixpath.basename(f)] = "bible/" + posixpath.basename(f)[:-3] + ".html"
for ch in CHAPTERS:
    for f in sorted(glob.glob(os.path.join(ROOT, "chapters", ch, "story", "*.md"))):
        base = posixpath.basename(f)[:-3]
        SRC2SITE["chapters/%s/story/%s.md" % (ch, base)] = "read/%s/%s.html" % (ch, base)
    for f in sorted(glob.glob(os.path.join(ROOT, "chapters", ch, "characters", "cast-*.md"))):
        base = posixpath.basename(f)[:-3]
        SRC2SITE["chapters/%s/characters/%s.md" % (ch, base)] = "read/%s/%s.html" % (ch, base.replace("cast-page", "cast"))
    for f in sorted(glob.glob(os.path.join(ROOT, "chapters", ch, "characters", "*.md"))):
        base = posixpath.basename(f)[:-3]
        if base.startswith("cast-"):
            continue
        SRC2SITE["chapters/%s/characters/%s.md" % (ch, base)] = "characters/%s.html" % base
    SRC2SITE["chapters/%s/chapter-summary.md" % ch] = "read/%s/index.html" % ch
SRC2SITE["chapters/chapter-001/other/locations.md"] = "world/locations.html"
SRC2SITE["chapters/chapter-001/other/glossary.md"] = "world/glossary.html"
# Character model sheets link to their art page rather than to a raw PNG, so every existing
# `Art: [<name>-ref.png]` line in a cast file lands on the gallery for free.
REF_REPO_PATHS = set()
for _ch in CHAPTERS:
    for _f in sorted(glob.glob(os.path.join(ROOT, "chapters", _ch, "characters", "*-ref.png"))):
        _base = posixpath.basename(_f)[:-len("-ref.png")]
        _repo = "chapters/%s/characters/%s-ref.png" % (_ch, _base)
        SRC2SITE[_repo] = "characters/%s-art.html" % _base
        REF_REPO_PATHS.add(_repo)

# --------------------------------------------------------------------------- template
NAV = [
    ("index.html", "Home"),
    ("read/index.html", "Read"),
    ("bible/00-overview.html", "Bible"),
    ("characters/index.html", "Characters"),
    ("world/glossary.html", "World"),
    ("about.html", "About"),
]

def nav_chapters(root):
    """Build a chapters dropdown for the header nav."""
    items = []
    for c in CHAPTERS:
        if not pages_of(c):
            continue
        chnum = c.split("-")[1]
        n = len(pages_of(c))
        status = chapter_status(c)
        items.append('<a href="%sread/%s/index.html">Chapter %s <span>%d pages · %s</span></a>'
                     % (root, c, chnum, n, status))
    return ('<div class="nav-chapters">'
            '<button class="nav-ch-btn" aria-expanded="false">Chapters ▾</button>'
            '<div class="nav-ch-dropdown" hidden>%s</div></div>' % "".join(items))

def page(title, site_rel, body, sidebar="", lang="en", crumb=""):
    root = posixpath.relpath(".", posixpath.dirname(site_rel) or ".")
    if root == ".":
        root = ""
    else:
        root += "/"
    nav = "".join(
        '<a class="%s" href="%s%s">%s</a>' % ("on" if root + h == site_rel else "", root, h, label)
        for h, label in NAV)
    nav += nav_chapters(root)
    return """<!DOCTYPE html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s · THREADBORN</title>
<link rel="stylesheet" href="%sassets/site.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="%sindex.html">THREADBORN <span>सुत्रजात</span></a>
<nav>%s</nav>
</div></header>
%s
<main class="wrap %s">
%s
%s
</main>
<footer class="wrap"><p>THREADBORN — सुत्रजात · a from-scratch webtoon manga · built from the markdown canon in
<a href="%sabout.html">the repo</a>. EN + Hindi. Chapters 001–010 complete · model sheets for every
named character · a trading card game after chapter 500.</p></footer>
</body>
</html>
""" % (lang, esc(title), root, root, nav,
       ('<div class="crumb wrap">%s</div>' % crumb) if crumb else "",
       "with-side" if sidebar else "",
       ('<aside class="side">%s</aside>' % sidebar) if sidebar else "",
       body, root)

def write(site_rel, html):
    path = os.path.join(SITE, site_rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  wrote", site_rel)

# --------------------------------------------------------------------------- pages
def chapter_title(ch):
    f = os.path.join(ROOT, "chapters", ch, "story", "page-001.md")
    if not os.path.exists(f):
        return "Untitled"
    m = re.search(r"\*\*Chapter title:\*\* \*([^*]+)\*", open(f, encoding="utf-8").read())
    return m.group(1).strip() if m else "Untitled"

def chapter_status(ch):
    return "complete" if os.path.exists(os.path.join(ROOT, "chapters", ch, "chapter-summary.md")) else "in progress"

def pages_word(n):
    return "1 page" if n == 1 else "%d pages" % n

def pages_of(ch):
    ens = sorted(posixpath.basename(f)[:-3] for f in
                 glob.glob(os.path.join(ROOT, "chapters", ch, "story", "page-*.md"))
                 if not posixpath.basename(f).endswith(".hi.md"))
    return ens

def reader_sidebar(ch, current):
    items = []
    for pg in pages_of(ch):
        num = pg.split("-")[1]
        cls = ' class="on"' if pg == current else ""
        items.append('<a%s href="%s.html"><b>%s</b><span>EN</span></a>' % (cls, pg, num))
        cls = ' class="on"' if pg + ".hi" == current else ""
        items.append('<a%s href="%s.hi.html"><b>%s</b><span>हि</span></a>' % (cls, pg, num))
    return '<div class="side-box"><h4>Chapter %s</h4>%s</div>' % (
        ch.split("-")[1], "".join(items))

def build_reader(ch):
    chnum = ch.split("-")[1]
    pgs = pages_of(ch)
    for idx, pg in enumerate(pgs):
        num = pg.split("-")[1]
        img = posixpath.relpath("../chapters/%s/images/%s.png" % (ch, pg),
                                posixpath.dirname("read/%s/%s.html" % (ch, pg)))
        prev_l = '<a class="btn" href="%s.html">← Page %s</a>' % (pgs[idx - 1], pgs[idx - 1].split("-")[1]) if idx else '<a class="btn" href="index.html">← Chapter cover</a>'
        nxt_l = '<a class="btn next" href="%s.html">Page %s →</a>' % (pgs[idx + 1], pgs[idx + 1].split("-")[1]) if idx + 1 < len(pgs) else '<a class="btn next" href="../../read/index.html">Next chapter →</a>'
        for lang, suffix in (("en", ""), ("hi", ".hi")):
            src = "chapters/%s/story/%s%s.md" % (ch, pg, suffix)
            if not os.path.exists(os.path.join(ROOT, src)):
                continue
            site_rel = "read/%s/%s%s.html" % (ch, pg, suffix)
            body = render_md(src, site_rel)
            toggle = ('<div class="lang"><a class="%s" href="%s.html">English</a>'
                      '<a class="%s" href="%s.hi.html">हिन्दी</a></div>' % (
                          "on" if lang == "en" else "", pg, "on" if lang == "hi" else "", pg))
            links = ('<div class="pagelinks">%s<a class="btn" href="cast-%s.html">Cast &amp; card lines</a>%s</div>'
                     % (prev_l, num, nxt_l))
            reader = ('<div class="reader"><div class="rtoggle">%s</div>'
                      '<div class="rscript">%s</div></div>' % (toggle, body))
            peek = ('<a class="artpeek" href="%s" target="_blank" rel="noopener" '
                    'aria-label="Show page art">🖼 Art</a>'
                    '<div class="artoverlay"><img src="%s" alt="Chapter %s page %s art, full page">'
                    '<span>✕ close</span></div>'
                    '<script src="../../assets/site.js"></script>' % (img, img, chnum, num))
            html = page("Ch.%s Page %s%s" % (chnum, num, " (HI)" if suffix else ""), site_rel,
                        reader + links + peek,
                        sidebar=reader_sidebar(ch, pg + suffix), lang=lang,
                        crumb='<a href="../../index.html">Home</a> / <a href="../index.html">Read</a> / <a href="index.html">Chapter %s</a> / Page %s%s' % (chnum, num, " · हिन्दी" if suffix else ""))
            write(site_rel, html)
    # per-page cast lists
    for f in sorted(glob.glob(os.path.join(ROOT, "chapters", ch, "characters", "cast-page-*.md"))):
        base = posixpath.basename(f)[:-3]
        src = "chapters/%s/characters/%s.md" % (ch, base)
        site_rel = SRC2SITE[src]
        num = base.split("-")[2]
        html = page("Ch.%s Page %s — Cast" % (chnum, num), site_rel,
                    render_md(src, site_rel),
                    sidebar=reader_sidebar(ch, ""),
                    crumb='<a href="../../index.html">Home</a> / <a href="../index.html">Read</a> / '
                          '<a href="index.html">Chapter %s</a> / <a href="page-%s.html">Page %s</a> / Cast'
                          % (chnum, num, num))
        write(site_rel, html)
    # chapter cover
    site_rel = "read/%s/index.html" % ch
    grid = "".join(
        '<a class="tile" href="%s.html"><img src="%s" loading="lazy" alt="page %s"><b>%s</b></a>' % (
            pg, posixpath.relpath("../chapters/%s/images/%s.png" % (ch, pg), posixpath.dirname(site_rel)),
            pg.split("-")[1], pg.split("-")[1])
        for pg in pgs)
    summary = render_md("chapters/%s/chapter-summary.md" % ch, site_rel) if os.path.exists(
        os.path.join(ROOT, "chapters/%s/chapter-summary.md" % ch)) else ""
    html = page("Chapter %s" % chnum, site_rel,
                '<h1>Chapter %s — <em>%s</em></h1>'
                '<p class="lede">Arc I — The Unspooling · Agnikhand · %s · %s · English + Hindi. '
                'Pick a page, or read straight through.</p><div class="grid">%s</div>%s' % (
                    chnum, chapter_title(ch), pages_word(len(pgs)), chapter_status(ch), grid, summary),
                crumb='<a href="../../index.html">Home</a> / <a href="../index.html">Read</a> / Chapter %s' % chnum)
    write(site_rel, html)

def build_bible():
    for src, site_rel in [(k, v) for k, v in SRC2SITE.items() if k.startswith("series-bible/")]:
        html = page(posixpath.basename(src)[:-3], site_rel, render_md(src, site_rel),
                    crumb='<a href="../index.html">Home</a> / Series bible')
        write(site_rel, html)

def ref_of(src_md):
    """The model sheet that sits beside a character sheet, repo-relative, or None."""
    ref = src_md[:-3] + "-ref.png"
    return ref if os.path.exists(os.path.join(ROOT, ref)) else None

def display_name(src_md):
    return posixpath.basename(src_md)[:-3].replace("-", " ").title()

def sheet_section(src_md, prefixes=("## Appearance", "## Visual sheet")):
    """Pull one section out of a character sheet so the art page can reprint it."""
    lines = open(os.path.join(ROOT, src_md), encoding="utf-8").read().split("\n")
    for i, line in enumerate(lines):
        low = line.strip().lower()
        if re.match(r"^## [^#]", line.strip()) and any(low.startswith(p.lower()) for p in prefixes):
            j = i + 1
            while j < len(lines) and not re.match(r"^## [^#]", lines[j].strip()):
                j += 1
            return "\n".join(lines[i + 1:j]).strip()
    return ""

DEFAULT_PANELS = ["front", "side", "back", "face", "detail", "hands", "kit", "action"]

def sheet_panels(src_md):
    """Panel list for a model sheet — from the sheet's own `**Ref sheet panels:**` line.
    Continuation lines are allowed (and joined), so long panel lists stay readable in markdown."""
    lines = open(os.path.join(ROOT, src_md), encoding="utf-8").read().split("\n")
    for i, line in enumerate(lines):
        m = re.match(r"^\*\*Ref sheet panels:\*\*\s*(.*)$", line)
        if not m:
            continue
        parts = [m.group(1)]
        for nxt in lines[i + 1:]:
            s = nxt.strip()
            if not s or re.match(r"^(\*\*[^*]+:\*\*|#|\||-{3,})", s):
                break
            parts.append(s)
        joined = " ".join(" ".join(parts).split())
        return [x.strip().lower() for x in re.split(r"\s*[·|]\s*", joined) if x.strip()]
    return list(DEFAULT_PANELS)

def sheet_panel_lede(panels):
    """One honest sentence about the panels this model sheet actually has."""
    n = len(panels)
    if n >= len(DEFAULT_PANELS):
        return "the eight required panels \u2014 front \u00b7 side \u00b7 back \u00b7 face \u00b7 detail \u00b7 hands \u00b7 kit \u00b7 action"
    have = [p.split(" (")[0].strip() for p in panels]
    missing = [s for s in DEFAULT_PANELS if s not in have]
    return ("%d panels \u2014 %s. Carried over from the first art pass; still to add at the next "
            "one: %s" % (n, " \u00b7 ".join(panels), ", ".join(missing)))

def ref_card(src_md, site_rel):
    """The model-sheet card that opens a character's art page (or None if they have no ref)."""
    ref = ref_of(src_md)
    if not ref:
        return ""
    base = posixpath.basename(src_md)[:-3]
    res = Resolver(src_md, site_rel)
    img = res("../" + ref)
    return ('<figure class="refcard">'
            '<a class="refopen" href="%s-art.html">'
            '<img src="%s" loading="lazy" alt="%s — model sheet">'
            '<span class="refopen-tag">Open art page →</span></a>'
            '<figcaption><b>Model sheet</b> — %d panels. Press the art to see it full size.'
            '</figcaption></figure>' % (base, img, display_name(src_md), len(sheet_panels(src_md))))

def build_character_art(src_md, ref, names):
    """`characters/<name>-art.html` — the clickable model-sheet gallery page."""
    base = posixpath.basename(src_md)[:-3]
    site_rel = "characters/%s-art.html" % base
    chnum = src_md.split("/")[1].split("-")[1]
    res = Resolver(src_md, site_rel)
    img = res("../" + ref)
    panels = sheet_panels(src_md)
    chips = "".join('<span class="panelchip"><i>%d</i>%s</span>' % (i + 1, esc(p))
                    for i, p in enumerate(panels))
    brief = sheet_section(src_md)
    brief_html = ('<h2>Drawing brief</h2><div class="brief">%s</div>'
                  % blocks(brief.split("\n"), res)) if brief else ""
    i = names.index(base)
    prevn = names[i - 1] if i > 0 else names[-1]
    nextn = names[(i + 1) % len(names)]
    links = ('<div class="pagelinks"><a class="btn" href="%s-art.html">← %s</a>'
             '<a class="btn" href="index.html">All cast</a>'
             '<a class="btn next" href="%s-art.html">%s →</a></div>'
             % (prevn, display_name(prevn + ".md"), nextn, display_name(nextn + ".md")))
    body = ('<h1>%s <em>— model sheet</em></h1>'
            '<p class="lede">Chapter %s · first appearance. The drawing reference for every page '
            'this character is on — %s, in the house panel order, per '
            '<a href="../bible/05-character-art-spec.html">the character art spec</a>.</p>'
            '<figure class="sheetart">'
            '<img class="zoomable" src="%s" alt="%s model sheet — %s" tabindex="0">'
            '<figcaption>Press the sheet to open it full size · scroll to zoom · drag to move · '
            'Esc to close</figcaption>'
            '<div class="zoomhint"><span>🔍 click to zoom</span></div></figure>'
            '<div class="panels">%s</div>%s%s'
            '<p class="pagelinks-note">Full written sheet, canon rules and card-game line: '
            '<a href="%s.html">%s</a></p>'
            % (display_name(src_md).upper(), chnum, sheet_panel_lede(panels), img,
               display_name(src_md), esc(" · ".join(panels)),
               chips, brief_html, links, base, display_name(src_md)))
    html = page("%s — art" % display_name(src_md), site_rel, body,
                crumb='<a href="../index.html">Home</a> / <a href="index.html">Characters</a> / '
                      '<a href="%s.html">%s</a> / Art' % (base, display_name(src_md)))
    write(site_rel, html)
    return site_rel

def build_characters():
    sheets = [(k, v) for k, v in SRC2SITE.items()
              if v.startswith("characters/") and v != "characters/index.html"
              and k.endswith(".md")]
    sheets.sort(key=lambda kv: kv[1])
    names = [posixpath.basename(src)[:-3] for src, _ in sheets]
    cards = []
    art_pages = 0
    for src, site_rel in sheets:
        ref = ref_of(src)
        body = ref_card(src, site_rel) + render_md(src, site_rel)
        html = page(posixpath.basename(src)[:-3], site_rel, body,
                    crumb='<a href="../index.html">Home</a> / <a href="index.html">Characters</a>')
        write(site_rel, html)
        name = display_name(src)
        if ref:
            build_character_art(src, ref, names)
            art_pages += 1
            base = posixpath.basename(src)[:-3]
            rel = posixpath.relpath("../" + ref, "characters")
            card = ('<div class="char">'
                    '<a class="charthumb" href="%s-art.html" title="Open %s\'s model sheet">'
                    '<img src="%s" loading="lazy" alt="%s model sheet thumbnail"></a>'
                    '<div class="charmeta"><a class="charname" href="%s">%s</a>'
                    '<a class="charart" href="%s-art.html">%d-panel art ↗</a></div></div>'
                    % (base, name, rel, name, base, name, base, len(sheet_panels(src))))
        else:
            card = ('<div class="char"><a class="charname plain" href="%s">%s</a>'
                    '<span class="charart off">no ref sheet yet</span></div>'
                    % (posixpath.basename(site_rel), name))
        cards.append(card)
    html = page("Characters", "characters/index.html",
                '<h1>Cast</h1><p class="lede">Full sheets with art-continuity rules and card-game lines. '
                '<b>Press any sheet to open its model-sheet art page</b> — the eight panels every page is '
                'drawn from (front · side · back · face · detail · hands · kit · action).</p>'
                '<p class="meta">%d character sheets · %d model sheets.</p>'
                '<div class="chars">%s</div>' % (len(sheets), art_pages, "".join(cards)),
                crumb='<a href="../index.html">Home</a> / Characters')
    write("characters/index.html", html)

def build_world():
    # merge every chapter's locations + glossary into two living documents
    for kind, site_rel in (("locations", "world/locations.html"), ("glossary", "world/glossary.html")):
        parts = ['<h1>%s</h1>' % ("Locations" if kind == "locations" else "Glossary"),
                 '<p class="lede">Merged across chapters — the living document. Chapter-scoped source '
                 'files remain the canon of record.</p>']
        for ch in CHAPTERS:
            src = "chapters/%s/other/%s.md" % (ch, kind)
            if os.path.exists(os.path.join(ROOT, src)):
                parts.append('<h2>Chapter %s</h2>' % ch.split("-")[1])
                parts.append(render_md(src, site_rel))
        html = page(kind.title(), site_rel, "\n".join(parts),
                    crumb='<a href="../index.html">Home</a> / World')
        write(site_rel, html)

def build_docs():
    for src, site_rel in (("README.md", "about.html"), ("ringbound-era-analysis.md", "legacy.html")):
        html = page(posixpath.basename(src)[:-3], site_rel, render_md(src, site_rel),
                    crumb='<a href="index.html">Home</a>')
        write(site_rel, html)

def home_tiles():
    out = []
    for c in CHAPTERS:
        if not pages_of(c):
            continue
        out.append('<a class="tile big" href="read/%s/index.html">'
                   '<img src="%s" loading="lazy" alt="Chapter %s cover art">'
                   '<b>Chapter %s — %s</b><span>%s · %s</span></a>' % (
                       c, posixpath.relpath("../chapters/%s/images/page-001.png" % c, "."),
                       c.split("-")[1], c.split("-")[1], chapter_title(c),
                       pages_word(len(pages_of(c))), chapter_status(c)))
    return "".join(out)

def build_home_and_index():
    ch = CHAPTERS[0]
    pgs = pages_of(ch)
    html = page("Home", "index.html",
        '<section class="hero"><h1>THREADBORN <span>सुत्रजात</span></h1>'
        '<p class="pitch">Everyone is born owing the world a thread of power. '
        '<b>Ira Sutar was born with hers already taken</b> — and she is the only person alive who can '
        '<em>mend</em> the weave instead of pulling from it.</p>'
        '<p class="meta">Full-colour webtoon · vertical scroll · English + Hindi · '
        'Chapter 1 complete (%d pages) · a trading card game after chapter 500.</p>'
        '<div class="cta"><a class="btn next" href="read/%s/page-001.html">Start reading — Page 001</a>'
        '<a class="btn" href="read/%s/index.html">Chapter 1 cover</a>'
        '<a class="btn" href="bible/00-overview.html">Series bible</a></div></section>'
        '<section class="homegrid"><div class="hometiles">%s</div>'
        '<div class="homecol">'
        '<a class="box" href="characters/index.html"><b>Cast</b><span>Sheets, refs &amp; card-game lines</span></a>'
        '<a class="box" href="world/glossary.html"><b>Glossary</b><span>Every term, Devanagari included</span></a>'
        '<a class="box" href="world/locations.html"><b>Locations</b><span>Agnikhand, stair to terraces</span></a>'
        '<a class="box" href="legacy.html"><b>Ringbound-era analysis</b><span>Why the old site was scrapped</span></a>'
        '</div></section>' % (len(pgs), ch, ch, home_tiles()))
    write("index.html", html)
    rows = "".join(
        '<a class="row" href="%s/index.html"><b>Chapter %s</b><span>%s · %s · %s</span><i>→</i></a>'
        % (c, c.split("-")[1], chapter_title(c), pages_word(len(pages_of(c))), chapter_status(c))
        for c in CHAPTERS if pages_of(c))
    # Enhanced read index with per-chapter page lists and position info
    ch_cards = []
    for c in CHAPTERS:
        if not pages_of(c):
            continue
        chnum = c.split("-")[1]
        pgs_list = pages_of(c)
        status = chapter_status(c)
        page_links = []
        for i, pg in enumerate(pgs_list):
            num = pg.split("-")[1]
            pos = i + 1
            page_links.append(
                '<a class="rn-page" href="%s/index.html#%s"><b>%s</b><span>Page %s of %s</span></a>'
                % (c, pg, num, pos, len(pgs_list)))
        ch_cards.append(
            '<div class="rn-chapter"><div class="rn-header">'
            '<a href="%s/index.html"><b>Chapter %s</b></a>'
            '<span>%s · %s · %s</span></div>'
            '<div class="rn-pages">%s</div></div>'
            % (c, chnum, chapter_title(c), pages_word(len(pgs_list)), status,
               "".join(page_links)))
    html = page("Read", "read/index.html",
                '<h1>Read</h1><p class="lede">Chapter by chapter, page by page. Every page exists in '
                'English and Hindi; the art carries no lettering by design.</p>'
                '<div class="readnav">%s</div>%s' % ("".join(ch_cards), rows),
                crumb='<a href="../index.html">Home</a> / Read')
    write("read/index.html", html)

# --------------------------------------------------------------------------- main
def main():
    if os.path.isdir(SITE):
        for entry in os.listdir(SITE):
            if entry in ("build.py", "assets"):
                continue
            shutil.rmtree(os.path.join(SITE, entry)) if os.path.isdir(os.path.join(SITE, entry)) \
                else os.remove(os.path.join(SITE, entry))
    print("building site from", ROOT)
    build_home_and_index()
    build_docs()
    build_bible()
    for ch in CHAPTERS:
        if pages_of(ch):
            build_reader(ch)
    build_characters()
    build_world()
    print("done.")

if __name__ == "__main__":
    main()
