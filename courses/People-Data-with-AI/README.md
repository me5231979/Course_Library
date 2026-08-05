# People Data, Safely · Read the Patterns, Coach the Person

An interactive, single-page teaching site on the data side of coaching:
using AI to interpret engagement results, spot themes across your own
1:1 notes, and prepare better feedback and reviews, inside hard privacy
lines (the Aggregate Rule and the Coach's Loop). A **Learning on Demand**
program: the facilitator projects it while learners scan a QR code and
work every exercise on their own devices, or share the link for
self-paced review. Private by design: every exercise runs on patterns and
roles (never names) and nothing typed is saved or sent anywhere.

Part of the Vanderbilt Learning Series and the Manager Voyage program.
Catalog: [Course Library](https://me5231979.github.io/Course_Library/) ·
Sister program: Coaching for Performance (the human method this course feeds)

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/People-Data-with-AI/
- **Self-paced edition:** https://me5231979.github.io/Course_Library/courses/People-Data-with-AI/web/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/People-Data-with-AI/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8106
```

## What it teaches (6 sections)

1. The new expectation: the HR-tech wave (Culture Amp's AI Coach, Lattice,
   15Five), Gallup's manager-effect research, and the gap where survey
   results change nothing
2. The Aggregate Rule: the shared AI traffic light applied to people data,
   including the small-team trap (small-n aggregates stay red)
3. Themes from the noise: the three interrogation questions (themes,
   contrasts, the question behind the question) and the ground truth test
4. Feedback, rehearsed: AI as rehearsal partner (roles, never names; SBI
   and feedforward); the verdict stays the manager's
5. The Review Prep Lab: run review season for a team of eight across four
   stages and see which cycle results: fair, or the grievance
6. From data to conversation: the share-back, the 1:1 question bank, and
   measuring conversations instead of dashboard views

Ends with a scored recap, the **People-Data Card capstone** (one source,
one first move, one line never crossed, one date), a flip-card glossary,
and a commitment close. `worksheet.html` mirrors the capstone on paper;
`cheatsheet.html` is built to sit next to the keyboard during the
theme-to-conversation session.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| The expectation | **Guess the number** | Call four Gallup findings before the reveal; missed guesses stick |
| The rule | **Red, yellow, or green** | Give five people-data cases their light, traps included |
| The themes | **Interrogation plan builder** | Privately turn their own signal, suspicion, and mystery into three AI questions plus the humanize test |
| The rehearsal | **Judge the draft** | Call five AI-assisted feedback lines: specific and owned, generic mush, or crosses the line |
| The lab | **The Review Prep Lab** | Choose four review-season stages and run the cycle two weeks forward |
| The conversation | **Judge the share-back** | Call five ways of presenting survey themes to a team |
| Recap | **Scored quiz** | 6 questions mapped to the objectives |
| Capstone | **My People-Data Card** | Build and copy a dated, private people-data commitment |

## Instructional design

- **Bloom's ladder:** objectives run Apply (the rule) → Use/Analyze
  (interrogation) → Draft (rehearsal) → Prepare/Evaluate (review cycle) →
  Run/Create (the conversation and the card).
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 people-data card + 7-day pulse + 30-day re-poll (templates on the
  facilitator briefing slide). The headline L3 metric: theme-to-conversation
  sessions actually held.
- **Adult learning:** learners bring one real people-data source
  (pre-work), every exercise runs on their own material held privately,
  and the capstone ships as a dated 45-minute working session.
- **Privacy by design:** patterns and roles, never names; the builder and
  people-data card state explicitly that nothing is saved or transmitted.
  The Aggregate Rule outranks every technique taught.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (gnGame, tlSort, draftJudge, shareJudge)
- Interrogation builder: `intPlan` block · Review Prep Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup workplace research (manager effect
  ~70% of engagement variance, ~1 in 5 engaged globally, ~1 in 3 US
  employees using AI at work, ~a fifth report a clear org AI plan),
  Culture Amp / Lattice / 15Five (the AI-coach tooling wave, framing
  only). The traffic light must match Start Smarter and AI 201 exactly:
  green public/generic, yellow internal in approved VU tools only, red
  private information about people, never.
