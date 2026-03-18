# Design Review — Grading Rubric

**Assignment:** Design Review (Capstone Checkpoint 1)
**Course:** CS-AI-2025 — Building AI-Powered Applications | Spring 2026
**Type:** Team submission (one PDF per team, submitted by team lead)
**Due:** Thursday 2 April 2026 at 23:59
**Total Points:** 10.0
**Capstone Weight:** 10 of 45 capstone points

---

## Summary Rubric

| Section | Max Points | Primary check |
|---------|-----------|---------------|
| 1. Problem Statement and Real User Need | 2.0 | Specificity, evidence, honest problem description |
| 2. Proposed Solution and AI-Powered Differentiator | 2.0 | Clear product, genuine AI value, non-AI comparison |
| 3. Technical Architecture with Diagram | 2.5 | Complete stack, architecture diagram present, data flow |
| 4. Risk and Failure Mode Analysis | 1.5 | AI-specific risks, concrete mitigations |
| 5. Team Roles and Week-by-Week Plan | 1.5 | Named ownership, realistic timeline, milestone alignment |
| 6. IRB-Light Checklist | 0.5 | All six questions answered explicitly |
| **Total** | **10.0** | |

**Automatic deductions:**
- **-1.0** if architecture diagram is absent (a text-only Section 3 cannot score above 1.5 regardless of quality)
- **-0.5** if the document is submitted as `.docx` or `.pages` rather than PDF
- **-0.5** if the document does not include all six required sections (even if partially completed)

**Late penalty:** 1.0 point per 24 hours after Thursday 2 April 23:59. Zero after 5 days.

---

## Section 1: Problem Statement and Real User Need (2.0 pts)

This is the most heavily weighted single section per point value. Everything else in the Design Review flows from having a clearly defined problem and user. Graders will spend proportionally more time here.

### What graders look for

**User specificity:** The document must name a type of user with enough detail to be real. "Students" earns 0 specificity points. "Second-year medical students in Georgia studying anatomy without cadaver access" earns full specificity points. The user description should be specific enough that a stranger could identify whether they qualify.

**Problem evidence:** The strongest submissions cite primary research — talking to real users. Acceptable alternatives: pointing to a documented workaround (something people already do to cope with the problem), citing a published source about the problem space, or referencing a statistic about the problem's frequency or cost. "We assume this is a problem" is not evidence.

**Problem-solution distinction:** The problem statement must describe the world without the solution. Submissions that conflate problem and solution ("The problem is that there is no app that...") will lose points in this section regardless of how good the rest of the document is.

**Cost of the problem:** At least one quantified cost — time, money, error rate, missed opportunity, or documented risk.

### Scoring anchors

| Score | Criteria |
|-------|---------|
| 2.0 | Specific named user type; clear evidence of real problem (primary or secondary); compelling statement of current inadequacy; at least one quantified cost |
| 1.5 | Good user specificity; problem is clear and believable; some evidence present but not primary research |
| 1.0 | User and problem described but vague; evidence is thin or implied rather than cited |
| 0.5 | Problem implied rather than stated; user is "everyone" or "people who need X" |
| 0.0 | No problem statement, or problem is entirely constructed around the technology ("the problem is that AI has not been applied to X") |

---

## Section 2: Proposed Solution and AI-Powered Differentiator (2.0 pts)

### What graders look for

**Product clarity:** A reader with no prior knowledge should understand what the application does after reading this section. The description should cover: what the user does, what the app does in response, and what the outcome is.

**Feature specificity:** 3–5 core features listed with user benefits (not just feature names). "Image upload" is a feature name. "Upload a receipt photo and receive itemised line items extracted automatically" describes a feature with a benefit.

**Genuine AI differentiator:** The document must explicitly name the AI capability being used (vision, text generation, structured extraction, RAG, function calling) and explain why it fits the problem. Vague statements ("uses AI to analyse data") will not earn the differentiator points. The test: would removing the AI make the product substantially worse or impossible?

**Non-AI comparison:** A brief description of what the non-AI version of the product looks like and why it is inferior. This is a simple but high-signal indicator that the team has thought carefully about whether AI is actually necessary.

### Scoring anchors

| Score | Criteria |
|-------|---------|
| 2.0 | Clear product description; 3+ features with user benefits; specific AI capability named and justified; non-AI comparison present |
| 1.5 | Features clear; AI role described but justification is thin or generic |
| 1.0 | Product concept clear but AI role is vague ("uses AI to improve results") |
| 0.5 | Features listed without user benefits; AI not clearly differentiated from "it uses an AI API" |
| 0.0 | No solution description |

---

## Section 3: Technical Architecture with Diagram (2.5 pts)

This is the most points-dense section. A high-quality architecture section can significantly elevate a weak submission elsewhere.

### Architecture diagram requirement

The diagram must show:
- User / browser
- Frontend (framework named on the diagram)
- Backend or API layer (language/framework named)
- AI model call (model string or model family named)
- Data storage, if applicable
- Data flow arrows connecting all components

Acceptable formats: Miro, draw.io, Excalidraw, Figma, hand-drawn photograph, whiteboard photograph. Any diagram that shows all required components and data flow arrows earns the diagram points. A polished diagram earns no more than a rough but complete diagram.

**A text-only architecture section cannot score above 1.5 points regardless of quality.** The diagram is required.

### What graders look for

**Full technology stack:** Every layer named — frontend framework, backend language and framework, database (if applicable), AI model(s) with the specific model strings or model family, hosting for frontend and backend separately.

**Justified choices:** One sentence of justification per major technology choice. "We chose Next.js because it is fast" is not justification. "We chose Next.js because server-side rendering reduces the perceived latency for the document analysis results page" is justification.

