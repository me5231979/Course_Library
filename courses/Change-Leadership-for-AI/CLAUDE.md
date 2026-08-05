# Change Leadership for AI · Vanderbilt Learning Series

Single-page interactive classroom experience (Learning on Demand).
Published inside the Course_Library repo at
https://me5231979.github.io/Course_Library/courses/Change-Leadership-for-AI/

Sister programs: AI_Classroom (AI Basics), AI-Advanced (AI 201), Workflow
(Workflow & Process Redesign), Difficult_Conversations,
Coaching-for-Performance, Emotional-Intelligence; catalog at
me5231979/Course_Library. Same engine, same standing principles.

## Standing design principles (do not regress these)

1. **Simulators, practice, and play throughout.** Every teaching section
   has an interaction; the Change Lab is the signature piece, Guess the
   Number is the skeptic-converter, and the private conversation-plan
   builder feeds the capstone.
2. **A reason and facilitation behind every activity.** Learner-visible
   "Why this matters" lines; activities labeled As a group / On your own
   with steps, timings, and solo variants.
3. **Every section facilitatable, learning validatable.** ATD runbook in
   `facilitator/notes.json`. Kirkpatrick: L1 fist-to-five, L2 recap mapped
   to objectives, L3 change card + 7-day pulse + 30-day re-poll; the
   headline L3 metric is naming conversations actually held.
4. **Facilitator edition is generated, never hand-edited.** Run
   `python3 tools/build-facilitator.py` after ANY change to index.html or
   notes.json. Its QR encodes the LEARNER url.
5. **Privacy by design; this course runs on real team situations.**
   Situations and roles, never people's names; the builder and change card
   are private (nothing saved or sent) and must SAY so in learner-visible
   copy. Never add telemetry, storage, or sharing to the personal
   exercises.
6. **The traffic light is shared with the AI courses and never
   contradicted:** green = public or generic, yellow = internal, approved
   VU tools only, red = private information about people, never. The light
   outranks every technique in this course, including in the ethics
   section it anchors.
7. **Stay tool-agnostic.** The course teaches change leadership, not any
   product. No tool names, no vendor pitches; capability claims carry
   cited, linked sources (Accenture for the 18 percent and curiosity,
   courage, connection; Gallup for the communication and trust findings).
8. **Brand: Vanderbilt FLH system.** Black #1C1C1C / white / flat gold
   #CFAE70; Libre Caslon Display headlines (one italic word), Inter body,
   Antonio eyebrows; motion at 400ms or less; real VU lockups (authorized
   use only).
9. **No frameworks.** One CSS file, one JS file, vendored QR lib,
   self-hosted fonts; the hero uses the gold particle canvas (no video).
10. **Zero em or en dashes anywhere**, including JS strings, JSON, and
   markdown. Rewrite around them.

## Layout (14 slides)

Welcome/QR (privacy norm), Hero (5 objectives), Agenda,
01 Why AI change fails (Guess the Number), manifesto ("People don't resist
change. They resist being changed."), 02 Name the fear (opening-line
trainer + method cards + honesty rules), 03 Safety to stumble (Read the
Room trainer), 04 The ethics conversation (traffic light + private
conversation-plan builder), 05 The Change Lab (graded 4-moment rollout),
06 Hold for the long arc (long-arc trainer + quick check), Recap quiz,
Capstone Change Card, Glossary, Closing (footer lives inside the closing
slide).

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (gapGuess, lineJudge, roomRead, arcMove)
- Builder: `convoPlan` block · Change Lab: `SLOTS` + reaction tiers
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Accenture (around 18 percent lead AI
  investments effectively; curiosity, courage, connection as the
  differentiators), Gallup (around 15 percent report a clear communicated
  AI plan; under a quarter strongly trust leadership). No invented
  statistics; psychological-safety material is framing only.
