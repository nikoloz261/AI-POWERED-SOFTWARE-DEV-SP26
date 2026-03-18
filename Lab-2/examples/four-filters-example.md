# Four Filters — Completed Example

**Team Name:** MedScript AI
**Team Members:** Ana K. | Giorgi M. | Tamar B. | Luka N.
**Date:** Friday 20 March 2026

> *This is a fictional example created to illustrate how the Four Filters exercise should look when completed properly. It is not a real team's submission.*

---

## Step 1: Surface All Ideas

| # | Idea | Proposed by |
|---|------|-------------|
| 1 | App that reads handwritten prescriptions and digitises them | Ana |
| 2 | AI tutor for Georgian high school students learning English | Giorgi |
| 3 | Restaurant menu translation app for tourists | Tamar |
| 4 | Expense tracker that reads receipts from photos | Luka |
| 5 | Legal contract summariser for small Georgian businesses | Ana |

---

## Step 2: Quick Filter Pass

| Idea # | Filter 1: Real Problem? | Filter 2: AI Adds Value? | Filter 3: Buildable? | Filter 4: Motivated? | Overall |
|--------|------------------------|--------------------------|---------------------|----------------------|---------|
| 1 (Prescription reader) | ✓ | ✓ | ? | ✓ | Strong survivor |
| 2 (English tutor) | ✓ | ? | ✓ | ? | Weak survivor |
| 3 (Menu translator) | ✓ | ? | ✓ | ✗ | Eliminated |
| 4 (Receipt tracker) | ✓ | ✓ | ✓ | ? | Survivor |
| 5 (Contract summariser) | ? | ✓ | ? | ✓ | Weak survivor |

**Ideas that survived:** 1 (Prescription reader), 2 (English tutor), 4 (Receipt tracker), 5 (Contract summariser)

---

## Step 3: Deep Dive on Survivors

### Idea 1: Prescription reader

**Weakest filter:** Filter 3 — Buildable in 12 weeks?

**What would need to be true for this filter to be a clear pass?**

The handwriting OCR needs to be accurate enough to be trusted. Gemini Flash's vision has been demonstrated to handle handwritten medical text at roughly 85–90% accuracy for printed-style handwriting, lower for highly idiosyncratic scripts. For the MVP, we would limit to typed/printed prescriptions and treat handwritten as a stretch goal.

The regulatory concern is real — we cannot legally advise on medications. We would position this as a pharmacist tool (professional user, not patient) and include clear disclaimers that every output requires pharmacist verification before dispensing.

**Can this idea be reshaped to address the weakness? How?**

Yes. Scope down to: printed prescriptions only for MVP, typed handwriting in stretch goal, handwritten as post-course if we pursue this further. Add a mandatory "pharmacist review required" confirmation step before any data is shown to prevent users bypassing verification.

---

### Idea 4: Receipt tracker

**Weakest filter:** Filter 4 — Team motivated?

**What would need to be true for this filter to be a clear pass?**

This is a solved problem (Expensify, Klarna, Google Photos all do receipt scanning). Our version would need a differentiated angle that the team actually cares about. Options: focus on Georgian language receipts and VAT formats (niche but genuinely unserved), or build for small business owners managing multi-currency expenses in a tourism business.

**Can this idea be reshaped to address the weakness? How?**

The Georgian VAT receipt angle is genuinely interesting to Luka (whose family owns a small hotel in Batumi). Scope: extract Georgian-language receipt data, calculate VAT correctly for Georgian tax filing, export to the standard Georgian tax authority format. This is specific, motivated, and technically differentiated.

---

## Step 4: Decision

**Our chosen project:** MedScript — a pharmacist-facing tool that digitises printed prescriptions using vision AI, extracts medication name, dosage, and frequency with confidence scoring, and routes low-confidence fields to manual review.

**Why this idea over the alternatives:**

The prescription reader passes all four filters more cleanly than the alternatives once scoped correctly. The problem is real and documented (prescription transcription errors are a leading cause of medication errors globally). AI adds genuine value (OCR with confidence scoring is not achievable with rule-based approaches for varied prescription formats). The feasibility concern resolves when we scope to printed prescriptions only. Two team members have direct domain connection — Ana's mother is a pharmacist, Tamar did a secondary school internship at a hospital.

**The one thing we are most uncertain about:**

Whether Gemini Flash is accurate enough on the specific typography used in Georgian pharmacy systems. We will test this in Week 3 with real (anonymised) prescription samples.

---

## Filter Answers for MedScript

### Filter 1: Problem

