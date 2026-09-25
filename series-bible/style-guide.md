# Art Direction & Style Guide

**Format:** Webtoon, vertical scroll, full colour
**Target canvas:** tall vertical strip, ~800 × 2600 px equivalent, 6–9 stacked panels
**Reference feel:** *Solo Leveling* / *Omniscient Reader's Viewpoint* — cinematic, glowing, readable on a phone

---

## Global look

- **Full colour, cinematic lighting.** Every panel needs a clear light source.
- **Strong rim-light** on characters against dark backgrounds.
- **Thread is always visible when used** — glowing filaments, physically drawn, never abstract sparkles.
- **Debt-marks are always visible when owed** — thin dark lines on skin. If a character used power,
  the marks are in the panel. No exceptions.
- **Ash in Agnikhand.** Constant. In the air, on shoulders, in hair. It is the Sector's signature.
- **Panel shape:** irregular, angled, overlapping. Never a uniform grid.

## Palette by Sector

| Sector | Palette |
|---|---|
| Agnikhand | Black basalt, ash-grey, ember orange, bruised purple sky |
| Jalkhand | Sunken teal, drowned gold, bioluminescent cyan |
| Vayukhand | Cloud-white, sunrise rose, pale cyan |
| Dharakhand | Loam brown, moss green, warm stone |
| Chhayakhand | Charcoal, smoke violet, single violet rim-light |
| Raktakhand | Rust red, bone white, dry ochre |
| Tarakhand | Night indigo, cold white, faint gold |
| Yantrakhand | Brushed steel, warning amber *(reserved)* |
| Shunyakhand | Pure negative space *(reserved)* |

## Character design rules

- **Manavkin must look inconsistent** — mismatched eyes, patchy scales, one odd feature. That is the
  point. Never draw a Manavkin as a clean single-race design.
- **Manav are drawn plain on purpose**, so every other Kind reads instantly.
- **Asura are beautiful and wrong.** Horns are scar tissue. Asymmetry is the tell.
- **Deva are too symmetrical.** The reader should feel unease before understanding it.
- **Silhouette test:** every named character must be recognisable from a solid black silhouette.

## Lettering

- **Narration boxes:** clean sans, dark box, light text
- **Dialogue:** rounded sans, white balloon, black text
- **Thought:** cloud-edge balloon, italic
- **SFX:** hand-lettered look, integrated into the panel art
- **Hindi:** Devanagari in the same balloon styles, kept in `page-XXX.hi.md`, not rendered into the
  image in the English release

---

## Reusable image-prompt block

Paste this into every image generation call, then append the page-specific panel list.

```
Full-colour webtoon manhwa art, vertical scrolling comic strip, cinematic lighting,
painterly digital rendering in the style of modern Korean webtoons, dramatic rim light,
rich saturated colour with deep shadow contrast, irregular overlapping panel borders,
detailed environments, expressive character faces, high detail, clean lineart under paint.
NO text, NO speech bubbles, NO lettering, NO watermark.
```

## Panel budget per page

| Page type | Panels |
|---|---|
| Standard | 6–7 |
| Action-heavy | 8–9 (smaller, faster) |
| Reveal / hook | 4–5 (one large panel dominates) |

**Page 1 of any chapter always ends on a hook panel.** No exceptions.

## Canvas

**Page art is always portrait, taller than it is wide** — the webtoon scrolls vertically, and a
landscape page cannot be read in it. House target 768 × 1376 (ratio ≈ 1.8); ratios up to ~2.5 are
fine. A page that comes back landscape is regenerated, never rotated or cropped.

**"Portrait" means `height > width` strictly, and the check is `h <= w` → regenerate.** Run 11 found
a page at **1024 × 1024** that had passed every previous run's check, because that check tested for
*landscape* (`w > h`) and a square is neither. A square page fails the same way a landscape one
does — it does not scroll. Check the ratio, not the shape's name.

*Six tiers is acceptable when two beats share a frame* (run 11, Ch. 002 p009: beats 2 and 3 read as
one wide panel). **Seven beats in six tiers passes; seven beats in six tiers with one beat missing
fails.**

Model sheets are exempt (`05-character-art-spec.md`): there the eight panels decide the shape, so a
sheet may be wide (Ira 1376 × 768) or tall (Patra 704 × 1484).

## Page-art QA gate — before a page is called done

Every page passes these five, checked **against that page's own script**, at full resolution:

1. **Shape** — portrait (h > w). Landscape = regenerate.
2. **Panel count** — within ±2 of the script's `## PANEL n` list, and the hook panel is present.
3. **Beats** — walk the script's panel list in order. Each panel's stated camera subject must be the
   thing the drawing is actually of. A beautiful panel of the wrong subject is a failed page.
4. **Props and world** — nothing from the §3.1 blocklist in `05-character-art-spec.md` (electric
   light, mugs, plastic, watches, modern furniture, printed signage…). Every slate, ledger, banner,
   form and seal is **blank or knot-script**.
5. **Canon markers** — debt-marks in-panel whenever power is spent, thread drawn as physical filament
   (never abstract sparkle or aura), Agnikhand palette (basalt / ash / ember / bruised purple), and
   the character sheets followed for face, build, costume state and mends.

Record the verdict with the page. **"Regenerated" is a claim that needs a panel-list check, not a
feeling** — runs 5, 7 and 9 each reported pages complete that this gate fails on inspection.

### Who may call a page verified — READ THIS BEFORE SIGNING ANYTHING OFF

Checks 1, 2 and part of 4 are mechanical and can be run by a script: `python3 tools/art_screen.py`
does shape, weight, dead bands and palette, and prints panel count as advisory (it is measured to
undercount this art style — see its header).

**Checks 3 (*beats*) and 5 (*canon markers*) require a reader who can actually see the image.** No
exceptions, and no substitutes:

- **A dimension check is not a content check.** Knowing a page is 768 × 1376 tells you nothing about
  what is drawn on it. Run 11 installed three pages at 768 × 1376 and called them verified; the
  agent had no vision, and every content claim it made was withdrawn in run 12.
- **If you cannot see the image, say so.** Render candidates, measure them, rank them, and mark every
  output as **unread**. Do not write "7 beats in order, hook last" about a file you have not opened.
- **Name the reader in the record.** A verdict in `AUDIT.md` must say who looked at it — a person, or
  a model with vision in that session. "Verified" with no name behind it is the failure mode §7,
  §R11.7 and §R12.2 all exist to document.
- **An off-palette screen is not a content verdict.** `art_screen.py --rank` ranks candidates for
  human review; it cannot distinguish an off-world forest from a canon jade bead.
