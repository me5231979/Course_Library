# People Data with AI · Vanderbilt Learning Series

Single-page interactive classroom experience (Learning on Demand). Lives
inside the Course_Library repo at
https://me5231979.github.io/Course_Library/courses/People-Data-with-AI/

Sister programs: AI_Classroom (AI Basics), AI-Advanced (AI 201),
Coaching-for-Performance (the human method this course feeds),
Difficult_Conversations, Emotional-Intelligence, Workflow; catalog at
me5231979/Course_Library. Same engine, same standing principles.

## Standing design principles (do not regress these)

1. **Simulators, practice, and play throughout.** Every teaching section
   has an interaction; the Review Prep Lab is the signature piece, Guess
   the Number is the skeptic-converter, and the private interrogation-plan
   builder feeds the capstone.
2. **A reason and facilitation behind every activity.** Learner-visible
   "Why this matters" lines; activities labeled As a group / On your own
   with steps, timings, and solo variants.
3. **Every section facilitatable, learning validatable.** ATD runbook in
   `facilitator/notes.json`. Kirkpatrick: L1 fist-to-five, L2 recap mapped
   to objectives, L3 people-data card + 7-day pulse + 30-day re-poll; the
   headline L3 metric is theme-to-conversation sessions actually held.
4. **Facilitator edition is generated, never hand-edited.** Run
   `python3 tools/build-facilitator.py` after ANY change to index.html or
   notes.json. Its QR encodes the LEARNER url.
5. **Privacy by design; this course runs on real people data.** Patterns
   and roles, never people's names; the builder and people-data card are
   private (nothing saved or sent) and must SAY so in learner-visible
   copy. Never add telemetry, storage, or sharing to personal exercises.
6. **The traffic light is shared with the AI courses and never
   contradicted:** green = public or generic, yellow = internal, approved
   VU tools only, red = private information about people, never. In this
   course it appears as the Aggregate Rule, and it outranks every
   technique taught, including all of sections 03 through 05.
7. **Stay honest on people data.** The small-n trap (under five
   respondents stays red), the ground truth test, and the verdict line
   (AI rehearses, the manager judges) are canon; capability claims carry
   cited, linked sources (Gallup workplace research; Culture Amp for the
   tooling wave, framing only).
8. **Brand: Vanderbilt FLH system.** Black #1C1C1C / white / flat gold
   #CFAE70; Libre Caslon Display headlines (one italic word), Inter body,
   Antonio eyebrows; motion 400ms or less; real VU lockups (authorized
   use only).
9. **No frameworks.** One CSS file, one JS file, vendored QR lib,
   self-hosted fonts; the hero uses the gold particle canvas (no video).

## Layout (14 slides)

Welcome/QR (privacy norm) then Hero (5 objectives) then Agenda, then
01 The new expectation (Guess the Number), the manifesto ("Data can find
the theme. Only you can have the conversation."), 02 The Aggregate Rule
(traffic-light trainer + small-n trap), 03 Themes from the noise (three
questions + private interrogation builder), 04 Feedback, rehearsed
(draft-judging trainer + rehearsal pattern), 05 The Review Prep Lab
(graded 4-stage cycle), 06 From data to conversation (share-back trainer
+ question bank), Recap quiz, Capstone People-Data Card, Glossary, and
the Closing (footer lives inside the closing slide).

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (gnGame, tlSort, draftJudge, shareJudge)
- Interrogation builder: `intPlan` block · Review Prep Lab: `SLOTS` +
  reaction tiers
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup (manager effect ~70% of engagement
  variance; ~1 in 5 engaged globally; ~1 in 3 US employees using AI at
  work; ~a fifth report a clear org AI plan), Culture Amp / Lattice /
  15Five (AI-coach wave, framing only, no invented statistics).
