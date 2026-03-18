# Design Review Guide

**The first formal capstone checkpoint — due Thursday 2 April 2026 at 23:59**
**Worth 10 points toward your capstone grade**

---

## What the Design Review Is

The Design Review is not a project proposal in the traditional academic sense. It is a design document — a written record of a decision your team has made and can defend.

The distinction matters. A proposal says "here is what we are thinking of doing." A design document says "here is what we are doing, here is why we chose it, here is how it will work, and here is what could go wrong."

Graders are not looking for a perfect idea. They are looking for evidence of rigorous thinking. A team that picks a modest, well-defined project and demonstrates that they have thought carefully about risks and architecture will outscore a team that picks a grandiose idea and describes it superficially.

---

## What You Submit

A single PDF, submitted via the course LMS by your team lead, before **Thursday 2 April 2026 at 23:59**.

File naming convention: `[TeamName]-DesignReview-CS-AI-2025.pdf`

The document should be 4–8 pages of content. Not shorter (you will not have covered all the required sections), not much longer (concision is a skill the graders are evaluating).

Start from the template: [`../templates/design-review-template.md`](../templates/design-review-template.md)

---

## Scoring Breakdown

| # | Section | Points | What graders look for |
|---|---------|--------|-----------------------|
| 1 | Problem Statement and Real User Need | 2.0 | Specificity of user, evidence of problem, non-obvious need |
| 2 | Proposed Solution and AI-Powered Differentiator | 2.0 | Clear product description, genuine AI value, not AI-as-decoration |
| 3 | Technical Architecture with Diagram | 2.5 | Complete stack, sensible choices, architecture diagram present |
| 4 | Risk and Failure Mode Analysis | 1.5 | Honest acknowledgment of AI limitations, mitigation strategies |
| 5 | Team Roles and Week-by-Week Plan | 1.5 | Clear ownership, realistic timeline, milestone alignment |
| 6 | IRB-Light Checklist | 0.5 | Data handling questions answered explicitly |
| **Total** | | **10.0** | |

**Late penalty:** 1 point deducted per 24 hours. Submissions more than 5 days late receive 0.

---

## Section-by-Section Guidance

### Section 1: Problem Statement and Real User Need (2.0 pts)

This is the most important section. Everything else follows from having a clearly defined problem and a clearly defined user.

**What graders want to see:**
- A named user type with enough specificity to be real. "Students" is too vague. "Second-year medical students in Georgia studying anatomy without cadaver access" is specific.
- Evidence that the problem is real. The best evidence is talking to an actual user. Second-best is pointing to a documented workaround (something people already do to cope with the problem). Third-best is citing a published source about the problem space.
- A clear statement of what the world looks like without your solution. What does the user currently do? Why is that inadequate?

**Common mistakes:**
- Describing a problem only you have (validate with at least 3 people outside your team)
- Conflating the problem and the solution ("The problem is that there is no app that...")
- Assuming the problem is obvious and not actually describing it

**Scoring anchors:**
- **2.0** — Specific user, clear evidence of real problem, compelling statement of current inadequacy
- **1.5** — Good user specificity, problem is clear, some evidence present
- **1.0** — User and problem described but vague; could apply to many things
- **0.5** — Problem is implied but not explicitly stated, or user is "everyone"
- **0.0** — No problem statement

---

### Section 2: Proposed Solution and AI-Powered Differentiator (2.0 pts)

Describe what your application does. Then explain what AI specifically contributes.

**What graders want to see:**
- A clear description of 3–5 core features
- An explicit statement of which feature is the AI-powered differentiator — the thing that would not exist or would be substantially worse without AI
- A statement of which AI capability (from the course syllabus) is being used and why it fits the problem
- A brief description of what the non-AI version of this product would look like and why it is inferior

**Common mistakes:**
- Describing features without explaining the user benefit
- Using AI for a task where a simple keyword search or rule-based system would work equally well
- Listing AI as a feature without explaining what it actually does

**Scoring anchors:**
- **2.0** — Clear features, specific AI capability named and justified, non-AI comparison present
- **1.5** — Features clear, AI role described but justification is thin
- **1.0** — Product concept clear but AI role is vague ("uses AI to improve results")
- **0.5** — Features listed without clear AI role
- **0.0** — No solution description

---

### Section 3: Technical Architecture with Diagram (2.5 pts)

This section requires a diagram. A text-only architecture section cannot score above 1.5 points.

**What graders want to see:**
- A diagram showing the major components and how they connect. It does not need to be polished — hand-drawn and photographed is fine. What matters is that all the components are present and the data flow makes sense.
- The full technology stack: frontend framework, backend language/framework, database (if applicable), AI model(s), hosting platform
- An explanation of why you chose each major component (one sentence per choice is enough)
- The data flow for the core user action: what happens when a user triggers the main AI feature?

