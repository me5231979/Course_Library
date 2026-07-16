#!/usr/bin/env python3
"""Generate printable course-description pages (syllabus-*.html) for the
Course Library. One page per course: description, objectives, topics,
activities, outcomes/measurement, delivery details, links.

Run after editing the COURSES data below:

    python3 tools/build-syllabi.py
"""
import html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COURSES = [
    {
        "slug": "ai-basics",
        "title": "AI Basics",
        "subtitle": "A classroom introduction to artificial intelligence",
        "audience": "All Vanderbilt staff; no technical background needed",
        "length": "90 minutes (full) or 60 minutes (core); also works self-paced",
        "format": "Instructor-led, in person or virtual; learners join on their own devices via QR code",
        "group": "Any size; group activities work best with tables of 3 to 6",
        "description": "A working picture of how AI actually works, built for people who use it at work, not people who build it. The session moves from what AI is (and isn't), through how machines learn and how language models generate answers, to the practical skills: writing prompts that work, verifying output before trusting it, and choosing the right Vanderbilt-approved tool for the sensitivity of the data involved. It closes with each learner building a one-week plan to put AI on one of their own tasks.",
        "objectives": [
            "Distinguish AI, machine learning, and generative AI, and spot each in the tools you already use",
            "Explain how a language model produces an answer, and why the same question gives different answers",
            "Construct four-part prompts (role, context, task, format) that get useful, reliable results on real work",
            "Evaluate AI output before trusting it, and route tasks to the right Vanderbilt tool by data sensitivity",
            "Create a one-week plan that puts AI on one of your own tasks, and keeps the time it saves"
        ],
        "topics": [
            ("What AI actually is", "AI, machine learning, deep learning, and generative AI, untangled with an interactive ring diagram"),
            ("How machines learn", "Supervised, unsupervised, and reinforcement learning, practiced in a you-be-the-engineer scenario game"),
            ("Inside a neural network", "Layers, weights, and why even builders can't fully explain one decision"),
            ("Language models", "Next-token prediction, felt firsthand in a build-a-sentence simulator"),
            ("Steering the output", "Temperature and randomness, explored with a live slider"),
            ("Prompting well", "The four-part prompt and the Persona Pattern, then practiced in a graded Prompt Lab"),
            ("Strengths and limits", "What AI is genuinely good at, where it fails, and what a hallucination is"),
            ("Using AI responsibly", "Bias, privacy, accountability, and Vanderbilt's green/yellow/red data rules"),
            ("Keeping the time AI saves", "Workload creep, wellbeing, and deciding where the saved hour goes")
        ],
        "activities": "Six interactive simulators (concept rings, ML trainer, neural network, token predictor, temperature slider, prompt anatomy), a graded Prompt Lab, inline knowledge checks in every section, a six-question scored recap, and the My AI Plan capstone.",
        "outcomes": "Learners leave with a tested four-part prompt structure, a personal verification habit, clarity on which tool (Amplify, Copilot, ChatGPT) fits which data level, and a written one-week plan for applying AI to their own work. Learning is measured in session (knowledge checks and a recap quiz mapped to the objectives) and after (the capstone plan and a follow-up pulse).",
        "takehomes": [
            ("Printable cheat sheet", "https://me5231979.github.io/AI_Classroom/cheatsheet.html")
        ],
        "learner": "https://me5231979.github.io/AI_Classroom/",
        "facilitator": "https://me5231979.github.io/AI_Classroom/facilitator/",
        "frameworks": "Grounded in Vanderbilt's Dr. Jules White's prompt-pattern research, current AI-at-work research on workload intensification (HBR), and Vanderbilt's AI platform guidance."
    },
    {
        "slug": "difficult-conversations",
        "title": "Navigating Difficult Conversations",
        "subtitle": "A manager's toolkit for candor, trust, and courage",
        "audience": "People managers, team leads, and HR/talent partners",
        "length": "90 minutes (full) or 60 minutes (core); also works self-paced",
        "format": "Instructor-led, in person or virtual; learners join on their own devices via QR code",
        "group": "8 to 24 works best for the pair practice",
        "description": "Most managers already know what they need to say; they freeze on how. This session gives leaders a shared, research-backed language for the conversations they've been avoiding: the feedback that gets softened into vagueness, the redirect that never happens, the conflict that quietly erodes trust. Rather than one script, it blends the field's most respected frameworks into a single practical toolkit, practiced live. Each learner carries one real avoided conversation through the whole session and leaves with it planned and dated.",
        "objectives": [
            "Name the three conversations hiding inside any hard exchange (What Happened, Feelings, Identity), and spot the one that trips you up",
            "Turn a vague concern into specific, fair feedback using the SBI model",
            "Open a candid conversation in a way that keeps the other person safe, using STATE",
            "Assess your own trust-building behaviors with the BRAVING inventory and pick one to strengthen",
            "Plan one real conversation you've been avoiding, and commit to having it within seven days"
        ],
        "topics": [
            ("The cost of avoiding", "Why postponed conversations compound, with McKinsey's obligation-to-dissent framing"),
            ("The three conversations", "The Harvard Negotiation Project model, practiced in a label-the-line game"),
            ("SBI feedback", "Situation, Behavior, Impact (CCL), then assembled hands-on in a graded Feedback Lab"),
            ("Opening with STATE", "Crucial Conversations' safe-opening moves, rehearsed out loud in pairs"),
            ("Trust and BRAVING", "Brené Brown's seven trust behaviors, self-scored privately, plus the circle of safety"),
            ("Radical Candor", "Kim Scott's care/challenge grid, practiced in a quadrant-sorting game"),
            ("The first 30 seconds", "SHRM's three questions and one assembled opening line"),
            ("Sideways and listening", "Recovering from tears, anger, and silence; contrast statements; the listening turn")
        ],
        "activities": "An avoidance-cost meter, a conversation labeler, a graded SBI Feedback Lab, tap-to-explore SBI and STATE anatomies, a private BRAVING scorecard, a Radical Candor quadrant sort, out-loud pair practice with partner verdicts, a six-question scored recap, and the My Conversation Plan capstone.",
        "outcomes": "Learners leave with a written opener for a real conversation, a recovery line for when it gets heated, a listening plan, and a date within seven days, plus a shared team vocabulary (SBI, STATE, BRAVING, Radical Candor). Learning is measured in session (checks and a recap mapped to objectives), at close (readiness check and public commitment), and after (a seven-day follow-up pulse).",
        "takehomes": [
            ("Printable cheat sheet", "https://me5231979.github.io/Difficult_Conversations/cheatsheet.html"),
            ("Capstone plan worksheet", "https://me5231979.github.io/Difficult_Conversations/worksheet.html")
        ],
        "learner": "https://me5231979.github.io/Difficult_Conversations/",
        "facilitator": "https://me5231979.github.io/Difficult_Conversations/facilitator/",
        "frameworks": "Blends Stone, Patton & Heen (Harvard Negotiation Project), CCL's SBI, Crucial Conversations' STATE, Brené Brown's BRAVING, Kim Scott's Radical Candor, SHRM's manager guidance, ATD's CLEAR, and McKinsey's courageous-conversations research."
    },
    {
        "slug": "coaching-for-performance",
        "title": "Coaching for Performance",
        "subtitle": "Building managers who grow people, not just manage tasks",
        "audience": "People managers, team leads, and HR/talent partners",
        "length": "90 minutes (full) or 60 minutes (core); also works self-paced",
        "format": "Instructor-led, in person or virtual; learners join on their own devices via QR code",
        "group": "8 to 24 works best for the pair and triad practice",
        "description": "Google's largest study of its own managers found one behavior at the top of the list, ahead of technical skill: 'is a good coach.' Yet most managers were promoted for being excellent doers, so they default to telling, fixing, and directing. This session rewires the default: a repeatable coaching structure (GROW), the question craft that makes it work, Marshall Goldsmith's Feedforward exchange, and the judgment to know when directing is actually the right call. Learners coach a virtual coachee, then each other, then commit to coaching a real person on their team within the week.",
        "objectives": [
            "Explain why coaching, not directing, is the top predictor of great management, and spot your own telling default",
            "Structure a full coaching conversation with the GROW model, from goal to committed action",
            "Convert closed, leading, and advice-loaded lines into open, powerful questions",
            "Give and receive future-focused Feedforward suggestions without judgment or defense",
            "Choose your coaching model (GROW, CLEAR, or OSKAR) and commit to one real coaching conversation this week, opening question written"
        ],
        "topics": [
            ("The case for coaching", "Google's Project Oxygen and McKinsey's controller-to-coach shift, plus a private coaching-ratio self-check"),
            ("Your telling default", "Goleman's leadership styles and why excellent doers over-direct, practiced in a catch-the-style game"),
            ("The GROW conversation", "Goal, Reality, Options, Will, run live against a virtual coachee in the Coach Jordan simulator, then with a partner"),
            ("Powerful questions", "The ICF's three tests (open, clean, theirs), the six-second silence, and a question-conversion drill"),
            ("Feedforward", "Goldsmith's future-only development exchange, run live in triads"),
            ("Choose your model", "GROW vs CLEAR vs OSKAR, matched to real coaching situations"),
            ("When NOT to coach", "Situational judgment: when directing is right, and how to default back to coaching")
        ],
        "activities": "A coaching-ratio meter (the baseline for a 30-day re-measure), a style-spotting trainer, the Coach Jordan GROW conversation simulator, a powerful-question converter, a feedforward classifier, a model matcher, live pair and triad practice, a six-question scored recap, and the My Coaching Plan capstone.",
        "outcomes": "Learners leave with a chosen coaching model, a written opening question for a real team member, a counter-move for their personal telling trap, and a date within seven days. Learning is measured in session (trainer scores, simulator outcomes, and a recap mapped to objectives), at close (readiness check and public commitment), and after (a seven-day pulse and a 30-day coaching-ratio re-poll against the in-session baseline).",
        "takehomes": [
            ("Printable cheat sheet", "https://me5231979.github.io/Coaching-for-Performance/cheatsheet.html"),
            ("Coaching plan worksheet", "https://me5231979.github.io/Coaching-for-Performance/worksheet.html")
        ],
        "learner": "https://me5231979.github.io/Coaching-for-Performance/",
        "facilitator": "https://me5231979.github.io/Coaching-for-Performance/facilitator/",
        "frameworks": "Blends Google re:Work's Project Oxygen, Whitmore's GROW, the ICF core competencies, Marshall Goldsmith's Feedforward, Goleman's leadership styles, McKinsey's leadership research, Hawkins' CLEAR, the solution-focused OSKAR model, and Ibarra & Scoular's 'The Leader as Coach' (HBR)."
    },
    {
        "slug": "ai-201",
        "title": "AI 201: Beyond the Basics",
        "subtitle": "How models actually work, and how to run them responsibly",
        "audience": "Anyone who completed AI Basics (101) or equivalent: knowledge workers, managers, L&D and talent teams",
        "length": "90 minutes (full) or 60 minutes (core); also works self-paced",
        "format": "Instructor-led, in person or virtual; learners join on their own devices via QR code. No coding, no math. Prerequisite: AI Basics",
        "group": "8 to 24 works best for pairs; scales larger with polling instead of breakouts",
        "description": "Most AI training stops at prompting technique. This session goes underneath the prompt box: why long conversations lose the thread (context and attention), how Retrieval-Augmented Generation grounds answers in real, current sources, and how to choose between prompting, RAG, and fine-tuning with a cheapest-first decision framework. It adds four advanced prompt patterns from the academic catalog behind AI Basics, then covers what happens when AI starts acting on its own: the agent loop, its documented failure modes, and where the human checkpoint belongs. It closes with the skills that make everything safe at work: spotting hallucinations, red-teaming as a discipline, the NIST AI Risk Management Framework, and governance tiering, all converging in a governed AI workflow each learner builds for a real recurring task.",
        "objectives": [
            "Explain how context and attention shape a model's answer, and why long conversations lose the thread",
            "Describe what Retrieval-Augmented Generation fixes (trustworthy sources) and what it doesn't (a smarter model)",
            "Choose between prompting, RAG, and fine-tuning for a task, weighing cost, data needs, and maintenance",
            "Apply four advanced prompt patterns: Few-Shot, Chain-of-Thought, Template, and Flipped Interaction",
            "Recognize the agent plan-act-observe loop, name its documented failure modes, and place the human checkpoint",
            "Classify information into governance tiers and build one real, governed AI workflow for your team"
        ],
        "topics": [
            ("Context and attention", "The finite window every answer is built from, felt in a live simulator where your instruction falls out of the window (3Blue1Brown)"),
            ("Grounding with RAG", "A toggle simulator contrasts the fluent guess with the cited, source-grounded answer (IBM)"),
            ("Choosing your method", "Prompting vs RAG vs fine-tuning, practiced as a five-scenario routing game"),
            ("Advanced prompt patterns", "Few-Shot, Chain-of-Thought, Template, Flipped Interaction, matched to tasks and applied to a real prompt"),
            ("Multimodal and agentic AI", "The plan-act-observe loop, and five agent traces where learners catch the documented failure modes"),
            ("Spot the hallucination", "Six AI answers, real or invented: calibrating the detector and meeting red-teaming (NIST)"),
            ("Governance that scales", "The NIST AI RMF's four functions as plain questions, and green/yellow/red tiering drilled to reflex")
        ],
        "activities": "A context-window simulator, a RAG grounding toggle with a retrieved-source panel, five scenario trainers (method routing, pattern matching, agent-trace reading, hallucination spotting, governance tiering), inline knowledge checks, a six-question scored recap, and the Team AI Workflow capstone.",
        "outcomes": "Learners leave with a governed AI workflow card for a real recurring task: trigger, AI step, prompt pattern, human checkpoint, and governance tier, plus the shared vocabulary (RAG, fine-tuning, agents, red-teaming, NIST AI RMF) to evaluate vendors and tools. Learning is measured in session (trainer scores and a recap mapped to the six objectives), at close (readiness check and a trigger-and-tier commitment round), and after (a 7-day pulse and a 30-day census of written, tiered team workflows).",
        "takehomes": [
            ("Printable cheat sheet", "https://me5231979.github.io/AI-Advanced/cheatsheet.html"),
            ("Workflow card worksheet", "https://me5231979.github.io/AI-Advanced/worksheet.html")
        ],
        "learner": "https://me5231979.github.io/AI-Advanced/",
        "facilitator": "https://me5231979.github.io/AI-Advanced/facilitator/",
        "frameworks": "Grounded in 3Blue1Brown's attention walkthrough, IBM's RAG and agent research explainers, White et al.'s prompt pattern catalog (Vanderbilt), Wei et al. (chain-of-thought), Brown et al. (few-shot), Adaline Labs' agent failure research, and NIST's AI red-teaming definition and AI Risk Management Framework."
    }
]

