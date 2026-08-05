# Numbers, Faster · Data and Analysis with AI

An interactive, single-page teaching site for the highest-payoff everyday
AI skill Gallup's workplace research keeps surfacing: interrogating a
spreadsheet with AI and verifying what comes back. The course teaches the
**Data Loop** (Describe, Ask, Check, Tell): describe the data before you
ask, climb the question ladder one rung at a time, recompute before you
believe, and tell the finding in two plain sentences. A **Learning on
Demand** program: the facilitator projects it while learners scan a QR
code and work every exercise on their own devices, or share the link for
self-paced review. Private by design: every exercise runs on datasets and
columns (never names or personal records) and nothing typed is saved or
sent anywhere.

Part of the Vanderbilt Learning Series (CHART Program). Catalog:
[Course Library](https://me5231979.github.io/Course_Library/) ·
Sibling course: "Answers, Faster" teaches ask-anchor-check for research;
this course is its numbers twin.

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/Numbers-Faster/
- **Self-paced edition:** https://me5231979.github.io/Course_Library/courses/Numbers-Faster/web/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/Numbers-Faster/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8101
```

## What it teaches (6 sections)

1. The case for AI on numbers: Gallup's findings (data work near the top
   of AI use cases by payoff, ~3 in 4 users report gains, frequent users
   gain most, most staff still work by hand) and where AI's math breaks
2. Safe data in: the shared AI traffic light applied to data files, and
   the five-minute de-identification ritual
3. Ask the sheet: the describe step (columns, period, source, quirks) and
   the question ladder (summarize, compare, outliers, explain), with a
   privately built Data Loop starter
4. Check the math: the check ritual (recompute one number, totals and
   counts, row trace on surprises), with SHRM's four-hours-a-week fixing
   finding as the cost of checking too late
5. The Analysis Lab: run a month-end enrollment analysis, one decision
   per loop step, and see the four-week outcome
6. Tell the story: the two-sentence finding, chart briefs, and the
   recommendation that never gets delegated

Ends with a scored recap, the **Data Loop Card capstone** (one dataset,
one first move, one named failure mode, one dated first run), a
flip-card glossary, and a commitment close. `worksheet.html` mirrors the
capstone on paper; `cheatsheet.html` is built to sit next to the
keyboard during the first run.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| The case | **Guess the number** | Call four Gallup findings before the reveal; missed guesses stick |
| Safe data in | **Green, yellow, or red** | Call the traffic light on five real-feeling datasets |
| Ask the sheet | **Data Loop starter** | Privately name their dataset, grind question, and wish question |
| Check the math | **Catch the error** | Judge five AI outputs: let it through, broken math, or not in the data |
| The lab | **The Analysis Lab** | Run the month-end one decision at a time and see week four |
| Tell the story | **Judge the finding** | Call five data narrations: plain, fog, or past the data |
| Recap | **Scored quiz** | 6 questions mapped to the objectives |
| Capstone | **My Data Loop Card** | Build and copy a dated, private first-run commitment |

## Instructional design

- **Bloom's ladder:** objectives run Explain, Prepare/Apply (safety),
  Apply (the loop), Build (comparison and chart brief), Verify/Evaluate.
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 Data Loop card + 7-day pulse + 30-day re-poll (templates on the
  facilitator briefing slide). The headline L3 metric: first runs
  actually completed.
- **Adult learning:** learners bring one real dataset (pre-work), every
  exercise runs on their own material held privately, and the capstone
  ships as a dated 20-minute first run.
- **Privacy by design:** datasets and columns, never names; the starter
  and Data Loop card state explicitly that nothing is saved or sent.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (statGuess, lightSort, errSpot, findJudge)
- Data Loop starter: `dlMap` block · Analysis Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup workplace AI research (~3 in 4 data
  users report gains, frequent-user gap, data work near the top by
  payoff, most work still manual), SHRM (about 4 hours a week fixing AI
  output). The traffic light must match AI Basics and AI 201 exactly:
  green public/generic, yellow internal in approved VU tools only, red
  private information about people, never.
