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
        "coreSkills": ['Embodies an entrepreneurial spirit and leverages data and technology'],
        "skills": ['Artificial Intelligence', 'Digital Fluency/Information Literacy', 'Data Security'],
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
        "coreSkills": ['Leads and inspires teams'],
        "skills": ['Conflict Resolution', 'De-escalation Techniques', 'Influencing Skills'],
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
        "coreSkills": ['Grows self and others', 'Leads and inspires teams'],
        "skills": ['Coaching Techniques', 'Leadership Development', 'Employee Engagement'],
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
        "slug": "working-smarter",
        "coreSkills": ['Embodies an entrepreneurial spirit and leverages data and technology'],
        "skills": ['Artificial Intelligence', 'Prompt Writing', 'Digital Fluency/Information Literacy'],
        "title": "Working Smarter",
        "subtitle": "Learn the new tools by using them",
        "audience": "All Vanderbilt staff; no technical background needed",
        "length": "60 to 90 minutes for the core path; every module is skippable, and embedded videos are optional extras",
        "format": "Classroom (instructor-led, in person or virtual; learners join on their own devices) or fully self-paced online",
        "group": "Any size in the classroom; the self-paced edition works alone at a desk",
        "description": "The flagship course of the Working Smarter program (formerly CHART). Instead of talking about AI, it has you use it: you watch a language model predict the next word, map your own role the way AI actually meets it (task by task), learn the CRIT prompt framework, and drill it in working practice apps before taking one real task into your own tools. Along the way you learn the two questions that route any task to the right Vanderbilt tool, ChatGPT EDU, Amplify, or Copilot: how sensitive is the data, and where are you already working. It closes with a knowledge check and a personal plan for the week ahead.",
        "objectives": [
            "Explain what AI tools like ChatGPT are, and why they sometimes state made-up things as fact",
            "Map your own role task by task, identify where AI can help, and build a 30/60/90 development plan from that list",
            "Write clear, complete prompts with the CRIT framework: Context, Role, Interview, Task",
            "Choose the right approved tool for any task by data sensitivity: ChatGPT EDU, Amplify, or Copilot",
            "Use AI responsibly: verify outputs before they leave your hands, disclose substantive AI help, and keep sensitive data out of public tools"
        ],
        "topics": [
            ("What AI is, and how it works", "Five terms that build on each other (AI, machine learning, generative AI, large language models, agents), plus an in-page demo where you watch a model predict the next word"),
            ("Your role, task by task", "A readiness assessment that looks at your job the way AI meets it, task by task, and starts your 30/60/90 development plan"),
            ("The CRIT prompt framework", "Context, Role, Interview, Task: the four-part way to write a prompt, assembled step by step in the CRIT builder"),
            ("The Playground", "Practice apps with no live AI: build prompts for your own work in the Prompt Lab, tighten them in the Prompt Grader, then take one real task from your week"),
            ("Your three tools", "ChatGPT EDU, Amplify, and Copilot compared card by card, then drilled in Tool Match; the right tool depends on the data"),
            ("The AI Opportunity Simulator", "Describe one real task and get back an opportunity map, starter prompts, data flags, and the first 30 days of a plan"),
            ("Using AI responsibly", "Six guardrail habits, the never-paste list, and four workplace scenarios that test your judgment"),
            ("The knowledge check", "Eight self-scored questions covering the whole course; nobody sees your score, and you can retake it anytime"),
            ("Put it to work this week", "A five-step weekly loop that turns the course into a habit, closing with completion marked in Oracle Learning")
        ],
        "activities": "An in-page next-word prediction demo, a role readiness assessment with a 30/60/90 plan, four working practice apps (the CRIT builder, the Prompt Lab, the Prompt Grader, and Tool Match), the AI Opportunity Simulator, section-by-section self-checks with progress tracking, an eight-question knowledge check, and a closing shelf of Oracle Learning picks, podcasts, and videos for continued learning.",
        "outcomes": "Learners leave with a tested CRIT prompt for a real task from their own week, the two-question rule for routing any task to the right tool, the never-paste list, a 30/60/90 development plan built from their own task list, and a five-step weekly loop for putting AI on one task at a time. Learning is self-measured in the course (section self-checks and the eight-question knowledge check), and learners record completion themselves in Oracle Learning.",
        "takehomes": [],
        "learner": "https://me5231979.github.io/estesstite/learn/classroom/",
        "facilitator": "https://me5231979.github.io/estesstite/learn/classroom/facilitator/",
        "selfpaced": "https://me5231979.github.io/estesstite/learn/",
        "frameworks": "CRIT (Context, Role, Interview, Task) is credited to Geoff Woods, The AI-Driven Leader. Prompt patterns draw on Vanderbilt's Dr. Jules White (the Persona pattern). Task-exposure research from Eloundou et al., 'GPTs are GPTs,' and the Anthropic Economic Index. Tool routing follows Vanderbilt's data classification."
    },
    {
        "slug": "emotional-intelligence",
        "coreSkills": ['Grows self and others', 'Radically collaborates and cultivates belonging'],
        "skills": ['Conflict Management', 'Communication Strategies'],
        "title": "Emotional Intelligence & Interpersonal Skills",
        "subtitle": "Lead yourself, then lead others",
        "audience": "Managers, team leads, and individual contributors who work through relationships: anyone whose week includes feedback, conflict, or collaboration",
        "length": "90 minutes (full) or 60 minutes (core); also works self-paced",
        "format": "Instructor-led, in person or virtual; learners join on their own devices via QR code. Private by design: exercises use roles (never names) and nothing typed is saved or transmitted",
        "group": "9 to 24 works best (the listening drill runs in triads); scales larger with pairs and room votes",
        "description": "When researchers studied what separates star performers from average ones, emotional intelligence came out roughly twice as important as IQ and technical skill combined, yet 95 percent of people believe they're self-aware and only 10 to 15 percent are. This session closes that gap with practice, not platitudes. It opens with the published evidence (Goleman, McKinsey, DDI, SHRM), installs the four-domain map with the Mayer-Salovey science named underneath, then works inward: mapping blind spots with the Johari Window and using UCLA's affect-labeling research to turn reactivity into regulation. The second half turns outward: active listening scored against a real rubric in a triad drill, rebuilding accusations with Rosenberg's Nonviolent Communication in a graded lab, and Edmondson's psychological safety, saying the hard thing with candor AND care. Every learner leaves with a commitment card: one relationship, one practice, one date.",
        "objectives": [
            "Explain Goleman's four EI domains and map your own blind spots with the Johari Window",
            "Identify the Mayer-Salovey ability model, the research foundation beneath the applied one",
            "Name emotions precisely and use affect labeling to turn reactivity into regulation",
            "Practice active listening, paraphrase, clarify, withhold judgment, against a real rubric",
            "Reframe an accusation into Nonviolent Communication's Observation, Feeling, Need, Request",
            "Raise a hard truth with candor and care, and commit one practice to a real relationship this week"
        ],
        "topics": [
            ("The case for EI", "Four research findings played as a guessing game: Goleman's 2x finding, DDI's empathy data, McKinsey's demand projections, SHRM on respect"),
            ("The map", "Goleman's four domains in sequence (notice, steer, read the room, move together), with the Mayer-Salovey ability model underneath"),
            ("Self-awareness and the Johari Window", "Eurich's 95-vs-10-15 gap, the four quadrants, and a private blind-spot mapper; only feedback shrinks the blind quadrant"),
            ("Name it to tame it", "UCLA's affect-labeling neuroscience: precise emotional labels calm the amygdala and point at the next move"),
            ("Active listening", "Paraphrase, clarify, withhold judgment, drilled in scored triads with an observer holding the rubric"),
            ("The NVC reframe", "Rosenberg's Observation, Feeling, Need, Request, practiced in a graded lab where the reply changes as each part sharpens"),
            ("Candor with care", "Edmondson's psychological safety and Google's Project Aristotle: safety plus standards, not niceness")
        ],
        "activities": "A guess-the-number research game, a domain-spotting trainer, a private Johari Window mapper, an emotion-label upgrader, a rate-the-reply listening trainer plus a live triad drill, a graded NVC Reframe Lab, a judge-the-opener candor trainer, inline knowledge checks, a scored recap, and the EI Commitment Card capstone.",
        "outcomes": "Learners leave with a dated commitment card: one real relationship, one practice (listening, NVC, candor with care, or affect labeling), one named failure mode to avoid, and a first rep within seven days, plus the blind-spot question to ask a trusted colleague. Learning is measured in session (trainer scores, a graded lab, and a recap mapped to the objectives), at close (a confidence check and a spoken commitment round), and after (a 7-day pulse on the first rep and a 30-day self-check re-poll).",
        "takehomes": [
            ("Printable cheat sheet", "https://me5231979.github.io/Emotional-Intelligence/cheatsheet.html"),
            ("Commitment card worksheet", "https://me5231979.github.io/Emotional-Intelligence/worksheet.html")
        ],
        "learner": "https://me5231979.github.io/Emotional-Intelligence/",
        "facilitator": "https://me5231979.github.io/Emotional-Intelligence/facilitator/",
        "frameworks": "Grounded in Goleman's 'What Makes a Leader?' (HBR) and four-domain model, the Mayer-Salovey-Caruso ability model, Tasha Eurich's self-awareness research, Lieberman et al.'s affect-labeling studies (UCLA, Psychological Science 2007), Luft & Ingham's Johari Window, Rosenberg's Nonviolent Communication, and Amy Edmondson's psychological safety research with Google's Project Aristotle."
    },
    {
        "slug": "presentation-public-speaking",
        "coreSkills": ['Continuously strives for excellence'],
        "skills": ['Public Speaking', 'Storytelling', 'Strategic Communication', 'Stakeholder Communications'],
        "title": "Presentation & Public Speaking",
        "subtitle": "Building and delivering to a room or leadership audience",
        "audience": "Managers, senior ICs, and leaders who present to teams, stakeholders, or executive and board audiences",
        "length": "90 minutes (full) or 60 minutes (core); also works self-paced",
        "format": "Instructor-led, in person or virtual; learners join on their own devices via QR code. Practice-heavy: everyone speaks out loud at least once. Pre-work: bring one real upcoming presentation",
        "group": "8 to 20 works best so every participant gets a live speaking rep with feedback",
        "description": "Public speaking is not most people's top fear anymore — the 2024 Chapman Survey ranks it 59th of 85, behind sharks. What actually separates forgettable presenters from ones a room remembers is structure and presence, and both are learnable. This session opens with that myth-busting evidence and the career stakes (Coqual found 67 percent of senior executives name gravitas as the core signal of leadership readiness; Deloitte's CFOs rank communication skills the #1 quality in a successor). Then it builds: Duarte's Big Idea distills a real presentation into one sentence of point-of-view-plus-stakes; her Sparkline shapes it for hearts and minds; Minto's SCQA and Pyramid Principle restructure it for the executive room, leading with the answer. Delivery technique comes from Chris Anderson, Carmine Gallo, and the AMA's Seven Principles, drilled in a live, strictly-timed speaking round where every participant delivers their Big Idea and opening line for one piece of framework-anchored feedback. It closes with tough-question handling — the AMA bridge — under rapid fire, and a capstone that rebuilds one real upcoming presentation with the opening line written word for word.",
        "objectives": [
            "Explain why gravitas and communication, not technical mastery alone, decide how a leader's message lands, and name your own executive-presence growth edge",
            "Distill a real presentation topic into one resonant sentence using Duarte's Big Idea: point of view plus what's at stake",
            "Structure a presentation with Duarte's Sparkline, alternating What Is and What Could Be toward New Bliss",
            "Structure an executive briefing with Minto's Pyramid Principle and SCQA, leading with the answer",
            "Apply the delivery techniques of Anderson's and Gallo's HBR frameworks and the AMA's Seven Principles in a live, timed speaking round",
            "Handle pointed questions with the acknowledge-answer-return bridge, and commit to rebuilding one real presentation with the opening line written"
        ],
        "topics": [
            ("The myth and the case", "Chapman's fear data (public speaking: 59th of 85), Coqual's gravitas finding, and Deloitte's CFO communication stat, played as a guessing game"),
            ("Executive presence", "Hewlett's three pillars — gravitas 67%, communication 28%, appearance 5% — and each learner's growth edge"),
            ("The Big Idea", "Duarte's one-sentence discipline: a point of view someone could oppose, plus what's at stake, drafted privately for a real talk"),
            ("The Sparkline", "What Is alternating with What Could Be, ending in New Bliss — the shape under MLK's Dream speech and the great product launches"),
            ("SCQA and the Pyramid Principle", "Minto's executive structure: Situation, Complication, Question, Answer-first, practiced in a graded briefing lab"),
            ("Delivery", "Anderson's five keys, Gallo's five tips, and AMA's Seven Principles, applied in a live 60-to-90-second speaking round with peer feedback"),
            ("The tough question", "The AMA bridge — acknowledge, answer directly, return to the Big Idea — drilled under rapid fire from a mock executive")
        ],
        "activities": "A research guessing game, a pillar-spotting trainer, a topic-or-Big-Idea judge plus a private Big Idea drafter, a Sparkline beat tagger, a graded SCQA Exec Briefing Lab where the executive room reacts to each choice, a delivery-fix trainer, a live timed speaking round for every participant, a judge-the-bridge Q&A trainer with live rapid fire, inline knowledge checks, a scored recap, and the Presentation Rebuild capstone.",
        "outcomes": "Learners leave with one real presentation rebuilt: a one-sentence Big Idea, a structure chosen for the actual audience (Sparkline or SCQA), the literal opening line written and spoken aloud, one deck vice named and cut, and a rehearsal committed. Learning is measured in session (trainer scores, the graded briefing lab, a recap mapped to the six objectives, and the live round itself), at close (readiness check and a spoken structure-plus-opening-line commitment), and after (a 7-day pulse on the delivered talk and a 30/60/90-day structure check on whether decks are shifting from bullet-heavy to story-led and answer-first).",
        "takehomes": [
            ("Printable cheat sheet", "https://me5231979.github.io/Presentation-Public-Speaking/cheatsheet.html"),
            ("Rebuild worksheet", "https://me5231979.github.io/Presentation-Public-Speaking/worksheet.html")
        ],
        "learner": "https://me5231979.github.io/Presentation-Public-Speaking/",
        "facilitator": "https://me5231979.github.io/Presentation-Public-Speaking/facilitator/",
        "frameworks": "Grounded in Nancy Duarte's Presentation Principles (Big Idea™, Presentation Sparkline™; TEDxEast), Barbara Minto's Pyramid Principle and SCQA (McKinsey), Chris Anderson's 'How to Give a Killer Presentation' (HBR/TED), Carmine Gallo's 'What It Takes to Give a Great Presentation' (HBR), the AMA's Seven Principles of Effective Public Speaking and Effective Executive Speaking curriculum, SHRM's six pre-speaking questions, Coqual/Hewlett's Executive Presence research, Deloitte's CFO Signals survey, and the Chapman Survey of American Fears."
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
  .pills { display: flex; flex-wrap: wrap; gap: 5px; margin: 0 0 4px; }
  .pill { display: inline-block; font-family: 'Antonio', Impact, sans-serif; font-weight: 700;
    text-transform: uppercase; letter-spacing: .05em; font-size: 9.5px; line-height: 1.4;
    padding: 3px 9px; border-radius: 999px; border: 1px solid rgba(148,110,36,.5); color: #946E24; }
  .pill--core { background: #CFAE70; border-color: #CFAE70; color: #1C1C1C; }
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
    pills = ''.join(f'<span class="pill pill--core">{esc(x)}</span>' for x in c.get('coreSkills', [])) + \
            ''.join(f'<span class="pill">{esc(x)}</span>' for x in c.get('skills', []))
    topics = ''.join(f'<li><b>{esc(t)}.</b> {esc(d)}</li>' for t, d in c['topics'])
    takehomes = ' · '.join(f'<a href="{u}">{esc(n)}</a>' for n, u in c['takehomes'])
    link_lines = [
        f'<b>Take the course:</b> <a href="{c["learner"]}">{c["learner"].replace("https://","")}</a>',
        f'<b>Deliver it (facilitator edition):</b> <a href="{c["facilitator"]}">{c["facilitator"].replace("https://","")}</a>'
    ]
    if c.get('selfpaced'):
        link_lines.append(f'<b>Self-paced edition:</b> <a href="{c["selfpaced"]}">{c["selfpaced"].replace("https://","")}</a>')
    if takehomes:
        link_lines.append(f'<b>Take-homes:</b> {takehomes}')
    links = '<br>\n    '.join(link_lines)
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
      <p class="eyebrow">Vanderbilt · Staff Learning Collection · Course description</p>
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

  <h2>Skills this course builds</h2>
  <div class="pills">{pills}</div>

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
    {links}
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
