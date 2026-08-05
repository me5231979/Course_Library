# Trust, Then Verify · Verifying AI Output and Critical Review

An interactive, single-page teaching site on the skill that decides whether
AI saves time or costs it: verifying AI output. Learners study how AI
errors actually look (fluent, specific, wrong), learn the five failure
modes and their tells, and install the Three Reads: the claim read
(underline every checkable claim), the source read (trace the riskiest
claims to a source you open), and the slant read (what is it assuming, who
is missing, what would the opposite case say). The check is sized to the
stakes, and three stop rules say when AI leaves a task entirely. A
**Learning on Demand** program: the facilitator projects it while learners
scan a QR code and work every exercise on their own devices, or share the
link for self-paced review. Private by design: exercises run on outputs
and tasks (never private information about people) and nothing typed is
saved or sent anywhere.

Part of the Vanderbilt Learning Series (CHART Program). Catalog:
[Course Library](https://me5231979.github.io/Course_Library/)

- **Learner edition:** https://me5231979.github.io/Course_Library/courses/Trust-Then-Verify/
- **Self-paced edition:** https://me5231979.github.io/Course_Library/courses/Trust-Then-Verify/web/
- **Facilitator edition:** https://me5231979.github.io/Course_Library/courses/Trust-Then-Verify/facilitator/

## Running it

Plain HTML/CSS/JS, no build step:

```bash
python3 -m http.server 8103
```

## What it teaches (6 sections)

1. The cost of belief: SHRM's finding that AI-using workers spend around
   4 hours a week fixing output, and why fluent errors fool smart readers
2. Know the failure modes: hallucination, staleness, slant, omission, and
   faked math, each with a one-line tell
3. The Three Reads: claim, source, slant, worked on a policy-summary
   example with an invented deadline, a stale figure, and a loaded frame
4. Size the check: verification budgets from no-check to human expert, the
   three stop rules, and the traffic light (which outranks every read)
5. The Verification Lab: an AI-drafted briefing for a dean, due in an
   hour, with an invented citation and a slanted paragraph inside it
6. Make it a habit: the 90-second daily version, the blame-free miss log,
   the "caught one" ritual, and bias review as a checklist question

Ends with a scored recap, the **Verification Card capstone** (one
recurring output, one first move, one line not to cross, one date), a
flip-card glossary, and a commitment close. `worksheet.html` is a
printable verification card for any single output; `cheatsheet.html` puts
the Three Reads, the failure-mode tells, and the stop rules on one page.

## The interactive tools

| Slide | Tool | What learners do |
|---|---|---|
| The cost | **Guess the number** | Call four findings on the cleanup tax before the reveal |
| Failure modes | **Name the failure** | Diagnose five real-looking outputs by their tells |
| Three Reads | **Find the fault line** | Pick which claim in each sentence gets checked first |
| Size the check | **Check, ship, or stop** | Size five situations: ship as is, run the reads, or stop |
| The lab | **The Verification Lab** | Handle the dean's briefing: checks, the unfindable citation, the slant, the sign-off |
| The habit | **Build your ritual** | Privately name the unchecked output, its worst miss, and the 90-second check |
| Recap | **Scored quiz** | 6 questions mapped to the objectives |
| Capstone | **My Verification Card** | Build and copy a dated, private verification commitment |

## Instructional design

- **Bloom's ladder:** objectives run Recognize (error texture) →
  Distinguish (failure modes) → Apply (the Three Reads) → Evaluate (size
  the check, stop rules) → Create/Commit (the ritual and the card).
- **Kirkpatrick:** L1 fist-to-five at close; L2 inline checks + recap;
  L3 verification card + 7-day pulse + 30-day re-poll (templates on the
  facilitator briefing slide). The headline L3 metric: first verified
  outputs actually shipped, with what the reads caught.
- **Adult learning:** learners bring one real AI output they use
  (pre-work), every exercise runs on their own material held privately,
  and the capstone ships as a dated first verified output.
- **Privacy by design:** outputs and tasks, never private information
  about people; the ritual builder and verification card state explicitly
  that nothing is saved or transmitted.

## The facilitator edition

Generated at `/facilitator/` by `python3 tools/build-facilitator.py` from
`facilitator/notes.json`: ATD-scripted rails (Say / Do / Ask with expected
answers / Debrief / Transition), a briefing slide (prep, materials,
contingencies, tough questions, three copy-paste templates), Full 90 /
Core 60 timing. Its QR encodes the learner URL.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (statGuess, modeName, faultLine,
  shipCheck)
- Ritual builder: `ritualBuild` block · Verification Lab: `SLOTS` in main.js
- Capstone maps: `PRACTICE` / `NOT` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (timing must sum: Full 90 / Core 60)
- Citations to keep honest: SHRM workplace AI research (around 4 hours a
  week fixing AI output), Stanford AI Index (reported AI incidents at
  record highs), automation-bias research (framing only, no invented
  numbers). The traffic light must match Start Smarter and AI 201 exactly:
  green public, yellow internal in approved VU tools only, red private
  information about people, never. The light outranks every read.
