# Admin, Automated · Personal Automation and Repetitive-Task Elimination

An interactive, single-page teaching site on the best-evidenced everyday AI
skill there is: finding the repetitive layer of your own week and handing it
to templates, rules, and AI you stay accountable for (the Repeat Audit:
spot it, template it, route it, retire it). A **Learning on Demand**
program: the facilitator projects it while learners scan a QR code and work
every exercise on their own devices, or share the link for self-paced
review. Private by design: every exercise runs on the learner's own tasks
(never other people's names) and nothing typed is saved or sent anywhere.

Part of the Vanderbilt Learning Series (CHART Program). Catalog:
[Course Library](https://me5231979.github.io/Course_Library/)

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/Admin-Automated/
- **Self-paced edition:** https://me5231979.github.io/Course_Library/courses/Admin-Automated/web/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/Admin-Automated/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8000
```

## What it teaches (6 sections)

1. The repeat tax: Gallup's finding that automating repetitive tasks is the
   highest-payoff everyday AI use (~77% report clear gains), and Leadership
   Circle's warning that saved time evaporates unless banked
2. Spot it: the recurrence inventory, the three tells (the search, the
   rebuild, the echo), and a private ranked top-three candidate list
3. Template it: three de-identified past examples in, slotted skeleton out,
   voice intact; template hygiene and the leftover-name incident
4. Route it: three-pile email triage (needs me today / this week / not at
   all) with AI drafting and read-then-send, plus calendar rules
5. The Automation Lab: rebuild the monthly report cycle step by step and
   see how the design holds at month two
6. Retire it and bank it: the test retirement (skip one cycle, manager in
   the loop) and visible banking of the recovered hours

Ends with a scored recap, the **Automation Card capstone** (one task, one
move, one named failure mode, one dated 20-minute build session, the bank
named), a flip-card glossary, and a commitment close. `worksheet.html` is
the printable Repeat Audit card; `cheatsheet.html` is built to sit next to
the keyboard during the build session.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| The repeat tax | **Guess the number** | Call four findings before the reveal; missed guesses stick |
| Spot it | **Recurrence inventory** | Privately list the message, the report, and the request they repeat, ranked |
| Template it | **Judge the template** | Call five templates: reusable with slots, specifics baked in, or too generic |
| Route it | **Triage the inbox** | Sort five incoming items into the three piles |
| The lab | **The Automation Lab** | Rebuild the monthly report cycle and run two simulated months |
| Retire and bank | **Keep, shrink, or retire** | Sort five recurring obligations |
| Recap | **Scored quiz** | 6 questions mapped to the objectives |
| Capstone | **My Automation Card** | Build and copy a dated, private automation commitment |

## Instructional design

- **Bloom's ladder:** objectives run Identify → Build → Set up →
  Apply → Decide (Create/Evaluate at the capstone).
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 automation card + 7-day pulse + 30-day re-poll (templates on the
  facilitator briefing slide). The headline L3 metric: build sessions
  actually held.
- **Adult learning:** learners bring one noticed repeat (pre-work), every
  exercise runs on their own material held privately, and the capstone
  ships as a dated 20-minute build session.
- **Privacy by design:** the learner's own tasks, never other people's
  names; the inventory and automation card state explicitly that nothing
  is saved or transmitted.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (rtGuess, tplJudge, triSort, ksrSort)
- Recurrence inventory: `raBuild` block · Automation Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup workplace AI research (automating
  repetitive tasks as the highest-payoff use case, ~77% reporting clear
  productivity gains), Leadership Circle (the evaporation warning, framing
  only, no invented numbers). The traffic light must match Start Smarter and
  AI 201 exactly: green public, yellow internal in approved VU tools only,
  red private information about people, never.
- Publishing is handled inside the Course_Library repo by the orchestrator.