CSS = """
  @font-face { font-family: 'Libre Caslon Display'; font-style: normal; font-weight: 400;
    src: url('assets/fonts/libre-caslon-display-latin-400-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Inter'; font-style: normal; font-weight: 400;
    src: url('assets/fonts/inter-latin-400-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Inter'; font-style: normal; font-weight: 600;
    src: url('assets/fonts/inter-latin-600-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Antonio'; font-style: normal; font-weight: 700;
    src: url('assets/fonts/antonio-latin-700-normal.woff2') format('woff2'); }
  * { box-sizing: border-box; }
  body { margin: 0; font-family: 'Inter', Arial, sans-serif; color: #1C1C1C; background: #fff;
    font-size: 13px; line-height: 1.5; }
  .sheet { max-width: 820px; margin: 0 auto; padding: 28px 32px; }
  header { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px;
    border-bottom: 2px solid #CFAE70; padding-bottom: 14px; margin-bottom: 16px; }
  header img { width: 150px; flex-shrink: 0; }
  h1 { font-family: 'Libre Caslon Display', 'Times New Roman', serif; font-weight: 400;
    font-size: 27px; margin: 0; line-height: 1.15; }
  h1 em { font-style: italic; color: #946E24; }
  .eyebrow { font-family: 'Antonio', Impact, sans-serif; font-weight: 700; text-transform: uppercase;
    letter-spacing: .08em; font-size: 10px; color: #946E24; margin: 0 0 6px; }
  .subtitle { margin: 4px 0 0; color: #555; font-size: 14px; }
  .facts { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px 20px; margin: 0 0 16px;
    border: 1px solid #E4E4E4; border-radius: 4px; padding: 12px 14px; }
  .facts div b { display: block; font-family: 'Antonio', Impact, sans-serif; font-weight: 700;
    text-transform: uppercase; letter-spacing: .06em; font-size: 10px; color: #946E24; }
  h2 { font-family: 'Antonio', Impact, sans-serif; font-weight: 700; text-transform: uppercase;
    letter-spacing: .06em; font-size: 13px; color: #946E24; margin: 18px 0 6px; }
  p { margin: 0 0 8px; }
  ol, ul { margin: 0 0 8px; padding-left: 20px; }
  li { margin-bottom: 4px; }
  .topics li b { font-weight: 600; }
  .frameworks { color: #555; font-size: 12px; font-style: italic; }
  .links { border: 1px solid #CFAE70; background: #fdf9ef; border-radius: 4px; padding: 12px 14px; margin-top: 14px; }
  footer { margin-top: 16px; border-top: 1px solid #E4E4E4; padding-top: 10px; font-size: 11px; color: #777;
    display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; }
  a { color: #946E24; }
  .printbtn { position: fixed; right: 18px; top: 18px; background: #CFAE70; border: 0; border-radius: 4px;
    padding: 9px 16px; font-family: Inter, Arial, sans-serif; font-weight: 600; font-size: 13px; cursor: pointer; }
  @media print { .printbtn { display: none; } body { font-size: 11.5px; } .sheet { padding: 0; max-width: none; }
    .links { break-inside: avoid; } }
  @media (max-width: 640px) { .facts { grid-template-columns: 1fr; } header { flex-direction: column; } }
"""

