# Across Your Week · The CHART Integrator Course

An interactive, single-page teaching site built on Gallup's sharpest workplace
AI finding: people who use AI for seven or more distinct tasks are roughly
twice as likely to report real productivity gains as people who use it for one
or two. Each CHART course builds one use case; this capstone strings them
together across one real week with the **Week Map** method: inventory the
week's recurring blocks, match each block to a CHART method, stack two methods
on one task, and bank the saved time by name. A **Learning on Demand**
program: the facilitator projects it while learners scan a QR code and work
every exercise on their own devices, or share the link for self-paced review.
Private by design: every exercise runs on blocks, roles, and workflows (never
names) and nothing typed is saved or sent anywhere.

Part of the Vanderbilt Learning Series (CHART Program). Catalog:
[Course Library](https://me5231979.github.io/Course_Library/)

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/AI-Across-Your-Week/
- **Self-paced edition:** https://me5231979.github.io/Course_Library/courses/AI-Across-Your-Week/web/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/AI-Across-Your-Week/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8104
```

## What it teaches (6 sections)

1. The breadth effect: Gallup's finding that range beats depth; the
   seven-plus user versus the one-trick user, and why single-use habits
   plateau
2. The inventory: the week as recurring blocks with an honest hour cost,
   written privately, bounded by the shared AI traffic light
3. The method match: the CHART toolbox on one slide (Answers, First Drafts,
   Minutes, Slides, Ideas, Decisions, Numbers) and the rule: match the
   block's verb, never its topic
4. The stack: chaining two methods on one task, with a check at every link;
   a chain is only as trustworthy as its weakest verify
5. The Week Lab: plan a program coordinator's Monday to Friday and see
   where the hours actually go at week four
6. Bank the time: recovered time evaporates into meetings unless deliberately
   banked; name the destination, block it, report it

Ends with a scored recap, the **Week Map capstone** (five blocks, one stack,
one named failure mode, one dated calendar pass), a flip-card glossary, and a
commitment close. `worksheet.html` is the printable Week Map;
`cheatsheet.html` carries the CHART toolbox table (method, verb, check) and
the Week Map steps.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| The breadth effect | **Guess the number** | Call four Gallup findings before the reveal; missed guesses stick |
| The inventory | **Inventory your week** | Privately write their heaviest, most repetitive, and most postponed blocks |
| The method match | **Match the method** | Pair five real week-blocks with the CHART method that fits the verb |
| The stack | **Build the chain** | Pick the right two-method stack for five real tasks |
| The Week Lab | **The Week Lab** | Plan the coordinator's four blocks and run four simulated weeks |
| Bank the time | **Judge the bank** | Call five accounts of saved time: banked, evaporated, or busywork |
| Recap | **Scored quiz** | 6 questions mapped to the objectives |
| Capstone | **My Week Map** | Build and copy a dated, private five-assist commitment |

## Instructional design

- **Bloom's ladder:** objectives run Explain (breadth) into Inventory
  (Analyze) into Match (Apply) into Stack (Create) into Commit (Create).
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 Week Map + 7-day pulse + 30-day re-poll (templates on the facilitator
  briefing slide). The headline L3 metric: calendar passes actually run and
  distinct-use counts grown.
- **Adult learning:** learners bring their own real week (pre-work: skim
  last week's calendar), every exercise runs on their own material held
  privately, and the capstone ships as a dated 30-minute calendar pass.
- **Privacy by design:** blocks and workflows, never names; the inventory
  and Week Map state explicitly that nothing is saved or transmitted.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (bgGuess, mmMatch, bcChain, jbBank)
- Week inventory: `wkInv` block · Week Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup workplace AI research (the seven-plus
  doubling, the plateau at one or two uses, frequent versus occasional
  users, gains concentrating among broad habitual users), Leadership Circle
  (recovered time refills unless banked; framing only, no invented
  statistics). The traffic light must match Start Smarter and AI 201 exactly.
- The sibling CHART method courses are named in section 03 and the closing;
  the Course Library link is the canonical catalog pointer.
