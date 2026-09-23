# THREADBORN — FULL REPO AUDIT

**Date:** 2026-09-19 · **Branch:** `arena/01a0b63a-manga` · **Scope:** chapters 001–008, website, tooling
**Auditor:** Arena agent · **Method:** automated sweep + manual image inspection

---

## 0. Headline

| | |
|---|---|
| **Critical findings** | **0** (run 10) — Hindi complete for Ch. 001–010 (letters-only floor 80%: min 93.3% / median 97.4%) |
| **Major findings** | **1 open** (run 10 + 8b) — the run-5 **style split** is now **closed for Ch. 001** (pages 001–010 all rebuilt and verified, §8b); what remains is **Ch. 002–005**, and the 91 pages that have not yet had the §3 sample treatment. **~~Ch. 005 p004, Ch. 003 p010, Ch. 006 p010~~ → fixed and verified in the same session (§8); landscape page art now zero.** |
| **Minor findings** | **3 open** (run 10) — cast-file card-line drift (78/100 files), image dimension variation (20 sizes), the Hindi-floor tool missing from the repo. Nima's sheet closed and the 8-panel gap closed in runs 7–9. |
| **Fixed in run 5** | 133 missing `Camera:`/`कैमरा:` labels (Ch. 004–005) · 19 pages given notes sections (EN+HI) · Ch. 001–002 headings normalised · Ch. 004 p008 page-type line · 28 obsolete `.gitkeep` files · README's false "PR #3 merged" claim |
| **Structural integrity** | **PASS** — 100/100 EN scripts, 100/100 HI scripts, 100/100 images, 100/100 cast files, 10/10 summaries, 20/20 `other/` files, 0 junk |
| **Continuity integrity** | **PASS** — mother never on panel, Loom never speaks, chain-stop budget accounted for in every chapter that states one |
| **Merge state** | **PR #3 merged into `main` this run** (user instruction, after audit) |

## Audit run 10 — 2026-09-21 (full sweep + page-art verification by sample)

Scope: whole repo after run 9 (Nima closed, Ch. 001 pages 001–005 rebuilt). Method: automated sweep of
every folder, every image and every script **plus a visual read of nine pages at full resolution**,
each checked against its own panel list.

### 0. Result in one line

Structure, Hindi, continuity guard-rails and the site: **clean, with numbers**. Page art: **three pages
fail their own scripts**, and the sample rate says the "Ch. 006–010 are one consistent production"
verdict (run 5) cannot be relied on.

| | |
|---|---|
| **Critical** | **0** |
| **Major (open)** | **3 page-art defects** — Ch. 003 p010 (wrong shape + invented content), Ch. 006 p010 (wrong shape, partial beats), Ch. 005 p004 (wrong beats entirely) |
| **Minor (open)** | cast-file card-line drift (78/100 files), image dimension variation (20 distinct sizes), Nandi's kit brush |
| **Fixed this run** | *Canvas* rule + **page-art QA gate** written into `style-guide.md`; sheet-shape rule in `05-character-art-spec.md` corrected to match reality; regeneration prompts written for all three failing pages |
| **Verified** | 100/100 EN · 100/100 HI · 100/100 pages · 100/100 cast · 10/10 summaries · 20/20 `other/` · 9 sheets + 1 alt · 0 junk · 0 duplicate images · 16,066 site links / 0 broken · build reproducible (rebuild = no diff) |

### 1. Structural sweep — PASS

| Check | Result |
|---|---|
| Chapters | 10, each with `story/ characters/ other/ images/` + `chapter-summary.md` |
| Files per chapter | EN 10 · HI 10 · images 10 · cast 10 · other 2 — **no gaps, no extras, in every chapter** |
| Naming | 0 off-convention filenames; 0 obsolete `.gitkeep`; 0 junk (`.DS_Store`, `*.orig`, `tmp-*`) |
| Sheets in the right chapter | 9 sheets + 1 alt, each in the chapter of first appearance |
| Repo weight | 110 images, 1.66–2.73 MB each (nothing over 3 MB); `chapters/` ≈ 252 MB |

### 2. Image sweep

