# Admin, Automated · Vanderbilt Learning Series

Single-page interactive classroom experience (Learning on Demand). Lives
inside the Course_Library repo, served at
https://me5231979.github.io/Course_Library/courses/Admin-Automated/


Sister programs: AI_Classroom (AI Basics), AI-Advanced (AI 201),
Difficult_Conversations, Coaching-for-Performance, Emotional-Intelligence;
catalog at me5231979/Course_Library. Same engine, same standing principles.

## Standing design principles (do not regress these)

1. **Simulators, practice, and play throughout.** Every teaching section
   has an interaction; the Automation Lab is the signature piece, Guess the
   Number is the skeptic-converter, and the private recurrence inventory
   feeds every later section.
2. **A reason and facilitation behind every activity.** Learner-visible
   "Why this matters" lines; activities labeled As a group / On your own
   with steps, timings, and solo variants.
3. **Every section facilitatable, learning validatable.** ATD runbook in
   `facilitator/notes.json`. Kirkpatrick: L1 fist-to-five, L2 recap mapped
   to objectives, L3 automation card + 7-day pulse + 30-day re-poll; the
   headline L3 metric is build sessions actually held.
4. **Facilitator edition is generated, never hand-edited.** Run
   `python3 tools/build-facilitator.py` after ANY change to index.html or
   notes.json. Its QR encodes the LEARNER url.
5. **Privacy by design: this course runs on the learner's real tasks.**
   Their own tasks and templates, never other people's names; the
   inventory and automation card are private (nothing saved or sent) and
   must SAY so in learner-visible copy. Never add telemetry, storage, or
   sharing to the personal exercises.
6. **The traffic light is shared with the AI courses and never
   contradicted:** green = public or generic, yellow = internal, approved
   VU tools only, red = private information about people, never. The light
   outranks every automation technique in all copy, and names baked into
   templates are called out as red flags.
7. **Stay tool-agnostic.** The course teaches the Repeat Audit, not any
   product. No vendor pitches; capability claims carry cited, linked
   sources (Gallup workplace AI research for the ~77 percent payoff
   finding; Leadership Circle for the evaporation warning).
8. **Brand: Vanderbilt FLH system.** Black #1C1C1C / white / flat gold
   #CFAE70; Libre Caslon Display headlines (one italic word), Inter body,
   Antonio eyebrows; motion at or under 400ms; real VU lockups only.
9. **No frameworks.** One CSS file, one JS file, vendored QR lib,
   self-hosted fonts; the hero uses the gold particle canvas (no video).

## Layout (14 slides)

Welcome/QR (privacy norm) then Hero (5 objectives) then Agenda then
01 The repeat tax (Guess the Number) then manifesto ("Anything you have
typed three times is a template you have not met yet.") then 02 Spot it
(three tells + traffic light + private inventory) then 03 Template it
(hygiene rules + Judge the Template) then 04 Route it (three piles +
calendar rules + Triage the Inbox) then 05 The Automation Lab (graded
4-step rebuild) then 06 Retire it and bank it (safe test + Keep, Shrink,
or Retire) then Recap quiz then Capstone Automation Card then Glossary
then Closing (footer lives inside the closing slide).

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (rtGuess, tplJudge, triSort, ksrSort)
- Recurrence inventory: `raBuild` block · Automation Lab: `SLOTS` +
  reaction tiers
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup workplace AI research (automating
  repetitive tasks as the highest-payoff use case, around 77 percent
  reporting clear productivity gains), Leadership Circle (evaporation
  framing only, no invented statistics).
