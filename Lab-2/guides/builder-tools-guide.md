# Builder Tools Guide: Scaffolding with AI-Native Dev Tools

**Time budget for the Builder Sprint in lab: 35 minutes**
**Goal: A running application scaffold pushed to your team GitHub repo before the end of the sprint**

---

## What the Builder Sprint Is (and Is Not)

The Builder Sprint is not about writing production code. It is about proving your idea is buildable and getting a working shell in front of your team as fast as possible.

A working scaffold at the end of 35 minutes means:
- The app runs without crashing
- There is a visible structure matching your product concept
- An image upload or file input is present somewhere
- The code is in your team GitHub repo with at least one commit

You are not writing business logic today. You are not connecting the AI pipeline yet — that happens in the OpenRouter exercises immediately after. You are creating the container that everything else will go inside.

---

## The Tools

You are CS students. You will learn to build real software, not click through drag-and-drop UIs. The tools below are professional-grade AI-assisted development environments that are widely used in the industry. The goal is to become fast with them, not dependent on them.

---

### Google AI Studio — Code Generation (Recommended starting point, zero install)

**URL:** [aistudio.google.com](https://aistudio.google.com)

You already have a Google AI Studio account from Lab 1. Beyond the prompt playground, AI Studio can generate entire code files from a description. Use it to bootstrap your backend in under 10 minutes without installing anything new.

**How to use it for the sprint:**

Open AI Studio with Gemini 3.1 Flash and prompt it with your specific requirements. Be precise — the more specific you are, the less you need to edit.

**Backend prompt template:**

```
Generate a Python FastAPI application with the following specification:

Project: [your project name and one-sentence description]

Endpoints:
1. POST /api/analyse
   - Accepts a multipart file upload (image, JPEG or PNG, max 5MB)
   - Returns JSON: { "status": "ok", "fields": {}, "message": "placeholder" }
   - Include a comment block showing where the OpenRouter API call will go
   - Return HTTP 413 if file exceeds 5MB
   - Return HTTP 415 if file type is not JPEG or PNG

2. GET /health
   - Returns: { "status": "ok" }

3. CORS enabled for http://localhost:3000 and http://127.0.0.1:5500

Include:
- requirements.txt: fastapi, uvicorn, python-multipart, python-dotenv, openai
- .env.example showing OPENROUTER_API_KEY=sk-or-your-key-here
- Brief inline comments explaining each section

Do not include a database. Do not include authentication. Keep it minimal.
```

Copy the output into your project folder as `main.py` and `requirements.txt`. Review every line before committing.

**Frontend prompt template:**

```
Generate a single HTML file (no frameworks, no npm, vanilla JavaScript only)
for an image upload interface. It should:

- Accept JPEG and PNG files via drag-and-drop OR click-to-browse
- Show a preview of the selected image (use FileReader API)
- Disable the submit button until an image is selected
- Send the file to POST http://localhost:8000/api/analyse using fetch()
- Show a loading message ("Analysing...") while waiting for the response
- Display the returned JSON in a <pre> block once received
- Show an error message if the request fails

Style: plain CSS, clean, no frameworks. Minimal and readable.
```

This gives you `frontend/index.html`. Push both files and you have a scaffold.

**Testing prompts before writing code:** The AI Studio playground is also excellent for refining your vision prompt before you write the code around it. Upload a sample image and test your extraction prompt directly in the chat. This saves OpenRouter credits — use the free tier here first.

---

### Cursor (Recommended if you have time to install it before lab)

**URL:** [cursor.com](https://cursor.com) — download and install; takes under 3 minutes

Cursor is a code editor built on VS Code with a deeply integrated AI agent. Composer mode (Ctrl+I on Windows/Linux, Cmd+I on Mac) lets you describe a project and the agent writes files directly into your project folder — no copy-pasting.

**Why Cursor is the strongest option for this sprint:** It writes to your actual filesystem, is aware of all files already in your project, and can iterate across multiple files in one prompt. You describe a change; it makes the change everywhere it needs to.

**Sprint workflow:**

```bash
# Create your project folder and initialise git
mkdir my-capstone && cd my-capstone && git init

# Write a one-line README first — Cursor uses this as context
echo "# MyProject — [one sentence description]" > README.md

# Open Cursor
cursor .
```

Open Composer with Ctrl+I and enter your project brief:

```
Create a Python FastAPI project for [your project description].

Files to create:
- main.py — FastAPI with POST /api/analyse (image upload, returns placeholder JSON)
  and GET /health. CORS for localhost:3000. Error handling for file size and type.
- requirements.txt — fastapi, uvicorn, python-multipart, python-dotenv, openai
- .env.example — OPENROUTER_API_KEY=sk-or-your-key-here
- .gitignore — covers .env, venv/, __pycache__/, *.pyc
- frontend/index.html — vanilla JS image upload with fetch to /api/analyse, 
  shows preview and results

The /api/analyse endpoint should have a comment block showing exactly where
the OpenRouter call will be inserted in the next exercise.
```

Review each file as Cursor creates it. Accept the ones that look correct; use follow-up prompts to fix anything that does not.

**Follow-up prompts for iteration:**
- "Add a 5MB file size check to the analyse endpoint with a 413 response"
- "Add a loading spinner to the frontend using CSS animation, no libraries"
- "Add a .gitignore that covers .env, venv/, __pycache__, node_modules/"

---

### Claude Code (Strong option for terminal-comfortable students)

**Install:** `npm install -g @anthropic-ai/claude-code` (requires Node.js 18+)
**Requires:** An Anthropic API key in `ANTHROPIC_API_KEY` environment variable

Claude Code is Anthropic's terminal-based agentic coding tool. It reads your entire project, understands what exists, and makes targeted edits — writing files, modifying existing code, and running commands. Unlike a chat interface, it is fully aware of your codebase context.

**Sprint workflow:**

```bash
mkdir my-capstone && cd my-capstone && git init

# Write a short project description — Claude Code reads this first
cat > README.md << 'EOF'
# MyProject
[Your one-sentence project description]
Target user: [who uses this]
Core feature: [what the AI does]
EOF

# Start Claude Code
claude
```

At the Claude Code prompt:

```
Create a Python FastAPI backend for this project based on the README.
Include POST /api/analyse (image upload → placeholder JSON with where 
the OpenRouter call will go), GET /health, CORS, requirements.txt,
.env.example, .gitignore, and a frontend/index.html with vanilla JS
image upload that calls the API and displays results.
```

Claude Code will lay out what it intends to do before executing. Review the plan, then confirm. It will create all files, tell you what it changed, and flag anything it was uncertain about.

**Note on API key:** If you do not have an `ANTHROPIC_API_KEY`, use Cursor or the AI Studio approach instead. Do not create a personal Anthropic account on course credits — use the tools you already have access to.

---

### GitHub Copilot in VS Code (Good if your university provides it)

VS Code with Copilot Chat (Ctrl+Shift+I) is a reliable fallback if Cursor is not an option. For the sprint, use Copilot Chat rather than inline suggestions — describe the file you want in the chat and let it generate the full implementation.

Copilot is slower than Cursor for initial project scaffolding but excellent for iterating on individual functions once the structure is in place.

---

## Choosing Your Tool Today

| Your situation | Best choice |
|---------------|-------------|
| Cursor already installed | Cursor — fastest complete project scaffold |
| Comfortable with terminal, Node.js installed | Claude Code |
| Nothing installed, want to start immediately | Google AI Studio code gen |
| VS Code + GitHub Copilot from university | Copilot Chat in VS Code |

**If you need to install Cursor:** Do it in the first 5 minutes of the sprint. The download is approximately 150MB and installation takes under 3 minutes. Worth it.

**If you have nothing installed and no time:** AI Studio is in your browser right now. The prompts above will generate a working scaffold you can copy into VS Code in under 10 minutes.

---

## The Builder Sprint Workflow (35 minutes)

### Minutes 0–5: Write your brief before you open any tool

Before generating anything, write a one-paragraph description of your project. This forces your team to agree on the scope before the AI touches it. Use this as your first prompt.

A good brief covers:
- What the application does (one sentence)
- Who uses it (one sentence)
- The core endpoint — what data goes in, what comes out
- The tech stack: Python FastAPI backend, vanilla HTML or React frontend

### Minutes 5–20: Generate and read every file

Let the tool generate the initial structure. Then read everything it produced. This is not optional — you are responsible for code you commit. Look for:
- API keys or credentials hardcoded into source files (remove immediately)
- Missing `.gitignore` entries for `.env` and `venv/`
- The upload endpoint — does it handle file size limits?
- Any `TODO` or placeholder comments — these are your tasks after the sprint

### Minutes 20–30: Make one targeted improvement

Pick the single most important gap and use your tool to fix it with a follow-up prompt. Do not fix everything — pick one:
- Add file size validation to the upload endpoint
- Add an error state to the frontend
- Add CORS to the FastAPI app if it is missing

### Minutes 30–35: Commit and push

```bash
git add .
git commit -m "feat: initial project scaffold from Lab 2 builder sprint

Generated with [Cursor / Claude Code / AI Studio].
Project: [one-sentence description]
Team: [team name]"

git push origin main
```

Your team repo must have at least one commit with real code by the end of this sprint. An incomplete scaffold with real code is better than nothing pushed.

---

## What Your Scaffold Should Contain

**Minimum at end of sprint:**

```
your-project/
├── README.md                   ← Project name + one-sentence description
├── .gitignore                  ← Covers .env, venv/, __pycache__/, *.pyc
├── .env.example                ← OPENROUTER_API_KEY=sk-or-your-key-here
├── requirements.txt            ← fastapi, uvicorn, python-multipart, python-dotenv, openai
├── main.py                     ← FastAPI with /api/analyse and /health
└── frontend/
    └── index.html              ← Image upload UI with results placeholder
```

The `/api/analyse` endpoint does not need to call the AI yet. A placeholder is fine and expected:

```python
@app.post("/api/analyse")
async def analyse(file: UploadFile = File(...)):
    # ─────────────────────────────────────────────────────────
    # TODO (Lab 2, Exercise 2): Replace this placeholder with
    # the OpenRouter vision API call from 02_image_analyser.py
    # ─────────────────────────────────────────────────────────
    return {
        "status": "placeholder",
        "filename": file.filename,
        "message": "AI integration coming — see Exercise 2",
        "fields": {}
    }
```

---

## A Note on Using AI Tools Responsibly

You are using AI to scaffold code faster than you could write it by hand. This is legitimate and increasingly standard in professional development. The responsibility that comes with it:

Read every line before you commit it. If you cannot explain what a line does, ask the tool to explain it before you ship it. By Week 12, every function in your capstone should be understood by at least one team member — not because a rule says so, but because you will be presenting it to an audience and answering questions about it.

AI tools make bad programmers faster at being bad. They also make good programmers dramatically more productive. The difference is whether you are reading and understanding what gets generated.

---

*Builder Tools Guide for CS-AI-2025 Lab 2, Spring 2026.*
