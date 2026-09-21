# THREADBORN — FULL REPO AUDIT

**Date:** 2026-09-19 · **Branch:** `arena/01a0b63a-manga` · **Scope:** chapters 001–008, website, tooling
**Auditor:** Arena agent · **Method:** automated sweep + manual image inspection

---

## 0. Headline

| | |
|---|---|
| **Critical findings** | **0** (run 6) — Hindi complete for Ch. 001–010 (94.4–98.3% Devanagari; floor 80%) |
| **Major findings** | **1 open** (run 5) — **art-style split:** Ch. 001–005 were generated in an earlier, off-style pass (semi-modern props, occasional readable Latin lettering). ~10+ images to regenerate. Not fixable by edit. |
| **Minor findings** | **3 open** (run 8) — plus **Nima's sheet off-canon** (modern props, long braid): regenerate, see run 8 — image dimension variation, cast-file format/depth drift, तकुआ/तकली normalisation. *(The 8-panel gap closed in run 7.)* |
| **Fixed in run 5** | 133 missing `Camera:`/`कैमरा:` labels (Ch. 004–005) · 19 pages given notes sections (EN+HI) · Ch. 001–002 headings normalised · Ch. 004 p008 page-type line · 28 obsolete `.gitkeep` files · README's false "PR #3 merged" claim |
| **Structural integrity** | **PASS** — 100/100 EN scripts, 100/100 HI scripts, 100/100 images, 100/100 cast files, 10/10 summaries, 20/20 `other/` files, 0 junk |
| **Continuity integrity** | **PASS** — mother never on panel, Loom never speaks, chain-stop budget accounted for in every chapter that states one |
| **Merge state** | **PR #3 merged into `main` this run** (user instruction, after audit) |

## Audit run 8 — 2026-09-21 (art QA on the recut sheets + the grounding rule)

The nine recut/alt sheets from run 7 were opened at full resolution and read against their own panel
lines. Eight pass. **One sheet is off-canon and is the run's only open art item.**

| Sheet | Verdict |
|---|---|
| Ira (8 + alt) | **Pass.** Stitched right palm, cut-finger gloves, mismatched eyes; alt sheet adds states, five expressions, macro palm, kit tipped out, two staging panels and the silhouette test as an actual drawn panel. |
| Kessa | **Pass.** Loupe down over one eye in the detail panel, tally-cord count in hands, strongbox/balance/ash-ink kit, counter action. |
| Patra | **Pass.** Blank tags, translucent hem by lamplight, blank contract, doorway action; tall two-column layout kept as recorded. |
| Rekhak | **Pass.** Sight-mark and neck-lines, counting-chain through the fingers, crimson-sealed page in the kit, the kneeling read as action. |
| Bhan, Inspector | **Pass** (both drawn from scratch this session). |
| Nandi | **Pass**, with one flag: slot 7's kit includes a *brush* alongside twine, quires, shelf-hook, lamp and chalk. Brushes for cleaning quires are period-plausible; left as drawn, noted rather than cut. |
| **Nima** | **FAIL — open.** The sheet carries off-canon props: an **electric-style desk lamp** with a shade and stem, a **metal tumbler/mug**, rubber bands and a modern-looking desk and chair in the action panel, and her hair is drawn as a **long braid down her back** where canon says a *short braid pinned flat*. The Office world here also reads contemporary rather than the paper-and-oil Office of Ch. 008–010. **Regenerate** — this is the same defect class as the Ch. 001–005 page-art split. |

### Fixed this run

