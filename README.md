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
| **Pages completed** | Ch. 001: **001**–**010** (complete) · Ch. 002: **001**–**006** |
| **NEXT page to build** | **Chapter 002 · Page 007** |
| **Open PR** | [Kyabtao/Manga#2](https://github.com/Kyabtao/Manga/pull/2) (targets `main`; PR #1 is merged) |

### Next-page brief (Chapter 002 · Page 007)
Dusk, basin: **Patra returns** (first appearance since Ch. 001 Page 009) at the shut stall's doorstep
where Ira still waits — the principal's broker moves in person because the principal's paperwork now
needs a mender: a commission slip, **crimson-sealed, unbroken**, offered with both hands (broker's
courtesy): a mend commissioned at the principal's expense, client unnamed, the mark described only in
paperwork prose. Ira's terms stand from Ch. 001 Page 006: *nothing gets sewn till I've seen the tear* —
she does not accept unseen work, and Patra expects nothing else (that expectation is the menace). Hook,
last panel: reading the prose aloud in her mender's flat tone, Ira matches it line by line to what she
sewed on Bhan's forearm: same fray, same night-shift hour, same *"nothing touched it"* — **the tearing
has a schedule, and the schedule has an owner on paper**. The slip's payment line, smaller and worse
than coin: *one line of your registration form, restored* — existence offered back one line at a time.
Rules carried: the chain never stops again in Chapter 2 (Rekhak off-panel carries the oath-link); the
four notes silent until Ch. 3; shutters day seven, no slit; census suppression continues; Lekh's
cuff-chit sleeps; the Grey Clerk stays gone; Patra gets no face close-up wider than Ch. 001 established;
the Loom never speaks; crimson on panel only as the unbroken seal until the hook panel's prose-matching
(caption carries the match, art stays letterless).
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
- **Ch. 002 · Page 002** — The dock worker from the alley mend is named **Bhan**, and his left-forearm
  tear re-tears identically with "nothing touched it" — patience, not anger, as the menace register.
  Ira mends him at the shut Knot & Nail doorstep (the mend follows the shutters); mid-mend the fold in
  her palm **lends through the needle unasked** — her first power bleed, and it feels like kindness, so
  she doesn't stop it. No debt, no debt-mark; the only evidence is a faint **whorl-grain** in the
  finished seam (no owner on panel). Kessa performs entirely as architecture: a finger-width shutter
  slit opens at head height, then is closed. Hook: Bhan, rolling his sleeve — *"It doesn't itch
  anymore."* Fray-adjacent marks always itch. Up-terrace, Rekhak walks to the re-review while Lekh
  files the chair-empty minute like a record; the chain-stop budget stays unspent.
- **Ch. 002 · Page 003** — The rumour grows paperwork: the pot-row **blink census** (ink, charcoal, one
  fingernail scratch, three Kshudra knots) is nailed to the list-post — witnesses only, never the event.
  First Council fear enters the market: a **Grey Clerk** descends the Council Stair (daylight warning:
  the pot's steam bends toward the stair) and buys the list with **new-struck Office coin** — minted
  overnight; fear spending faster than procedure. Guthli: *"It's not ours anymore."* Hook, mid-stair: at
  the list's foot, in no market hand, one name added then crossed out in **crimson, dry before the coin
  was counted** — Ira Sutar, the threadless girl who could not have blinked. The principal's paperwork
  counted her among the witnesses, then corrected itself; procedure re-rolls and quickens its step.
- **Ch. 002 · Page 004** — Inside the filing end (first Office interior): the census arrives as a
  **count** ("Names are a count. The category wins."), and Lekh finds the crimson cross-out with **no
  initial** — Rule 9 says an uninitialled cross-out was never made, so the name under it is still on the
  list. His choice: grey file-chit or black flag-chit (flag = audit of the audit). He files broken and
  keeps an off-book **cuff-chit** — the first seed of the basin's trusted up-terrace face. Basin: the
  pot-row's *owned* quiet (a sold rumour nobody dares repeat), Bhan's double shift on the itch-less
  mark, and — pattern broken — the Knot & Nail slit does **not** open at all on day four. Hook: by
  morning the cross-out has initialled itself, crimson and dry, in no clerk's hand. The last three words
  of the page: *He stands up.*
- **Ch. 002 · Page 005** — First single-room page in the series: the **re-review chamber door** (plain,
  unmarked, opens inward, never closed this chapter) is drawn at last. Three nameless auditors read
  Rekhak's falsified audit back to him **by its initials** — every line his hand, his initial, including
  the lie. New canon, harmonised with Ch. 001: a momentary chain-stop is a costless tell; a **held-stop
  oath** (chain stood still first sworn word to last) opens the owner's ledger — a false word under it is
  not a tell but a *deposit*. Demanded at tomorrow's first bell; his one line, first words since Ch. 001:
  *"It always runs."* Hook: the chamber's docket-slate shows the re-review **scheduled one day before his
  audit was filed** — the principal did not react to the lie, the principal *pre-filed* it. Tomorrow's
  first bell has two owners; only one of them is procedure.
- **Ch. 002 · Page 006** — The oath page: Chapter 2's one chain-stop, **spent** on three sentences
  smaller than the truth and entirely true — *"The palm held a fold, not a door. I saw the fold. In the
  palm, I saw nothing else."* The limiting clause does the lying; the chain stays cleanly stopped (no
  deposit), and the auditors' millimetre-flinch is at the size of the truth left over. One-panel basin
  cutaway at the bell: Ira feels nothing, but the Spindle's light doing *nothing* is, after the night it
  flickered, an event. Hook: releasing the oath, the chain starts again and **one link does not** — the
  dark oath-link, readable forever by the basin's one chain-reader; the smallest bill in the building,
  and the only one addressed to a girl who was not in the room. Art canon added: the chamber slate bore
  a dry crimson initial from before the bell — the pre-touch reaches inside the chamber record.

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

- Generated HTML **is committed** (so anyone can read without building); `website/build.py`,
  `website/assets/site.css` and `website/assets/site.js` are the only hand-maintained files in `website/`.
- Reader pages keep the **page art visible while reading**: on wide screens the art sits in a sticky
  column beside the script; on narrow screens a floating **🖼 Art** button opens a full-screen overlay
  (Esc or tap to close; without JS it degrades to opening the art in a new tab).
- Pages link to the **original** images under `chapters/…` by relative path — one copy of every asset.
- Re-run the build after finishing any page; commit the refreshed HTML with the page commit.

# 🛠️ WORKFLOW (how each page is made)

1. **Script** — write `story/page-NNN.md` in English.
2. **Translate** — mirror it in `story/page-NNN.hi.md`.
3. **Cast** — log every character in `characters/`, with a card-game line.
4. **World** — log places & terms in `other/`.
5. **Art** — render `images/page-NNN.png` from `style-guide.md`'s prompt block.
6. **Track** — update this README's CURRENT POSITION; commit; push; refresh PR.
