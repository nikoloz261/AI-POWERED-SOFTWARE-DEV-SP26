# The Four Filters: A Team Convergence Framework

**Time budget for this exercise in lab: 30 minutes**

---

## Why You Need a Convergence Framework

You have spent a week thinking about project ideas. Your teammates have spent a week thinking about different ideas. Left to their own devices, teams at this stage fall into one of three failure modes:

**The loudest voice wins.** The most confident person advocates for their idea, the team defers to avoid conflict, and three weeks later nobody is motivated to work on a project they did not choose.

**The committee compromise.** Every idea gets merged into an ever-growing feature list. The project scope becomes unmanageable and the team has no clear focus.

**Analysis paralysis.** The team cannot decide between two good ideas and spends two weeks going back and forth while the semester moves on without them.

The Four Filters is a structured way to run a 30-minute team decision that produces a genuine consensus, surfaces the ideas most likely to succeed, and leaves everyone feeling that the process was fair — even if their original idea was not selected.

---

## The Four Filters

Each idea your team is considering gets passed through four filters in sequence. An idea must pass all four to be seriously considered. An idea that fails a filter is not necessarily dead — it might be scaled back or pivoted until it passes.

---

### Filter 1: The Problem Filter

**Question to answer:** Does a real problem exist, and do real people have it?

A real problem is one that someone currently experiences and would pay money (or meaningful effort) to solve. It is not a problem you invented to justify a technology you wanted to use.

Ask for each idea:
- Who specifically has this problem? (Name a type of person, not "everyone")
- How do they currently solve it? (Workarounds count — they prove the problem is real)
- What is the cost of the problem not being solved? (Time, money, frustration, risk)
- Can you reach a real user of this type in the next two weeks to validate your assumption?

**Fail signals:**
- "Everyone has this problem" (too vague — who specifically?)
- "There's no good solution right now" (almost never true — there is always a workaround)
- "I would use this" (you are a CS student, not a representative user for most domains)
- The problem only exists if the technology exists (a solution in search of a problem)

**Pass signal:** You can name a specific type of person, describe their current workaround, and explain why your solution is meaningfully better.

---

### Filter 2: The AI Filter

**Question to answer:** Does AI meaningfully improve the solution, or is it decoration?

Many "AI applications" are CRUD apps with a chatbot bolted on. The AI does not improve the core value proposition — it is just there because AI is fashionable.

A genuine AI application is one where removing the AI would make the product substantially worse or impossible.

Ask for each idea:
- What does AI specifically do in this product? (Name the capability: vision, text generation, classification, extraction, generation, reasoning)
- What would the product look like without AI? Would it still be useful?
- Is the AI doing something that was impossible or impractically expensive before?
- Which lecture topic (Week 2: vision, Week 3: image gen, Week 4: audio, Week 5: RAG...) does this use most heavily?

**Fail signals:**
- "AI summarises user content" (often marginal value — summarisation is a weak AI differentiator)
- "AI helps users write things" (extremely crowded, very hard to differentiate)
- "AI provides recommendations" (needs to be grounded in something specific and proprietary)
- The same product would work 80% as well with a simple search and filter

**Pass signal:** There is a specific AI capability (from the course syllabus) that is core to the product's value, and the product would be fundamentally broken without it.

---

### Filter 3: The Feasibility Filter

**Question to answer:** Can this team build a working demo by Week 12?

Week 12 is your Peer Review Presentation. You need a working, demonstrable product — not a prototype that "mostly works" under controlled conditions. This filter is about honest self-assessment.

Ask for each idea:
- What APIs does this require? Are they available, affordable, and accessible?
- Does this require training a custom model? (Almost certainly no — reframe around inference)
- Does this require a dataset you do not have? (Where will you get it?)
- What is the hardest technical problem in this project? Does anyone on the team know how to solve it, or can they learn it in time?
- Does this involve user-generated data at scale? (Dangerous scope creep)
- Does this require regulatory compliance (HIPAA, GDPR, financial regulations)? (Possible but must be explicit)

**Fail signals:**
- Requires fine-tuning or training a model from scratch
- Requires a proprietary dataset you cannot obtain
- Requires hardware you do not have (robotics, sensors, edge devices)
- Core value depends on having many users (social/network effects are not a feature you can build)
- Three of the five core features are completely unknown territory for the whole team

**Pass signal:** The hardest part is hard, not impossible. The team has a realistic path to a working demo using APIs that exist today, at costs you can afford with the semester credit allocation.

---

### Filter 4: The Motivation Filter

**Question to answer:** Will this team still be excited about this in Week 10?

This is the filter most teams skip, and it is the one that most often kills projects. Technical problems are solvable. Motivation collapse is not.

Ask for each idea:
- If this project goes perfectly, what does the demo look like? Does thinking about that make you excited?
- Is there a person on this team who cares about this problem domain, not just the technology?
- Would you be proud to show this to someone outside the course?
- Is there a version of this that could exist beyond the course — as an actual product, a portfolio piece, a startup idea?

**Fail signals:**
- "It would be a good portfolio piece" (thin motivation — everyone's portfolio piece looks the same)
- "It seems technically interesting" (interesting problems are everywhere — you need more than that)
- Nobody on the team has domain expertise or personal connection to the problem
- You would not tell your parents about this project

**Pass signal:** At least one team member would build this outside class if the course did not require it. The rest of the team is genuinely interested, not just willing.

---

## Running the Exercise (30 minutes)

### Step 1: Surface all ideas (5 minutes)
Each team member names their top idea from their Lab 1 brainstorming and HW1 reflection. One person records all ideas in the Four Filters template. No discussion yet — just surface them.

### Step 2: Quick filter pass (10 minutes)
Go through each idea and apply the four filters quickly. Rate each idea on a simple 3-point scale per filter:
- ✓ Clear pass
- ? Needs work but possible
- ✗ Clear fail

This is not a deep analysis — it is triage. You are looking for which ideas survive all four filters at the "?" level or better.

### Step 3: Deep dive on survivors (10 minutes)
For each idea that survived the quick pass, spend 2–3 minutes on the weakest filter. What would need to be true for that filter to be a clear pass? Can the idea be reshaped to address the weakness?

### Step 4: Decision (5 minutes)
If one idea is clearly stronger across all four filters, choose it. If two ideas are comparable, use a simple vote with each team member ranking their top two. Take the option with the highest combined ranking. Record the decision in the template and move on.

> **Rule:** Once the decision is made in this exercise, it is final for today. No relitigating in the builder sprint. Debate is valuable before the decision; it is destructive after.

---

## What to Do With a Failed Idea

A failed idea is not wasted. Ideas that fail Filter 1 (no real problem) often contain a genuine technical interest that can be redirected to a different problem domain. Ideas that fail Filter 3 (too complex) often have a simpler version inside them. Ask: "What is the smallest version of this idea that still passes all four filters?"

Some of the strongest capstone projects have come from stripping an ambitious idea down to its essential AI insight and building that well.

---

## Deliverable From This Exercise

Complete [`../templates/four-filters-template.md`](../templates/four-filters-template.md) as a team before moving to the Builder Sprint. The completed template does not need to be submitted anywhere — it is your internal working document. The Design Review (due 2 April) will build on this analysis.

See [`../examples/four-filters-example.md`](../examples/four-filters-example.md) for a completed example.

---

*Four Filters Guide for CS-AI-2025 Lab 2, Spring 2026.*