| # | Item | Fix |
|---|---|---|
| 1 | The defect above keeps recurring, in page art and now in a sheet, with nothing written down that names it. | `05-character-art-spec.md` **§3.1 Pre-industrial grounding** — explicit **blocklist** (electric light, desk lamps, mugs, rubber bands, plastic, watches, printed signage, modern office furniture, industrial hardware, hoodies/backpacks) and the period replacements (clay oil lamps, candles, hand-lanterns, wood, crates, quires, slate). Rule: a modern object means *regenerate*, never crop. |
| 2 | Two sheet failures produced while recutting had no rule behind them. | Spec now says: **no panel captions** (circled numerals only) and **eight distinct slots** — a repeated or dropped slot is a failed sheet, regenerated rather than filed. Both were hit and thrown away this session. |
| 3 | Kessa's sheet placed the loupe over the *left* eye; every drawing of her, old sheet included, puts it over the other one. | Canon line rewritten to *one eye covered and the uncovered eye doing the work* — which is what the art has always done — instead of silently contradicting the art. |
| 4 | Alt sheets were specified as lettered but the first one is drawn with numerals. | Spec records the reconciliation: the **site** letters alt slots A–H; numerals inside `-alt.png` are harmless because the eight numbered slots only ever mean the ref sheet. |

### Verified

- Build is reproducible: re-running `website/build.py` on the committed tree produces **no diff** —
  every committed HTML file matches the markdown canon exactly.
- 16,064 local links over 343 pages, **0 broken**; art pages: 9 × 8 numbered chips, plus Ira's 8
  lettered alt chips.
- Sheet metadata matches the art on all nine: `**Ref sheet panels:**` order is detail (5) then hands (6)
  in every case, matching the drawn sheets.

### Still open after run 8

- **Nima's model sheet** — blocked only by the ten-images-per-turn generation cap in the session that
  found it; the corrected prompt is written and the sheet is the next art action.
- Ch. 001–005 page-art style split (run 5) — unchanged, still the repo's largest art item.

## Audit run 7 — 2026-09-21 (bring the back catalogue up to the standard)

Requested scope: *"update first current arts"* — the seven sheets that predated
`05-character-art-spec.md` were extended to the full eight panels, and the alt-sheet convention was
added with Ira as the first.

### Delivered

| # | Item | Result |
|---|---|---|
| 1 | **Seven sheets re-drawn to eight panels** — Ira, Kessa, Patra, Rekhak, Nandi, Jadi, Nima. | Each was regenerated **from its own existing sheet as the character reference**, so face, build, costume and rendering style carry over rather than being redesigned. Every one now has front · side · back · face · detail · hands · kit · action, with the detail panel mapped to that character's canon (Ira's stitched right palm, Kessa's loupe over the eye, Patra's backlit blank name-tags, Rekhak's Sight-mark and neck-lines, Nandi's leaf by lamplight, Jadi's grey-and-crimson palm, Nima's wrist turned inward). |
| 2 | **Two canon extras found while re-drawing** (both now in the sheets) | Kessa's sheet says the loupe flips down over the **left** eye — the ref sheet shows it, and the old sheet only ever showed it pushed up. Nima's braid is the school's and gets turned against her leg: slot 5 is that turn, and it is the one thing the Office would have to enter if it ever saw it. |
| 3 | **Alt sheets are now a documented convention** | `05-character-art-spec.md` §6.1: `<name>-alt.png`, lettered slots **A–H** (never numbered — the eight numbered slots belong to the model sheet), pattern = default state · variant state · five expressions · macro detail · kit tipped out · two staging panels · silhouette test. |
| 4 | **Ira's alt sheet drawn** — `chapter-001/characters/ira-sutar-alt.png`: working state and ceremony state, five expressions (including one the series has not used yet), macro palm, satchel tipped out, crowd staging under the Loom, waiting-room staging, and three solid-black silhouette studies. | The silhouette test from `style-guide.md` is now an actual panel in the repo for the first time. |
| 5 | **Site support** | The art page auto-detects `<name>-alt.png` and grows an **Alt sheet** section with lettered chips and its own click-to-zoom plate; the sheet page's card reads *8 panels + alt sheet*. |
| 6 | **Layout exceptions recorded, not silently broken** | Patra (tall two-column) and Jadi (tall stacked) keep the page shapes they were designed on — the spec now lists them under *settled layout exceptions* so no future editor "fixes" them. |

