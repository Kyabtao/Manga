# Card Game — Design Notes (carried forward from Chapter 1)

**Goal:** by the time the manga passes 500 chapters there is a cast large enough to populate a full
TCG. These notes exist so the story never paints the game into a corner.

> **Rule for the writers' room:** every chapter should introduce at least one thing that could later
> become a card — a character, a thread, a place, or a debt. Track it in the chapter's `other/` folder.

---

## Why the card game is free

The world's physics *is* a card game:

| Story concept | Card mechanic |
|---|---|
| Thread | The card itself |
| Kind | Card race / tribe |
| Sector | Card faction / element |
| Debt | Resource cost |
| Fraying | Risk mechanic + shared discard |
| Mending | Counter / cancellation archetype |

No new systems need inventing. Every card is a thing that already happened in the story.

## Core loop

- Each player is a **Thread-bearer** with a **Debt track** (0 → Terminal).
- Playing a card adds **debt-marks**. Marks clear over turns with rest.
- Push past **Terminal** and you gain enormous power this turn — but your excess cards go to the
  shared **Fray pile**, where they can be recruited by your opponent as **Asura**.
- **Mend** cards cancel debt instead of paying it. The Ira archetype. Low ceiling, absurd floor.

## Card families available from day one

9 Kinds × 9 Sectors = **81 base families**, each with its own art direction. Plus:

- **Debt-carrier** cards (tragic, cheap, disposable) — the moral texture of the game
- **Bonded pairs** (Pashu + animal) — two-card combos
- **Relic** cards (objects, like Ira's needles)
- **Sector law** cards (global effects — "in Agnikhand, all costs double")

## Reserved for later (do not design yet)

- **Yantra** — chrome faction, reserved for ~Chapter 180 reveal
- **Shunyakhand** — anti-card / banish mechanic, final-act set
- **Deva** — deliberately over-costed until the story proves they are not gods, then rebalanced
  *in-fiction*. The set release should track the plot reveal.

## Production pipeline the manga must keep clean

For 500+ chapters to convert into cards, every chapter's `characters/` file must record, per new
character:

```
Name / Kind / Sector / Thread colour / Debt tendency / Signature ability / One-line hook
```

That single line becomes the card's rules text later. **Do not skip it**, even for a one-panel
extra. The bulk cast *is* the product.
