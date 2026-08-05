# Facilitation Guide · Delegating, Rethought

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

**Pre-work:** bring one task you have been holding that someone or
something else could do, held privately, plus a rough sense of what it
costs you in a normal week. **The norm**, stated in minute one and
repeated before the role-math sketch and the capstone: tasks and roles,
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
| 01 The new triage | 9 | 6 |
| Manifesto | 1 | skip |
| 02 The Routing Test | 12 | 9 |
| 03 Stretch vs grunt | 11 | 7 |
| 04 Role math | 12 | 8 |
| 05 The Routing Lab | 14 | 10 |
| 06 The handoff | 10 | 6 |
| Recap quiz | 4 | 4 |
| My Routing Card (capstone) | 6 | 6 |
| Glossary | 1 | skip |
| Closing / commitment | 4 | 1 |
| **Total** | **90** | **60** |

**Core-path rules:** every trainer, the role-math sketch, the Routing Lab,
the recap, and the capstone stay. Pair drills drop to one round or a solo
pass (never zero practice), debriefs shrink to one voice each, and the lab
runs once instead of run-plus-rerun. Per-section cuts live in each
`coreNote`.

**Timing discipline:** the pair drills (02, 03, 04) and the brief-aloud
(06) are the stretchy blocks. Protect the last 15 minutes (recap,
capstone, closing) by trimming debriefs first, never the role-math sketch,
the lab, or the capstone; they carry the practice objectives.

**Safety rails:** if someone names a colleague or starts prosecuting a
specific person's job, protect the norm in one warm move (script in
contingencies). If a real data-privacy question surfaces, it outranks the
agenda: restate the traffic light, then route genuine ambiguity to the
right owner rather than improvising policy from the front of the room.

## Validation model

- **In the moment:** inline checks (01, 04, 06), trainer scores (01, 02,
  03, 06), the graded Routing Lab with its rerun delta (05), and the
  room-judged handoff briefs (06).
- **End of session:** the 6-question recap maps to the objectives
  (Level 2); the closing fist-to-five is the Level 1 check; the routing
  card and the task-and-destination commitment round are the transfer
  artifacts.
- **After:** the 7-day pulse (did the handoff conversation happen, what
  did the person or verifier do with it) is Level 3 evidence; the
  **30-day re-poll** (same fist-to-five + what the routing freed up and
  what the new rep produced) closes the loop and pairs with the in-room
  baseline.
- **Privacy guard:** validation counts handoffs held and confidence,
  never the contents of anyone's sketch, card, or task list.
