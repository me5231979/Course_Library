# Facilitation Guide · Hiring & Talent Decisions with AI

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

**Pre-work:** bring one hiring or talent decision that is live or coming,
held privately. **The norm**, stated in minute one and repeated before the
structure builder and the capstone: roles and processes, never a
candidate's or colleague's name, and nothing typed leaves the learner's
screen. The course practices the exact discipline it teaches.

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
| 01 The temptation and the line | 9 | 6 |
| Manifesto | 1 | skip |
| 02 The red side, exactly | 12 | 8 |
| 03 The wide funnel | 12 | 9 |
| 04 Structure before candidates | 11 | 7 |
| 05 The Hiring Lab | 14 | 10 |
| 06 Bias, watched | 10 | 6 |
| Recap quiz | 4 | 4 |
| My Structure Card (capstone) | 6 | 6 |
| Glossary | 1 | skip |
| Closing / commitment | 4 | 1 |
| **Total** | **90** | **60** |

**Core-path rules:** every trainer, the structure builder, the Hiring
Lab, the recap, and the capstone stay. Pair drills drop to one round or a
solo pass (never zero practice), debriefs shrink to one voice each, and
the lab runs once instead of run-plus-rerun. Per-section cuts live in
each `coreNote`.

**Timing discipline:** the pair swaps (02, 03, 04) and the lab debrief
(05) are the stretchy blocks. Protect the last 15 minutes (recap,
capstone, closing) by trimming debriefs first, never the builder, the
lab, or the capstone; they carry the practice objectives.

**Safety rails:** if someone names a real candidate or colleague, protect
the norm in one warm move (script in contingencies). If someone admits a
past red-line violation, thank them, give the clean path (stop, delete,
escalate if sensitive), and convert the case into the swap teaching
moment; that confession is the session working. Any real privacy incident
outranks the agenda: restate the traffic light, then route it to HR and
VU policy rather than improvising remediation from the front of the room.

## Validation model

- **In the moment:** inline checks (01, 04, 06), trainer scores (01, 02,
  03, 06), the graded Hiring Lab with its rerun delta and the violation
  tier (05), and the anchor rewrites read aloud (06).
- **End of session:** the 6-question recap maps to the sections
  (Level 2); the closing fist-to-five is the Level 1 check; the structure
  card and the role-and-first-move commitment round are the transfer
  artifacts.
- **After:** the 7-day pulse (did the first move happen, what changed,
  is the red line holding) is Level 3 evidence; the **30-day re-poll**
  (same fist-to-five + what does your next search have that the last one
  lacked) closes the loop and pairs with the in-room baseline.
- **Privacy guard:** validation counts moves made and confidence, never
  the contents of anyone's plan, card, or search.