**Required diagram elements:**
- User / browser
- Frontend (with framework named)
- Backend API (with language/framework named)
- AI model call (with model string named)
- Data storage (if applicable)
- Arrows showing data flow

**Common mistakes:**
- Architecture diagram missing
- Architecture describes ideal future state, not what you will actually build for the capstone
- No explanation of technology choices
- Data flow stops at "the AI processes it" without explaining what happens to the output

**Scoring anchors:**
- **2.5** — Complete diagram, full stack with justified choices, clear data flow for core feature
- **2.0** — Diagram present, stack described, minor gaps in justification or data flow
- **1.5** — Diagram present but incomplete, or full stack described without diagram
- **1.0** — Partial architecture, no diagram
- **0.0** — No architecture section

---

### Section 4: Risk and Failure Mode Analysis (1.5 pts)

This section separates good capstone projects from great ones. Every AI application fails in predictable ways. Demonstrating that you know your failure modes shows you have thought seriously about the product.

**What graders want to see:**
- At least three specific failure modes, each with a description of what happens when it occurs and a mitigation strategy
- At least one failure mode that is specific to AI (not just a generic software risk)
- For vision applications: explicit acknowledgment of where the vision model is unreliable and what the fallback is
- Honest assessment of the AI's capability limits for your specific use case

**Failure mode categories to consider:**
- AI accuracy failures (wrong output, hallucination, low confidence)
- Input failures (bad image quality, unsupported format, unexpected user input)
- API failures (rate limits, latency spikes, model downtime)
- Scope failures (feature too complex to build in time, dataset not available)
- User behaviour failures (users misuse the tool in ways you did not anticipate)

**What graders do not want:**
- "The AI might give wrong answers. We will test carefully." (too vague — what specifically could go wrong, and what specifically will you do about it?)
- Generic software risks only (no server, no internet) without AI-specific risks
- Risks listed without mitigation strategies

**Scoring anchors:**
- **1.5** — 3+ specific failure modes, at least one AI-specific, each with a concrete mitigation
- **1.0** — 2–3 failure modes described, mitigation present but generic
- **0.5** — Risks acknowledged but not analysed
- **0.0** — No risk analysis

---

### Section 5: Team Roles and Week-by-Week Plan (1.5 pts)

**What graders want to see:**
- Named roles for each team member (not just "frontend" — who specifically owns each area)
- A realistic week-by-week plan from Week 3 (now) through Week 12 (Peer Review Presentation)
- Milestones aligned with the course capstone checkpoints
- Honest assessment of which weeks will be hardest and why

**Role categories to consider:**
- Frontend development
- Backend / API integration
- AI integration and prompt engineering
- Testing and quality assurance
- Documentation and project management
- Design / UX (can be shared)

**Scoring anchors:**
- **1.5** — Named roles, realistic timeline, capstone milestones mapped, risk weeks identified
- **1.0** — Roles assigned, timeline present but some weeks are vague
- **0.5** — Roles listed without timeline, or timeline without role mapping
- **0.0** — No team structure or plan

---

### Section 6: IRB-Light Checklist (0.5 pts)

IRB stands for Institutional Review Board — the process universities use to ensure research involving human subjects is conducted ethically. Your capstone is not formal research, but the same questions apply.

Answer each question explicitly (yes/no, then a one-sentence explanation if yes):

1. Does your application collect images of real people?
2. Does your application process photographs of faces?
3. Does your application handle sensitive documents (medical, legal, financial, government IDs)?
4. Does your application store user-uploaded data? If yes, for how long and where?
5. Do users need to understand what happens to their data before using the application?
6. If any of the above are "yes": describe your consent flow. How does a user know what data is collected and how it is used?

**Scoring anchor:** Full 0.5 points for answering all six questions explicitly. Zero for skipping the section or answering vaguely.

---

## Tips for Scoring Well

**Be specific, not comprehensive.** A 2-page document with specific, well-reasoned content in each section scores higher than a 10-page document full of generic statements. Graders can tell the difference between genuine analysis and padded content.

**Name things.** "We will use a cloud database" is weaker than "We will use Supabase (PostgreSQL), hosted on their free tier." Specificity signals that you have actually made decisions, not just described a vague plan.

**Show your reasoning, not just your conclusions.** "We chose Next.js because it has good performance" is weak. "We chose Next.js over a pure React SPA because our product requires server-side rendering for the document analysis results page — SSR reduces the time from API response to visible output by approximately 300ms for the average user" is strong.

**The architecture diagram is not optional.** Even a rough sketch counts. Take a photo of a whiteboard drawing if nothing else. A diagram that covers all components and shows data flow will earn more points than a text description that does not.

**Start today.** The sections that take longest — risk analysis and architecture — require thought that cannot happen the night before. You have twelve days between this lab and the deadline. Use them.

---

*Design Review Guide for CS-AI-2025 Lab 2, Spring 2026.*
