# Hiring & Talent Decisions with AI · Fair, Useful, and Inside the Lines

An interactive, single-page teaching site for managers who hire: it draws
the hard line first (candidate materials are private information about
people, and AI never ranks, scores, or screens a person), then teaches
everything valuable on the right side of the line: inclusive job
descriptions, structured interviews, scoring rubrics built before
candidates, and a skills map of the team. A **Learning on Demand**
program: the facilitator projects it while learners scan a QR code and
work every exercise on their own devices, or share the link for
self-paced review. Private by design: every exercise runs on roles and
processes (never names) and nothing typed is saved or sent anywhere.

Part of the Vanderbilt Learning Series and the Manager Voyage program.
Catalog: [Course Library](https://me5231979.github.io/Course_Library/)

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/Hiring-with-AI/
- **Self-paced edition:** https://me5231979.github.io/Course_Library/courses/Hiring-with-AI/web/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/Hiring-with-AI/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8000
```

## What it teaches (6 sections)

1. The temptation and the line: why pasting resumes into a chatbot fails
   on privacy, fairness, and legal grounds at once
2. The red side, exactly: the two never rules, the shared AI traffic
   light (green / yellow / red), and the subtle cases (reference notes,
   gut notes, the tone check, the nameless template)
3. The wide funnel: skills map first, then the requirement audit
   (proxies, degree inflation, jargon walls) and the plain-language pass
4. Structure before candidates: the structure dividend, anchored 1-to-5
   scoring, and the before-candidates rule that keeps it fair and green
5. The Hiring Lab: fill an open analyst role moment by moment, with the
   chatbot screen wired as the one unrecoverable choice
6. Bias, watched: the three bias doors (inherited stereotypes,
   culture-coded anchors, the fit laundromat) and the four guardrails

Ends with a scored recap, the **Hiring Structure Card capstone** (one
talent decision, one structural first move, one named temptation, one
date, plus the red-line pledge), a flip-card glossary, and a commitment
close. `worksheet.html` mirrors the capstone on paper; `cheatsheet.html`
is built to sit next to the keyboard during the structure session.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| The line | **Guess the number** | Call four AI-in-hiring findings before the reveal; missed guesses stick |
| The red side | **Over the line?** | Classify five hiring uses of AI: red never, yellow approved tools, green go |
| The funnel | **Fix the posting** | Diagnose five posting lines: proxy, jargon wall, degree inflation, or fine |
| The structure | **Structure plan builder** | Privately build a role's question seeds, probe, and rubric skeleton |
| The lab | **The Hiring Lab** | Choose the posting, screen, interviews, and decision, then run the hire |
| Bias | **Spot the bias door** | Find the open door in five legitimate-looking setups |
| Recap | **Scored quiz** | 6 questions mapped to the sections |
| Capstone | **My Structure Card** | Build and copy a dated, private hiring commitment |

## Instructional design

- **Bloom's ladder:** objectives run Classify → Use/Apply →
  Build (rubric) → Run (skills map) → Recognize/Evaluate (bias).
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 structure card + 7-day pulse + 30-day re-poll (templates on the
  facilitator briefing slide). The headline L3 metric: first moves
  actually made (audits run, rubrics built, maps done, piles pulled
  out of AI).
- **Adult learning:** learners bring one live talent decision
  (pre-work), every exercise runs on their own material held privately,
  and the capstone ships as a dated 30-minute structure session.
- **Privacy by design:** roles and processes, never names; the builder
  and structure card state explicitly that nothing is saved or
  transmitted. The course practices the discipline it teaches.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (gnGame, olGame, fpGame, sbGame)
- Structure builder: `structPlan` block · Hiring Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: SHRM AI research (roughly 1 in 4
  organizations using AI for HR, recruiting leading), the Amazon 2018
  scrapped screener (Reuters reporting; the "women's" penalty), NYC
  Local Law 144 (bias audit + candidate notice), Stanford AI Index
  (AI regulations rising sharply). The traffic light must match
  AI Basics and AI 201 exactly, and the red line must never soften.