| Check | Result |
|---|---|
| PNG validity | 110/110 valid by magic number + IHDR decode |
| Duplicates (SHA-256) | **0** |
| Landscape **page** art | **2** — `ch003/p010` and `ch006/p010`, both 1408 × 768. A vertical webtoon cannot read these; the QA gate now fails them on shape alone. |
| Blank / unfinished bands | Detected by a flat-row scan (8 × 220 profile per page, uniform-run detector): **0 pages** with a dead band over 8% of height. The suspected grey void on Ch. 001 p001 is the page's own margin, not missing art. |
| Dimensions | **20 distinct sizes.** Largest group 768 × 1376 (55 files). Ch. 001 pages 006–010 are the extremes (352 × 2928, ratio 8.3) — they are the *old* art still queued for rebuild. Standardisation stays open, and the rebuilds shrink the list from the outlier end. |
| Palette screen | A cool-hue histogram screen flagged 12 pages at 11–25% cool pixels — all canon night / night-terrace scenes (bruised purple sky). **Screened, not a finding**; impression-based palette audits are not reliable here. |

### 3. Visual sample — nine pages read at full resolution against their own scripts

| Page | Verdict | Evidence |
|---|---|---|
| Ch. 001 p001 (rebuilt) | ✅ | Loom over the basin, the queue, the alley mend, Ira's face, the taut boy, the palm, the stitch close. **The taut-boy panel was checked against the script and passes**: Ch. 001 p001 Panel 5 says *"arms thrown wide, a bright taut orange thread bursting from his palm… crowd recoils. Embers."* It reads oddly out of context and is on-script. |
| Ch. 001 p002 (rebuilt) | ✅ | Unspooling Court → processional → stair → Under-Market → Kessa with loupe → macro hand under the loupe (stitch visible) → the two at the counter. Palette and world hold; slate blank. |
| Ch. 001 p005 (rebuilt) | ✅ | Ash-free terraces, the clerks' room, the broker, the blank three-line form, the arm-macro with the crimson-sealed page. **Run 9's logged defect confirmed and it is mild**: the blond broker figure appears twice in the lower panels — a duplication artifact, not a canon conflict. |
| Ch. 006 p002, Ch. 008 p001, Ch. 009 p001, Ch. 010 p001 | ✅ | Knotted script page and portrait; first-bell arrival; the served paper; the basement annex and the tally — each consistent with its script. |
| **Ch. 005 p004** | ❌ **Wrong beats** | Script: *"The First Pull"* — the Knot & Nail counter in the afternoon, **the first mend**: Rekhak gone, the torn dock-worker's mark, macro of the braided thread, the sleeve rolled, no itch, the market queue returns, Ira's palm in equilibrium, the lockbox hook. Art: a **lava basalt cavern**, a **glowing gemstone**, a **gem appraiser**, glowing ore passed hand to hand, an ember burst. None of it is on the page, in the chapter, or in the series' power vocabulary. |
| **Ch. 003 p010** | ❌ **Wrong shape + wrong content** | Script: 7 panels — the Knot & Nail after, Kessa's verdict, the box between them, the dock at dusk, the roof at night, the palm, the basin sleeping. Art: landscape 4-column grid, ~12 panels, an **appraiser's workshop with a magic crystal in a chest**, a **stair with a luminous ritual circle**, a **golden winged-eye emblem** — the chapter finale's emotional beats are absent. |
| **Ch. 006 p010** | ❌ **Wrong shape + partial beats** | Script: 7 panels (morning, the mend, the chain, the Council Stair, the letter, Ira finds the letter, the lockbox hook). Art: landscape 4-column grid; the sign, the mender and the letter are present, but the panels are arranged horizontally, the **chain panel is missing**, and the world reads as a warm bazaar rather than the chapter's ash-and-paper Office. |

**Defect rate: 3 of 9 sampled pages.** Two of the three sit in chapters earlier runs reported verified,
which is the finding of this audit: **page claims in this log have been asserted, not panel-checked.**

### 4. Hindi — PASS (metric stated, because the previous number is not reproducible)

| Metric | Result |
|---|---|
| Devanagari share of all non-space characters | min 77.5% (Ch. 001 p001) · median 86.0% |
| **Devanagari share of letters only** (the historical 80%-floor metric) | **min 93.3% · median 97.4% · max 98.5% — nothing below the floor** |

The 77.5% figure counts markdown syntax and punctuation; the floor still passes comfortably. But the
tool that held this gate (`gen_support.py`, credited in run 5) **does not exist in the repo**, so the
gate has been unenforceable since run 5. Recommend re-adding it as a three-line check, or dropping the
claim.

