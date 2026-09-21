# Character Art Spec — the standard model sheet

**Status:** canon. Every named recurring character gets one, and every one looks the same.
**As of 2026-09-21:** all nine sheets carry the full eight panels.
**Applies to:** `chapters/<chapter>/characters/<name>-ref.png` — the file beside the sheet, in the
chapter of that character's **first appearance**, forever (see README *Structure conventions*).

---

## 1. The rule

> **A character is not finished until their model sheet exists.** A `<name>.md` sheet without a
> `<name>-ref.png` beside it is an unfinished character.

The reason is production, not decoration: this series draws the same face across hundreds of pages,
generated page by page. The ref sheet is the **only** thing that keeps a character one person. It is
also the first thing the website shows when a reader clicks a character — *press the art, see the art*
(`website/characters/<name>-art.html`, built automatically from the file).

Set by **Ira Sutar** (`chapter-001/characters/ira-sutar-ref.png`) — front · side · back · face ·
working hands — and kept by every sheet since.

---

## 2. Required panels

**Eight slots, in this order, left-to-right and top-to-bottom.** Extras go **after** slot 8.

| # | Slot | What must be in it |
|---|---|---|
| 1 | **Front** | Full length, whole body in frame, relaxed stance, arms visible. The silhouette test lives here: cover the face — is this person still recognisable? |
| 2 | **Side** | Full length, three-quarter or true profile. Depth, posture, how the clothes hang and move. |
| 3 | **Back** | Full length, from behind. Hair, coat back, belt, bundles — the view the audience gets when the character is walking away. |
| 4 | **Face** | Head and shoulders. Eyes, marks, asymmetry, exact hairline. The panel that fixes the drawing for every later page. |
| 5 | **The detail** | Close-up of the one thing that matters most on this character — a mark, a stitch, a scar, a tell, a prop they are never without. |
| 6 | **Hands** | Both hands. In a story about debt and mending, hands are the argument; never skip this slot. |
| 7 | **Kit** | Their carried objects laid out flat, like a table after they empty their pockets. Every recurring prop is in this panel. |
| 8 | **Action** | The same design in use, under pressure — mid-work, mid-reading, mid-standing-in-a-doorway. Proof the model sheet survives a scene. |
| 9+ | **Anything else** | Optional extras after slot 8: extra costume state, an alternate hand, a second expression, a seasonal/arc variant. Add them; never renumber the eight. |

**Settled layout exceptions** (both predate the standard and are kept deliberately — the panels are
all there, the page just reads differently):

| Sheet | Layout | Why |
|---|---|---|
| `patra-ref.png` | tall, two columns (1 2 / 3 4 / 5 6 / 7 8) | the tall page shape Patra was designed on; keep it |
| `jadi-ref.png` | tall stacked (3 / 2 / 2) | Jadi's sheet was always the tall one; the extra height suits a woman drawn wide and stooped |

**Slot reducers:** if a character genuinely has no kit, slot 7 carries what the *scene* carries
(chairs, ledgers, lamps) — an empty slot is a wasted panel.

---

## 3. Drawing rules (house)

- **No text in art.** No lettering, signage, labels, stamps or readable numbers anywhere in the sheet.
  Documents, signs, seals and slates are **blank or knot-script only**. This is a standing constraint
  across the whole repo (see `AUDIT.md`).
- **No panel captions.** The eight slots are marked with small circled numerals only — never printed
  titles under the panels (*FRONT VIEW*, *KIT*). A sheet that comes back captioned is regenerated.
- **Eight distinct slots.** No slot repeats another and none is dropped: a sheet with two back views
  and no portrait is regenerated, not filed.
- **They are mid-story, not models.** Costume state must match the sheet's own text: mends, stains,
  ash, salt, ink, wear. Agnikhand's ash is on everyone who lives there.
- **No new costume.** The ref sheet illustrates the character sheet; it never invents canon. If a
  panel needs something the `<name>.md` does not describe, fix the sheet first, then the art.
- **Palette:** follow `style-guide.md` for the character's Sector — Agnikhand is black basalt,
  ash-grey, ember orange, bruised purple. Debt-marks are thin dark lines *on skin*, never glowing
  tattoos; thread is drawn as physical filament, never abstract sparkle.
- **Consistency across the eight panels** beats beauty in any single panel. Same face, same build,
  same mends, same props in all eight.
- **Neutral ground.** Plan mid-grey, minimal clutter, no environment art; the page art carries the
  world, the sheet carries the design.
- **Silhouette test** (from `style-guide.md`) applies to every named character: recognisable as a
  solid black shape.

## 3.1 Pre-industrial grounding — the one rule art keeps breaking

Agnikhand is ash, oil light, hand tools, paper and thread. The single most repeated failure in this
repo (Ch. 001–005 page art, and one model sheet) is **modern props drawn into a pre-industrial world**.

**Blocklist — none of these may appear on a model sheet or a page, in any panel:**

