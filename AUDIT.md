# THREADBORN — FULL REPO AUDIT

**Date:** 2026-09-19 · **Branch:** `arena/01a0b63a-manga` · **Scope:** chapters 001–008, website, tooling
**Auditor:** Arena agent · **Method:** automated sweep + manual image inspection

---

## 0. Headline

| | |
|---|---|
| **Critical findings** | **1** — Hindi translations for Chapters 003–008 are ~93% English |
| **Major findings** | **2** — one wholly wrong page image; one landscape image in a vertical strip |
| **Minor findings** | **3** — cast-file format drift, cast-file depth drift, one unresolved pronoun in a style guide |
| **Structural integrity** | **PASS** — 80/80 scripts, images, casts, summaries all present and correctly named |
| **Continuity integrity** | **PASS** — lockbox chain, stitch state, four-notes rule and wax grammar all hold |

---

## 1. CRITICAL — Hindi translation coverage collapses after Chapter 002

This is the most important finding in the audit and it violates a standing user constraint
(*"webtoon full colour, vertical strip, **English + Hindi**"*).

`chapters/gen_support.py` generates the `.hi.md` files for Chapters 003–008 by:
1. swapping a fixed list of ~150 strings pulled from a `HINDI` dict, and
2. renaming the **section headers** (`## PANEL` → `## चित्र-खाना`, `**Camera:**` → `**कैमरा:**`, etc.)

Everything else — all prose, all camera directions, all image descriptions, all writing notes, and
the large majority of dialogue and captions — **is left in English.** Chapters 001–002 were
hand-translated and are essentially complete.

### Measured coverage

**Progress:** Chapter 003 has been fully hand-translated (see below). Chapters 004–008 remain.

| Chapter | Devanagari chars | Latin chars | % Devanagari | Verdict |
|---|---:|---:|---:|---|
| 001 | 47,165 | 1,544 | **96.8%** | complete |
| 002 | 55,457 | 1,092 | **98.1%** | complete |
| 003 | 7,694 → 71,266 | 36,109 → 2,043 | 17.6% → **97.2%** | ✅ **FIXED** |
| 004 | 1,797 → 58,455 | 21,930 → 3,466 | 7.6% → **94.4%** | ✅ **FIXED** |
| 005 | 2,062 → 21,487 | 21,211 → 1,280 | 8.9% → **94.4%** | ✅ **FIXED** |
| 006 | 2,789 → 34,161 | 35,216 → 1,290 | 7.3% → **96.4%** | ✅ **FIXED** |
| 007 | 3,671 | 51,886 | 6.6% | **broken** |
| 008 | 2,975 | 54,020 | 5.2% | **broken** |

Quoted-line analysis (dialogue and captions only, ≥3 Latin words and zero Devanagari = untranslated):

| Chapter | untranslated quoted lines |
|---|---:|
| 003 | 130 (37%) |
| 004 | 96 (53%) |
| 005 | 105 (50%) |
| 006 | 165 (51%) |
| 007 | 352 (48%) |
| 008 | 401 (47%) |

### Sample — `chapter-008/story/page-006.hi.md`

```
## चित्र-खाना 1 — Close, the name (~13%)

**कैमरा:** Jadi drinks the tea and sets it down. Ira has not answered the request. Instead she
asks the question she has been holding since the doorway.

**चित्र:** Two women at a counter, a cup of tea, and a transaction that is not about money.
```

Headers are translated; the content is not. This is a *mechanical* substitution, not a translation.

### Second defect in the same generator: Hindi word order for names

`gen_support.py` writes character headers as `Ira Sutar — इरा सुतार`, i.e. Latin name first. The
hand-written Chapter 001–002 casts consistently use the Hindi form in the running text. Cosmetic,
but it is the same generator and should be fixed in the same pass.

### Recommendation

Chapters 003–008 needed **60 files re-translated**. **Chapters 003–006 are now complete** (40 files,
97.2%, 94.4%, 94.4% and 96.4%). **Chapters 007–008 remain — 20 files.** This is a real translation job, not a script run.

**Method that worked for Chapter 003** (use it for the rest): read the EN page, write the HI page
in full — prose, camera, image, captions, dialogue, SFX, notes and card hooks — then re-run
`gen_support.py` and confirm the coverage gate clears the chapter. Ten pages per session is a
comfortable pace.

Two options if a full re-translation is not wanted:

- **Option A (recommended):** re-translate all 60 files to the Chapter 001–002 standard, chapter by
  chapter, starting with 003 so the back catalogue stays in order.
- **Option B:** accept the current state as "English script with Hindi apparatus" and update the
  README to say so explicitly, rather than claiming full bilingual parity.

**Do not** run `gen_support.py` again for chapters 003–008 until this is resolved — it will not
improve the output and will overwrite any hand-translation that is added.

---

## 2. MAJOR — Chapter 004 Page 001 image is from a different project entirely

