# Making It Normal · Teams Adopt Behavior, Not Tools

An interactive, single-page teaching site on the leadership side of team AI
adoption: Gallup's research says a team's AI use follows the manager's
visible behavior and the presence of AI in real workflows, so this course
teaches the Show, Say, Set, Sustain method: model AI use out loud (misses
included), give explicit permission and limits, install norms into the 1:1s
and team meetings that already exist, and keep adoption alive past the
month-three novelty cliff. A **Learning on Demand** program: the facilitator
projects it while learners scan a QR code and work every exercise on their
own devices, or share the link for self-paced review. Private by design:
every exercise runs on roles and rituals (never names) and nothing typed is
saved or sent anywhere.

Part of the Vanderbilt Learning Series and the Manager Voyage program.
Catalog: [Course Library](https://me5231979.github.io/Course_Library/) ·
Mechanics companion:
[Workflow & Process Redesign](https://me5231979.github.io/Workflow/)
(that course redesigns the work; this one leads the people).

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/Leading-AI-Adoption/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/Leading-AI-Adoption/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8000
```

## What it teaches (6 sections)

1. The modeling effect: Gallup's numbers (~40% of employees use AI, 19%
   frequently, only 22% have heard a clear plan, 4.7x comfort with clear
   leadership) and the permission gap
2. Show: model out loud: narrated use (prompt, draft, fix), modeling the
   check rather than the speed, admitting misses so imperfect use is safe
3. Say: permission and limits: the encouraged list, the never list (the
   shared AI traffic light restated), and the gray-zone routing
4. Set: norms in the rituals: the 1:1 question, the share-one round, the
   no-blame miss log, the enthusiast-skeptic pairing, psychological safety
5. The Adoption Lab: lead a six-person team through ninety days and see
   what your visibility, permission, ritual, and skeptic choices produce
6. Sustain past the novelty cliff: protected learning time, celebrated
   catches, and reporting stories instead of leaderboards

Ends with a scored recap, the **Adoption Plan capstone** (one team, one
first move, one refused failure mode, one date), a flip-card glossary, and
a commitment close. `worksheet.html` mirrors the capstone on paper;
`cheatsheet.html` is built to sit next to your 1:1 notes.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| The Effect | **Guess the number** | Call four Gallup findings before the reveal; missed guesses stick |
| Show | **Judge the model** | Call five manager behaviors: real modeling, nothing to copy, or speed without the check |
| Say | **Permission talk builder** | Privately draft the encouraged line, the never line, and the gray-zone answer |
| Set | **Fix the ritual** | Diagnose five team-ritual setups: safety, cadence, enthusiast-only, or working |
| The Lab | **The Adoption Lab** | Make four leadership choices and run ninety simulated days |
| Sustain | **Month-three moves** | Pick the sustaining move for four novelty-cliff dip scenarios |
| Recap | **Scored quiz** | 6 questions mapped to the objectives |
| Capstone | **My Adoption Plan** | Build and copy a dated, private adoption commitment |

## Instructional design

- **Bloom's ladder:** objectives run Explain (evidence), Model (Apply),
  Give permission (Apply), Install (Apply/Analyze), Sustain
  (Evaluate/Create), landing in the built plan (Create).
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 adoption plan + 7-day pulse + 30-day re-poll (templates on the
  facilitator briefing slide). The headline L3 metric: first moves
  actually made within 7 days.
- **Adult learning:** every exercise runs on the learner's real team held
  privately, and the capstone ships as a dated first move inside a meeting
  that already exists.
- **Privacy by design:** roles and rituals, never names; the builder and
  plan state explicitly that nothing is saved or transmitted.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (gallupGuess, judgeModel, fixRitual,
  monthMoves)
- Permission talk builder: `ptBuild` block · Adoption Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup workplace AI research (~40% use, 19%
  frequent, 22% clear plan, 4.7x comfort). The traffic light must match
  Start Smarter and AI 201 exactly: green public, yellow internal in approved
  VU tools only, red private information about people, never.
- This build ships inside Course_Library; the orchestrator publishes it.