### 5. Continuity guard-rails — PASS

- **Mother never on panel:** every match is either a standing rule line (*"Mother never on panel"*) or a
  reference to *her file* — no panel description puts her in frame.
- **Loom never speaks:** zero Loom dialogue lines across all 100 scripts.
- **Chain-stop budget:** stated once per chapter where the arc requires it; no duplicate spend.

### 6. Site — PASS

- 16,066 local links over 343 pages, **0 broken**.
- `python3 website/build.py` on the committed tree produces **no diff** — the committed HTML matches the
  markdown canon exactly (reproducible build).
- 9 art pages, 8 numbered chips each, plus Ira's 8 lettered alt chips; cast-index thumbnails and cast-file
  `Art:` links all resolve to art pages.

### 7. Corrected in the record this run

| Claim | Status |
|---|---|
| Run 5: *"Ch. 006–010 read as one consistent production"* | **Not supported.** Ch. 006 p010 fails on shape and beats; the claim needs the nine-page sample re-run over the whole 100 before it can be restored. |
| Run 5/7: *"Ch. 005 verified"* / fix lists naming Ch. 005 and Ch. 007 pages | **Ch. 005 p004 is off-beat**, which no run has recorded. Named fixes on other pages of those chapters may well hold; the *chapter-level* clean bill does not. |
| Run 9: Ch. 001 p005 *"broker drawn twice"* | **Confirmed** (see sample table). |
| Run 9: Ch. 001 001–005 rebuilt to house style | **Holds for the five pages** (p001–p004 pass; p005 passes with the logged duplication). |
| Run 9: Nima's sheet closed | **Holds.** Read at full resolution: 8 distinct panels, numeral order 1–8, short braid pinned flat, the school's strand under the skin, kit = slate · stylus · counting chain · brass instrument · **clay oil lamp** · sleeve band · blank paper · cord — no timepiece, no mug, no lamp shade. |

### 8. The three failing pages — REGENERATED AND VERIFIED (same session)

Each page was generated from its own script's panel list, portrait canvas, character sheets attached
as references, no lettering anywhere, §3.1 blocklist in force. **All three now pass the QA gate.**

*Generator note, logged because it nearly caused a silent error:* the three images came back with
their content attached to **swapped filenames** — the render of Ch. 003's finale was written to
`ch005-p004.png` and vice versa. Nothing about the files identified which was which, so the mapping
was decided **by reading each image against its page's panel list**, and only then installed:

| File installed | Content verified | QA gate |
|---|---|---|
| `ch003/images/page-010.png` | stall after the confession (empty cup, open lockbox, Ira at the threshold) · Kessa tying a new knot and pushing the closed box across · the box between Kessa's scarred hands and Ira's gloves · Bhan at the dock, sleeve rolled, mend + charcoal mark + the looped second thread · Ira on the roof under the turning Loom, palm open · extreme close of the stitched palm · the basin asleep at night, wide hook | **Pass** — 7 beats in order, hook last, 768 × 1376 portrait, palette and characters on-model, no text. *Note: panel 4's second thread-loop is drawn subtly rather than emphasised.* |
| `ch005/images/page-004.png` | afternoon counter with the left cup, Ira's palm open · **the first mend** on the dock worker's forearm at the counter · macro of the braided thread through the needle into the mark · the worker rolling his sleeve, puzzled, not pained · the market alley **queue forming for mending** · Ira's open palm in lamplight, clean, thread held · macro hook of the lockbox under Kessa's hand | **Pass** — matches *"The First Pull"* panel for panel; the cave, the glowing gem and the gem appraiser are gone. |
| `ch006/images/page-010.png` | the stall opening in falling ash · the routine mend · **Rekhak walking his rounds with the counting chain through his fingers** (the missing panel, now present) · the letter at the foot of the Council Stair, both waxes touching · the letter unopened with grey and crimson wax · Ira stooping to pick it up at dawn, the strand reaching toward the crimson wax · macro hook — the unopened letter beside the closed lockbox under Kessa's hand | **Pass** — 7 beats, hook last, portrait. Seals carry **knot-script emblems, not letters** (allowed by the standing rule). |

**Result: landscape page art in the repo is now zero**, and the three ch./p. entries that failed the
sample are closed:

