# Facilitation Guide · Across Your Week

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

**Pre-work:** skim last week's real calendar and sent folder and arrive
knowing your three biggest recurring blocks, held privately. **The norm**,
stated in minute one and repeated before the inventory and the capstone:
blocks and workflows, never people's names, and nothing typed leaves the
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
| 01 The breadth effect | 9 | 6 |
| Manifesto | 1 | skip |
| 02 The inventory | 12 | 8 |
| 03 The method match | 12 | 9 |
| 04 The stack | 11 | 7 |
| 05 The Week Lab | 14 | 10 |
| 06 Bank the time | 10 | 6 |
| Recap quiz | 4 | 4 |
| My Week Map (capstone) | 6 | 6 |
| Glossary | 1 | skip |
| Closing / commitment | 4 | 1 |
| **Total** | **90** | **60** |

**Core-path rules:** every trainer, the private inventory, the Week Lab,
the recap, and the capstone stay. Pair drills drop to one round or a solo
pass (never zero practice), debriefs shrink to one voice each, and the lab
runs once instead of run-plus-rerun. Per-section cuts live in each
`coreNote`.

**Timing discipline:** the pair swaps (02, 03, 04) and the lab debrief (05)
are the stretchy blocks. Protect the last 15 minutes (recap, capstone,
closing) by trimming debriefs first, never the inventory, the lab, or the
capstone; they carry the practice objectives.

**Safety rails:** if someone names a colleague or turns a block into a
complaint about a person, protect the norm in one warm move (script in
contingencies). If a real data-privacy question surfaces, it outranks the
agenda: restate the traffic light, then route genuine ambiguity to the
right owner rather than improvising policy from the front of the room.

## Validation model

- **In the moment:** inline checks (01, 03, 06), trainer scores (01, 03,
  04, 06), the graded Week Lab with its rerun delta (05), and the read-back
  output of the private inventory (02).
- **End of session:** the 6-question recap maps to the objectives
  (Level 2); the closing fist-to-five is the Level 1 check; the Week Map
  and the stack-and-day commitment round are the transfer artifacts.
- **After:** the 7-day pulse (did the calendar pass run, how many assists
  are placed, where is the bank block) is Level 3 evidence; the **30-day
  re-poll** (same fist-to-five + the distinct-use count and what the bank
  bought) closes the loop and pairs with the in-room baseline.
- **Privacy guard:** validation counts calendar passes run, assist counts,
  and confidence, never the contents of anyone's inventory or map.
