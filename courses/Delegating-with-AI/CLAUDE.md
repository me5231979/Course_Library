# Delegating, Rethought · Vanderbilt Learning Series

Single-page interactive classroom experience (Learning on Demand). Lives
inside the Course_Library repo at
https://me5231979.github.io/Course_Library/courses/Delegating-with-AI/

Sister programs: AI_Classroom (Start Smarter), AI-Advanced (AI 201),
Difficult_Conversations, Coaching-for-Performance, Emotional-Intelligence,
Workflow (Workflow & Process Redesign); catalog at me5231979/Course_Library.
Same engine, same standing principles.

## Standing design principles (do not regress these)

1. **Simulators, practice, and play throughout.** Every teaching section
   has an interaction; the Routing Lab is the signature piece, Guess the
   Pattern is the evidence-opener, and the role-math sketch feeds the
   capstone.
2. **A reason and facilitation behind every activity.** Learner-visible
   "Why this matters" lines; activities labeled As a group / On your own
   with steps, timings, and solo variants.
3. **Every section facilitatable, learning validatable.** ATD runbook in
   `facilitator/notes.json`. Kirkpatrick: L1 fist-to-five, L2 recap mapped
   to objectives, L3 routing card + 7-day pulse + 30-day re-poll; the
   headline L3 metric is handoff conversations actually held.
4. **Facilitator edition is generated, never hand-edited.** Run
   `python3 tools/build-facilitator.py` after ANY change to index.html or
   notes.json. Its QR encodes the LEARNER url.
5. **Privacy by design: this course runs on real tasks and roles.**
   Tasks and roles, never people's names; the role-math sketch and routing
   card are private (nothing saved or sent) and must SAY so in
   learner-visible copy. Never add telemetry, storage, or sharing to the
   personal exercises.
6. **The traffic light is shared with the AI courses and never
   contradicted:** green = public or generic, yellow = internal, approved
   VU tools only, red = private information about people, never. The light
   outranks the Routing Test in all copy.
7. **Stay tool-agnostic.** The course teaches the routing decision, never
   a product. No tool names, no vendor pitches; capability claims carry
   cited, linked sources (Gallup workplace AI research; Stanford GSB
   insights for the redesign framing).
8. **Brand: Vanderbilt FLH system.** Black #1C1C1C / white / flat gold
   #CFAE70; Libre Caslon Display headlines (one italic word), Inter body,
   Antonio eyebrows; motion at or under 400ms; real VU lockups (authorized
   use only).
9. **No frameworks.** One CSS file, one JS file, vendored QR lib,
   self-hosted fonts; the hero uses the gold particle canvas (no video).

## Layout (14 slides)

Welcome/QR (privacy norm) then Hero (5 objectives) then Agenda then
01 The new triage (Guess the Pattern) then manifesto ("Every task you
route is a lesson you give or take away.") then 02 The Routing Test
(Route the Task + traffic light) then 03 Stretch vs grunt (Stretch or
Grunt) then 04 Role math (quick check + private role-math sketch) then
05 The Routing Lab (graded 4-task quarter) then 06 The handoff (quick
check + Judge the Handoff) then Recap quiz then Capstone Routing Card
then Glossary then Closing (footer lives inside the closing slide).

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (patGuess, routeTask, stretchGrunt,
  handoffJudge)
- Role-math builder: `roleMath` block · Routing Lab: `SLOTS` + reaction
  tiers
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup (about 40% use AI at work a few times
  a year or more, nearly doubled in two years; about 8% daily; about 22%
  say their org communicated a clear AI plan), Stanford GSB (leaders
  redesign roles and processes rather than simply oversee execution).
  No invented statistics. The traffic light must match Start Smarter and
  AI 201 exactly.
