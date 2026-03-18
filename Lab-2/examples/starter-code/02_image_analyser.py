"""
Exercise 2: Image Analyser with Confidence Scoring
CS-AI-2025 Lab 2 | Spring 2026

This exercise implements the 6-stage multimodal pipeline from Lecture 2:
  Stage 1: Input Capture  — accept image URL or local file path
  Stage 2: Preprocessing  — validate and prepare image data
  Stage 3: Prompt Construction — build a structured extraction prompt
  Stage 4: API Inference  — call the vision model via OpenRouter
  Stage 5: Confidence Scoring — parse per-field confidence from the response
  Stage 6: UX Response    — display results with routing by confidence level

Run with a sample image URL, then point it at an image relevant to your project.

Usage:
    python examples/starter-code/02_image_analyser.py
"""

import os
import base64
import json
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────

MODEL = "google/gemini-3.1-flash"

# Sample image for testing — a public domain image of text
# Replace this with an image relevant to YOUR project
SAMPLE_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png"


# ─────────────────────────────────────────────────────────────
# Client setup
# ─────────────────────────────────────────────────────────────

def create_client() -> OpenAI:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in .env file")
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        default_headers={
            "HTTP-Referer": "https://github.com/ZA-KIU-Classroom/AI-POWERED-SOFTWARE-DEV-SP26",
            "X-Title": "CS-AI-2025 Lab 2"
        }
    )


# ─────────────────────────────────────────────────────────────
# Stage 1 + 2: Input Capture and Preprocessing
# ─────────────────────────────────────────────────────────────

def prepare_image_from_url(image_url: str) -> dict:
    """Prepare an image from a URL for the vision API."""
    # For URL-based images, we pass the URL directly
    # OpenRouter forwards this to the vision model
    return {
        "type": "image_url",
        "image_url": {
            "url": image_url
        }
    }


def prepare_image_from_file(file_path: str) -> dict:
    """
    Prepare a local image file for the vision API.
    Encodes as base64 — required for local files that are not publicly accessible.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Image file not found: {file_path}")

    # Check file size — keep under 5MB for reliable API performance
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if file_size_mb > 5:
        print(f"  Warning: Image is {file_size_mb:.1f}MB — consider compressing to under 5MB")

    # Detect media type from extension
    ext = file_path.lower().split(".")[-1]
    media_types = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "webp": "image/webp"
    }
    media_type = media_types.get(ext, "image/jpeg")

    # Encode as base64
    with open(file_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    return {
        "type": "image_url",
        "image_url": {
            "url": f"data:{media_type};base64,{image_data}"
        }
    }


# ─────────────────────────────────────────────────────────────
# Stage 3: Prompt Construction
# ─────────────────────────────────────────────────────────────

def build_extraction_prompt(task_description: str, fields_to_extract: list[str]) -> str:
    """
    Build a structured extraction prompt that requests JSON output with confidence scoring.

    This prompt pattern is from Lecture 2: specificity + structured output + confidence elicitation.
    """
    fields_str = "\n".join(f"  - {field}" for field in fields_to_extract)

    return f"""You are an expert data extractor. Your task: {task_description}

Extract the following fields from the image:
{fields_str}

For each field you extract:
1. Provide the extracted value (or null if not present in the image)
2. Rate your confidence as exactly one of: HIGH, MEDIUM, or LOW
3. Add a brief note if confidence is not HIGH (explain why you are uncertain)

Respond ONLY with valid JSON. No preamble, no explanation outside the JSON.
Use this exact structure:

