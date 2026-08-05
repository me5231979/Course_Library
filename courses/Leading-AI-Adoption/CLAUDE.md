# Making It Normal · Vanderbilt Learning Series

Single-page interactive course site (no frameworks). Lives inside the
Course_Library repo at `courses/Leading-AI-Adoption/`; published at
https://me5231979.github.io/Course_Library/courses/Leading-AI-Adoption/

## Rules that must hold

1. **Zero em or en dashes anywhere**: HTML, JS strings, JSON, markdown.
   Rewrite around them; grep before shipping.
2. **One italic word per headline** (`.h2` uses exactly one `<em>`).
3. **The traffic light is canon** and matches Start Smarter and AI 201:
   green = public or generic, go; yellow = internal, approved VU tools
   only; red = private information about people, never. It outranks every
   technique taught here.
4. **Generated editions are never hand-edited**: `web/index.html` comes
   from `python3 tools/build-web.py`; `facilitator/index.html` and
   `facilitator/guide.html` come from `python3 tools/build-facilitator.py`.
   Regenerate both after any change to `index.html` or
   `facilitator/notes.json`.
5. **Timing invariant**: notes.json section `minutes` sum to exactly 90
   and `coreMinutes` to exactly 60.
6. **Privacy by design**: every exercise runs on roles and rituals, never
   people's names; nothing typed is saved or transmitted, and the copy
   says so wherever learners type.
7. **Citations stay honest**: Gallup workplace AI research only (~40% use,
   19% frequent, 22% clear plan, 4.7x comfort), linked where claimed.

## Editing map

- Copy: `index.html` (14 slides, horizontal deck)
- Interactions: `assets/js/main.js` (trainers gallupGuess / judgeModel /
  fixRitual / monthMoves, the ptBuild permission-talk builder, the
  adoptLab SLOTS, capstone PRACTICE / NOT / WHEN, recap QUESTIONS)
- Runbook: `facilitator/notes.json`
- Printables: `cheatsheet.html`, `worksheet.html`
- Slide screenshots for the printable guide: `facilitator/img/<slide-id>.jpg`
