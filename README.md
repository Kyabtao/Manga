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
| **Chapter in progress** | **001** — *The Girl With No Thread* |
| **Pages completed** | **001**–**006** |
| **NEXT page to build** | **007** |
| **Open PR** | [Kyabtao/Manga#2](https://github.com/Kyabtao/Manga/pull/2) (targets `main`; PR #1 is merged) |

### Next-page brief (Chapter 001 · Page 007)
The descent and the consult: Ira comes down the Council Stair before dusk and brings the deal to Kessa
at the Knot & Nail. Kessa reacts to the **material**, not the metaphor: *"Thread that has never been
pulled… then it wasn't a mending that went into you, be. Mendings leave a debt-shaped hole. That was a
**sealing**."* She agrees to witness and to tie the hour-knots round Ira's wrist — but her price is not
coins: *"When this is over, you tell me one true thing about your mother. Your first debt, be. I'll keep
it safe till you can pay it."* End hook: Kessa ties the last knot and does not let go. CAPTION: *The
girl who owed nothing / went to sleep owing one true thing.* Keep the sewer a locked box; keep the
crimson buyer unnamed.

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
  chapter-001/
    story/     page-001..005 .md / .hi.md            (scripts EN + Hindi)
    characters/ ira-sutar.md, kessa.md, rekhak-vahni.md, patra.md,
                cast-page-001..005.md, *-ref.png
    other/     locations.md, glossary.md
    images/    page-001..005.png
```

Every chapter follows the same `story/ characters/ other/ images/` layout.

# 🛠️ WORKFLOW (how each page is made)

1. **Script** — write `story/page-NNN.md` in English.
2. **Translate** — mirror it in `story/page-NNN.hi.md`.
3. **Cast** — log every character in `characters/`, with a card-game line.
4. **World** — log places & terms in `other/`.
5. **Art** — render `images/page-NNN.png` from `style-guide.md`'s prompt block.
6. **Track** — update this README's CURRENT POSITION; commit; push; refresh PR.