`chapters/chapter-004/images/page-001.png` (1408×768) contains: a modern police officer in a
contemporary uniform with a shoulder patch, a chalkboard reading **EXCHANGE 1** with Hebrew
lettering underneath, a green goblin in a hoodie, and a young woman in a backpack. There is no
panel, character, costume or object from THREADBORN in it.

The script for that page (`chapter-004/story/page-001.md`) calls for: the Knot & Nail opening, a
Grey Clerk at the threshold with a slate requesting lockbox inspection, Kessa reading the slate
without touching it.

**Status: FIXED this session.** Regenerated at 768×1376 (portrait, correct cast and content).

---

## 3. MAJOR — Chapter 007 Page 007 image was landscape in a vertical strip

`chapters/chapter-007/images/page-007.png` was 1376×768. Content was broadly correct (the disbound
archive, the old keeper with a needle, the girl among the open books) but the aspect ratio is
horizontal, which breaks the series' vertical-scroll format and produces a squashed panel in the
reader.

**Status: FIXED this session.** Regenerated at 768×1376.

### Remaining dimension spread (informational)

54 images are 768×1376 (the dominant format, correct). Others: 14 × 864×1821, 5 × 672×1584,
3 × 860×1828, 1 × 887×1774, 1 × 848×1264. All portrait, all valid PNGs, but the spread means panels
scale differently between chapters in the reader. Consider standardising on 768×1376 for future
chapters.

---

## 4. MINOR — Cast-file format drift between Chapters 001–002 and 003–008

Chapters 001–002 have **hand-written, page-specific cast notes** — e.g.
`chapter-002/characters/cast-page-003.md` carries a `> **Page 003 note:**` block describing what
Ira does on that page and what Guthli does on that page.

Chapters 003–008 have **machine-generated cast files** containing only a name, a Devanagari form
and a back-link to the character sheet. Every file is structurally valid and every link resolves
(0 broken links across all 80 files) — but roughly 50 of them carry no actual page information.

**Recommendation:** decide whether cast files are "who is on this page" (current Chapters 003–008
behaviour) or "who is on this page and what they do" (Chapters 001–002 behaviour), then either
backfill or amend the convention in `README.md` § Structure conventions.

### Cast-file coverage check — PASS

All 80 cast files reference Ira Sutar (case-insensitive check). An earlier automated pass flagged 7
files in Chapter 002 as missing her; that was a **case-sensitivity false positive** and is not a
defect.

---

## 5. MINOR — Unresolved placeholder in the style guide

`series-bible/style-guide.md` line 48 contains `page-XXX.hi.md` in a Hindi-formatting instruction.
This is a *legitimate* use of `XXX` as a filename pattern, not a TODO — **no action required**, noted
for completeness so a future audit does not re-flag it.

All other placeholder patterns (`TODO`, `FIXME`, `TBD`, `Lorem`, `placeholder`, `[ ]`, `(pending)`)
return zero hits across all Markdown in the repo.

---

## 6. PASS — Structural integrity

| Artifact | Expected | Found | Status |
|---|---:|---:|---|
| EN scripts (`page-NNN.md`) | 80 | 80 | ✅ |
| Hindi scripts (`page-NNN.hi.md`) | 80 | 80 | ✅ |
| Page images (`page-NNN.png`) | 80 | 80 | ✅ |
| Cast files (`cast-page-NNN.md`) | 80 | 80 | ✅ |
| Chapter summaries | 8 | 8 | ✅ |
| Glossary + locations per chapter | 16 | 16 | ✅ |

- **Naming conventions:** zero off-convention files across `story/`, `images/`, `characters/`.
  Every file matches `page-NNN.md`, `page-NNN.hi.md`, `page-NNN.png`, `cast-page-NNN.md`,
  `<name>.md` or `<name>-ref.png`.
- **Character sheet placement:** correct per the "chapter of first appearance" rule —
  `chapter-001/` (ira-sutar, kessa, rekhak-vahni, patra), `chapter-006/` (nandi), `chapter-008/`
  (jadi). Later chapters link back and do not copy.
- **Image validity:** all 80 files are valid PNGs by magic number, all > 50 KB, none corrupt.
- **Repository weight:** 211 MB in `chapters/`, 80 images averaging ~2.5 MB. No file exceeds 5 MB.
  Well within the 128 MB / 10,000 file patchset cap.

---

## 7. PASS — Continuity audit

### Lockbox object chain — consistent

Ch.003 p001 (opens) → p002 **3** → p006 **4** → Ch.004 p005 **5** → p008 **6** → p010 **7** →
Ch.005 p001 **7** → Ch.006 p006 **8** → p007/p009/p010 **8** → Ch.007 p001 **8**.
The counts ascend without contradiction. The earlier Ch.003 p002 `Two objects → Three objects`
correction is confirmed present in both EN (`line 123`) and Hindi (`line 123`).