**Who specifically has this problem?**
Pharmacists at small, independent pharmacies in Georgia who receive handwritten or printed prescriptions and must manually transcribe them into their dispensing system. Approximately 60% of pharmacies in Georgia are independent (not part of a chain), and most operate without digital prescription intake systems.

**What do they currently do about it?**
Manual transcription — a pharmacist reads the prescription and types the medication name, dosage, and frequency into their software. This takes 2–3 minutes per prescription and introduces transcription errors when handwriting is unclear or medication names are abbreviated.

**What is the cost?**
At a busy pharmacy processing 80+ prescriptions per day, transcription occupies 2.5–4 hours of pharmacist time. More critically, transcription errors — reading "10mg" as "100mg" or confusing similar drug names — contribute directly to medication errors. A 2022 WHO report estimated prescription transcription errors affect approximately 1 in 150 prescriptions globally.

**Can you reach a real user in the next two weeks?**
Yes. Ana's mother is a pharmacist at an independent pharmacy in Kutaisi and has agreed to provide anonymised sample prescriptions and to give a 30-minute interview about her current workflow.

---

### Filter 2: AI

**What does AI specifically do?**
Vision OCR with structured extraction — the model reads the prescription image and extracts specific fields (medication name, dosage, frequency, prescribing doctor name, date) as structured JSON. The model also provides a confidence score per field, enabling the application to route uncertain fields to manual review rather than displaying them as certain.

**Which course week is most relevant?**
Week 2 (Vision and Multimodal I/O) is the primary capability. Week 6 (Structured Outputs) will be used for the JSON extraction pattern. Week 5 (RAG) may be used to build a medication name database for validation.

**What would the product look like without AI?**
Without AI, this is a form where a pharmacist manually types what they read. There is no value added — that is exactly what they do today.

**Is AI doing something impossible before?**
Not impossible — OCR has existed for decades. But doing it accurately on variable prescription formats, with confidence scoring per field and structured output, at a cost of essentially zero per prescription, is new. Traditional OCR solutions for prescription digitisation cost $0.05–$0.15 per page and still require significant post-processing.

---

### Filter 3: Feasibility

**Required APIs:**
OpenRouter with Gemini Flash for vision — available in our org account. No other external APIs required for the MVP. For the medication name validation stretch goal: we would use a public drug database API (OpenFDA in the US; no Georgian equivalent exists, so we would build a small local lookup table).

**Hardest technical problem:**
Accuracy on varied prescription formats. Georgian pharmacies do not use a standardised template. Font sizes, layouts, and abbreviation conventions vary significantly between hospitals and individual doctors.

**Does anyone know how to solve it?**
Ana has prior experience with image processing from a computer vision project last year. The approach — multiple prompt strategies tested against a validation set of sample prescriptions — is something the team can execute in Weeks 3–4.

**MVP (minimum viable version):**
Extract medication name, dosage, and frequency from a printed prescription image. Return results with HIGH/MEDIUM/LOW confidence per field. Show a "requires pharmacist review" warning for any MEDIUM or LOW confidence field. That alone is useful and demonstrable.

---

### Filter 4: Motivation

**Week 12 demo scene:**
A pharmacist takes a photo of a prescription on their phone. The app processes it in under 3 seconds and displays the extracted fields on a clean card: medication name (HIGH confidence ✓), dosage (HIGH confidence ✓), frequency (MEDIUM confidence — verify). The pharmacist taps "verify" on the dosage field, corrects it with one tap, and approves the record. It then exports to a simple CSV for their dispensing system.

**Who cares about this domain?**
Ana (mother is a pharmacist, this is a real problem she has described for years). Tamar (hospital internship — saw transcription errors firsthand).

**Beyond the course?**
This could be a real product. The Georgian healthcare system does not have a digitised prescription pathway. A pharmacist tool that works offline-first on mobile would have genuine commercial value. The team has discussed approaching the Kutaisi City Hall health department after Demo Day.

---

## Next Steps

| Action | Owner | Deadline |
|--------|-------|----------|
| Create team GitHub org: `medscript-ai-kiu` | Giorgi | End of today's lab |
| Push scaffold (FastAPI backend + upload UI) | Luka | End of today's lab |
| Draft Design Review Sections 1 and 2 | Ana | Tuesday 24 March |
| Architecture diagram | Giorgi | Tuesday 24 March |
| Complete full Design Review draft | Whole team | Thursday 2 April |

---

*Completed Four Filters Example for CS-AI-2025 Lab 2, Spring 2026.*
*This is a teaching example — not a real team submission.*
