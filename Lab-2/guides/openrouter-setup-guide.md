# OpenRouter and API Access Setup Guide

**Which API access path to use, how to set it up, and how to swap keys when credits arrive**

---

## The Three-Tier Access Strategy

Depending on where we are in the semester's organisational setup, you will be on one of three tiers. All three tiers use the same code — you swap one line in your `.env` file to move between them.

| Tier | When to use | What you pay | Models available |
|------|-------------|-------------|-----------------|
| **Tier 1** | OpenRouter org credits not yet available | $0 | Gemini 3 Flash (free tier) via Google AI Studio |
| **Tier 2** | Org account pending, you want access now | Your own money (~$5 covers the semester) | All OpenRouter free-tier models + paid with your credits |
| **Tier 3** | Org account confirmed and credits provisioned | $0 (course-provided budget) | Full model access via course org account |

**Check with your TA at the start of lab which tier applies today.** The code in this lab is written to support all three without modification — only the `.env` file changes.

---

## Tier 1: Gemini Free Tier via Google AI Studio (No OpenRouter needed)

If OpenRouter org credits have not arrived yet, you can complete all of today's exercises using the Gemini free tier directly — the same setup you used in Lab 1.

### What changes in the code

The starter code files use the OpenAI SDK pointed at OpenRouter. To use the Google AI Studio free tier instead, you use the `google-genai` SDK directly. Here is the equivalent pattern:

**Install:**

```bash
uv add google-genai python-dotenv
# or: pip install google-genai python-dotenv
```

**Your `.env` file:**

```
GEMINI_API_KEY=AIzaSyYourKeyFromAIStudioHere
```

**Equivalent client pattern (replaces the OpenRouter client in starter code):**

```python
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")

# Text call
response = model.generate_content("Your prompt here")
print(response.text)

# Vision call (image URL)
import httpx
image_bytes = httpx.get("https://your-image-url.com/image.jpg").content

response = model.generate_content([
    {"mime_type": "image/jpeg", "data": image_bytes},
    "Describe what you see in this image."
])
print(response.text)
```

**Free tier models available via Google AI Studio:**

| Model string | What it is | Context | Speed |
|-------------|-----------|---------|-------|
| `gemini-3-flash-preview` | Standard fast model — your primary | 1M tokens | Fast |
| `gemini-3.1-flash-lite-preview` | Lightweight reasoning variant | 1M tokens | Fast |

**Rate limits on free tier:**
- 10 requests per minute
- 1,000 requests per day

For a 2-hour lab session these limits are more than sufficient. If you hit a 429 error, wait 30 seconds and retry.

**When to move off Tier 1:** As soon as OpenRouter org credits are confirmed (your TA will announce this), switch to Tier 3. The switch requires changing two lines of code and one environment variable.

---

## Tier 2: Personal OpenRouter Account (Free Tier + Optional Credits)

If you want access to more models now and cannot wait for the org account, create a personal OpenRouter account. OpenRouter offers a free tier with access to a curated set of models at no cost, and you can add $5–$10 of personal credits for the models that are not on the free tier.

**This is optional.** Tier 1 (Gemini free tier) is sufficient to complete all lab exercises. Tier 2 gives you access to more models and the unified OpenRouter interface, which is closer to the production pattern your capstone will use.

### Step 1: Create a personal OpenRouter account