*Note:* Ch.003 p001 line 69 reads *"Two objects, one question"* — this refers to the charcoal
rubbing and the cut-end laid side by side, **not** to the box. Correct as written; not a regression.

### Stitch state timeline — consistent

Ch.004 p008 opens the stitch → Ch.005 p001 carries it open → Ch.007 p010 **Ira closes it herself**
on the supply step → Ch.008 p001 shows it closed (drawn twice, deliberately) → Ch.008 p009 **she
re-opens it** at the hatch. Every state change is scripted, motivated and visible on panel.

### Four-notes rule — consistent

*"Four notes must match wrongly first; nothing audible may match them before then."*
Ch.002 stores them (off-key, never words). Ch.003 p006 matches them **wrongly** through Rekhak's
chain (wrong key, same shape). Ch.006 p007 hears them **correctly** through the thread's memory.
Ch.007 p005 live. Ch.008 p009 live and immediate. The constraint holds.

### Wax grammar — consistent

Crimson = the principal's private hand; grey = the Council. Verified across the posting order (Ch.003),
the call-slip (Ch.002), the census cross-out (Ch.002), the licence and its two-pour seal (Ch.007),
the crease-writs (Ch.007), and the Office warrant with a crimson countersignature (Ch.008).

### Locked character rules — held

- **Kessa's interiority is shutters and hands only** — she never monologues. Verified: her
  interiority is rendered through the hatch she does not climb (Ch.007 p001), the loupe, the flat
  hands on the counter, and the tally-thread.
- **The Loom never speaks** — it turns and is described; it never comments. Verified across all
  chapters including both citywide responses (Ch.001 p008, Ch.008 p009, where it is deliberately
  absent).
- **The mother never appears on panel and never speaks** — verified across Ch.006 (file only),
  Ch.007 (wax, thread, extracted spines, a passed sentence), Ch.008 (a hatch, a forearm, a roster
  recited twice).

### Canon correction applied mid-session — now consistent

Ch.007 p008 originally stated the Roll of Hands listed *"Name, kind, the year the strand went in."*
Ch.008 reveals the Roll **never held names** (a name is a handle; the store of names was kept by
Jadi in her head). Corrected in:
- `chapter-007/story/page-008.md` (Nandi's dialogue)
- `chapter-007/chapter-summary.md` (canon rule 8, with a note on the correction)
- `README.md` (story-so-far entry)

### Flagged for Chapter 009

**The chain-stop budget is OVERDUE.** It has been held unspent across Chapters 006, 007 and 008 —
three consecutive chapters. The README next-page brief and `chapter-008/chapter-summary.md` both
carry this flag. Chapter 009 must spend it.

---

## 8. PASS — Website and links

- `python3 website/build.py` runs clean; 267 HTML files generated including all of `chapter-008/`.
- **11,131 internal HTML links checked across the built site — 0 broken.**
- **0 broken links across all 80 cast files and 8 chapter summaries.**
- Generated HTML is committed alongside content, per the repo's stated convention.

---

## 9. PASS — Git and PR state

- Working tree clean at the time of audit apart from this session's fixes.
- Branch `arena/01a0b63a-manga` → remote `origin/arena/01a0b63a-manga` in sync.
- PR [#3](https://github.com/Kyabtao/Manga/pull/3) OPEN, 551 changed files.

**Note:** PR #3's title still reads *"Ch. 003 Page 001: The Hand That Opens — morning of the letter"*,
which described the session's first commit. It now covers Chapters 003–008. **Update the PR title and
body** to reflect the full scope before review.

**Incident logged:** at the start of this audit the local working tree had been reset to the branch
point `a06417c`, losing Chapters 003–008 locally. The remote branch was intact and the work was fully
recovered from `origin` (`49bedd0`). No content was lost. Worth knowing that a workspace
re-provision resets the local clone against the remote.

---

## 10. Action list

| # | Priority | Item | Status |
|---|---|---|---|
| 1 | **Critical** | Re-translate Hindi — **Ch.003–006 done** (97.2 / 94.4 / 94.4 / 96.4%); Ch.007–008 remain (20 files) | 🔶 in progress |
| 2 | Major | `chapter-004/images/page-001.png` was the wrong project's art | ✅ fixed |
| 3 | Major | `chapter-007/images/page-007.png` landscape, not portrait | ✅ fixed |
| 4 | Minor | Cast-file depth/format drift (Ch. 003–008 vs 001–002) | ⬜ open |
| 5 | Minor | Standardise image dimensions on 768×1376 | ⬜ open |
| 6 | Housekeeping | Update PR #3 title and body to Chapters 003–008 | ⬜ open |
| 8 | Minor | Ch.004 p008 said "END OF CHAPTER FOUR" mid-chapter (p010's line) — removed from EN + HI | ✅ fixed |
| 7 | Process | Hindi-coverage gate added to `gen_support.py`; correctly clears Ch.003, flags Ch.004–008 | ✅ done |

---

*End of audit.*