- **Ch. 005 p004** — was *wrong beats entirely*; now the first-mend page its script describes.
- **Ch. 003 p010** — was *landscape + invented content*; now the quiet chapter finale, portrait.
- **Ch. 006 p010** — was *landscape, chain panel missing*; now portrait with the chain panel present.

All three are 768 × 1376 — i.e. they shrink the dimension-outlier list from the top as well as the
wrong-art list.

- **`chapters/chapter-005/images/page-004.png`** — 7 panels, portrait: the Knot & Nail counter in the
  afternoon with Rekhak's cup gone; **the first mend** (torn dock-worker's mark, needle, the mark
  *listening*); macro of the ash-grey shadowless braided thread moving through the seam; the dock worker
  rolling his sleeve, the seam invisible, no itch; the market news spreading and the filing queue
  returning; Ira's open palm with the thread contained, in equilibrium; hook — Kessa's hand on the
  lockbox lid, seven objects inside. Attach `ira-sutar-ref.png`, `kessa-ref.png`, `bhan-ref.png`.
- **`chapters/chapter-003/images/page-010.png`** — 7 panels, portrait, **chapter finale**: the stall
  after, Kessa's verdict, the lockbox between them, the dock at dusk, the roof at night under the Loom,
  the palm close, the basin sleeping as the final wide. Attach `ira-sutar-ref.png`, `kessa-ref.png`.
- **`chapters/chapter-006/images/page-010.png`** — 7 panels, portrait: morning in the basement annex,
  the mend, the **compliance chain close-up**, the Council Stair, the letter close-up, Ira finding the
  letter, hook — macro of the lockbox. Attach `ira-sutar-ref.png`, `kessa-ref.png`, `nandi-ref.png`.

### 8b. Ch. 001 p006–010 rebuilt and verified (same session)

The five closing pages of the chapter were generated from their own scripts' panel lists (portrait
canvas, no lettering, §3.1 blocklist in force, character sheets attached) and installed over the old
extreme-ratio art. Before → after: 368×2832, 656×1632, 352×2928, 544×1936, 464×2320 → **all five
768×1376**. Landscape page art remains zero.

| Page | Content verified against its own panel list | QA gate |
|---|---|---|
| `chapter-001/images/page-006.png` | the clerk's room, blank form face-down under Ira's glove · three gloved fingers counting · Patra leaning, wall-shadow still · Patra held sharp in the lamplight, edges flaring · the week's arithmetic · Rekhak one step inside, ash off his coat · hook — Patra's warm alarm-smile with the shadow smiling a half-beat late | **Pass** — 7 panels, hook last, portrait, no text. |
| `chapter-001/images/page-007.png` | the stair down to the lit terraces · the night pawnbroker's stall, Kessa at her tally-cord · the loupe flipped up · the deal sealed, cat eyes flicking to the lockbox · macro of the sixty-knot hour-cord · her hands stopped flat · hook — two hands over the counter, the last knot untightened | **Pass** — 7 panels, the hour-cord drawn as knotted rope, hook last. |
| `chapter-001/images/page-008.png` | the stall before dawn, the cord tying two wrists · Rekhak kneeling, glove slid off · his closed eyes, brow-seam reopened, the chain running fast · the packed fold under the stitch and its sealing rows · the sleeping whorl knot mid-fold · the sky's great lattice going dim, threaded people looking up — *"the absence is the sound"* · hook — Ira staring at her own unchanged palm | **Pass** — 7 panels incl. hook; the vision renders the fold as physical filament, not aura. *Note: panel 3 crops Rekhak above the collar, so the high collar hides his hair; face scar and chain present.* |
| `chapter-001/images/page-009.png` | dawn at the stall — **Ira seated opposite Kessa**, the knotted rope wrist to wrist · the finished form in knot-script, middle line darker · Ira tight on the middle line, Kessa still behind · the form set at the table's middle · the week's arithmetic re-added · the cut rope across Kessa's palm · hook — **the extra knot** (uncanny whorl) on the rope, Ira's glove reaching, Patra's shadow already through the door | **Pass** (third generation; rejects below) — round human ears, rope (never a chain), knot-script only, no lettering, hook last. |
| `chapter-001/images/page-010.png` | the rooftop under the turning Loom · ash on the closed hand · the mismatched eyes above the hiding fist, one flake staying · Kessa lifting the thrice-wrapped bundle from the lockbox · the swatch that **catches no light and casts no shadow** while everything else casts one · her face turned up past it toward the tenement roofs · hook — lamp guttering, the end-knot whorl in extreme close | **Pass** — 7 panels, hook last, quiet finale. *Note: the three wrappings read as one layer in panel 4.* |

