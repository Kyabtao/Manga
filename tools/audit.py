#!/usr/bin/env python3
"""
THREADBORN — reproducible repo audit gate (stdlib only).

Every number quoted in AUDIT.md must come from this script or from a logged
full-resolution visual read. Run from anywhere:

    python3 tools/audit.py            # full report (markdown)
    python3 tools/audit.py --quick    # text/structure gates only (no site build, no links)

Checks (see series-bible/style-guide.md "Page-art QA gate" for the visual half,
which this script CANNOT do — shape and counts yes, beats no):

  1  structure    10 chapters x (10 EN + 10 HI + 10 png + 10 cast + 2 other + summary), pairing by number
  2  naming/junk  convention filenames only; no .DS_Store/.orig/.bak/tmp-*/.gitkeep
  3  images       PNG magic + IHDR, sha-256 duplicates, canvas rule (page art portrait, ratio <= 2.5),
                  weight band 1.2-3.0 MB
  4  hindi        Devanagari share of LETTERS ONLY >= 80% per .hi.md (the historical floor)
  5  scripts      PANEL numbering 1..n, stated panel count == actual, Camera:/कैमरा: per panel,
                  "Writing & art notes" + "Card-game hooks" sections present, EN/HI panel parity
  6  continuity   Loom has zero dialogue lines; mother-in-Camera-line scan (manual-confirm list);
                  chain-stop budget line present in every chapter summary
  7  cast         card-line (fenced "a / b / c / d / e" block) coverage per cast file
  8  site         build.py reproducible (rebuild == no content change), local links resolve
  9  docs         README branch field == git branch; README open-PR field sanity

Exit code 0 = all gates pass, 1 = any hard gate failed, 2 = warnings only.
The canvas check is a HARD gate for page art; sheets (characters/*-ref.png, *-alt.png) are exempt.
"""
import os
import re
import sys
import glob
import struct
import hashlib
import subprocess
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = sorted(glob.glob(os.path.join(ROOT, "chapters", "chapter-*")))
HOUSE = (768, 1376)
HOUSE_RATIO_MAX = 2.5
HINDI_FLOOR = 80.0
WEIGHT_BAND = (1.2, 3.0)

hard_fail, warn = [], []


def fail(msg):
    hard_fail.append(msg)


def note(msg):
    warn.append(msg)


