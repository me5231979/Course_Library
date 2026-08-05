# Change Leadership for AI · Naming Fear, Building Safety, Leading the Conversation

An interactive, single-page teaching site on the human side of AI change:
naming the fear in the room, answering the job-security question honestly,
building psychological safety around experimenting, hosting the team's own
ethics conversation, and holding the change steady over months (the Name,
Frame, Invite, Hold method). A **Learning on Demand** program: the
facilitator projects it while learners scan a QR code and work every
exercise on their own devices, or share the link for self-paced review.
Private by design: every exercise runs on situations and roles (never
names) and nothing typed is saved or sent anywhere.

Part of the Vanderbilt Learning Series and the Manager Voyage program.
Catalog: [Course Library](https://me5231979.github.io/Course_Library/) ·
Sibling programs: Workflow & Process Redesign (the mechanics of where AI
fits the work) and Leading AI Adoption (modeling the behavior yourself);
this course is the human-change layer between them.

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/Change-Leadership-for-AI/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/Change-Leadership-for-AI/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8110
```

## What it teaches (6 sections)

1. Why AI change fails: the Accenture finding (only around 18 percent of
   leaders lead AI investments effectively) and the pattern: change
   announced as technology, experienced as threat; curiosity, courage,
   and connection as the differentiators
2. Name the fear: the unsaid question ("am I being automated?"), the
   naming move with scripts, and the honesty rules (never promise no
   change; promise how change is handled)
3. Safety to stumble: psychological safety applied to AI adoption: public
   experiments, no-blame misses, the leader going first, and why the
   anxious quiet ones decide whether change sticks
4. The ethics conversation: hosting rather than outsourcing, disagreement
   as material, escalation to policy owners, the traffic light as the
   floor, and a private conversation-plan builder
5. The Change Lab: six months of leading an AI rollout in four decisive
   moments, with month-six outcomes from team ownership to compliance
   theater over quiet dread
6. Hold for the long arc: the revisit cadence, the quiet signals, courage
   as a habit, connection as the multiplier, and measuring trust alongside
   usage

Ends with a scored recap, the **Change Card capstone** (one change, one
first conversation, one named failure mode, one date), a flip-card
glossary, and a commitment close. `worksheet.html` mirrors the capstone on
paper; `cheatsheet.html` carries the method, the naming scripts, and the
honest job answer.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| Why it fails | **Guess the number** | Call four findings (Accenture, Gallup) before the reveal; missed guesses stick |
| Name the fear | **Judge the opening line** | Call five manager lines: honest naming, happy talk, or a threat in disguise |
| Safety | **Read the room** | Pick the safety-building response to five rollout moments |
| Ethics | **Conversation plan builder** | Privately build the naming line, frame, invitation, and first ethics agenda |
| The lab | **The Change Lab** | Lead six months of an AI rollout through four forks and read month six |
| Long arc | **The long-arc move** | Pick the sustaining move in five months-later scenarios |
| Recap | **Scored quiz** | 6 questions mapped to the objectives |
| Capstone | **My Change Card** | Build and copy a dated, private change-leadership commitment |

## Instructional design

- **Bloom's ladder:** objectives run Explain (why change fails) to Name /
  Apply (the naming move) to Build (safety) to Facilitate (ethics) to
  Sustain / Create (the long arc and the capstone card).
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 change card + 7-day pulse + 30-day re-poll (templates on the
  facilitator briefing slide). The headline L3 metric: naming
  conversations actually held.
- **Adult learning:** learners bring one real AI change (pre-work), every
  exercise runs on their own situation held privately, and the capstone
  ships as a dated first conversation.
- **Privacy by design:** situations and roles, never names; the builder
  and change card state explicitly that nothing is saved or transmitted.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (gapGuess, lineJudge, roomRead, arcMove)
- Conversation-plan builder: `convoPlan` block · Change Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Accenture (around 18 percent of leaders lead
  AI investments effectively; curiosity, courage, connection), Gallup
  (around 15 percent say leadership communicated a clear AI plan; under a
  quarter strongly trust leadership). The traffic light must match AI
  Basics and AI 201 exactly, and it outranks every technique taught here.
- The orchestrator publishes this course inside the Course_Library repo;
  do not push it as its own Pages site.
