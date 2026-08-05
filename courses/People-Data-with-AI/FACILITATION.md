# Facilitation Guide · People Data with AI

Every activity carries a learner-visible **"Why this matters"** line, and
every teaching section has (1) an **interactive tool or practice moment**,
(2) a **labeled, timed activity**, *As a group* or *On your own*, and
(3) a **validation point**.

The full runbook lives in [`facilitator/notes.json`](facilitator/notes.json)
on the **ATD facilitator-guide framework**: per section a verbatim **Say**
script, **Do** choreography, an **Ask** with anticipated responses, a
**Debrief** line, and a scripted **Transition**, plus front matter
(materials, prep checklists, contingencies, tough questions, and copy-paste
templates: pre-work invite, 7-day pulse, 30-day re-poll).

**Pre-work:** bring one real people-data source, engagement results, a
retro board, a pulse, or your own 1:1 notes, held privately, with a rough
sense of what it has been waiting for. **The norm**, stated in minute one
and repeated before the builder and the capstone: patterns and roles,
never people's names, and nothing typed leaves the learner's screen.

The **facilitator edition is live at `/facilitator/`**. Regenerate after
any change to `index.html` or `notes.json`:

```bash
python3 tools/build-facilitator.py
```

## Run of show, two paths

| Slide | Full (90 min) | Core (60 min) |
|---|---|---|
| Welcome / QR | 3 | 2 |
| Objectives | 2 | 1 |
| Agenda | 1 | skip |
| 01 The new expectation | 9 | 6 |
| Manifesto | 1 | skip |
| 02 The Aggregate Rule | 12 | 9 |
| 03 Themes from the noise | 11 | 8 |
| 04 Feedback, rehearsed | 11 | 7 |
| 05 The Review Prep Lab | 14 | 10 |
| 06 From data to conversation | 10 | 6 |
| Recap quiz | 4 | 4 |
| My People-Data Card (capstone) | 6 | 6 |
| Glossary | 1 | skip |
| Closing / commitment | 5 | 1 |
| **Total** | **90** | **60** |

**Core-path rules:** every trainer, the interrogation-plan builder, the
Review Prep Lab, the recap, and the capstone stay. Pair drills drop to one
round or a solo pass (never zero practice), debriefs shrink to one voice
each, and the lab runs once instead of run-plus-rerun. Per-section cuts
live in each `coreNote`.

**Timing discipline:** the trap-invention drill (02), the mystery swap
(03), and the share-back draft-aloud (06) are the stretchy blocks. Protect
the last 15 minutes (recap, capstone, closing) by trimming debriefs first,
never the builder, the lab, or the capstone; they carry the practice
objectives.

**Safety rails:** if someone names a colleague or reads a real comment
aloud, protect the norm in one warm move (script in contingencies). If a
real privacy question surfaces, it outranks the agenda: restate the
Aggregate Rule, confirm the case against it, and route genuine ambiguity
to HR or the privacy office rather than improvising policy from the front
of the room.

## Validation model

- **In the moment:** inline checks (01, 04, 06), trainer scores (01, 02,
  04, 06), the graded Review Prep Lab with its rerun delta (05), and the
  room-judged share-back lines (06).
- **End of session:** the 6-question recap maps to the objectives
  (Level 2); the closing fist-to-five is the Level 1 check; the
  people-data card and the source-and-day commitment round are the
  transfer artifacts.
- **After:** the 7-day pulse (did the theme-to-conversation session run,
  what theme survived the ground truth test, which conversation is on the
  calendar) is Level 3 evidence; the **30-day re-poll** (same fist-to-five
  plus which conversations happened and what they changed) closes the loop
  and pairs with the in-room baseline.
- **Privacy guard:** validation counts sessions held and confidence, never
  the contents of anyone's data, card, or notes.
