# THREADBORN — सुत्रजात

A full-colour **webtoon manga**, written chapter by chapter, page by page, with images — designed
from the first page to become a **trading card game** once the cast passes 500 chapters.

> This is a **from-scratch rewrite.** The earlier AI-generated site (analysed in
> [`ringbound-era-analysis.md`](ringbound-era-analysis.md)) was scrapped: its 120 "chapters" were one
> five-scene template with names swapped in. This repo builds the story properly.

**Format:** webtoon, vertical scroll, full colour · **Languages:** English + Hindi (Devanagari)

---

# 📍 CURRENT POSITION — READ THIS FIRST

> **If you are a new chat / new session, start here.** This block is the single source of truth for
> where the project stands and what to do next. **Update it every time you finish a page.**

| Field | Value |
|---|---|
| **Series** | THREADBORN (सुत्रजात) |
| **Branch** | `arena/01a0b2c8-manga` (the only branch we work on — each Arena session gets a fresh one; keep this field current) |
| **Chapter in progress** | **002 — *The Minute That Owes* / *वह मिनट जो ऋणी है*** — Chapter 001 *The Girl With No Thread* is **COMPLETE** (10 pages, close-out in `chapters/chapter-001/chapter-summary.md`) |
| **Pages completed** | Ch. 001: **001**–**010** (complete) · Ch. 002: **001** |
| **NEXT page to build** | **Chapter 002 · Page 002** |
| **Open PR** | [Kyabtao/Manga#2](https://github.com/Kyabtao/Manga/pull/2) (targets `main`; PR #1 is merged) |

### Next-page brief (Chapter 002 · Page 002)
Ban comes back down the stair with the fray-adjacent mark on his forearm **torn again** — same tear,
same hour of work undone, and he is not angry, which is worse. Ira takes the mend at the Knot & Nail
doorstep in daylight: the mend takes **half** the time it should, because the fold in her palm is
*lending through the needle, unasked* — her first power bleed, and it feels like kindness. No debt is
created (nothing was pulled), so no debt-mark appears; the only evidence is the work itself: the mended
seam carries a faint **whorl-grain**, the knot-shape's fingerprint in her stitching (guard: the
knot-shape gets no owner on panel — the whorl is texture, not a reveal). Hook line, Ban rolling his
sleeve down: *"It doesn't itch anymore."* — fray-adjacent marks **always** itch. Meanwhile the crimson
call-slip's hour arrives off-panel: Rekhak leaves the Office walking, and Lekh files the chair-empty
minute like a record. Rules carried forward from `chapters/chapter-001/chapter-summary.md`: chain-stop
budget for Chapter 2 is **one**, spend it late and on something smaller than the truth (not before
Page 006); rumour register ("four hundred blinked") and truth register (one silent second) stay
separate; the four notes must not match anything audible before Chapter 3; the Loom never speaks;
Kessa's thinking is shown through shutters, never interiority.

### Format decisions (user-confirmed — do not relitigate)
- Fresh world (NOT the old Aetherra) · webtoon full colour · vertical strip · English + Hindi.

---

# 🔁 HOW TO RESUME IN A NEW CHAT (step by step)

1. Read this README (especially **CURRENT POSITION**).
2. Read the canon: `series-bible/00-overview.md`, `02-power-system.md`, `style-guide.md`.
3. Read the previous page's script + its `characters/` and `other/` notes so continuity holds
   (e.g. `chapters/chapter-001/story/page-002.md`).
4. Build the **next page** using the Workflow below.
5. **Update CURRENT POSITION** above (pages completed + next-page brief).
6. Commit to the session branch named in CURRENT POSITION, push, and open/refresh the PR (see Git rules).

### Git rules
- Work only on the branch named in **CURRENT POSITION** (each Arena session gets a fresh
  `arena/…-manga` branch; update the field when it changes). Commit, then
  `git push origin <that branch>`.