{{
  "field_name": {{
    "value": "extracted value or null",
    "confidence": "HIGH | MEDIUM | LOW",
    "note": "explanation if not HIGH, otherwise null"
  }}
}}
"""


# ─────────────────────────────────────────────────────────────
# Stage 4: API Inference
# ─────────────────────────────────────────────────────────────

def call_vision_model(
    client: OpenAI,
    image_content: dict,
    task_prompt: str,
    model: str = MODEL
) -> tuple[str, dict]:
    """
    Call the vision model with an image and task prompt.

    Returns:
        (response_text, usage_dict)
    """
    start_time = time.time()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    image_content,                          # The image
                    {"type": "text", "text": task_prompt}  # The task
                ]
            }
        ],
        max_tokens=1024
    )

    latency_ms = (time.time() - start_time) * 1000
    response_text = response.choices[0].message.content

    usage = {
        "input_tokens": response.usage.prompt_tokens if response.usage else 0,
        "output_tokens": response.usage.completion_tokens if response.usage else 0,
        "latency_ms": latency_ms,
        "model": model
    }

    return response_text, usage


# ─────────────────────────────────────────────────────────────
# Stage 5: Confidence Scoring
# ─────────────────────────────────────────────────────────────

def parse_extraction_response(response_text: str) -> dict:
    """
    Parse the model's JSON response.

    Handles cases where the model wraps JSON in markdown fences.
    Returns the parsed dict or an error dict if parsing fails.
    """
    # Strip markdown code fences if present (```json ... ```)
    cleaned = response_text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        cleaned = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        return {
            "_parse_error": {
                "value": f"Failed to parse model response as JSON: {e}",
                "confidence": "LOW",
                "note": "Raw response stored for debugging"
            },
            "_raw_response": response_text
        }


def route_by_confidence(extracted_fields: dict) -> dict:
    """
    Route each extracted field to one of three buckets based on confidence.

    Returns a dict with keys: "auto_accept", "verify", "manual_entry"
    """
    routes = {
        "auto_accept": [],   # HIGH confidence — display directly
        "verify": [],        # MEDIUM confidence — show with verification prompt
        "manual_entry": []   # LOW confidence — hide, require manual entry
    }

    for field_name, field_data in extracted_fields.items():
        if field_name.startswith("_"):
            continue  # Skip internal keys

        confidence = field_data.get("confidence", "LOW").upper()
        value = field_data.get("value")
        note = field_data.get("note")

        entry = {
            "field": field_name,
            "value": value,
            "confidence": confidence,
            "note": note
        }

        if confidence == "HIGH":
            routes["auto_accept"].append(entry)
        elif confidence == "MEDIUM":
            routes["verify"].append(entry)
        else:
            routes["manual_entry"].append(entry)

    return routes


# ─────────────────────────────────────────────────────────────
# Stage 6: UX Response (terminal display)
# ─────────────────────────────────────────────────────────────

def display_results(routes: dict, usage: dict):
    """
    Display extraction results in the terminal with confidence routing.

    In a real application this would render UI components.
    In this exercise, we simulate the three-tier display in the terminal.
    """
    print()
    print("─" * 60)
    print("EXTRACTION RESULTS")
    print("─" * 60)

    # HIGH confidence — show directly
    if routes["auto_accept"]:
        print()
        print("  ✓ AUTO-ACCEPTED (HIGH confidence — display directly to user):")
        for item in routes["auto_accept"]:
            print(f"    {item['field']}: {item['value']}")

    # MEDIUM confidence — show with warning
    if routes["verify"]:
        print()
        print("  ⚠ REQUIRES VERIFICATION (MEDIUM confidence — user must confirm):")
        for item in routes["verify"]:
            note_str = f" — {item['note']}" if item['note'] else ""
            print(f"    {item['field']}: {item['value']}{note_str}")

    # LOW confidence — hide, require manual entry
    if routes["manual_entry"]:
        print()
        print("  ✗ MANUAL ENTRY REQUIRED (LOW confidence — value not displayed):")
        for item in routes["manual_entry"]:
            note_str = f" — Reason: {item['note']}" if item['note'] else ""
            print(f"    {item['field']}: [hidden]{note_str}")

    # Usage stats
    print()
    print("─" * 60)
    print("USAGE:")
    print(f"  Model:         {usage['model']}")
    print(f"  Input tokens:  {usage['input_tokens']}")
    print(f"  Output tokens: {usage['output_tokens']}")
    print(f"  Latency:       {usage['latency_ms']:.0f}ms")

    cost = (usage["input_tokens"] / 1_000_000 * 0.10) + (usage["output_tokens"] / 1_000_000 * 0.40)
    print(f"  Cost (approx): ${cost:.6f}")
    print()


# ─────────────────────────────────────────────────────────────
# Main exercise
# ─────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("CS-AI-2025 Lab 2 | Exercise 2: Image Analyser")
    print("=" * 60)
    print()
    print("This exercise implements the 6-stage multimodal pipeline")
    print("from Lecture 2 using a real image and the OpenRouter API.")
    print()

    # Set up client
    client = create_client()

    # ── STAGE 1 + 2: Input Capture and Preprocessing ─────────
    print("Stage 1 + 2: Input Capture and Preprocessing")
    print(f"  Using sample image URL: {SAMPLE_IMAGE_URL[:60]}...")
    image_content = prepare_image_from_url(SAMPLE_IMAGE_URL)
    print("  Image prepared for API.\n")

    # ── STAGE 3: Prompt Construction ─────────────────────────
    print("Stage 3: Prompt Construction")

    # For the sample image (PNG transparency demo), we extract visual properties.
    # In YOUR project, change task_description and fields_to_extract to match
    # what your application needs to extract from an image.
    task_description = "Describe the visual content of this image accurately."
    fields_to_extract = [
        "main_subject",       # What is the primary subject of the image?
        "dominant_colours",   # What colours are most visible?
        "image_type",         # Is this a photograph, illustration, diagram, screenshot, etc.?
        "text_present",       # Is any text visible in the image?
        "background_type"     # Is the background solid, transparent, complex, etc.?
    ]

    prompt = build_extraction_prompt(task_description, fields_to_extract)
    print(f"  Task: {task_description}")
    print(f"  Fields to extract: {', '.join(fields_to_extract)}\n")

    # ── STAGE 4: API Inference ────────────────────────────────
    print("Stage 4: API Inference")
    print(f"  Sending image to {MODEL} via OpenRouter...")
    response_text, usage = call_vision_model(client, image_content, prompt)
    print(f"  Response received in {usage['latency_ms']:.0f}ms.\n")

    # ── STAGE 5: Confidence Scoring ───────────────────────────
    print("Stage 5: Confidence Scoring")
    extracted = parse_extraction_response(response_text)

    if "_parse_error" in extracted:
        print("  WARNING: Could not parse JSON response.")
        print(f"  Raw response: {response_text[:200]}...")
        return

    routes = route_by_confidence(extracted)
    total = len(routes["auto_accept"]) + len(routes["verify"]) + len(routes["manual_entry"])
    accepted_pct = len(routes["auto_accept"]) / total * 100 if total > 0 else 0
    print(f"  {total} fields extracted.")
    print(f"  {len(routes['auto_accept'])} HIGH ({accepted_pct:.0f}%) | "
          f"{len(routes['verify'])} MEDIUM | "
          f"{len(routes['manual_entry'])} LOW\n")

    # ── STAGE 6: UX Response ──────────────────────────────────
    print("Stage 6: UX Response")
    display_results(routes, usage)

    # Exercise tasks
    print("=" * 60)
    print("YOUR TASKS:")
    print("=" * 60)
    print()
    print("1. Change SAMPLE_IMAGE_URL to an image relevant to your project.")
    print("   Ideas:")
    print("   - A receipt or invoice (if building an expense tool)")
    print("   - A document or form (if building a document processor)")
    print("   - A product photo (if building a shopping or inventory tool)")
    print("   - A screenshot of a UI (if building a dev tool)")
    print()
    print("2. Update task_description and fields_to_extract to match")
    print("   what YOUR project needs to extract from images.")
    print()
    print("3. Notice the confidence routing. If you get a MEDIUM or LOW")
    print("   on a field that should be HIGH, improve the prompt.")
    print("   Hint: be more specific about the field definition.")
    print()
    print("4. Try calling prepare_image_from_file() with a local image.")
    print("   This is the pattern you will use in your capstone backend.")
    print()
    print("When done: python examples/starter-code/03_multimodal_chat.py")


if __name__ == "__main__":
    main()