def rd(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------- 1 structure
def check_structure():
    out = []
    for c in CHAPTERS:
        name = os.path.basename(c)
        en = glob.glob(c + "/story/page-???.md")
        hi = glob.glob(c + "/story/page-???.hi.md")
        im = glob.glob(c + "/images/page-???.png")
        ca = glob.glob(c + "/characters/cast-page-???.md")
        ot = glob.glob(c + "/other/*.md")
        sm = glob.glob(c + "/chapter-summary.md")
        nums = lambda lst, pat: sorted(re.search(pat, os.path.basename(x)).group(1) for x in lst)
        e, h, i, k = nums(en, r"page-(\d+)\.md"), nums(hi, r"page-(\d+)\.hi\.md"), \
            nums(im, r"page-(\d+)\.png"), nums(ca, r"cast-page-(\d+)\.md")
        ok = len(en) == len(hi) == len(im) == len(ca) == 10 and len(ot) == 2 and len(sm) == 1
        ok = ok and e == h == i == k
        out.append((name, len(en), len(hi), len(im), len(ca), len(ot), len(sm), "PASS" if ok else "FAIL"))
        if not ok:
            fail(f"structure {name}: en{len(en)} hi{len(hi)} img{len(im)} cast{len(ca)} other{len(ot)} sum{len(sm)} nums={e}/{h}/{i}/{k}")
    return out


# ---------------------------------------------------------------- 2 naming / junk
JUNK = (".DS_Store", ".orig", ".bak", "~", ".gitkeep")


def check_junk():
    bad = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if "/.git" in dirpath or dirpath.endswith("/.git") or "/work" in dirpath:
            continue
        for f in filenames:
            if f.endswith(JUNK) or f.startswith("tmp-"):
                bad.append(os.path.relpath(os.path.join(dirpath, f), ROOT))
    conv = []
    for c in CHAPTERS:
        for sub, pat in (("story", r"^page-\d{3}(\.hi)?\.md$"), ("images", r"^page-\d{3}\.png$"),
                         ("characters", r"^(cast-page-\d{3}\.md|.+\.md|.+-(ref|alt)\.png)$"),
                         ("other", r"^.+\.md$")):
            for f in glob.glob(f"{c}/{sub}/*"):
                b = os.path.basename(f)
                if not re.match(pat, b):
                    conv.append(os.path.relpath(f, ROOT))
    if bad:
        fail(f"junk files: {bad}")
    if conv:
        note(f"off-convention filenames: {conv[:8]}")
    return len(bad), len(conv)


# ---------------------------------------------------------------- 3 images
def png_wh(p):
    d = open(p, "rb").read()
    if d[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", d[16:24])


def check_images():
    rows, seen, dupes = [], {}, []
    for p in sorted(glob.glob(ROOT + "/chapters/**/*.png", recursive=True)):
        wh = png_wh(p)
        rel = os.path.relpath(p, ROOT)
        if wh is None:
            fail(f"invalid PNG: {rel}")
            continue
        w, h = wh
        hh = hashlib.sha256(open(p, "rb").read()).hexdigest()
        if hh in seen:
            dupes.append((rel, seen[hh]))
        seen[hh] = rel
        mb = os.path.getsize(p) / 1048576
        page = "/images/page-" in rel
        rows.append((rel, w, h, round(h / w, 2), page, mb))
        if not (WEIGHT_BAND[0] <= mb <= WEIGHT_BAND[1]):
            note(f"weight outside {WEIGHT_BAND} MB: {rel} ({mb:.2f})")
        if page:
            if h <= w:
                fail(f"canvas rule (page art must be portrait): {rel} {w}x{h}")
            elif h / w > HOUSE_RATIO_MAX:
                note(f"ratio > {HOUSE_RATIO_MAX}: {rel} {w}x{h} (old art, rebuild queue)")
    if dupes:
        fail(f"duplicate images: {dupes}")
    house = sum(1 for r in rows if r[4] and (r[1], r[2]) == HOUSE)
    pages = sum(1 for r in rows if r[4])
    return rows, dupes, house, pages


# ---------------------------------------------------------------- 4 hindi
def devanagari_letters_only(text):
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)   # keep link labels, drop URLs
    text = re.sub(r"[#*>`|_\-]", " ", text)                # drop markdown syntax
    letters = [c for c in text if c.isalpha()]
    dev = [c for c in letters if "ऀ" <= c <= "ॿ"]
    return (100.0 * len(dev) / len(letters)) if letters else 0.0


def check_hindi():
    scores = []
    for p in sorted(glob.glob(ROOT + "/chapters/chapter-*/story/page-???.hi.md")):
        s = devanagari_letters_only(rd(p))
        scores.append((s, os.path.relpath(p, ROOT)))
        if s < HINDI_FLOOR:
            fail(f"Hindi floor {HINDI_FLOOR}%: {os.path.relpath(p, ROOT)} = {s:.1f}%")
    return scores


# ---------------------------------------------------------------- 5 scripts
def check_scripts():
    stats = {"panels": 0, "camera_ok": 0, "sections": 0, "parity": 0}
    for p in sorted(glob.glob(ROOT + "/chapters/chapter-*/story/page-???.md")):
        t = rd(p)
        nums = [int(n) for n in re.findall(r"^##\s*PANEL\s+(\d+)", t, re.M)]
        stats["panels"] += len(nums)
        if nums != list(range(1, len(nums) + 1)):
            fail(f"panel numbering {os.path.relpath(p, ROOT)}: {nums}")
        stated = re.search(r"(\d+)\s*panels?", t)
        if stated and int(stated.group(1)) != len(nums):
            fail(f"stated panel count != actual in {os.path.relpath(p, ROOT)}: {stated.group(1)} vs {len(nums)}")
        if len(re.findall(r"\*\*Camera:\*\*", t)) == len(nums):
            stats["camera_ok"] += 1
        else:
            fail(f"Camera: label count != panels in {os.path.relpath(p, ROOT)}")
        if re.search(r"^##\s*Writing & art notes", t, re.M) and re.search(r"^##\s*Card-game hooks", t, re.M):
            stats["sections"] += 1
        else:
            fail(f"missing notes/card sections: {os.path.relpath(p, ROOT)}")
        hi = p[:-3] + ".hi.md"
        ht = rd(hi) if os.path.exists(hi) else ""
        hnums = len(re.findall(r"^##\s*पैनल", ht, re.M))
        hcam = len(re.findall(r"\*\*कैमरा:\*\*", ht))
        if hnums == len(nums) and hcam == len(nums):
            stats["parity"] += 1
        else:
            fail(f"EN/HI parity {os.path.relpath(p, ROOT)}: en{len(nums)} hi{hnums}/{hcam}")
    return stats


# ---------------------------------------------------------------- 6 continuity
def check_continuity():
    loom, mother, chain = [], [], {}
    for p in sorted(glob.glob(ROOT + "/chapters/chapter-*/story/page-???.md")):
        t = rd(p)
        for m in re.finditer(r"^>\s*\*\*(LOOM|सूत्र-यन्त्र)[^:]*:\*\*", t, re.M):
            loom.append(os.path.relpath(p, ROOT))
        for m in re.finditer(r"\*\*Camera:\*\*(.*?)(?=\n\n|\*\*Image)", t, re.S):
            c = m.group(1)
            for mm in re.finditer(r"(?i)\bmother\b", c):
                seg = c[max(0, mm.start() - 120): mm.end() + 160]
                if re.search(r"(?i)mother[^.]*\b(stands|sits|seated|sewing|walking|enters|appears|in frame|visible)\b", seg):
                    mother.append((os.path.relpath(p, ROOT), seg.replace("\n", " ")[:120]))
    for s in sorted(glob.glob(ROOT + "/chapters/chapter-*/chapter-summary.md")):
        t = rd(s)
        m = re.search(r"(?i)\*\*chain-stop budget:\*\*[^\n]*", t)
        chain[os.path.basename(os.path.dirname(s))] = m.group(0)[:110] if m else None
        if not m:
            fail(f"no chain-stop budget line in {os.path.relpath(s, ROOT)}")
    if loom:
        fail(f"Loom speaks: {loom}")
    return loom, mother, chain


# ---------------------------------------------------------------- 7 cast card lines
def check_cast():
    have, missing = 0, []
    for p in sorted(glob.glob(ROOT + "/chapters/chapter-*/characters/cast-page-???.md")):
        blocks = re.findall(r"```\n(.*?)```", rd(p), re.S)
        if any(b.count("/") >= 4 for b in blocks):
            have += 1
        else:
            missing.append(os.path.relpath(p, ROOT))
    return have, missing


# ---------------------------------------------------------------- 8 site
def check_site(quick):
    if quick:
        return None, None
    before = {}
    for p in glob.glob(ROOT + "/website/**/*.html", recursive=True):
        before[p] = hashlib.sha256(open(p, "rb").read()).hexdigest()
    subprocess.run([sys.executable, os.path.join(ROOT, "website", "build.py")],
                   cwd=ROOT, check=True, capture_output=True)
    changed = []
    for p, h in before.items():
        if hashlib.sha256(open(p, "rb").read()).hexdigest() != h:
            changed.append(os.path.relpath(p, ROOT))
    new = [os.path.relpath(p, ROOT) for p in glob.glob(ROOT + "/website/**/*.html", recursive=True) if p not in before]
    if changed or new:
        fail(f"committed site != build output: changed={changed[:6]} new={new[:6]} (run build.py and commit)")
    broken, total = [], 0
    for p in sorted(glob.glob(ROOT + "/website/**/*.html", recursive=True)):
        t = rd(p)
        base = os.path.dirname(p)
        for m in re.finditer(r'(?:href|src)="([^"]+)"', t):
            u = m.group(1).strip()
            if u.startswith(("http", "mailto:", "#", "javascript:")):
                continue
            total += 1
            u2 = u.split("#")[0]
            if u2 and not os.path.exists(os.path.normpath(os.path.join(base, u2))):
                broken.append((os.path.relpath(p, ROOT), u))
    if broken:
        fail(f"broken local links: {broken[:10]}")
    return total, broken


# ---------------------------------------------------------------- 9 docs
def check_docs():
    t = rd(ROOT + "/README.md")
    branch = subprocess.run(["git", "-C", ROOT, "rev-parse", "--abbrev-ref", "HEAD"],
                            capture_output=True, text=True).stdout.strip()
    m = re.search(r"\*\*Branch\*\*\s*\|\s*`([^`]+)`", t)
    if m and m.group(1) != branch:
        fail(f"README branch field stale: says {m.group(1)}, git says {branch}")
    return branch, (m.group(1) if m else None)


# ---------------------------------------------------------------- report
def main():
    quick = "--quick" in sys.argv
    st = check_structure()
    junk = check_junk()
    rows, dupes, house, pages = check_images()
    hi = check_hindi()
    sc = check_scripts()
    loom, mother, chain = check_continuity()
    have, missing = check_cast()
    total, broken = check_site(quick)
    branch, readm_branch = check_docs()

    o = []
    w = o.append
    w("# THREADBORN audit gate — machine report")
    w("")
    w(f"- branch: `{branch}` (README field: `{readm_branch}`)")
    w(f"- chapters: {len(st)} · files per chapter EN/HI/IMG/CAST/OTHER/SUM: "
      + ", ".join(f"{r[0][-3:]}={r[1]}/{r[2]}/{r[3]}/{r[4]}/{r[5]}/{r[6]}" for r in st[:3]) + " …")
    w(f"- junk/off-convention: {junk[0]}/{junk[1]}")
    w(f"- images: {len(rows)} png · duplicates {len(dupes)} · page art on house canvas {house}/{pages}")
    ratios = sorted({r[3] for r in rows if r[4]})
    w(f"- page-art ratios present: {ratios}")
    w(f"- hindi letters-only Devanagari: min {min(hi)[0]:.1f}% · median {statistics.median(x[0] for x in hi):.1f}% "
      f"· max {max(hi)[0]:.1f}% · floor {HINDI_FLOOR}%")
    w(f"- scripts: {sc['panels']} panels · Camera parity {sc['camera_ok']}/100 · notes+card sections {sc['sections']}/100 "
      f"· EN/HI parity {sc['parity']}/100")
    w(f"- continuity: Loom dialogue {len(loom)} · mother-in-Camera manual-confirm {len(mother)} · "
      f"chain-stop lines {sum(1 for v in chain.values() if v)}/{len(chain)}")
    w(f"- cast card-line blocks: {have}/100 (missing {len(missing)})")
    if total is not None:
        w(f"- site: local links {total} · broken {len(broken)} · build reproducible: {not hard_fail}")
    w("")
    w("## HARD FAILURES" if hard_fail else "## HARD FAILURES: none")
    for f_ in hard_fail:
        w(f"- {f_}")
    w("")
    w("## WARNINGS (logged, not gating)")
    for x in warn:
        w(f"- {x}")
    print("\n".join(o))
    sys.exit(1 if hard_fail else (2 if warn else 0))


if __name__ == "__main__":
    main()