- One PR per branch. A merged PR does not follow a new branch: when the session branch changes, open a
  new PR from it (currently [PR #2](https://github.com/Kyabtao/Manga/pull/2); PR #1 is merged). After
  pushing, the open PR updates automatically — do **not** open a second PR from the same branch.
- If the local clone looks fresh (HEAD at "Initial commit", files untracked), that is expected in a
  new sandbox: `git add -A && git commit && git push` and the PR will pick everything up.

---

# 📖 STORY SO FAR (one line per page)

- **Page 001** — At the Unspooling, humankin thread-mender **Ira Sutar** draws **no thread**; the hook
  reveals an old surgical **stitch** sewn across her empty palm.
- **Page 002** — Kessa the Kshudra debt-appraiser reads Ira's palm: **zero debt**. Thesis lands:
  *"You're the only dry thing in the flood. That is not a defect. That is a price."* Hook: *"Who sewed you?"*
- **Page 003** — Kessa explains what a stitch *is* (a door nailed shut before it could open — Ira's
  thread was **hidden**, not missing) but never *who* sewed it. Then the market goes cold: **Rekhak
  Vahni**, Ash Council Debt-Reckoner, descends the Council Stair hunting "a hole" in the ledger — the
  girl the Court recorded but the Council never registered. Hook: he asks for **Ira Sutar** by name.
- **Page 004** — Ira's first words to an official are a negotiation. Rekhak's two-column invitation:
  climb at the third bell, or be **struck from the ledger** entirely. Kessa forbids the climb and sells
  her ash-ink in the same breath — *borrowed lines* so the debtless girl can pass as a debtor. On the
  stair Ira asks the one question Sight cannot read — *"What do you owe, Reckoner?"* — and his
  counting-chain stops: *"The one ledger I am not permitted to open. My own."*
- **Page 005** — The third-bell climb: first panel in the series with **no ash**. In the Reckoning
  Office waits **Patra**, a Preta broker for an unnamed principal — shadow falling toward the light,
  face and name that don't hold. The offer: three blank lines (Name. Kind. Thread.) — *existence as
  payment* — for one hour of Ira's palm under commissioned Sight. Hook: *"He doesn't want the door
  opened. He wants to be certain it stays closed."* Rekhak: silent, chain running, neck-line past the
  jaw overnight.
- **Page 006** — Ira negotiates like a mender (*nothing gets sewn till I've seen the tear*): three terms
  — Kessa as witness, the basin as ground, one true question. Patra accepts too easily and answers the
  question with a material: *thread that has never been pulled* — then the drip: *whoever sewed you was
  **lending**.* Rekhak spends his first word in two pages — *"Don't."* — chain still running. Patra's
  first real smile: *"Oh good. He's invested."*
- **Page 007** — The deal comes home: Kessa appraises it and names it — *not a mending, a **sealing***
  (canon vocabulary from this page on) — with a half-second eyeline to her lockbox at the word
  *unpulled*. She ties sixty hour-knots round Ira's wrist (*"my knots don't ask permission to end"*) and
  names her price: one true thing about Ira's mother. The girl who owed nothing sleeps owing her first
  debt.
- **Page 008** — The hour: Rekhak **kneels** (the Council does not kneel) and spends the commissioned
  Sight on Ira's palm. What he sees is not a door but a **fold** — her thread folded inward, pressed,
  bundled, *sleeping*, sewn round with shadowless thread. Then the silent second: the Loom's hum stops
  citywide, the Spindle flickers for the first time in four centuries, every threaded soul looks up.
  Hook: *"It moved. Fifteen years it never moved."* Knot count: sixty; the hour not over.
- **Page 009** — Payment and refusal: the form comes back **written** — Name *Ira Sutar*, Kind **Manav**,
  Thread *none* — because the Council's seal cannot hold a Kind it refuses to register. Ira: *"Write it
  true or don't write it."* Patra re-reads the deal: the principal bought an hour, not a signature.
  Rekhak falsifies the audit aloud (*"Nothing more"*) with the chain stopping — his first lie, Ira's
  first shield. Hook: Kessa counts the cut hour-rope: sixty went in, **sixty-one** sit in her palm.
- **Page 010 — FINALE** — On her roof under the turning Loom, Ira re-reads her hand (*not empty —
  packed*), folds her fist over the stitch and vows one word into her knuckles: **"Sleep."** The Page 001
  captions return and are answered: *"That was the first lie anyone told about her."* Late at the Knot &
  Nail, Kessa opens the lockbox: forty years of shadowless cut-end, never asked what it was cut from —
  and its end-knot is the same uncanny whorl as the sixty-first. The hum ends one note lower.
  **END OF CHAPTER ONE.**

**CHAPTER 002 — THE MINUTE THAT OWES (वह मिनट जो ऋणी है)**

- **Ch. 002 · Page 001** — The morning after, three rooms at once: basin gossip turns the silent second
  into a story (*"four hundred of us blinked together"* — the rumour register, kept separate from the
  truth register); up-terrace, every clerk re-stamps last night's records twice, two seals on one page,
  because Council fear *files*. At the Knot & Nail, Ira pays the mother-debt's first instalment
  **early and unasked**: four off-key notes, never words — and Kessa, who keeps no ink, stores them in
  the only ledger she trusts (thumb-rub on the tally-thread) and shuts the stall before noon for the
  first time in four Unspoolings. Hook, up-terrace: Lekh delivers a call-slip to Rekhak's bare desk —
  the hour's audit summoned for re-review — sealed in **crimson wax**: *the Council's wax is grey; this
  slip was not sealed by the Council.* Chain still running at the seal; Chapter 2's one-stop budget
  untouched.

---

# 🗂️ STRUCTURE

```
series-bible/            The canon. Read before writing anything.
  00-overview.md         Pitch, why it scales, why it becomes a card game
  01-the-nine-kinds.md   Races (human → demon, elf → goblin, humankin…), each with an art direction
  02-power-system.md     The Sutra, Debt, Fraying, Mending — the rules, and the rules that are banned
  03-the-nine-sectors.md Regions, each with a different law of pulling
  04-card-game-notes.md  The TCG design, carried forward from Chapter 1
  style-guide.md         Art direction + reusable image-prompt block

chapters/
  chapter-001/            COMPLETE — 10 pages (see chapter-summary.md)
    chapter-summary.md   close-out: synopsis, canon rules, open threads, bulk-cast ledger
    story/     page-001..010 .md / .hi.md          (scripts EN + Hindi)
    characters/ ira-sutar.md, kessa.md, rekhak-vahni.md, patra.md,
                cast-page-001..010.md, *-ref.png
    other/     locations.md, glossary.md
    images/    page-001..010.png
  chapter-002/            skeleton ready (story/ characters/ other/ images/ + .gitkeep)

website/                  generated reading site (committed) — build.py + assets/ are the sources
index.html                root redirect into website/
```

Every chapter follows the same `story/ characters/ other/ images/` layout.

### Structure conventions (audit-approved — keep these)

- **One folder per chapter**, always the four subfolders above, created empty (with `.gitkeep`) before
  the chapter starts — see `chapters/chapter-002/`.
- **Character sheets live in the chapter of first appearance, forever.** Later chapters' `cast-` files
  link back to the original sheet instead of copying it. Refs sit beside their sheet as `<sheet>-ref.png`.
- **`cast-page-NNN.md`** = everyone on that page + object card-lines. **`<name>.md`** = full sheet.
- **`chapter-summary.md` sits at the chapter root** (not in `other/`): the close-out document with
  synopsis, canon rules established, open threads and the bulk-cast ledger.
- **`other/` is chapter-scoped** (locations, glossary). The website merges them into living documents;
  the chapter files remain the canon of record.
- **Naming:** `page-NNN.md`, `page-NNN.hi.md`, `page-NNN.png`, `cast-page-NNN.md` — zero-padded, never
  renamed. Hindi mirrors carry the `.hi` infix.
- **Series-level docs live in `series-bible/`** (numbered 00–04 + `style-guide.md`); legacy reference
  docs stay at the root (`ringbound-era-analysis.md`).

# 🌐 WEBSITE — read it in a browser

A clean static reading site with page-wise navigation (EN + हिन्दी toggle, per-page cast links, chapter
covers, merged glossary/locations, character sheets with refs) is generated from this markdown canon:

```
python3 website/build.py          # dependency-free, stdlib only; regenerates website/*.html
python3 -m http.server 8000       # serve the REPO ROOT, then open /website/ (root index.html redirects)
```

- Generated HTML **is committed** (so anyone can read without building); `website/build.py` and
  `website/assets/site.css` are the only hand-maintained files in `website/`.
- Pages link to the **original** images under `chapters/…` by relative path — one copy of every asset.
- Re-run the build after finishing any page; commit the refreshed HTML with the page commit.

# 🛠️ WORKFLOW (how each page is made)

1. **Script** — write `story/page-NNN.md` in English.
2. **Translate** — mirror it in `story/page-NNN.hi.md`.
3. **Cast** — log every character in `characters/`, with a card-game line.
4. **World** — log places & terms in `other/`.
5. **Art** — render `images/page-NNN.png` from `style-guide.md`'s prompt block.
6. **Track** — update this README's CURRENT POSITION; commit; push; refresh PR.
