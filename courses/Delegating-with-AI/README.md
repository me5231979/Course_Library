# Delegating, Rethought · Routing Work Without Hollowing Out Your Team

An interactive, single-page teaching site on the distinctly managerial
dilemma nobody trained managers for: the same task can now go to AI, to a
junior team member as a stretch assignment, or stay with you. The course
teaches the Routing Test (growth, judgment, volume, asked in that order),
the stretch-versus-grunt distinction, role math for redesigning roles as
AI absorbs the routine layer, and the handoff brief in both directions.
A **Learning on Demand** program: the facilitator projects it while
learners scan a QR code and work every exercise on their own devices, or
share the link for self-paced review. Private by design: every exercise
runs on tasks and roles (never names) and nothing typed is saved or sent
anywhere.

Part of the Vanderbilt Learning Series (CHART Program) and the Manager
Voyage program. Catalog:
[Course Library](https://me5231979.github.io/Course_Library/)

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/Delegating-with-AI/
- **Self-paced edition:** https://me5231979.github.io/Course_Library/courses/Delegating-with-AI/web/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/Delegating-with-AI/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8000
```

## What it teaches (6 sections)

1. The new triage: every task has three destinations (AI, a person as
   stretch, keep it), and both easy defaults fail (Gallup adoption data,
   Stanford GSB's redesign framing)
2. The Routing Test: growth, judgment, volume, in an order that matters,
   bounded by the shared AI traffic light (green / yellow / red)
3. Stretch vs grunt: hard because it is new versus hard because it is
   long, and the trap of yesterday's apprenticeship becoming today's AI
   lane
4. Role math: as the routine layer drains, name what backfills (judgment
   reps, client contact, verification ownership) and have the conversation
5. The Routing Lab: route four real tasks (data pull, kickoff deck,
   process documentation, partner escalation) and see the team at quarter
   end
6. The handoff: briefing a person (outcome, context, checkpoints,
   productive struggle) and briefing AI (draft assignment plus named
   verifier); either way, you own what ships

Ends with a scored recap, the **Routing Card capstone** (one task, one
destination, one named failure mode, one dated handoff conversation), a
flip-card glossary, and a commitment close. `worksheet.html` mirrors the
capstone on paper; `cheatsheet.html` is built to sit next to a task list.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| The triage | **Guess the pattern** | Call four Gallup and Stanford GSB findings before the reveal |
| The Routing Test | **Route the task** | Route five real tasks: AI, stretch, or keep |
| Stretch vs grunt | **Stretch or grunt** | Call five tasks through a junior's eyes |
| Role math | **Role-math sketch** | Privately sketch one role: what AI absorbs, what backfills, the conversation |
| The lab | **The Routing Lab** | Route a quarter's four tasks and see the team at quarter end |
| The handoff | **Judge the handoff** | Call five delegation briefs: complete, dumped, or micromanaged |
| Recap | **Scored quiz** | 6 questions mapped to the objectives |
| Capstone | **My Routing Card** | Build and copy a dated, private routing commitment |

## Instructional design

- **Bloom's ladder:** objectives run Apply (the test) → Distinguish
  (stretch vs grunt) → Protect (the pipeline) → Redesign (role math) →
  Brief (the handoff, Create-level synthesis).
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 routing card + 7-day pulse + 30-day re-poll (templates on the
  facilitator briefing slide). The headline L3 metric: handoff
  conversations actually held.
- **Adult learning:** learners bring one real task they have been holding
  (pre-work), every exercise runs on their own material held privately,
  and the capstone ships as a dated 15-minute handoff conversation.
- **Privacy by design:** tasks and roles, never names; the role-math
  sketch and routing card state explicitly that nothing is saved or
  transmitted.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (patGuess, routeTask, stretchGrunt,
  handoffJudge)
- Role-math builder: `roleMath` block · Routing Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup workplace AI research (about 40% use
  AI at least a few times a year, roughly doubled in two years; about 8%
  daily; about 22% say their org has a clear AI plan), Stanford GSB
  insights (leaders redesign roles and processes rather than simply
  oversee execution). The traffic light must match Start Smarter and AI 201.
- Sister course for the AI lane's mechanics: Workflow & Process Redesign
  (draft, verify, decide), linked once from section 06.