**Two rejects in this batch, both on page 009, both caught at full resolution before install:**

1. **v1** returned with **readable English lettering** — "REGISTRATION FORM" typeset on the form — and
   **two copies of Ira in one panel**. Both are instant fails (documents are blank or knot-script; a
   character is never drawn twice in one panel). Regenerated.
2. **v2** was lettering-free but drew the hour-cord as a **metal chain** and gave Ira **pointed elfin
   ears**. Regenerated with those constraints promoted into the prompt's absolute rules.
3. **v3** passes.

*File-mapping note:* the run-10 batch came back under **swapped filenames**; this batch did **not** — a
mid-batch suspicion of a swap was disproved by a full-resolution crop of the suspect band plus a
band-brightness check (dark interior ≈ 49 vs pale form ≈ 92–133). Both batches were installed **by
content read against the panel list**, never by filename.

**Result: Ch. 001 is now fully on the current pass, pages 001–010**, all portrait 768 × 1376, each
verified against its own script. The chapter no longer carries the style split.

### 9. Next actions

| # | Priority | Item |
|---|---|---|
| 1 | ~~Major~~ | ~~Regenerate the three pages above~~ — **done and verified (§8).** |
| 2 | **Major** | Finish the style rebuild: ~~Ch. 001 pages 006–010~~ — **done and verified (§8b), so Ch. 001 is fully rebuilt 001–010**; remaining **Ch. 002–005**. |
| 3 | **Major** | Give the remaining 91 pages the §3 sample treatment, nine at a time — the QA gate in `style-guide.md` is the checklist. |
| 4 | Minor | Cast-file card-line drift: 78/100 cast files carry no card-line block. Either backfill for the TCG ledger or retire the convention in the README. |
| 5 | Minor | Re-add the Hindi floor check as a script, or drop the claim from the audit. |
| 6 | Minor | Image dimensions: standardise on 768 × 1376 opportunistically, as pages are regenerated anyway. |

## Audit run 9 — 2026-09-21 (Nima closed; Ch. 001 page art rebuilt)

### Delivered

| # | Item | Result |
|---|---|---|
| 1 | **Nima's model sheet regenerated** (run 8's only open art item). | Four passes to get there. Pass 1: modern props gone, but the face panel was dropped and the ground came back with red splatter. Pass 2: blocked by moderation. Pass 3: clean but the kit held two pocket watches. Pass 4 (targeted panel-7 fix): kit is now slate · stylus · Office counting chain · clay oil lamp · sleeve band · blank paper · coiled rope · featureless brass seal · plain brass weight, **no timepieces and no mug**. Pass 5 (targeted panel-5 fix): the school's strand now reads as a fine braid lying *under* the skin of the forearm, not a cord tied round it. **Sheet passes.** |
| 2 | **Ch. 001 page art rebuilt — pages 001–005.** These were the run-5 style-split pages (right beats, off-style world). | Regenerated one page at a time from the script's own panel list, with the **character sheets attached as references**: 001 (Loom + processional + the stitch reel), 002 (Unspooling Court → Under-Market → loupe macro), 003 (Kessa's two diagrams + the Reckoner's cold stair), 004 (the two empty columns + the painted borrowed lines + the collapsed chain), 005 (the ash-free terraces → the Office of heads-down clerks → the broker's blank three lines). All five now carry Agnikhand's basalt/ash/ember palette and **no readable lettering anywhere** — every slate, ledger, banner, seal and form is blank or knot-script. |
| 3 | **Known defect logged, not hidden.** | Ch. 001 Page 005's final panel draws Patra twice in the same room (the plate, not the panel list, is at fault). It is a duplication artifact, not a canon conflict; the page is still a large improvement on the old off-style art. Logged here for a later touch-up. |

### Still open after run 9

- **Ch. 001 pages 006–010** — the rest of the chapter's old art (broker's room, the sixty hour-knots, the kneeling read, the falsified audit, the roof finale). Prompts are written from each page's own panel list; blocked only by the ten-images-per-turn generation cap.
- **Ch. 002–005 page art** — ~40 pages, same defect class, same method (per-page script beats + character sheets as references).
- Alt sheets exist for Ira only; the convention is ready when another character needs one.

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
| 1 