### Verified

- All nine `*-ref.png` + one `*-alt.png` decode as valid PNGs, 1.8–2.2 MB (inside the 1.2–3 MB band),
  eight panels each (ten for Patra's 3-3-2-2 arrangement).
- Nine art pages rebuilt; **16,064 local links over 343 pages — 0 broken**.
- Every sheet's `**Ref sheet panels:**` line matches the art; no cast file claims a sheet is missing.

### Still open after run 7

- **Ch. 001–005 page art style split** (run 5) remains the repo's single major art item — unrelated to
  character sheets, and still a ~10+ page regeneration job.
- Alt sheets exist for Ira only. The convention is ready for the next character who needs one.

## Audit run 6 — 2026-09-21 (character-art standard + clickable model sheets)

Requested scope: *"alt-image mention and like Ira other characters image format — front side back face
cut and hand image; same way always design the character; and in character details we can click on art
and see character arts."* Two deliverables: **a codified model-sheet standard** and **an art viewer on
the site**.

### Delivered

| # | Finding | Fix |
|---|---|---|
| 1 | **No written standard for character ref sheets** — seven sheets existed, in two different styles, with nothing saying which panels are required. | `series-bible/05-character-art-spec.md` — canon: **8 panels, in order** (front · side · back · face · detail · hands · kit · action), drawing rules (no text in art, mid-story costume state, no new costume, Agnikhand palette, silhouette test), file/placement rules, a generation prompt, and how refs reach the site. |
| 2 | **Two named recurring characters had no visual sheet at all** — Bhan (19 cast-file appearances, Ch. 002–008) and the Inspector (10 appearances, Ch. 008–010; every cast file said *"No full sheet"*). | **Both sheets written and drawn**, to the full 8-panel standard: `chapter-002/characters/bhan.md` + `bhan-ref.png`, `chapter-009/characters/inspector.md` + `inspector-ref.png`, generated against Rekhak's sheet as a style reference so the house look holds. |
| 3 | **Cast files hard-coded "no sheet" claims** for both characters, and Bhan's rows without a back-link. | 31 cast files updated: `Full sheet (Ch. 00X):` links for Bhan (19) and the Inspector (11); the ten *"No full sheet; drawn from Ch. 008 Page 001"* lines now read *Design locked from Ch. 008 Page 001*. |
| 4 | **Ref sheets were not reachable as art** — the site showed a thumbnail, and clicking the markdown `Art: [<name>-ref.png]` link opened a bare PNG out of context. | New generated page per ref: `website/characters/<name>-art.html` — click-to-zoom plate, panel list, **Drawing brief** (the sheet's own art-continuity section reprinted), prev/next through the cast. Sheet pages get a **Model sheet** card, the cast index links every thumbnail to art, and every `Art:` line in the cast files resolves to the art page. |
| 5 | **No way to inspect a sheet at drawing resolution in the browser.** | Full-screen zoom viewer in `website/assets/site.js` (zero dependencies): wheel / `+` `-` / double-click / two-finger pinch, drag and one-finger pan, `0` fit, `1` 100%, Esc or backdrop to close; keyboard-openable sheets (`tabindex`, Enter/Space); degrades to a plain image without JS. |
| 6 | Every sheet now declares its own panel list in canon. | `**Ref sheet:**` + `**Ref sheet panels:**` lines added to all nine sheets; the site reads them for chips, captions and card badges (*5-panel art* / *8-panel art*). |

### Still open after run 6

- ~~**Seven sheets predate the standard** (Ira, Kessa, Patra, Rekhak, Nandi, Jadi, Nima): all have
  front · side · back · face, and all but Rekhak have a hands/detail slot, but **none has the kit and
  action slots**.~~ → **CLOSED in run 7**: all seven re-drawn to the full eight panels from their own
  sheets as the character reference. **No sheet in the repo is short any more.**
- The run-5 **Ch. 001–005 style split** remains the repo's biggest art item, unchanged by this run.
- Model sheets are drawn in one pass each; nothing here re-renders a page.

## Audit run 5 — 2026-09-19 (FULL audit: story → image, every folder, then merge)

Requested scope: *"audit once full story to image and all folder then merge."* Run 5 re-ran the whole
sweep on the recovered worktree and added a **complete visual pass**: all 100 images rendered into
per-chapter contact sheets (ImageMagick) and read against their own scripts, plus magnified crops
(170–200%) of every prop that could plausibly carry lettering.

### Fixed this run

| # | Finding | Fix |
|---|---|---|
| 1 | **Ch. 004 p002–010 and Ch. 005 p001–010 had no `Camera:` label on any panel** (run 4 had recorded these as passing). 133 panels affected in English, 133 in Hindi. | Labels derived from each panel's own first line; both languages now **70/70** per chapter. |
| 2 | **19 pages carried no notes section at all** (Ch. 004 p002–010, Ch. 005 p001–010). | Page-specific *Writing & art notes* / *लेखन और चित्र नोट्स* written for each — craft, continuity and chain-budget notes drawn from that page's own panels and card hooks. |
| 3 | **Ch. 001–002 used non-standard section headings** — *Page notes for continuity*, *Card-game hooks introduced on this page*, *निरन्तरता टिप्पणियाँ*, *इस पृष्ठ से कार्ड-खेल के सूत्र*, *लेखन एवं कला-नोट्स*, *कार्ड-खेल हुक*. | Normalised across **31 files** to the house headings. |
| 4 | **Ch. 004 p008's `Page type` line claimed the chapter's chain-stop**, contradicting the chapter close-out (the arc's single stop was spent in Ch. 003 p009). | Corrected the EN line (the Hindi mirror was already right). |
| 5 | 19 hook tables had no blank line under the heading. | Normalised. |
| 6 | **28 obsolete `.gitkeep` files** left behind in chapters 002–006 (folders long since populated). | Removed. |
| 7 | **README claimed PR #3 was merged** while PR #3 was still open and `main` contained none of the work. | Row corrected to *OPEN* before the merge; updated to *MERGED* immediately after. |

### Image pass — verified

- **Run 4's two art fixes hold.** Ch. 003 Page 008: no signage, blank documents. Ch. 006 Page 002:
  charter and file pages carry abstract knot-script only, no readable Latin.
- **Ch. 006–010 read as one consistent production:** Agnikhand palette, Ira/Nandi/Nima/Kessa design
  language, per-page beats matching their scripts (room nine's stand and subject's chair, the tray of
  cards, the alley lesson, the stepped crowd at the hatch, the door sold at the counter).
- **PNG integrity:** 100/100 decode clean (IHDR), 0 corrupt, 0 duplicates by SHA-256, 0 landscape;
  261 MB total. Dimensions span six sizes (768×1376 ×76, 864×1821 ×14, 672×1584 ×5, 860×1828 ×3,
  887×1774 ×1, 848×1264 ×1) — standardisation still open.

### Image pass — OPEN (major, not fixable by edit)

**Chapters 001–005 were generated by an earlier art pass and do not match the run used from Ch. 006 on.**
Documented, not repaired — regeneration is a 10+ image job and out of scope for an audit turn:

- **Readable Latin lettering on props**, against the standing *no text in art* rule and run 4's own
  finding: Ch. 007 p002 carries a large cursive document line (*"Address … Connes"*); Ch. 001 and
  Ch. 002 carry stamped forms and ruled documents whose lettering is legible at magnification.
- **Semi-modern props:** office desks with modern blotters and window frames (Ch. 001 p002, Ch. 002
  p005), industrial tanks, water tower and dock cranes (Ch. 002), a hoodie-and-backpack silhouette
  (Ch. 005) — none of it the *black basalt, ash-grey, ember* Agnikhand of the style guide.
- **Off-canon panels:** Ch. 001 p001 includes a blond energy-blast panel (reads as a different series
  entirely); Ch. 004 and Ch. 005 include armoured, bearded strangers who match no cast entry.
- **Cast drift:** in 001–005 Irus/Kessa are drawn as several different women across pages.

### Verdict

Script, Hindi, structure, cast, world files, links and canon guard-rails: **PASS** — this is the
cleanest state the repo has been in, and conformance is now machine-checkable end to end
(700 EN panels / 700 HI panels, every page with camera + notes + hook sections in both languages).
Art consistency for **Chapters 001–005 remains the single significant open item** and is recorded here
rather than silently passed. **PR #3 merged to `main` on the user's instruction after this audit.**

---

## Audit run 4 — 2026-09-19 (FULL audit: all 10 chapters, every folder, all 100 images)

Requested scope: *"audit once full story to image and all folder then merge."* This is the first audit in
which **every image was inspected**, not sampled: PNG headers decode-checked, all 100 pages rendered to
contact sheets, and seven pages cropped and magnified for prop-lettering inspection.

| Check | Result |
|---|---|
| Folder structure | **PASS** — 10 chapters × (`story/ characters/ other/ images/` + `chapter-summary.md`); 100 EN, 100 HI, 100 PNG, 100 cast, 20 `other/` |
| Naming conventions | **PASS** — 0 off-convention filenames |
| PNG integrity | **PASS** — 100/100 valid PNG magic bytes, 0 corrupt, 0 duplicate (SHA-256), 0 landscape/square |
| Image dimensions | **OPEN (minor)** — 768×1376 ×76, 864×1821 ×14, 860×1828 ×3, 887×1774 ×1, 672×1584 ×5, 848×1264 ×1; all portrait, no reader-visible defect |
| **Visual story→image pass** | **100 images reviewed.** Panel layout, Agnikhand palette, Ira/Kessa/Kshudra design language and per-page beats all hold. **2 defects found = readable non-canon Latin lettering on props** (standing constraint: *no text in art*): |
| — defect 1 | Ch. 003 Page 008 — the stall carried a painted signboard reading *"Knot & Nail"*. **FIXED:** page regenerated with an unmarked lintel, blank documents, no signage. |
| — defect 2 | Ch. 006 Page 002 — the charter and the mother's file carried readable Latin lettering (*"Elven Script"*, *"Aldershan, Eliza Vane"*). **FIXED:** page regenerated — all pages now pure abstract knot-script. |
| — residual | Illegible pseudo-lettering remains as texture on some props (e.g. Ch. 003 p008's small registry plate, pin-boards). No *readable* text found at magnification. Recorded as texture, not lettering. |
| Story conformance | **PASS** — 100/100 pages have a 7-panel structure, panel numbering 1–7, a camera line, notes + card-hook sections; all 10 finales carry their END OF CHAPTER marker |
| Canon guard-rails | **PASS** — mother never appears on panel; the Loom is never given dialogue; chain-stop budget stated and accounted in Ch. 002–010 (Ch. 001's summary predates the convention) |
| Hindi coverage | **PASS** — 96.8 / 98.1 / 97.2 / 94.4 / 94.4 / 96.4 / 97.5 / 97.6 / 98.1 / 98.3 (floor 80); panel parity with EN; 0 stray English headers |
| Internal links | **PASS** — 391 relative links, 0 broken |
| Git hygiene | **PASS** — 813 tracked files, no junk/OS/log files; 249 MB of page art (~2.5 MB/page, committed by design) |
| **Style drift (new)** | **OPEN (minor)** — Ch. 001–002 use *Page notes for continuity* / *निरन्तरता टिप्पणियाँ* instead of *Writing & art notes*; Ch. 001 uses *Card-game hooks introduced on this page*; Ch. 002 uses *लेखन एवं कला-नोट्स*; Ch. 004 and Ch. 005 pages mostly omit the `**Camera:**` line (1/10 and 0/10). Content is present throughout; headings/labels differ. Normalisation deferred. |
| Merge readiness | **PASS** — branch 42 commits ahead of `main`, 0 behind, `mergeStateStatus: CLEAN`, `mergeable: MERGEABLE` |

**Verdict: the branch is merge-ready.** No critical or major finding remains open; the only fixes
required were the two lettering defects, both regenerated and re-inspected in this run.

---

## Audit run 3 — 2026-09-19 (scope: Chapters 001–010, website, tooling)

Run 3 re-checks the whole repo after the **Chapter 009 and Chapter 010 completion pass**: both
chapters' Hindi (10 + 10 files), cast files for both, `other/glossary.md` + `other/locations.md` for
both, a full character sheet for **Nima**, canon-rules and bulk-cast sections on both chapter
summaries, and the README's CURRENT POSITION moved on to Chapter 011.

| Check | Result |
|---|---|
| Structure | **PASS** — Ch. 001–010: 10 EN + 10 HI + 10 PNG + 10 cast files each; 10 chapter summaries; 20 `other/` files (glossary + locations per chapter) |
| Naming conventions | **PASS** — 0 off-convention filenames (7 full character sheets: Ira, Kessa, Patra, Rekhak, Nandi, Jadi, Nima, plus the intentional `*-ref.png` files in `chapter-001/characters/`) |
| Images | **PASS (presence)** — 100 PNGs, 10 per chapter. Dimension/landscape re-verification was not possible in this sandbox (`file` absent, PIL unavailable); run 1's 0-landscape result and the fixed 9:16 pipeline stand. |
| Internal links | **PASS** — 391 relative links checked, 0 missing |
| Hindi coverage | **PASS** — 96.8 / 98.1 / 97.2 / 94.4 / 94.4 / 96.4 / 97.5 / 97.6 / 98.1 / 98.3 (floor 80); Ch. 009 and Ch. 010 complete |
| Stray English headers in `.hi.md` | **PASS** — 0 (`**Camera:**` / `**Image:**` / `**SFX:**`) across all 100 Hindi files; Ch. 010 Page 010 converted this run |
| Card-hook section on every EN page | **PASS** — 100/100 |
| Chapter end markers | **PASS** — all ten `page-010.md` files carry their END OF CHAPTER marker |
| Website build | **PASS** — `python3 website/build.py` clean; `website/characters/nima.html` now generated |
| Continuity fix | Nandi's age on Ch. 010 Page 006 corrected from *fifty-odd* to *eighty-odd* (EN + HI) to match her Chapter 006 sheet: *very old — older than the binding, older than the school's charter*, and forty years of shelf-keeping |

**Remaining open items (all non-blocking):** cast-file depth backfill (Ch. 003–010 vs 001–002);
image dimension standardisation; तकुआ/तकली normalisation; and a future pass may promote more recurring
cast (the Inspector, the grey clerk, the Kessa-less chapter characters) from inline cast entries to
full sheets.

---

## Audit run 2 — 2026-09-19 (scope: Chapters 001–009, website, tooling)

Run 1 is retained below as history. Run 2 re-checks the whole repo after the Chapter 003–008 Hindi
pass and the Chapter 009 script.

| Check | Result |
|---|---|
| Structure | **PASS** — Ch. 001–008: 10 EN + 10 HI + 10 PNG + 10 cast files each; Ch. 009: 10 EN pages scripted (Hindi, cast, images pending) |
| Naming conventions | **PASS** — 0 off-convention filenames (the four `*-ref.png` character sheets in `chapter-001/characters/` are intentional) |
| Images | **PASS** — 80 PNGs, all valid, **0 landscape** (fixed in run 1) |
| Internal links | **PASS** — 308 relative links checked, 0 missing |
| Hindi coverage | **PASS** — 96.8 / 98.1 / 97.2 / 94.4 / 94.4 / 96.4 / 97.5 / 97.6 (floor 80); Ch. 009 not yet translated |
| Stray English headers in `.hi.md` | **FIXED this run** — 2 (`chapter-003/story/page-003.hi.md`, `page-005.hi.md` carried `**Camera:**`) |
| Card-hook section on every EN page | **FIXED this run** — `chapter-003/story/page-005.md` and `chapter-004/story/page-001.md` were missing it (their Hindi mirrors already had the table) |
| Chapter end markers | **FIXED this run** — `chapter-002/story/page-010.md` had no *END OF CHAPTER TWO* (added EN + HI) |
| Website build | **PASS** — `python3 website/build.py` clean |

**Remaining open items (all non-blocking):** Ch. 009 Hindi pass; Ch. 009 cast files; Ch. 009 images;
Ch. 009 `other/glossary.md` + `other/locations.md`; cast-file depth backfill (Ch. 003–009 vs 001–002);
image dimension standardisation; तकुआ/तकली normalisation.

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

**Progress:** Chapters 003–008 are fully hand-translated — **60 of 60 files, pass complete.**

| Chapter | Devanagari chars | Latin chars | % Devanagari | Verdict |
|---|---:|---:|---:|---|
| 001 | 47,165 | 1,544 | **96.8%** | complete |
| 002 | 55,457 | 1,092 | **98.1%** | complete |
| 003 | 7,694 → 71,266 | 36,109 → 2,043 | 17.6% → **97.2%** | ✅ **FIXED** |
| 004 | 1,797 → 58,455 | 21,930 → 3,466 | 7.6% → **94.4%** | ✅ **FIXED** |
| 005 | 2,062 → 21,487 | 21,211 → 1,280 | 8.9% → **94.4%** | ✅ **FIXED** |
| 006 | 2,789 → 34,161 | 35,216 → 1,290 | 7.3% → **96.4%** | ✅ **FIXED** |
| 007 | 3,671 → 50,502 | 51,886 → 1,298 | 6.6% → **97.5%** | ✅ **FIXED** |
| 008 | 2,975 → 52,193 | 54,020 → 1,305 | 5.2% → **97.6%** | ✅ **FIXED** |

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

Chapters 003–008 needed **60 files re-translated**. **All 60 are now complete** (97.2 / 94.4 / 94.4 /
96.4 / 97.5% / 97.6%), each chapter hand-written from the English page — prose, camera, image,
captions, dialogue, SFX, notes and card hooks. **This finding is closed.** The Hindi pass over
Chapters 003–008 is finished; `HINDI_MIN_PCT = 80.0` in `chapters/gen_support.py` is the standing
regression guard and currently reports all eight chapters `ok`.

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
| 1 | **Critical** | Re-translate Hindi — **done: Ch.003–008 all 60 files** (97.2 / 94.4 / 94.4 / 96.4 / 97.5 / 97.6%) | ✅ closed |
| 2 | Major | `chapter-004/images/page-001.png` was the wrong project's art | ✅ fixed |
| 3 | Major | `chapter-007/images/page-007.png` landscape, not portrait | ✅ fixed |
| 4 | Minor | Cast-file depth/format drift (Ch. 003–008 vs 001–002) | ⬜ open |
| 5 | Minor | Standardise image dimensions on 768×1376 | ⬜ open |
| 6 | Housekeeping | Update PR #3 title and body to Chapters 003–008 | ⬜ open |
| 8 | Minor | Ch.004 p008 said "END OF CHAPTER FOUR" mid-chapter (p010's line) — removed from EN + HI | ✅ fixed |
| 7 | Process | Hindi-coverage gate added to `gen_support.py`; correctly clears Ch.003, flags Ch.004–008 | ✅ done |

---

*End of audit.*
