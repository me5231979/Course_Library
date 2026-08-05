# Trust, Then Verify · Vanderbilt Learning Series

Single-page interactive classroom experience (Learning on Demand). Live at
https://me5231979.github.io/Course_Library/courses/Trust-Then-Verify/


Sister programs: AI_Classroom (Start Smarter), AI-Advanced (AI 201),
Difficult_Conversations, Coaching-for-Performance, Emotional-Intelligence,
Workflow; catalog at me5231979/Course_Library. Same engine, same standing
principles.

## Standing design principles (do not regress these)

1. **Simulators, practice, and play throughout.** Every teaching section
   has an interaction; the Verification Lab is the signature piece, Guess
   the Number is the skeptic-converter, and the ritual builder converts
   the method into a personal habit.
2. **A reason and facilitation behind every activity.** Learner-visible
   "Why this matters" lines; activities labeled As a group / On your own
   with steps, timings, and solo variants.
3. **Every section facilitatable, learning validatable.** ATD runbook in
   `facilitator/notes.json`. Kirkpatrick: L1 fist-to-five, L2 recap mapped
   to objectives, L3 verification card + 7-day pulse + 30-day re-poll; the
   headline L3 metric is first verified outputs actually shipped.
4. **Facilitator edition is generated, never hand-edited.** Run
   `python3 tools/build-facilitator.py` after ANY change to index.html or
   notes.json. Its QR encodes the LEARNER url.
5. **Privacy by design: this course runs on real AI outputs.** Outputs
   and tasks, never private information about people; the ritual builder
   and verification card are private (nothing saved or sent) and must SAY
   so in learner-visible copy. Never add telemetry, storage, or sharing
   to the personal exercises.
6. **The traffic light is shared with the AI courses and never
   contradicted:** green = public or generic, yellow = internal, approved
   VU tools only, red = private information about people, never. The
   light outranks the verification budget and every read in all copy.
7. **Stay tool-agnostic.** The course teaches the checking discipline,
   not any product. No tool names, no vendor pitches; capability claims
   carry cited, linked sources (SHRM workplace AI research; Stanford AI
   Index; automation-bias framing without invented statistics).
8. **Brand: Vanderbilt FLH system.** Black #1C1C1C / white / flat gold
   #CFAE70; Libre Caslon Display headlines (one italic word), Inter body,
   Antonio eyebrows; motion 400ms or less; real VU lockups (authorized
   use only).
9. **No frameworks.** One CSS file, one JS file, vendored QR lib,
   self-hosted fonts; the hero uses the gold particle canvas (no video).

## Layout (14 slides)

Welcome/QR (privacy norm), Hero (5 objectives), Agenda,
01 The cost of belief (Guess the Number), manifesto ("The most expensive
sentence in AI is 'looks right to me.'"), 02 Know the failure modes
(Name the Failure), 03 The Three Reads (worked example + Find the Fault
Line), 04 Size the check (budget + stop rules + traffic light + Check,
Ship, or Stop), 05 The Verification Lab (graded 4-move briefing rescue),
06 Make it a habit (ritual builder), Recap quiz, Capstone Verification
Card, Glossary, Closing (footer lives inside the closing slide).

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (statGuess, modeName, faultLine,
  shipCheck)
- Ritual builder: `ritualBuild` block · Verification Lab: `SLOTS` +
  reaction tiers
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: SHRM (around 4 hours a week fixing AI
  output), Stanford AI Index (incident counts at record highs),
  automation bias (framing only, no invented statistics). Zero em or en
  dashes anywhere, including generated files.
