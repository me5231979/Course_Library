# AI Across Your Week · Vanderbilt Learning Series

Single-page interactive classroom experience (Learning on Demand). Published
inside the Course_Library repo at
https://me5231979.github.io/Course_Library/courses/AI-Across-Your-Week/

Sister programs: AI_Classroom (AI Basics), AI-Advanced (AI 201), the CHART
method courses (First Drafts, Answers, Minutes, Slides, Ideas, Decisions,
Numbers), Difficult_Conversations, Coaching-for-Performance,
Emotional-Intelligence; catalog at me5231979/Course_Library. Same engine,
same standing principles.

## Standing design principles (do not regress these)

1. **Simulators, practice, and play throughout.** Every teaching section
   has an interaction; the Week Lab is the signature piece, Guess the
   Number is the skeptic-converter, and the private inventory feeds every
   later section.
2. **A reason and facilitation behind every activity.** Learner-visible
   "Why this matters" lines; activities labeled As a group / On your own
   with steps, timings, and solo variants.
3. **Every section facilitatable, learning validatable.** ATD runbook in
   `facilitator/notes.json`. Kirkpatrick: L1 fist-to-five, L2 recap mapped
   to objectives, L3 Week Map + 7-day pulse + 30-day re-poll; the headline
   L3 metric is calendar passes actually run and distinct-use counts grown.
4. **Facilitator edition is generated, never hand-edited.** Run
   `python3 tools/build-facilitator.py` after ANY change to index.html or
   notes.json. Its QR encodes the LEARNER url.
5. **Privacy by design: this course runs on real calendars.** Blocks,
   roles, and workflows, never people's names; the inventory and Week Map
   are private (nothing saved or sent) and must SAY so in learner-visible
   copy. Never add telemetry, storage, or sharing to the personal
   exercises.
6. **The traffic light is shared with the AI courses and never
   contradicted:** green = public or generic, yellow = internal, approved
   VU tools only, red = private information about people, never. The light
   outranks the Week Map in all copy.
7. **Stay tool-agnostic.** The course teaches methods and the breadth
   habit, not any product. No tool names, no vendor pitches; capability
   claims carry cited, linked sources (Gallup workplace AI research for
   the breadth findings; Leadership Circle for the recovered-time framing,
   no invented statistics).
8. **Brand: Vanderbilt FLH system.** Black #1C1C1C / white / flat gold
   #CFAE70; Libre Caslon Display headlines (one italic word), Inter body,
   Antonio eyebrows; motion 400ms or less; real VU lockups (authorized use
   only).
9. **No frameworks.** One CSS file, one JS file, vendored QR lib,
   self-hosted fonts; the hero uses the gold particle canvas (no video).
10. **Zero em or en dashes anywhere**, including JS strings, JSON, and
    markdown. Rewrite around them.

## Layout (14 slides)

Welcome/QR (privacy norm), Hero (5 objectives), Agenda,
01 The breadth effect (Guess the Number), manifesto ("The gain is not in
the task. It is in the habit."), 02 The inventory (block cards + traffic
light + private inventory), 03 The method match (CHART toolbox + match
trainer), 04 The stack (chain cards + chain trainer), 05 The Week Lab
(graded 4-block week), 06 Bank the time (bank card + quick check + bank
trainer), Recap quiz, Capstone Week Map, Glossary, Closing (footer lives
inside the closing slide).

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (bgGuess, mmMatch, bcChain, jbBank)
- Week inventory: `wkInv` block · Week Lab: `SLOTS` + reaction tiers
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup workplace AI research (seven-plus
  distinct tasks roughly doubles reported gains versus one or two; most
  users parked at one or two uses; frequent users report gains far more
  often; gains concentrate among broad habitual users), Leadership Circle
  (recovered time refills with meetings unless deliberately banked;
  framing only). The traffic light must match AI Basics and AI 201.
