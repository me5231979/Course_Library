# AI Guardrails & Responsible Use · The Four Lines

An interactive, single-page teaching site on the governance session every
team needs before AI use scales: the Four Lines, a one-page working
agreement covering (1) what data goes into which tools, (2) when a human
verifies before an output travels, (3) when readers are told AI helped,
and (4) who owns the output. A **Learning on Demand** program: the
facilitator projects it while learners scan a QR code and work every
exercise on their own devices, or share the link for self-paced review.
Private by design: every exercise runs on tools and situations (never
people's names) and nothing typed is saved or sent anywhere.

Part of the Vanderbilt Learning Series (CHART Program). Catalog:
[Course Library](https://me5231979.github.io/Course_Library/) ·
Builds on: [AI Basics](https://me5231979.github.io/AI_Classroom/),
which taught the traffic light this course assumes.

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/AI-Guardrails/
- **Self-paced edition:** https://me5231979.github.io/Course_Library/courses/AI-Guardrails/web/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/AI-Guardrails/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8000
```

## What it teaches (6 sections)

1. Why written rules: Stanford's AI Index counts AI misuse incidents
   nearly doubling year over year; written lines versus vibes
2. Line one, what goes in: the traffic light with its hard cases
   (student work, meeting notes naming colleagues, letters about people)
3. Line two, when a human verifies: checks sized to blast radius, from
   no check to the full source check
4. Line three, when we disclose: the would-the-reader-feel-misled test
5. Line four, who owns it: the byline as a promise, plus the Guardrails
   Lab (write the four lines for a rollout and see month one)
6. Write your Four Lines: the one-page agreement drafted for the
   learner's own team

Ends with a scored recap, the **Four Lines Card capstone** (one team, one
first move, one named failure mode, one date), a flip-card glossary, and
a commitment close. `worksheet.html` is the printable team agreement;
`cheatsheet.html` is the one-page reference built to sit next to the
keyboard.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| Written rules | **Guess the number** | Call four findings on incidents, shadow AI, policy, and cost before the reveal |
| What goes in | **Green, yellow, or red** | Call the light on five hard cases beyond the poster examples |
| The check | **Size the check** | Triage five outputs: no check, quick read, or full source check |
| Disclosure | **Disclose or not** | Run the misled test on five scenarios, including a genuinely unclear one |
| Ownership | **The Guardrails Lab** | Write the four lines for a newsletter + FAQ rollout and run month one |
| The agreement | **Four Lines builder** | Privately draft lines one and two for their own team, pick a disclosure default |
| Recap | **Scored quiz** | 6 questions mapped to the objectives |
| Capstone | **My Four Lines Card** | Build and copy a dated, private rollout commitment |

## Instructional design

- **Bloom's ladder:** objectives run Explain, Classify, Decide,
  Assign, and Draft (Create).
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 the Four Lines card + 7-day pulse + 30-day re-poll (templates on
  the facilitator briefing slide). The headline L3 metric: team
  agreements actually drafted and given a home.
- **Adult learning:** learners bring their team's real outputs and data
  types (pre-work), every exercise runs on their own material held
  privately, and the capstone ships as a dated 20-minute team
  conversation.
- **Privacy by design:** tools and situations, never names; the builder
  and the capstone card state explicitly that nothing is saved or
  transmitted.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (gnGuess, tlSort, szCheck, dcCall)
- Four Lines builder: `flBuild` block · Guardrails Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: Stanford AI Index (incidents nearly doubling
  year over year, tracking adoption), Metaintro (AI policy as
  line-manager work, shadow AI framing). Round framings only; no precise
  numbers the sources do not carry. The traffic light must match
  AI Basics and AI 201 exactly: green public or generic, yellow internal
  in approved VU tools only (ChatGPT EDU, Amplify, Copilot), red private
  information about people, never.
- Publishing is handled by the Course_Library repo; this course ships as
  a self-contained folder under `courses/AI-Guardrails/`.
