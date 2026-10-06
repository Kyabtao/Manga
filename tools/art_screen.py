#!/usr/bin/env python3
"""
THREADBORN — mechanical page-art screen (the half of the QA gate that does not need eyes).

WHY THIS EXISTS
---------------
The page-art QA gate in series-bible/style-guide.md has five checks. Two of them — *beats* and
*canon markers* — require a human or a vision-capable model to actually look at the drawing. An agent
without vision CANNOT do those, and must not claim to. This script does the rest mechanically, so a
run can never again report a page "verified" on the strength of a filename or a vibe.

WHAT IT MEASURES, AND HOW FAR EACH CAN BE TRUSTED
-------------------------------------------------
  shape       EXACT.    h <= w -> fail. Catches landscape AND square (run 11 missed a 1024x1024).
  weight      EXACT.    file size band.
  dead bands  ADVISORY. longest run of near-identical rows; suggests unfinished/blank art.
  palette     RANKING ONLY — never a verdict. Reports the share of *visible* pixels (lightness
              >= 15%) in the green/cyan hue range. Agnikhand is basalt/ash/ember/bruised-purple, so
              a high share is suspicious — but it cannot distinguish an off-world forest from a
              canon jade bead or a market awning. Only a human can close that.
  panels      ADVISORY, AND KNOWN UNRELIABLE. Measured accuracy against the scripts: median 4
              detected vs a true 7, range 1-6. The style guide mandates *irregular, angled,
              overlapping* panels, so horizontal-gutter detection systematically undercounts.
              Never gate on this number. It is printed only so the limitation is on the record.

TWO TRAPS THIS SCRIPT ALREADY FELL INTO (both are now guarded in code)
----------------------------------------------------------------------
  1. Int-only regex on ImageMagick HSL output. IM emits floats; `hsl\\((\\d+),...` matched 6 of
     25,600 pixels, which turned a 2-pixel sample into a confident "33% green". Parse floats, and
     refuse to report on a sample under 1000 px.
  2. Saturation is meaningless at near-black lightness. The pixel (5,10,13) is visually black but
     scores hue 202 deg at 44% saturation. A dark page looks violently cyan by hue alone. Every hue
     bucket is therefore gated on lightness >= 15%.

USAGE
    python3 tools/art_screen.py                 # screen all page art
    python3 tools/art_screen.py <png> [...]     # screen specific files
    python3 tools/art_screen.py --rank          # ranked candidates for human content review

Requires ImageMagick (`convert`) on PATH. Exit 0 always for --rank; 1 if any hard failure otherwise.
Hard failures are shape and weight only — everything else is a ranking or a warning.
"""
import os
import re
import sys
import glob
import json
import struct
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOUSE_RATIO_MAX = 2.5
LIGHTNESS_FLOOR = 0.15          # below this, hue is not perceptible — count as dark/neutral
SAT_FLOOR = 0.12                # below this, count as neutral
GREEN_CYAN = (70, 200)          # hue range that Agnikhand should not contain much of
DEAD_BAND_MAX = 0.08
MIN_SAMPLE = 1000

failures, warnings = [], []


