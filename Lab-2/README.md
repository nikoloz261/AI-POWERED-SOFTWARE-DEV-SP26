# Lab 2 — From Ideas to Architecture

**Course:** CS-AI-2025 — Building AI-Powered Applications | Spring 2026
**Lab Date:** Friday 20 March 2026
**Group A:** 09:00 – 11:00 | **Group B:** 11:00 – 13:00
**Location:** Computer Lab, Kutaisi International University

---

## What This Lab Is For

Lab 1 was about individuals. Lab 2 is about teams and products.

By the end of today, your team will have done three things that cannot be undone:

1. **Converged on a single project idea** using a structured decision framework — the Four Filters
2. **Scaffolded a working application** using an AI-native development tool (Cursor, Claude Code, or Google AI Studio)
3. **Started the Design Review document** — the first formal capstone checkpoint, due Thursday 2 April at 23:59

This lab takes the individual brainstorming from Lab 1 (and from Homework 1's reflection questions) and turns it into a team commitment. You are not finalising every detail today. You are committing to a direction and proving you can build something.

---

## Prerequisites — Arrive Ready

Before you walk into this lab, you must have:

- [ ] Homework 1 submitted (GitHub link via LMS, due before this session starts)
- [ ] A rough project idea in your head — even a vague one is fine
- [ ] Your laptop with Python 3.10+ and Git working (from Lab 1)
- [ ] Your Gemini API key in a `.env` file and working
- [ ] Read your team's Lab 1 brainstorming notes (if you did team exercises)

If your HW1 is not submitted, do it now before the lab starts. The TA will check submission status at the start of the session.

---

## Lab Schedule

| Time | Activity | Duration | Who Leads |
|------|----------|----------|-----------|
| :00 | Arrival, HW1 check, team finalisation | 10 min | TA |
| :10 | Four Filters team convergence exercise | 30 min | Team |
| :40 | Builder Sprint — scaffold your application | 35 min | Team |
| :60 | (Short break — stretch, top up coffee) | 5 min | — |
| :65 | OpenRouter setup + first multimodal API call | 20 min | Team |
| :85 | Design Review document kickoff | 25 min | Team |
| :110 | Lab wrap-up, blockers, next steps | 10 min | Instructor / TA |
| :120 | End of lab | | |

*Group A runs 09:00 – 11:00. Group B runs 11:00 – 13:00. The schedule is identical for both groups.*

---

## How to Navigate This Lab

```
README.md  ← You are here. Start here every week.
    │
    ├── quickstart.md                   ← OpenRouter setup (do this at home if possible)
    │
    ├── guides/
    │   ├── four-filters-guide.md       ← The convergence framework — read before lab
    │   ├── builder-tools-guide.md      ← Cursor, Claude Code, AI Studio — which to use
    │   ├── openrouter-setup-guide.md   ← Getting your org API key working
    │   └── design-review-guide.md      ← What the Design Review requires and how to score well
    │
    ├── templates/
    │   ├── four-filters-template.md    ← Fill this in during the convergence exercise
    │   ├── design-review-template.md   ← The actual submission document — start this today
    │   └── team-repo-setup.md          ← Step-by-step: create your team GitHub repo
    │
    ├── examples/
    │   ├── four-filters-example.md     ← Completed example: MedScript AI
    │   ├── design-review-example.md    ← Completed Design Review for reference
    │   └── starter-code/
    │       ├── 01_openrouter_hello.py  ← First OpenRouter call (vision model)
    │       ├── 02_image_analyser.py    ← Image upload + analysis scaffold
    │       └── 03_multimodal_chat.py   ← Multi-turn conversation with image context
    │
    └── grading-rubric.md              ← Design Review grading criteria (10 pts)
```

---

## API Access — Which Tier Are You On?

**Check with your TA at the start of lab.** Depending on where we are in the org account setup, you will be on one of three tiers. The code is identical across all three — only your `.env` file changes.

| Tier | Situation | Key needed | Models |
|------|-----------|-----------|--------|
| **Tier 1** | OpenRouter org not yet active | `GEMINI_API_KEY` from Google AI Studio | Gemini 3 Flash free tier (from Lab 1) |
| **Tier 2** | Org pending, create personal OpenRouter account | Personal `OPENROUTER_API_KEY` | OpenRouter free-tier models + paid with own credits |
| **Tier 3** | Org credits confirmed, key distributed via LMS | Org `OPENROUTER_API_KEY` | Full model access, course-funded |

Full setup instructions for all three tiers: [`guides/openrouter-setup-guide.md`](./guides/openrouter-setup-guide.md)

**Primary models (Tiers 2 and 3 via OpenRouter):**

| Property | Standard — use for everything | Premium — sparingly |
|----------|------------------------------|---------------------|
| OpenRouter string | `google/gemini-3.1-flash` | `anthropic/claude-opus-4-6` |
| Vision | Yes | Yes |
| Input price | $0.10 / 1M tokens | $15.00 / 1M tokens |
| Output price | $0.40 / 1M tokens | $75.00 / 1M tokens |

**Tier 1 fallback (Google AI Studio direct, free):**

| Model string | Vision | Cost |
|-------------|--------|------|
| `gemini-3-flash-preview` | Yes | $0 free tier |

> **Credit discipline:** Whether you are spending your own money (Tier 2) or the course budget (Tier 3), use the cheapest model that meets your quality bar. `gemini-3.1-flash` handles all lab exercises. Document any decision to upgrade to a premium model in your Design Review.

---

## Key Concepts From Lecture 2 to Reinforce Today

These concepts from Thursday's lecture are directly exercised in this lab:

**Multimodal Pipeline** — Lecture 2 walked through the 6-stage vision pipeline: Input Capture → Preprocessing → Prompt Construction → API Inference → Confidence Scoring → UX Response. The starter code in Exercise 2 implements this pipeline. Understand each stage as you build it, not after.

**Capability Split** — Vision models are reliable at description, OCR, and document understanding. They are unreliable at precise counting, spatial coordinates, and subtle distinction. Your Design Review must acknowledge which category your use case falls into.

**Confidence-Aware UX** — Every field your application extracts from an image should carry a confidence signal. HIGH shows directly. MEDIUM prompts verification. LOW routes to human review. This is not optional design — it is the difference between a prototype and a product.

**Four Filters** — Not a lecture concept but a lab tool introduced today. Teams that skip the convergence exercise and jump straight to building consistently pick the wrong idea. The 30 minutes you spend on Four Filters will save 3 weeks of rebuilding.

---

## The Capstone Design Review — Due Thursday 2 April 23:59

The Design Review is the first formal capstone checkpoint. It is worth **10 points** toward your capstone grade (45 points total).

This is not a proposal in the traditional sense. It is a design document — a written record of a decision your team has made and can defend. The grader is not looking for a perfect idea. They are looking for evidence that your team has thought hard, stress-tested the idea, and made a deliberate choice.

**What you submit:** A single PDF, submitted via the course LMS by the team lead, before Thursday 2 April at 23:59.

**Required sections:**

| # | Section | Points |
|---|---------|--------|
| 1 | Problem Statement and Real User Need | 2.0 |
| 2 | Proposed Solution and AI-Powered Differentiator | 2.0 |
| 3 | Technical Architecture (with diagram) | 2.5 |
| 4 | Risk and Failure Mode Analysis | 1.5 |
| 5 | Team Roles and Week-by-Week Plan | 1.5 |
| 6 | IRB-Light Checklist | 0.5 |
| **Total** | | **10.0** |

Full rubric: [`grading-rubric.md`](./grading-rubric.md). Template to fill in: [`templates/design-review-template.md`](./templates/design-review-template.md). Completed example: [`examples/design-review-example.md`](./examples/design-review-example.md).

**Late penalty:** 1 point per 24 hours. After 5 days, the submission receives 0.

---

## Team Finalisation

If your team is not yet finalised, this happens in the first 10 minutes of the lab. Rules:

- Teams are **3 or 4 students**. No teams of 2. No solo capstone projects.
- Once formed, teams are **locked** unless there is a documented exceptional circumstance approved by the instructor.
- Each team must: choose a team name, designate a team lead (LMS submission point), create a shared GitHub organisation or repo before leaving lab today.
- See [`templates/team-repo-setup.md`](./templates/team-repo-setup.md) for the repo creation steps.

---

## Common Mistakes to Avoid Today

**Do not skip the Four Filters.** It feels like overhead when you are eager to build. Teams that skip it consistently waste time building something nobody on the team is excited about, or building something that turns out to be technically impossible for the capstone scope.

**Do not use the premium model for exercises.** Save `claude-opus-4-6` for high-stakes analysis in your capstone. Use the Flash tier for today's starter code exercises.

**Do not commit your API key.** Same rule as Lab 1. The key goes in `.env`. The `.env` goes in `.gitignore`. The `.env.example` goes in the repo with placeholder values only.

**Do not use premium models for exercises.** Save `claude-opus-4-6` and `gemini-3.1-pro` for specific, justified capstone needs. `gemini-3.1-flash` handles all of today's exercises. If you are on Tier 2 with personal credits, this is your own money.

**Do not accept AI-generated code you have not read.** Cursor, Claude Code, and AI Studio will generate scaffold code quickly. Read every file before you commit it. You are responsible for code in your repo.

---

## Resources

**In This Lab Folder:**
- [Quickstart](./quickstart.md) — OpenRouter setup, fastest path
- [Four Filters Guide](./guides/four-filters-guide.md) — convergence framework
- [Builder Tools Guide](./guides/builder-tools-guide.md) — Cursor, Claude Code, AI Studio
- [OpenRouter Setup Guide](./guides/openrouter-setup-guide.md) — API key, credits, cost tracking
- [Design Review Guide](./guides/design-review-guide.md) — how to write a strong Design Review
- [Design Review Template](./templates/design-review-template.md) — fill this in today
- [Grading Rubric](./grading-rubric.md) — 10-point Design Review scoring

**External:**
- [OpenRouter Documentation](https://openrouter.ai/docs) — API reference
- [Cursor](https://cursor.com) — AI-native code editor, recommended for the builder sprint
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — terminal-based agentic coding tool
- [Google AI Studio](https://aistudio.google.com) — browser-based code generation, zero install
- [Course GitHub](https://github.com/ZA-KIU-Classroom/AI-POWERED-SOFTWARE-DEV-SP26) — lab materials

**Questions?**
- During lab: raise your hand or approach the TA
- After lab: course forum (preferred — others benefit)
- Email: zeshan.ahmad@kiu.edu.ge — 48-hour response on weekdays
- Office hours: email to book a Google Meet slot

---

## Looking Ahead: What Lab 3 Will Expect

Lab 3 (Friday 27 March) is your first **working prototype lab**. By then, your team should have:
- A submitted Design Review (due 2 April — you have time, but start today)
- A team GitHub repo with the scaffold from today pushed and visible
- OpenRouter working and the multimodal pipeline running end-to-end
- A clear understanding of which AI capability is central to your product

Lab 3 will introduce image generation and audio I/O — two capabilities your capstone may use. You will integrate at least one into your prototype by the end of Lab 3.

---

*Lab materials for CS-AI-2025 Spring 2026.*
*Course repo: [github.com/ZA-KIU-Classroom/AI-POWERED-SOFTWARE-DEV-SP26](https://github.com/ZA-KIU-Classroom/AI-POWERED-SOFTWARE-DEV-SP26)*
*Last updated: March 2026.*
