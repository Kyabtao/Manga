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
| **Pages completed** | **001**, **002**, **003**, **004** |
| **NEXT page to build** | **005** |
| **Open PR** | [Kyabtao/Manga#2](https://github.com/Kyabtao/Manga/pull/2) (targets `main`; PR #1 is merged) |

### Next-page brief (Chapter 001 · Page 005)
The climb at the **third bell**: Ira crosses the Council Stair with borrowed lines under her sleeve and
sees the up-terrace for the first time — clear air, no ash, a sky that reads as *wrong* to her eyes.
In the Reckoning Office the buyer's intermediary waits (affiliation unnamed; nothing crimson on their
person; they speak only of "my principal"). The offer: one hour of her palm under a commissioned Sight,
in exchange for the Council **registering her** — name, Kind, thread. Existence as payment. End on the
intermediary's cost line: *"All it costs is your palm for one hour, child. He doesn't want the door
opened. He wants to be certain it stays closed."* Keep the buyer unnamed; keep the sewer a locked box.
Rekhak is present but silent the whole page — and his counting-chain is **running again**, which should
worry the reader more than the stop did.

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
    story/     page-001..003 .md / .hi.md            (scripts EN + Hindi)
    characters/ ira-sutar.md, kessa.md, rekhak-vahni.md,
                cast-page-001..003.md, *-ref.png
    other/     locations.md, glossary.md
    images/    page-001.png, page-002.png, page-003.png
```

Every chapter follows the same `story/ characters/ other/ images/` layout.

# 🛠️ WORKFLOW (how each page is made)

1. **Script** — write `story/page-NNN.md` in English.
2. **Translate** — mirror it in `story/page-NNN.hi.md`.
3. **Cast** — log every character in `characters/`, with a card-game line.
4. **World** — log places & terms in `other/`.
5. **Art** — render `images/page-NNN.png` from `style-guide.md`'s prompt block.
6. **Track** — update this README's CURRENT POSITION; commit; push; refresh PR.
