# Numbers, Faster · Vanderbilt Learning Series

Single-page interactive classroom experience (Learning on Demand) on data
and analysis with AI. Published inside the Course_Library repo at
https://me5231979.github.io/Course_Library/courses/Numbers-Faster/.

Sister programs: AI_Classroom (AI Basics), AI-Advanced (AI 201), and the
research sibling "Answers, Faster" (ask-anchor-check); catalog at
me5231979/Course_Library. Same engine, same standing principles.

## Standing design principles (do not regress these)

1. **Simulators, practice, and play throughout.** Every teaching section
   has an interaction; the Analysis Lab is the signature piece, Guess the
   Number is the skeptic-converter, and the private Data Loop starter
   feeds the lab and the capstone.
2. **A reason and facilitation behind every activity.** Learner-visible
   "Why this matters" lines; activities labeled As a group / On your own
   with steps, timings, and solo variants.
3. **Every section facilitatable, learning validatable.** ATD runbook in
   `facilitator/notes.json`. Kirkpatrick: L1 fist-to-five, L2 recap mapped
   to objectives, L3 Data Loop card + 7-day pulse + 30-day re-poll; the
   headline L3 metric is first runs actually completed.
4. **Facilitator edition is generated, never hand-edited.** Run
   `python3 tools/build-facilitator.py` after ANY change to index.html or
   notes.json. Its QR encodes the LEARNER url.
5. **Privacy by design: this course runs on real datasets.** Datasets and
   columns, never names or personal records; the starter and Data Loop
   card are private (nothing saved or sent) and must SAY so in
   learner-visible copy. Never add telemetry, storage, or sharing to the
   personal exercises.
6. **The traffic light is shared with the AI courses and never
   contradicted:** green = public or generic, yellow = internal, approved
   VU tools only (ChatGPT EDU, Amplify, Copilot), red = private
   information about people, never. For data files the light outranks the
   Data Loop in all copy, and de-identification is the taught bridge from
   red to yellow.
7. **Stay tool-agnostic beyond the approved-tools list.** The course
   teaches the loop, not a product. Capability claims carry cited, linked
   sources (Gallup workplace AI research; SHRM on AI at work).
8. **Brand: Vanderbilt FLH system.** Black #1C1C1C / white / flat gold
   #CFAE70; Libre Caslon Display headlines (one italic word), Inter body,
   Antonio eyebrows; motion at or under 400ms; real VU lockups only.
9. **No frameworks.** One CSS file, one JS file, vendored QR lib,
   self-hosted fonts; the hero uses the gold particle canvas (no video).
10. **Zero em or en dashes anywhere**, including JS strings, JSON, and
    markdown. Rewrite around them.

## Layout (14 slides)

Welcome/QR (privacy norm), Hero (5 objectives), Agenda,
01 The case for AI on numbers (Guess the Number), manifesto ("A number
you haven't checked is a rumor with decimals."), 02 Safe data in (traffic
light trainer + de-identification), 03 Ask the sheet (describe + ladder +
private Data Loop starter), 04 Check the math (Catch the Error + the
check ritual), 05 The Analysis Lab (graded 4-step month-end), 06 Tell the
story (Judge the Finding + chart briefs), Recap quiz, Capstone Data Loop
Card, Glossary, Closing (footer lives inside the closing slide).

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (statGuess, lightSort, errSpot, findJudge)
- Data Loop starter: `dlMap` block · Analysis Lab: `SLOTS` + reaction tiers
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Gallup workplace AI research (about 3 in 4
  employees using AI on data work report clear gains, frequent-user gap,
  data work near the top of use cases by payoff, most work still manual),
  SHRM (about 4 hours a week fixing AI output). No invented statistics.