**Data flow:** The path of data from user input to AI model response to user display must be explicitly described for the core feature. This can be a numbered list of steps.

### Scoring anchors

| Score | Criteria |
|-------|---------|
| 2.5 | Complete architecture diagram with all required elements; full stack with reasoned choices; clear step-by-step data flow for core feature |
| 2.0 | Diagram present with most elements; stack described; minor gaps in justification or data flow |
| 1.5 | Diagram present but missing key elements (no data flow arrows, AI model not named); or full stack described in text without a diagram |
| 1.0 | Partial architecture, no diagram; or diagram present but stack description very thin |
| 0.5 | Vague architecture description without stack details |
| 0.0 | No architecture section; or architecture describes ideal future state rather than what the team will actually build |

---

## Section 4: Risk and Failure Mode Analysis (1.5 pts)

### What graders look for

**Minimum three failure modes.** Fewer than three failure modes will not earn full marks regardless of quality.

**At least one AI-specific failure mode.** Generic software risks (server downtime, no internet connection) are necessary but insufficient. The submission must demonstrate that the team understands how AI can fail specifically — accuracy failures, hallucinations, confidence miscalibration, capability limits.

**Concrete mitigations.** "We will test carefully" is not a mitigation. A mitigation is a specific design decision, fallback path, or engineering choice that reduces the likelihood or impact of the failure. "If the extraction confidence is LOW, the field is hidden and the user must enter it manually" is a mitigation.

**Honesty.** Submissions that only list low-risk scenarios are penalised. The grader expects to see at least one failure mode with High impact. Acknowledging a genuine risk and mitigating it scores higher than pretending the risk does not exist.

### Scoring anchors

| Score | Criteria |
|-------|---------|
| 1.5 | 3+ failure modes; at least one AI-specific; at least one High-impact risk present; all mitigations are concrete and specific |
| 1.0 | 2–3 failure modes; mitigation present but some are generic; AI-specific risk may be present |
| 0.5 | Risks listed but no mitigations, or only one failure mode described |
| 0.0 | No risk section, or only trivial risks with no AI-specific content |

---

## Section 5: Team Roles and Week-by-Week Plan (1.5 pts)

### What graders look for

**Named ownership:** Each team member is assigned ownership of specific areas. "Everyone does everything" is not an acceptable role structure.

**Realistic timeline:** The plan must map from the current week (Week 2) through the Peer Review Presentation (Week 12). Plans that only describe the first 4 weeks will lose points. Plans that show unrealistically heavy delivery in the final week before Demo Day signal poor planning.

**Capstone milestone alignment:** The plan must acknowledge the course-defined checkpoints: Design Review (Week 4), Safety Audit (Week 11), Peer Review Presentation (Week 12), Demo Day (Week 15).

**Honest risk acknowledgment:** At least one week or deliverable should be identified as high-risk with a brief explanation. Teams that present a uniform "steady progress every week" plan are either not thinking about real constraints or are not being honest.

### Scoring anchors

| Score | Criteria |
|-------|---------|
| 1.5 | Named roles with specific ownership; timeline covers Weeks 2–12; capstone milestones mapped; at least one week identified as high-risk |
| 1.0 | Roles assigned; timeline present but some weeks are vague or uncovered; milestones partially mapped |
| 0.5 | Roles listed without meaningful differentiation; timeline covers only the first few weeks |
| 0.0 | No team structure or plan |

---

## Section 6: IRB-Light Checklist (0.5 pts)

All six questions must be answered explicitly with Yes/No and a one-sentence explanation for any "yes" answer.

If any answer is "yes," a data handling and consent approach paragraph must be present.

| Score | Criteria |
|-------|---------|
| 0.5 | All six questions answered with Yes/No; "yes" answers include explanations; if any "yes," consent approach is described |
| 0.25 | Most questions answered; some "yes" answers lack explanation |
| 0.0 | Section skipped; fewer than four questions answered |

---

## Automatic Deductions

| Deduction | Condition |
|-----------|-----------|
| -1.0 | Architecture diagram absent (Section 3 cannot exceed 1.5 without a diagram) |
| -0.5 | Submitted as .docx or .pages rather than PDF |
| -0.5 | Any of the six required sections is absent from the document |

---

## Common Mistakes

**Conflating the problem and the solution.** "The problem is that there is no app that reads prescriptions automatically" describes a solution gap, not a problem. The problem is: "Pharmacists spend 2.5 hours per day manually transcribing prescriptions, and 1 in 150 contains a transcription error."

**"AI" as a vague ingredient.** Saying "our app uses AI to analyse data and provide insights" tells the grader nothing. Name the model. Name the capability. Explain what it does in one sentence that a non-technical person could understand.

**Architecture diagram missing.** The most common reason for a Section 3 score below 2.0. Even a hand-drawn photograph of a whiteboard sketch is sufficient. Add it.

**Risk section is a formality.** Teams that write "the AI might give wrong answers — we will test it" in the risk section are treating this section as overhead. It costs them 0.5–1.0 points. The risk section should read like a team that has genuinely thought about how their product could harm a user.

**Timeline ends at Week 5.** The plan must cover through Week 12 (Peer Review Presentation). Graders will not give full marks to a plan that trails off.

**IRB checklist skipped.** This section is 0.5 points and takes 10 minutes. Skipping it for lack of time is an avoidable loss.

---

*Grading Rubric for CS-AI-2025 Lab 2 Design Review, Spring 2026.*
*Questions about scoring: post in the course forum or email zeshan.ahmad@kiu.edu.ge*
