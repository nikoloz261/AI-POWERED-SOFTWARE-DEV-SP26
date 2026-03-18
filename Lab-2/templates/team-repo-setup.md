# Team Repository Setup

**Complete this before leaving Lab 2 today.**
**Time required: ~10 minutes (do during the Builder Sprint)**

---

## Why Your Team Needs a GitHub Repo Today

Every capstone deliverable from this point forward is tracked through your team repository. The grader for the Design Review, Safety Audit, and Repo Review will look at your GitHub commit history. A repo created the night before the Design Review deadline is a red flag. A repo with commits spread across weeks of genuine development demonstrates real work.

Starting the repo today — with the scaffold from the Builder Sprint — means your commit history reflects the actual timeline of your project.

---

## Option A: GitHub Organisation (Recommended for teams of 4)

A GitHub Organisation gives every team member admin rights and keeps the repository under a shared namespace rather than one person's account.

**Step 1: Create the organisation**
1. Go to [github.com](https://github.com) and sign in to your personal account
2. Click your profile icon (top right) → **"Your organisations"**
3. Click **"New organisation"**
4. Choose **"Free"** plan
5. Organisation name: something like `team-[teamname]-kiu-2026` (lowercase, hyphens)
6. Add all team members as owners

**Step 2: Create the repository**
1. Inside your new organisation, click **"New repository"**
2. Repository name: `[project-name]-cs-ai-2025` (lowercase, hyphens, descriptive)
3. Set to **Private** (you control who sees it — the instructor and TA will be invited)
4. Check **"Add a README file"**
5. Check **"Add .gitignore"** and choose **"Python"** or **"Node"** depending on your stack
6. Click **"Create repository"**

**Step 3: Invite the instructor and TA**
Go to Settings → Collaborators → Add people:
- `zeshan-ahmad-kiu` (instructor — confirm handle with the TA)
- TA handle (confirm with TA at the start of lab)

---

## Option B: Repository Under One Member's Account (Simpler but less flexible)

If setting up an organisation feels like too much overhead today, create the repo under one team member's account and add everyone else as collaborators.

1. The designated team lead creates a new repository at [github.com/new](https://github.com/new)
2. Repository name: `[project-name]-cs-ai-2025`
3. Set to **Private**
4. Add a README and .gitignore (Python or Node)
5. Go to Settings → Collaborators and add all team members
6. Add the instructor and TA as collaborators

> **Note:** If the team lead leaves the course or loses access to their account, the whole team loses access to the repo. The organisation approach avoids this.

---

## Repository Structure

Set up this structure today. You do not need to fill every folder — just create them so the structure is clear:

```
[your-project-name]/
├── README.md                   ← What the project is, how to run it
├── .gitignore                  ← Covers .env, node_modules, __pycache__, venv/
├── .env.example                ← Variable names with placeholder values (no real keys)
├── AGENTS.md                   ← (optional but encouraged — see note below)
│
├── frontend/                   ← Or src/, app/, depending on your framework
│   └── [scaffold files from Builder Sprint]
│
├── backend/                    ← Or api/, server/
│   └── [any backend files]
│
├── docs/
│   └── design-review/          ← Put your Design Review PDF here when complete
│
└── tests/                      ← Empty for now — you will fill this in later weeks
```

---

## The .env.example File

Create this file now and commit it. It shows what environment variables the project needs without exposing any real values:

```bash
# .env.example
# Copy this file to .env and fill in your real values
# NEVER commit the .env file

OPENROUTER_API_KEY=sk-or-your-key-here

# Add other variables as your project grows:
# SUPABASE_URL=your-supabase-project-url
# SUPABASE_ANON_KEY=your-supabase-anon-key
# DATABASE_URL=postgresql://...
```

---

## AGENTS.md (Optional but Encouraged)

AGENTS.md is a convention contributed to the Agentic AI Foundation in January 2026. It tells AI coding agents (like Claude Code, Cursor, or Copilot) how to work with your repository. Think of it as a `.editorconfig` but for AI tools.

Creating it now costs 5 minutes and will be noticed by the Repo Review grader in Week 15.

```markdown
# AGENTS.md

## Project Overview
[One paragraph describing what this project does]

## Development Setup
[How to install dependencies and run the project]

## Key Conventions
- [Your naming conventions, e.g., "Use kebab-case for component files"]
- [Your branching strategy, e.g., "Feature branches, PRs required for main"]
- [Your testing approach]

## Important Files
- `backend/api/routes.py` — API route definitions
- `frontend/src/components/` — React components
- `.env.example` — Required environment variables

## What Not to Touch
- [Any files that should not be modified without team discussion]

## Current Focus
[What the team is currently working on — update this each week]
```

---

## Your First Commit

Once the scaffold from the Builder Sprint is exported to your repo, make sure your first real commit includes:

- [ ] The scaffold code generated via Cursor, Claude Code, or AI Studio
- [ ] `.gitignore` covering `.env`, `node_modules`, `__pycache__`, `venv/`
- [ ] `.env.example` with placeholder values
- [ ] A `README.md` that at minimum states the project name and one sentence about what it does

**Commit message for your first real push:**
```
feat: initial project scaffold from Lab 2 builder sprint

- Add [framework] scaffold generated via [Cursor / Claude Code / AI Studio]
- Add .gitignore and .env.example
- Project: [one-sentence project description]
- Team: [team name]
```

---

## Submit the Repo Link

After the lab, submit your team GitHub repository link via the course LMS in the "Team Repo" submission field. This is how the instructor and TA track which repo belongs to which team.

---

*Team Repository Setup for CS-AI-2025 Lab 2, Spring 2026.*