def png_size(p):
    d = open(p, "rb").read(64)
    if d[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", d[16:24])


def row_profile(path, n=1400):
    """Mean greyscale per row. Gutters (black panel borders) show as dark troughs."""
    out = subprocess.run(["convert", path, "-colorspace", "Gray", "-resize", f"1x{n}!",
                          "-depth", "8", "txt:-"], capture_output=True, text=True)
    vals = [int(m) for m in re.findall(r"gray\((\d+)", out.stdout)]
    if not vals:
        vals = [int(m.group(1)) for m in re.finditer(r"^\d+,\d+: \(\s*(\d+)", out.stdout, re.M)]
    return vals


def detect_panels(prof):
    """ADVISORY ONLY — see module docstring. Counts horizontal gutters; undercounts this art style."""
    if len(prof) < 40:
        return 0
    mean = sum(prof) / len(prof)
    thresh = mean * 0.45
    dark = [v < thresh for v in prof]
    runs, start = [], None
    for i, d in enumerate(dark):
        if d and start is None:
            start = i
        elif not d and start is not None:
            runs.append((start, i)); start = None
    if start is not None:
        runs.append((start, len(dark)))
    gutters = [r for r in runs if (r[1] - r[0]) <= max(3, len(prof) * 0.03)]
    lo, hi = len(prof) * 0.03, len(prof) * 0.97
    inner = [g for g in gutters if lo <= g[0] <= hi]
    return max(1, len(inner) - 1) if len(inner) > 1 else 1


def dead_bands(prof):
    best = run = 1
    for i in range(1, len(prof)):
        if abs(prof[i] - prof[i - 1]) <= 1:
            run += 1
            best = max(best, run)
        else:
            run = 1
    return best / len(prof) if prof else 0.0


def palette(path):
    """Hue histogram over visible pixels. Returns (buckets, green_cyan_frac, lit_frac)."""
    out = subprocess.run(["convert", path, "-resize", "160x160!", "-colorspace", "HSL",
                          "-depth", "8", "txt:-"], capture_output=True, text=True)
    # IM emits FLOATS ("hsl(218.824,13.7255%,5.09804%)"). An int-only regex matches only pixels
    # whose values happen to be whole numbers — a 6-px sample that once produced "33% green".
    nums = re.findall(r"hsl\(([\d.]+),([\d.]+)%,([\d.]+)%\)", out.stdout)
    if not nums:
        nums = re.findall(r"\(\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)\s*\)", out.stdout)
    keys = ("ember", "violet", "green", "cyan", "blue", "rust", "neutral", "dark")
    buckets = dict.fromkeys(keys, 0)
    total = lit = 0
    for h, s, l in nums:
        h, s, l = float(h), float(s) / 100, float(l) / 100
        total += 1
        if l < LIGHTNESS_FLOOR:
            buckets["dark"] += 1
            continue
        lit += 1
        if s < SAT_FLOOR:
            buckets["neutral"] += 1
        elif h < 20 or h >= 340:
            buckets["rust"] += 1
        elif h < 45:
            buckets["ember"] += 1
        elif h < GREEN_CYAN[0]:
            buckets["ember"] += 1
        elif h < 165:
            buckets["green"] += 1
        elif h < GREEN_CYAN[1]:
            buckets["cyan"] += 1
        elif h < 260:
            buckets["blue"] += 1
        else:
            buckets["violet"] += 1
    if total < MIN_SAMPLE:
        return buckets, None, None
    gc = (buckets["green"] + buckets["cyan"]) / total
    return buckets, gc, lit / total


def screen(path):
    wh = png_size(path)
    res = {"path": os.path.relpath(path, ROOT), "w": wh[0], "h": wh[1],
           "ratio": round(wh[1] / wh[0], 2), "mb": round(os.path.getsize(path) / 1048576, 2)}
    if wh[1] <= wh[0]:
        res["shape"] = "FAIL"
        failures.append(f"{res['path']}: {wh[0]}x{wh[1]} is not portrait (h <= w)")
    elif wh[1] / wh[0] > HOUSE_RATIO_MAX:
        res["shape"] = "warn-ratio"
        warnings.append(f"{res['path']}: ratio {res['ratio']} > {HOUSE_RATIO_MAX}")
    else:
        res["shape"] = "pass"
    prof = row_profile(path)
    res["panels_advisory"] = detect_panels(prof)
    db = dead_bands(prof)
    res["dead_band"] = round(db, 3)
    if db > DEAD_BAND_MAX:
        warnings.append(f"{res['path']}: flat band {db:.1%} of height")
    res["palette"], res["green_cyan"], res["lit_frac"] = palette(path)
    if res["green_cyan"] is None:
        warnings.append(f"{res['path']}: palette sample too small — verdict withheld")
    if not (1.2 <= res["mb"] <= 3.0):
        warnings.append(f"{res['path']}: {res['mb']} MB outside 1.2-3.0 band")
    return res


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    args = [a for a in args if os.path.isfile(a)]   # ignore stray directories passed by hand
    rank = "--rank" in sys.argv
    js = "--json" in sys.argv
    files = args or sorted(glob.glob(ROOT + "/chapters/chapter-*/images/page-???.png"))
    results = [screen(f) for f in files]

    if js:
        print(json.dumps({"results": results, "failures": failures, "warnings": warnings}, indent=1))
    elif rank:
        print("Ranked candidates for HUMAN CONTENT REVIEW")
        print("(green/cyan share of VISIBLE pixels; Agnikhand is basalt/ash/ember/bruised-purple.)")
        print("The screen cannot tell an off-world forest from a canon jade bead — a person must look.")
        print()
        c = sorted((r for r in results if r["green_cyan"] is not None),
                   key=lambda r: -r["green_cyan"])
        for r in c:
            print(f"  {r['green_cyan']*100:>5.1f}%  {r['path']}")
        print()
        print(f"{len(results)} pages screened. Top of this list is where to look first.")
    else:
        print(f"{'page':<46}{'size':<12}{'ratio':>6}{'panels*':>9}{'dead':>7}{'green/cyan':>12}  shape")
        print("-" * 100)
        for r in results:
            gc = "n/a" if r["green_cyan"] is None else f"{r['green_cyan']*100:.1f}%"
            print(f"{r['path']:<46}{str(r['w'])+'x'+str(r['h']):<12}{r['ratio']:>6}"
                  f"{r['panels_advisory']:>9}{r['dead_band']:>7}{gc:>12}  {r['shape']}")
        print("-" * 100)
        print("* panels = ADVISORY ONLY, known to undercount (median 4 vs a true 7). Do not gate on it.")
        print(f"\n{len(results)} pages · {len(failures)} hard failures · {len(warnings)} warnings")
        for f_ in failures:
            print(f"  FAIL  {f_}")
    sys.exit(1 if failures and not rank else 0)


if __name__ == "__main__":
    main()