electric light, desk or lamps with shades and cords, LED/fluorescent fixtures · metal tumblers, mugs
with handles, vacuum flasks, packaged or branded goods · rubber bands, plastic, zip fasteners, moulded
synthetic buttons, velcro · wristwatches, pocket watches, printed or stamped signage and paper with
readable print · modern office furniture (bent-tube desks, swivel chairs, filing cabinets with rails),
window frames with float glass and aluminium, cranes, water towers, industrial tanks · hoodies,
backpacks, sneakers.

**Replacements:** clay oil lamps with a wick and flame, candles, hand-lanterns; wooden benches, stools,
tables and shelves; crates, barrels, sacks, quires, slate and chalk; iron, brass, stoneware, cloth.

If the render drifts anyway, **regenerate rather than crop**: a modern object in a sheet teaches every
future page the wrong world.

## 4. File rules

- **Name:** `<sheet-name>-ref.png` — exactly the markdown sheet's filename plus `-ref`. `nandi.md` →
  `nandi-ref.png`. Nothing else is auto-detected by the site.
- **Placement:** the chapter folder of **first appearance**. Later chapters link back; they never copy.
- **Shape:** whatever the eight panels need — wide grids (Ira 1376 × 768, Rekhak 1264 × 843) and tall
  stacks (Patra 704 × 1484, Nandi 720 × 1456) are both house-legal. **Page art is the opposite: always
  portrait** (`style-guide.md` → *Canvas*). Stay between 1.2 MB and 3 MB.
- **Committed to git** with the character sheet, in the same commit as the sheet's prose.

## 5. Generation prompt

Start from the reusable block in `style-guide.md`, then append:

```
Vertical character model sheet, painted dark-fantasy webtoon style, neutral mid-grey studio ground,
eight clean bordered panels in reading order: 1 full-length front, 2 full-length side, 3 full-length
back, 4 head-and-shoulders face, 5 close-up of <the detail>, 6 both hands, 7 kit laid out flat,
8 the design in action. Consistent character design across every panel, same face and costume in all
eight, costume state per the character sheet, thin panel borders, small decorative circled panel
numerals. NO text, NO lettering, NO signage, NO stamps, NO watermark, NO speech bubbles.
```
Replace `<the detail>` with the character's slot-5 subject. Feed the closest existing ref sheet as a
**style reference only**, and say so in the prompt — otherwise the new character inherits the old
character's face.

## 6.1 Alt sheets — the second page (optional, for characters who need one)

When a character has states, expressions and staging that the eight slots cannot hold, add
**`<name>-alt.png`** beside the model sheet and list it in the character sheet:

```
**Alt sheet:** [`ira-sutar-alt.png`](ira-sutar-alt.png) — alternate states, expressions, staging
and silhouette (spec §7)
**Alt panels:** default state · ceremony-day state · five expressions · macro hands · satchel
tipped out · crowd staging · waiting-room staging · three silhouettes
```

Alt-sheet slots are **lettered A, B, C…** (never numbered — the eight numbered slots belong to the
model sheet). The house alt pattern, as first drawn for Ira:

| Slot | Panel |
|---|---|
| A | Default state, full length (the one every page uses) |
| B | One variant state, full length (costume state, weather, ceremony, arc variant) |
| C | An expression row — five head studies, one of them an expression not used yet |
| D | Macro of the character's single most important physical detail, at drawing resolution |
| E | Alternative/expanded kit — the bag tipped out |
| F–G | Two staging panels: the character inside their actual world, one crowded and warm, one institutional and cold |
| H | The **silhouette test**, run literally: three solid black shapes — standing, working, walking away |

An alt sheet is discovered automatically: drop the file, add the two lines, rebuild — the art page
grows an **Alt sheet** section with its own lettered chips and click-to-zoom plate.

The site letters the slots **A–H** in reading order. The first alt sheet (`ira-sutar-alt.png`) carries
plain numerals in the art itself; that is harmless — they are on a *different file* from the model
sheet, and the eight numbered slots of `05-character-art-spec.md` only ever mean the ref sheet.

## 6. How it reaches the site

`python3 website/build.py` scans every `chapters/*/characters/*-ref.png` and builds, for each one:

- a **thumbnail card** on `website/characters/index.html`;
- a **gallery page** `website/characters/<name>-art.html` — the full sheet as a click-to-zoom plate,
  the slot list as numbered chips, the character's **Drawing brief**, and (when one exists) the
  **alt sheet** below it with lettered chips;
- and a back-link strip on the character's sheet page.

Crops are generated into `website/characters/art/<name>-<slot>.png` by the build (ImageMagick) so the
gallery is light. Delete them and rebuild any time; they are derived, never edited by hand.

**Adding a character:** write `<name>.md`, drop `<name>-ref.png` beside it, add the
`**Ref sheet:**` line listing the panel order, then re-run the build. Nothing else to wire up.
