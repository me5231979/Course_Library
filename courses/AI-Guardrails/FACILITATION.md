# Facilitation Guide · AI Guardrails & Responsible Use

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

**Pre-work:** come knowing the two or three outputs your team ships most
often and the kinds of data they touch, held privately. **The norm**,
stated in minute one and repeated before the builder and the capstone:
tools and situations, never people's names, and nothing typed leaves the
learner's screen.

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
| 01 Why written rules | 8 | 5 |
| Manifesto | 1 | skip |
| 02 Line one: what goes in | 12 | 9 |
| 03 Line two: the check | 11 | 8 |
| 04 Line three: disclosure | 10 | 6 |
| 05 Line four: ownership + the Lab | 14 | 10 |
| 06 Write your Four Lines | 12 | 8 |
| Recap quiz | 4 | 4 |
| My Four Lines Card (capstone) | 6 | 6 |
| Glossary | 1 | skip |
| Closing / commitment | 5 | 1 |
| **Total** | **90** | **60** |

**Core-path rules:** every trainer, the Guardrails Lab, the Four Lines
builder, the recap, and the capstone stay. Pair drills drop to one round
or a solo pass (never zero practice), debriefs shrink to one voice each,
and the lab runs once instead of run-plus-rerun. Per-section cuts live in
each `coreNote`.

**Timing discipline:** the pair classification drill (02) and the
disclosure read-alouds (04) are the stretchy blocks. Protect the last 15
minutes (recap, capstone, closing) by trimming debriefs first, never the
lab, the builder, or the capstone; they carry the practice objectives.

**Safety rails:** if someone names a colleague or starts prosecuting a
specific person's AI use, protect the norm in one warm move (script in
contingencies). If someone reports a real incident or possible FERPA
exposure, it outranks the agenda: restate the traffic light, take it
offline, and route it to the right policy owner rather than adjudicating
from the front of the room.

## Validation model

- **In the moment:** inline checks (01, 02, 03, 04, 05), trainer scores
  (01, 02, 03, 04), the graded Guardrails Lab with its rerun delta (05),
  and the room-judged disclosure lines (04).
- **End of session:** the 6-question recap maps to the objectives
  (Level 2); the closing fist-to-five is the Level 1 check; the Four
  Lines card and the team-and-day commitment round are the transfer
  artifacts.
- **After:** the 7-day pulse (did the team conversation happen, where
  does the page live, which hard case surprised you) is Level 3
  evidence; the **30-day re-poll** (same fist-to-five + is the page
  findable, has it been pointed at during a real decision) closes the
  loop and pairs with the in-room baseline.
- **Privacy guard:** validation counts conversations held and pages
  drafted, never the contents of anyone's lines, card, or data.
