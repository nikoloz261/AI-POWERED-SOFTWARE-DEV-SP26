# Design Review: [Team Name]

**Course:** CS-AI-2025 — Building AI-Powered Applications | Spring 2026
**Team Name:** [Your team name]
**Team Members:** [Name 1] | [Name 2] | [Name 3] | [Name 4 if applicable]
**Team Lead (LMS submitter):** [Name]
**Submission Due:** Thursday 2 April 2026 at 23:59
**Total Points:** 10

---

> **How to use this template:**
> Fill in every section. Delete all instructional text in italics before submitting.
> Export as PDF. File name: `[TeamName]-DesignReview-CS-AI-2025.pdf`
> Submit via course LMS before the deadline. Only one submission per team (team lead submits).

---

## Section 1: Problem Statement and Real User Need (2.0 pts)

### 1.1 — Who has this problem?

*Describe your target user specifically. Not "students" but "second-year medical students at universities without access to cadaver labs." Not "small businesses" but "Georgian restaurant owners managing menus in two languages for tourist-facing apps." The more specific, the better.*

[Your answer here]

---

### 1.2 — What is the problem?

*Describe the problem clearly. One paragraph. Avoid describing your solution here — just the problem.*

[Your answer here]

---

### 1.3 — How do they currently solve it?

*What is the existing workaround? If no workaround exists, explain what happens as a result of the problem going unsolved. Evidence of a real workaround is strong evidence of a real problem.*

[Your answer here]

---

### 1.4 — What is the cost of this problem?

*Quantify where possible. Time lost, money spent on workarounds, mistakes made, opportunities missed, frustration experienced. At least one of these should be specific.*

[Your answer here]

---

### 1.5 — Evidence of the problem

*Did you talk to any real users? If yes, summarise what you learned in 2–3 sentences. If no, cite a credible source (published article, report, or documented practice) that validates the problem. "We assume this is a problem" is not evidence.*

[Your answer here]

---

## Section 2: Proposed Solution and AI-Powered Differentiator (2.0 pts)

### 2.1 — What does your application do?

*One clear paragraph describing the product. Imagine you are explaining it to an intelligent person who has never heard of it. What does the user do? What does the app do in response? What is the outcome?*

[Your answer here]

---

### 2.2 — Core features (3–5)

*List the core features. For each one, state the user benefit in one sentence.*

| Feature | What the user can do | Why this matters |
|---------|---------------------|-----------------|
| 1. | | |
| 2. | | |
| 3. | | |
| 4. | | |
| 5. | | |

---

### 2.3 — The AI-powered differentiator

*Which feature is the one that would not exist or would be substantially worse without AI? Explain the specific AI capability being used (vision, text generation, extraction, classification, RAG, function calling) and why it fits this problem.*

[Your answer here]

---

### 2.4 — What would the non-AI version look like?

*Describe the product without AI. Is it still useful? Why is AI the right tool here, not a simpler approach?*

[Your answer here]

---

## Section 3: Technical Architecture (2.5 pts)

### 3.1 — Architecture Diagram

*Insert your architecture diagram here. A hand-drawn photo is acceptable. The diagram must show: user/browser, frontend, backend (if applicable), AI model call, data storage (if applicable), and data flow arrows.*

[Insert diagram image here — PNG, JPG, or draw.io screenshot all acceptable]

---

### 3.2 — Technology Stack

*Fill in your full stack. For each choice, give a one-sentence justification.*

| Layer | Technology | Why this choice |
|-------|-----------|-----------------|
| Frontend framework | | |
| UI library / styling | | |
| Backend language | | |
| Backend framework | | |
| Database (if used) | | |
| AI model(s) | | |
| AI access method | OpenRouter via `openai` SDK | Course standard — provides access to all models with one API key |
| Hosting — frontend | | |
| Hosting — backend | | |
| Version control | GitHub | Course standard |

---

### 3.3 — Core Data Flow

*Describe what happens step by step when a user triggers the main AI feature. Be specific about what data moves and where.*