1. Go to [openrouter.ai](https://openrouter.ai) and click **"Sign up"**
2. Use your preferred email (not required to match your LMS email)
3. Verify your email
4. You are now on the free tier — no credit card required

### Step 2: Generate an API key

1. Click your profile icon → **"Keys"**
2. Click **"Create Key"**
3. Name it: `cs-ai-2025-personal`
4. Copy the key — it starts with `sk-or-`

### Step 3: Add to your `.env` file

```
OPENROUTER_API_KEY=sk-or-your-personal-key-here
```

### Step 4: Optional — add personal credits

If you want to access all models (including paid ones) during development before the org account arrives:
1. Go to **"Credits"** in your OpenRouter dashboard
2. Click **"Add credits"**
3. $5 is enough for all Lab 2 exercises and most of Lab 3 with Gemini 3.1 Flash

**Free-tier models available on a personal OpenRouter account (no credits required):**

| OpenRouter model string | Provider | Vision | Notes |
|------------------------|----------|--------|-------|
| `google/gemini-3.1-flash:free` | Google | Yes | Rate limited but sufficient for labs |
| `meta-llama/llama-3.1-8b-instruct:free` | Meta | No | Fast, good for text tasks |
| `mistralai/mistral-7b-instruct:free` | Mistral | No | Good for text generation |

Note: Free-tier models on OpenRouter append `:free` to the model string. If you add credits, you can drop the `:free` suffix and access the full-rate model with higher limits.

---

## Tier 3: Course Organisation Account (Preferred — use when available)

When the course OpenRouter organisation account is set up and credits are provisioned, your TA will distribute API keys via the course LMS. This is the preferred configuration for all lab work from Lab 2 onwards.

### Step 1: Accept the organisation invitation

Check the email address registered on the course LMS for an invitation from `noreply@openrouter.ai` with subject **"You've been invited to join the CS-AI-2025 organisation"**. Accept it and create or sign in to an OpenRouter account.

### Step 2: Generate an org-linked API key

1. In OpenRouter, ensure you are viewing the CS-AI-2025 organisation (check the dropdown at top left)
2. Go to **"Keys"**
3. Click **"Create Key"** — this key draws from the organisation's credit pool
4. Name it: `cs-ai-2025-[your-name]`
5. Copy the key — it starts with `sk-or-`

### Step 3: Update your `.env` file

```
OPENROUTER_API_KEY=sk-or-your-org-key-here
```

That is the only change needed. All the starter code and your capstone code will now route through the org account automatically.

---

## Swapping Between Tiers — The Key Design

The starter code is deliberately written so that switching between Tier 1, 2, and 3 requires changing as little as possible. Here is the full picture:

**Tier 1 (Gemini direct):** Uses `google-genai` SDK with `GEMINI_API_KEY`

```python
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3-flash-preview")
```

**Tier 2 and 3 (OpenRouter):** Uses `openai` SDK with `OPENROUTER_API_KEY`

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
```

**Switching from Tier 1 to Tier 2/3:** Change your `.env` file and swap the client initialisation. The rest of your code stays identical — same prompt structure, same response parsing.

**Switching from Tier 2 to Tier 3:** Only the value of `OPENROUTER_API_KEY` in `.env` changes. The code is identical.

Your `.env.example` should always show both variables so teammates know what is needed:

```bash
# .env.example
# Use ONE of these depending on your current access tier:

# Tier 1 — Google AI Studio free tier (no OpenRouter needed)
GEMINI_API_KEY=AIzaSyYour-google-ai-studio-key-here

# Tier 2/3 — OpenRouter (personal or org account)
OPENROUTER_API_KEY=sk-or-your-openrouter-key-here
```

---

## Model Reference — March 2026

### Via OpenRouter (Tiers 2 and 3)

**Standard tier — use for all lab exercises and prototyping:**

| OpenRouter model string | Provider | Vision | Input / 1M | Output / 1M |
|------------------------|----------|--------|-----------|------------|
| `google/gemini-3.1-flash` | Google | Yes | $0.10 | $0.40 |
| `google/gemini-3-flash-preview` | Google | Yes | $0.10 | $0.40 |
| `openai/gpt-4o-mini` | OpenAI | Yes | $0.15 | $0.60 |
| `anthropic/claude-haiku-3-5` | Anthropic | Yes | $0.80 | $4.00 |

**Premium tier — use sparingly, only when standard tier cannot meet your quality bar:**

| OpenRouter model string | Provider | Vision | Input / 1M | Output / 1M |
|------------------------|----------|--------|-----------|------------|
| `google/gemini-3.1-pro` | Google | Yes | $1.25 | $5.00 |
| `openai/gpt-4o` | OpenAI | Yes | $2.50 | $10.00 |
| `anthropic/claude-opus-4-6` | Anthropic | Yes | $15.00 | $75.00 |

> **Credit discipline:** Your org account has a fixed budget for the semester. `claude-opus-4-6` costs 150x more per output token than `gemini-3.1-flash`. Use the flash tier for everything until you have a concrete, demonstrated reason to upgrade. Document that reason in your Design Review.

### Via Google AI Studio direct (Tier 1 — free)

| google-genai model string | Vision | Free tier limits |
|--------------------------|--------|-----------------|
| `gemini-3-flash-preview` | Yes | 10 RPM, 1,000 RPD |
| `gemini-3.1-flash-lite-preview` | Yes | 10 RPM, 1,000 RPD |

---

## The OpenAI-Compatible Client Pattern (Tiers 2 and 3)

OpenRouter uses the OpenAI API format. This is the full pattern for the starter code exercises:

```python
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    default_headers={
        "HTTP-Referer": "https://github.com/ZA-KIU-Classroom/AI-POWERED-SOFTWARE-DEV-SP26",
        "X-Title": "CS-AI-2025"
    }
)

# Text call
response = client.chat.completions.create(
    model="google/gemini-3.1-flash",
    messages=[{"role": "user", "content": "Your prompt here"}],
    max_tokens=512
)
print(response.choices[0].message.content)

# Vision call (image URL)
response = client.chat.completions.create(
    model="google/gemini-3.1-flash",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": "https://your-image-url"}},
            {"type": "text", "text": "Describe this image"}
        ]
    }],
    max_tokens=512
)
print(response.choices[0].message.content)
```

Changing to a different model is one string change: replace `"google/gemini-3.1-flash"` with any model string from the table above. Everything else stays identical.

---

## Cost Tracking

Check your usage at [openrouter.ai/activity](https://openrouter.ai/activity) at the end of each lab session. For granular cost tracking in your code:

```python
# After any response:
if response.usage:
    input_tokens = response.usage.prompt_tokens
    output_tokens = response.usage.completion_tokens

    # Gemini 3.1 Flash pricing (March 2026)
    cost = (input_tokens / 1_000_000 * 0.10) + (output_tokens / 1_000_000 * 0.40)
    print(f"Cost this call: ${cost:.6f}")
```

---

## Security — Same Rules as Lab 1

- API keys live in `.env` — never in source files
- `.env` is in `.gitignore` before your first commit
- `.env.example` is in the repo with placeholder values, never real keys
- If you accidentally commit a key: revoke it immediately in OpenRouter settings or Google AI Studio, then generate a new one

---

## Troubleshooting

| Error | Likely cause | Fix |
|-------|-------------|-----|
| `401 Unauthorized` (OpenRouter) | Key missing or wrong | Check `.env` — key must start with `sk-or-` |
| `401 Unauthorized` (Gemini direct) | Key missing or wrong | Check `.env` — key must start with `AIza` |
| `403 Forbidden` | Org invite not accepted | Sign out of OpenRouter, sign back in, check Organisations |
| `404` on model string | Typo in model string | Copy-paste from the table above exactly |
| `429 Rate Limited` | Burst limit hit | Wait 10–30 seconds and retry |
| `usage` is `None` | Some models omit usage data | Guard with `if response.usage:` before accessing |
| Response has no vision content | Image URL blocked by model | Use base64 encoding for the image instead |

---

*OpenRouter and API Access Setup Guide for CS-AI-2025 Lab 2, Spring 2026.*
*This guide will be updated when the organisation account is confirmed active.*