def esc(t):
    return html.escape(t, quote=False)

def build(c):
    objectives = ''.join(f'<li>{esc(o)}</li>' for o in c['objectives'])
    topics = ''.join(f'<li><b>{esc(t)}.</b> {esc(d)}</li>' for t, d in c['topics'])
    takehomes = ' · '.join(f'<a href="{u}">{esc(n)}</a>' for n, u in c['takehomes'])
    title_words = c['title'].rsplit(' ', 1)
    h1 = f'{esc(title_words[0])} <em>{esc(title_words[1])}</em>' if len(title_words) == 2 else esc(c['title'])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(c['title'])} — Course Description | Vanderbilt</title>
<meta name="robots" content="noindex">
<style>{CSS}</style>
</head>
<body>
<button class="printbtn" onclick="window.print()">Print / Save as PDF</button>
<div class="sheet">
  <header>
    <div>
      <p class="eyebrow">Vanderbilt · Learning Series · Course description</p>
      <h1>{h1}</h1>
      <p class="subtitle">{esc(c['subtitle'])}</p>
    </div>
    <img src="assets/img/vu-lockup-black.png" alt="Vanderbilt University">
  </header>

  <div class="facts">
    <div><b>Audience</b>{esc(c['audience'])}</div>
    <div><b>Length</b>{esc(c['length'])}</div>
    <div><b>Format</b>{esc(c['format'])}</div>
    <div><b>Group size</b>{esc(c['group'])}</div>
  </div>

  <h2>About this course</h2>
  <p>{esc(c['description'])}</p>

  <h2>Learning objectives</h2>
  <p>By the end of this session, participants will be able to:</p>
  <ol>{objectives}</ol>

  <h2>Topics covered</h2>
  <ul class="topics">{topics}</ul>

  <h2>How you'll learn</h2>
  <p>{esc(c['activities'])} Every section pairs teaching with something to do; nothing is watch-only. Private exercises stay on the learner's screen and are never collected.</p>

  <h2>Outcomes and how learning is measured</h2>
  <p>{esc(c['outcomes'])}</p>

  <p class="frameworks">{esc(c['frameworks'])}</p>

  <div class="links">
    <b>Take the course:</b> <a href="{c['learner']}">{c['learner'].replace('https://','')}</a><br>
    <b>Deliver it (facilitator edition):</b> <a href="{c['facilitator']}">{c['facilitator'].replace('https://','')}</a><br>
    <b>Take-homes:</b> {takehomes}
  </div>

  <footer>
    <span>Vanderbilt Learning Series · <a href="https://me5231979.github.io/Course_Library/">Course Library</a></span>
    <span>Questions? <a href="mailto:chart@vanderbilt.edu">chart@vanderbilt.edu</a></span>
  </footer>
</div>
</body>
</html>
"""

for c in COURSES:
    out = os.path.join(ROOT, f"syllabus-{c['slug']}.html")
    open(out, 'w').write(build(c))
    print(f"wrote {out}")
