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
| **Branch** | `arena/01a0b63a-manga` (the only branch we work on — each Arena session gets a fresh one; keep this field current) |
| **Chapter in progress** | **Chapter 009 *The Reading* — pages 001–003 scripted (EN)** · Chapters 001–008 COMPLETE · **Hindi: Ch. 001–008 COMPLETE** (94.4–98.1% Devanagari, all above the 80% floor) |
| **Pages completed** | Ch. 001–008: **all complete** (80 pages, 80 images) · Ch. 009: 3 of 10 scripted |
| **NEXT page to build** | **Chapter 009 · Page 004** — the held-stop demand; the chain-stop is **spent on Page 006** |
| **Open PR** | [Kyabtao/Manga#3](https://github.com/Kyabtao/Manga/pull/3) (targets `main`) |

### Next-page brief (Chapter 009 · Page 001)
**The chain-stop budget is overdue.** It has been held unspent across Chapters 006, 007 and 008.
Chapter 009 opens its budget and must spend it — no further deferral.

Chapter 008 ended on a slate: a compliance chain read a braided palm, returned both years at once,
and a clerk wrote one word — **unreadable** — and underlined it twice. *There is no procedure for
that, which means by morning there will be one.* That is Chapter 009's opening problem. The Office
does not retaliate; it *codifies.* A new instrument will exist by the first bell, and it will be
aimed not at Ira but at the thing she cannot protect: **Jadi's hand is the proof of concept and
the only braided palm the Office can put on a slate.**

The page's shape: the new procedure arrives at the stall as paperwork, not force — a grey clerk
with a slate and a second, worse word. Ira has three days of breathing room at most and three
problems stacked behind each other: Nandi is in custody and has not been charged; clause four's
timer on the licence is still running; and the mother is four nights down a list of forty-one.
Kessa's counter-position: *he can have the books, I keep the reading* — the tally-thread is the
only copy of the crease-writs, and it makes her, not Ira, the piece on the board the Office has
not noticed yet.

The **chain-stop lands here**, and it should cost Rekhak rather than Ira: he is the basin's only
chain-reader and the only person who can explain what a braid does to a compliance instrument —
which means the Office will require him to swear to it. A held-stop oath on that subject is a
deposit waiting to happen, and he has one lie already on his ledger.

Continuity: Ira's stitch is **open** with a live channel; Jadi wears the school's first braid;
the Mendery has a clerk on a crate every second bell; the Roll of Hands and Jadi's roster of
forty-one are both with the mother; Loom never speaks; mother never on panel; the principal's
answered letter is still unread by him.

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

**CHAPTER 003 — THE HAND THAT OPENs (वह हाथ जो खोलता है)**

- **Ch. 003 · Page 001** — Morning of the letter: Kessa opens the lockbox in daylight, the shadowless cut-end on the counter. The reversal: the cutter taught Ira's stitch. The folded letter is a posting order transferring the blink census to the Knot & Nail. Kessa was not asked.
- **Ch. 003 · Pages 002–010** — Rekhak files the census transfer (Kessa refuses to sign). Ira investigates Bhan's nightly openings (ash-grey thread, same gauge). The supply line: one person, forty years. The four notes match *wrongly* through Rekhak's chain. Ira reads the oath-link; Rekhak confesses: "I saw what you are. I lied to protect it." Chain-stop spent. The lockbox grows to seven objects. The stitch moves. Fifth thread at the Council Stair foot. **END OF CHAPTER THREE.**

**CHAPTER 004 — THE WEIGHT OF THREAD (धागे का बोझ)**

- **Ch. 004 · Pages 001–010** — The cutter demonstrates: Ira's stitch reproduced on Bhan's arm. The cutter finishes the lesson, seals the arm permanently, leaves a child's first knot as payment. The stitch opens loop by loop — the old thread unwinds cleanly. The Sutra-mark is visible for the first time: projection type, dormant, braided (two strands: Ira's and the sewer's). The braid leaks into Ira's mending thread. The mark flickers. Seven objects in the lockbox. **END OF CHAPTER FOUR.**

**CHAPTER 005 — THE FIRST PULL (पहला खिंचाव)**

- **Ch. 005 · Pages 001–010** — The Spindle brightens for the second time. Ira's mark opens: braided thread emerges — ash-grey and shadowless, given not borrowed. The blank strand has no Sector, no Kind, no debt. Rekhak Sight-reads the mark ("Older than the current Loom-turn"). Ira mends debtlessly with the braided thread. The Office files the first grey-ink record of her thread. An Inspector recognizes: "Like the Mendery records." The posting order references a Mendery file. Kessa gives Ira a key to the Mendery's back door — her mother's key. Ira enters the archive: hundreds of files. Her mother's file carries crimson: "Sewn shut." And a second line, added later: "The braid will open. The thread will pull. The girl will come." The principal predicted her. **END OF CHAPTER FIVE.**

**CHAPTER 006 — THE MOTHER'S FILE (माँ की फ़ाइल)**

- **Ch. 006 · Pages 001–005** — Ira returns to the Mendery archive with her mother's key. Her mother's file: **Manavkin, braided, projection type, zero debt, bound twenty years, never released** — reason given: *unlicensed*. The back wall holds Kshudra files older than the Council's own records. Ira finds the charter of **The School of the Braided Thread**, founded by **Sutar (M.)** — her mother. Rule three: *the teacher's strand is sewn into the student before the student's first speech.* **Nandi**, the archive's old Kshudra keeper, closes the chapter's first half with the three-part revelation: **the sewer is her mother. The cutter is her mother. The supply line is her mother.** She bound herself, voluntarily, in a binding chair, for twenty years. She left three days ago, to find the principal.
- **Ch. 006 · Pages 006–010** — Ira returns to the basin and works: she pawns the charter to Kessa (lockbox to **eight objects**), mends Bhan at the stall counter with the braid showing whorl-grain in the seam, and hears the four notes **correctly** through the thread's memory for the first time — through the strand, not through the air. The Inspector returns with an **audit warrant**; the standoff at the counter is settled coin-on-seal, and he leaves — but not before reading the charter: *"Files were supposed to be destroyed."* That night a letter lies at the foot of the Council Stair: folded once, **grey wax on one flap, crimson on the other, touching.** Ira carries it to the stall and sets it beside the closed lockbox. Kessa's loupe goes down. **The letter is not opened.** **END OF CHAPTER SIX.**

**CHAPTER 007 — THE CRIMSON LINE (क़िरमिज़ी पंक्ति)**

- **Ch. 007 · Pages 001–005** — The night of not opening it. Ira lies under the Loom with the letter on the stitch, and the strand climbs past the grey to the crimson. Dawn: two hands on one fold — Ira takes grey, Kessa takes crimson. The grey **snaps** clean; the crimson **lifts**, soft and cloudy, **already broken and pressed back down.** The letter's body: a **Letter of Provisional Licence** naming *Ira Sutar, of the School of the Braided Thread*, four clauses — one stall, one basin, one name; threads at each second bell; the mark on the Council kind-roll; and **clause four: produce its founder before the seal.** Rekhak reads the register it came from and tells them the worst of it: the **third register** is a crimson-bound private hand's book; entries in it **license nothing — they inventory.** Sign and a writ goes after her mother. Stay silent and in one Unspooling the school reverts to him. Kessa notices the fold is too stiff. Pressed flat, the crease holds eleven words drawn in **sealing wax** where only a mender would look: *"The founder will not appear. Do not sign. — a hand of the school."* Somebody broke the principal's seal, dug a bead out of it with a thumbnail, wrote in the fold, and left the letter for Ira on a morning she'd be alone.
- **Ch. 007 · Pages 006–010** — Laid across the stitch, the strand settles into the writing and the braid opens: **crimson under the grey**, invisible in daylight for fifteen years. Four notes, correct — and then two dry stitches of **live** needlework. Kessa reads the sound — doubled folds, heavy needle, slow turn — that is **binding**, and the only hand-binder in the basin is the Mendery. Ira returns to a disbound archive: every quire opened, every spine unthreaded, forty years of her mother's thread in a pile on the floor. **Every file in the Mendery was held shut by Sutar, M.** On the back wall, one file's width of clean dust: the **Roll of Hands** is gone — the school's pupil register, forty years deep, kind and year and **no names** (a name is a handle and a handle can be read off a page). Nandi says why: *"Her freedom was the rent on that shelf."* And she delivers what she was left to hold: *"Tell her I did not write her name in the roll. Tell her I sewed her instead."* / *"Tell her not to sign anything that asks her to exist."* Ira answers in the fold — a second bead of wax, three lines in the same crease (*"The founder's hand has not signed. The stall is open."*), the fold closed so both messages vanish, then sewn shut with the blank strand and a **child's first knot.** Three seals on one letter: grey, crimson, braid. Kessa takes the only copy that cannot be audited — into her tally-thread. The letter goes down the supply chute. And on the step, Ira **closes her own stitch**, so the channel cannot be followed. **END OF CHAPTER SEVEN.**

**CHAPTER 008 — THE FIRST PUPIL (पहला शिष्य)**

- **Ch. 008 · Pages 001–005** — The Office comes down: two clerks, a slate, a lamp, and the Inspector with his hands behind his back. They find the archive taken apart, which makes the **room** evidence rather than the records. Ira saves it by declaring the Mendery **third-register property** — the principal's, not the Council's — which works, and which hands the Inspector a standing reason to return every second bell. They take **Nandi** instead, and she walks out on her own feet with one instruction: *the shelf — the empty one. Look at what's still standing next to it.* Beside the gap is the **Book of the Hand**: the school's method book, forty years of knot diagrams drawn for pupils who could not read, ending in one page per pupil — a **first knot stitched down, no names.** The mother took the names and left the knots, because a knot cannot be looked up. The last page is less than a year old.
- **Ch. 008 · Pages 006–010** — The school walks in the door. **Jadi** — Kshudra, seventy-odd, **first pupil of the School of the Braided Thread** — holds up a palm whose root seam has opened and calls Ira *the teacher.* She has come to have the thread **pulled out.** Her account rebuilds the missing twenty years: after the binding, the school ran as a **hatch** cut low in the Mendery's back door, one forearm at a time, in the dark, two taps to end. Jadi kept the roster in her head; the Roll held kind, year and knot and never a name. And for nine months the Office has been **dating** pupils — a chain across the palm, a number on a slate, no arrest, no violence, and four days later the hand stops knowing what a needle is for. Forty-one measured; six unable to mend. The Roll was **copied years ago.** Ira refuses to cut, and finds the answer on the school's first page: **rule three enrolls, rules one and two finish** — a single thread is a single date, a braid carries two years and a reader gets neither. *The school doesn't teach mending. The school makes people the Office cannot count.* Her mother was taken two months after enrolling Jadi — the root was never finished. Ira opens her own closed stitch and works at the hatch, laying a second strand into Jadi's palm, and **amends rule three: the teacher's strand goes in first, and then the teacher tells you what she did.** Up-terrace, a compliance chain reads a braid for the first time and returns both years at once. A clerk writes one word on a slate and underlines it twice: **unreadable.** **END OF CHAPTER EIGHT.**

**CHAPTER 009 — THE READING (पाठ)**

- **Ch. 009 · Pages 001–003** — By morning the Office has a procedure, and it has not sent anyone: it *posted.* **Provisional Ordinance forty-one, Unreadable Hands** — a hand that returns no year may not be entered in any ledger, licence, wage-book, charter or roll (clause one: forty years of the school's work, handed over as a punishment); every such hand must be **declared** by its owner *or by any person who knows it* within three days (clause two: the count did not vanish, it moved — the Office now counts the *absence* of a date, and a neighbour's form costs nothing); and no licensed practitioner may mend or instruct a declared hand (clause three: the second school is illegal the day it opens). Because the Mendery answered for itself as **third-register property** in Chapter 008, the new **Register of Unreadable Hands** is kept *there* — place of keeping, slot four, a desk in Ira's own cellar — and Ira is its keeper: the new teacher made the unpaid custodian of the instrument that indexes her own people. The commencement clause is the hook: the ordinance takes effect **from the third bell of the previous night**, which is hours *before* Ira braided Jadi's palm — a law written to be earlier than the thing it governs. The register arrives triple-sealed with **forty-one ruled lines** and a first entry already standing: no name, no kind, no year — a drawn palm with a **closed** seam, dated eleven days ago, the day Ira's provisional entry was written. **Jadi** — who cannot read a word of it — reads the drawing at a glance, because the school taught hands in drawings and the Office drew a hand. **Kessa** holds up the **tally-thread**: *he can have the books, I keep the reading.* And a summons with a chain-impression brings **Rekhak** to the counter as the basin's only chain-reader: at first bell he must swear, on a **held stop**, the Office's drafted sentence — *a braided hand returns no year, and no hand in this basin can be made to return two* — every word of which is false, and every word of which will be entered in the one ledger he has never been allowed to read. His reason is not nobility: he is buying the forty-one a **record**, and he is keeping himself necessary.

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
  chapter-002 .. chapter-008/  COMPLETE — same layout, 10 pages each
  chapter-009/            next — skeleton created before writing starts

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