Example format:
1. User uploads an image via the upload component
2. Frontend sends the image as base64 to the backend API endpoint `/api/analyse`
3. Backend preprocesses the image (resizes to max 1024px, strips EXIF metadata)
4. Backend calls OpenRouter with the processed image and a structured prompt
5. OpenRouter routes to `google/gemini-3.1-flash` and returns the response
6. Backend parses the response and extracts structured JSON
7. Backend returns the structured data to the frontend
8. Frontend displays results in the results panel with confidence indicators

[Your data flow here — numbered steps like the example above]

---

## Section 4: Risk and Failure Mode Analysis (1.5 pts)

*Identify at least three specific failure modes. At least one must be AI-specific. For each, describe what happens when it occurs and your mitigation strategy.*

---

### Risk 1: [Name the failure mode]

**What happens when this occurs:**

[Describe the failure scenario concretely]

**Likelihood:** Low / Medium / High

**Impact on user:** Low / Medium / High

**Mitigation strategy:**

[Specifically how you will handle or prevent this]

---

### Risk 2: [Name the failure mode]

**What happens when this occurs:**

[Describe the failure scenario concretely]

**Likelihood:** Low / Medium / High

**Impact on user:** Low / Medium / High

**Mitigation strategy:**

[Specifically how you will handle or prevent this]

---

### Risk 3: [Name the failure mode]

**What happens when this occurs:**

[Describe the failure scenario concretely]

**Likelihood:** Low / Medium / High

**Impact on user:** Low / Medium / High

**Mitigation strategy:**

[Specifically how you will handle or prevent this]

---

*(Add more risks if applicable — thoroughness is rewarded)*

---

## Section 5: Team Roles and Week-by-Week Plan (1.5 pts)

### 5.1 — Team Roles

| Team Member | Primary Role | Secondary Role | What they own |
|-------------|-------------|----------------|---------------|
| [Name 1] | | | |
| [Name 2] | | | |
| [Name 3] | | | |
| [Name 4] | | | |

---

### 5.2 — Week-by-Week Plan

*Map your major milestones from now through Week 12. Be honest about which weeks will be hardest.*

| Week | Dates | What you will build / complete | Who leads | Risk level |
|------|-------|-------------------------------|-----------|------------|
| 2 | 20 Mar | Lab 2: Scaffold built, Design Review started | Whole team | — |
| 3 | 27 Mar | Lab 3: First working prototype with core AI feature | [Name] | Medium |
| 4 | 3 Apr | Design Review due (2 Apr). [What else?] | [Name] | High |
| 5 | 10 Apr | | | |
| 6 | 17 Apr | | | |
| 7 | 24 Apr | | | |
| 8 | 1 May | | | |
| 9 | 8 May | Midterm week | — | — |
| 10 | 15 May | | | |
| 11 | 22 May | Safety Audit | [Name] | High |
| 12 | 29 May | Peer Review Presentation | Whole team | High |

---

### 5.3 — Honest Assessment

*What is the hardest week in your plan? What is the biggest technical risk between now and Demo Day?*

[Your answer here]

---

## Section 6: IRB-Light Checklist (0.5 pts)

*Answer each question explicitly. If yes, add a one-sentence explanation.*

| Question | Answer | If yes: explain |
|----------|--------|-----------------|
| 1. Does your app collect images of real people? | Yes / No | |
| 2. Does your app process photographs of faces? | Yes / No | |
| 3. Does your app handle sensitive documents (medical, legal, financial, ID)? | Yes / No | |
| 4. Does your app store user-uploaded data? | Yes / No | |
| 5. If storing data: for how long and where? | N/A / [answer] | |
| 6. Do users need to give informed consent before using the app? | Yes / No | |

**If any answers above are "yes":** Describe your consent and data handling approach in one paragraph below.

[Your answer here, or "Not applicable" if all answers are No]

---

## Appendix (optional)

*Wireframes, additional diagrams, user interview notes, market research, competitive analysis. Optional but can strengthen the submission.*

---

*Design Review Template for CS-AI-2025 Spring 2026.*
*Questions? Email zeshan.ahmad@kiu.edu.ge or post in the course forum.*
