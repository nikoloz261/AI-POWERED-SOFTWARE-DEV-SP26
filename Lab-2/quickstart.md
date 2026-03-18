# Lab 2 Quickstart

**Get your API access sorted and your first vision call running in 15 minutes.**

Before anything else: check with your TA which access tier applies today.

| Tier | You need | Go to |
|------|---------|-------|
| **Tier 1** — Org not ready yet | Your Gemini API key from Lab 1 | [Tier 1 section below](#tier-1-gemini-free-tier-no-openrouter-needed) |
| **Tier 2** — Org pending, want access now | Create a personal OpenRouter account | [Tier 2 section below](#tier-2-personal-openrouter-account) |
| **Tier 3** — Org credits confirmed | Org API key from LMS | [Tier 3 section below](#tier-3-course-organisation-account) |

All three tiers run the same starter code. Only your `.env` file differs. Once you have confirmed your tier and have a working key, skip to [Run Your First Call](#run-your-first-call).

---

## Tier 1: Gemini Free Tier (No OpenRouter Needed)

You already have everything you need from Lab 1. Your `GEMINI_API_KEY` from Google AI Studio works directly.

**Your `.env` file:**

```
GEMINI_API_KEY=AIzaSyYourKeyFromLab1
```

**The starter code for Tier 1** uses the `google-genai` SDK rather than the `openai` SDK. See [`guides/openrouter-setup-guide.md`](./guides/openrouter-setup-guide.md) for the equivalent code pattern.

When your TA confirms org credits are available, you move to Tier 3 by adding one line to `.env` and updating the client in your code.

---

## Tier 2: Personal OpenRouter Account

If you want broader model access now, create a free personal OpenRouter account.

1. Go to [openrouter.ai](https://openrouter.ai) and click **"Sign up"**
2. Verify your email
3. Go to **"Keys"** → **"Create Key"** → name it `cs-ai-2025-personal`
4. Copy the key (starts with `sk-or-`)

**Your `.env` file:**

```
OPENROUTER_API_KEY=sk-or-your-personal-key-here
```

Free-tier models include `google/gemini-3.1-flash:free` (note the `:free` suffix). If you add $5 of personal credits, use `google/gemini-3.1-flash` (without `:free`) for higher rate limits.

**Install the SDK:**

```bash
uv add openai python-dotenv
# or: pip install openai python-dotenv
```

---

## Tier 3: Course Organisation Account

Your TA will confirm when org credits are active and distribute keys via the LMS.

1. Check your LMS email for the OpenRouter org invitation and accept it
2. In OpenRouter, go to **"Keys"** → **"Create Key"** → name it `cs-ai-2025-[your-name]`
3. Copy the key (starts with `sk-or-`)

**Your `.env` file:**

```
OPENROUTER_API_KEY=sk-or-your-org-key-here
```

**Install the SDK:**

```bash
uv add openai python-dotenv
# or: pip install openai python-dotenv
```

---

## Run Your First Call

Once you have a working key in your `.env` file, run the first exercise:

```bash
# Make sure you are in the Lab-2 directory with your environment active
python examples/starter-code/01_openrouter_hello.py
```

**Expected output (Tiers 2 and 3):**

```
Connecting to OpenRouter...
Model: google/gemini-3.1-flash
Prompt: Explain what a vision-language model is in two sentences.

Response: A vision-language model is an AI system trained to process and reason
          about both images and text simultaneously, enabling tasks like image
          captioning, visual question answering, and document analysis. These
          models learn joint representations of visual and linguistic information
          during training on large datasets of paired image-text examples.

Token usage:
  Input tokens:  17
  Output tokens: 55
  Total tokens:  72

Estimated cost: $0.000027
Latency: 1.14 seconds
```

If you see a response like this, proceed to the Four Filters exercise.

---

## Troubleshooting

**`401 Unauthorized` (OpenRouter)**
Key has a typo or extra space. Open `.env` and verify the key starts with `sk-or-` with no quotes.

**`401 Unauthorized` (Gemini direct)**
Key missing or wrong. Verify it starts with `AIza`.

**`403 Forbidden` — organisation error**
You accepted the invitation but the org did not link. Sign out of OpenRouter, sign back in, check **"Organisations"** in account settings.

**`429 Rate Limited`**
Wait 15 seconds and retry. Add `time.sleep(2)` between API calls if you hit this repeatedly.

**`ModuleNotFoundError: No module named 'openai'`**
Your environment is not active or `openai` is not installed. Run `pip install openai` with your environment active.

**`.env` values reading as `None`**
Run the script from the `Lab-2/` directory. `load_dotenv()` looks for `.env` in the current working directory.

---

## What Comes Next

| Activity | Guide | Time |
|----------|-------|------|
| Four Filters convergence | `guides/four-filters-guide.md` + `templates/four-filters-template.md` | 30 min |
| Builder Sprint | `guides/builder-tools-guide.md` | 35 min |
| OpenRouter + vision exercises | `examples/starter-code/` | 20 min |
| Design Review kickoff | `templates/design-review-template.md` | 25 min |

---

*Quickstart for CS-AI-2025 Lab 2, Spring 2026.*
*If this guide has an error, raise your hand so we can fix it before Group B.*
