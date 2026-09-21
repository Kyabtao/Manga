# Character Art Spec — the standard model sheet

**Status:** canon. Every named recurring character gets one, and every one looks the same.
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

**Slot reducers:** if a character genuinely has no kit, slot 7 carries what the *scene* carries
(chairs, ledgers, lamps) — an empty slot is a wasted panel.

---

## 3. Drawing rules (house)

- **No text in art.** No lettering, signage, labels, stamps or readable numbers anywhere in the sheet.
  Documents, signs, seals and slates are **blank or knot-script only**. This is a standing constraint
  across the whole repo (see `AUDIT.md`).
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

## 4. File rules

- **Name:** `<sheet-name>-ref.png` — exactly the markdown sheet's filename plus `-ref`. `nandi.md` →
  `nandi-ref.png`. Nothing else is auto-detected by the site.
- **Placement:** the chapter folder of **first appearance**. Later chapters link back; they never copy.
- **Shape:** portrait or tall; the house sizes are 768 × 1376 and 848 × 1264. Stay between 1.2 MB and
  3 MB (same band as page art).
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

## 6. How it reaches the site

`python3 website/build.py` scans every `chapters/*/characters/*-ref.png` and builds, for each one:

- a **thumbnail card** on `website/characters/index.html`;
- a **gallery page** `website/characters/<name>-art.html` — the full sheet as a click-to-zoom plate,
  plus a labelled crop of each of the eight slots;
- and a back-link strip on the character's sheet page.

Crops are generated into `website/characters/art/<name>-<slot>.png` by the build (ImageMagick) so the
gallery is light. Delete them and rebuild any time; they are derived, never edited by hand.

**Adding a character:** write `<name>.md`, drop `<name>-ref.png` beside it, add the
`**Ref sheet:**` line listing the panel order, then re-run the build. Nothing else to wire up.
