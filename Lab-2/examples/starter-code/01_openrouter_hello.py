"""
Exercise 1: Hello OpenRouter
CS-AI-2025 Lab 2 | Spring 2026

Your first call to OpenRouter. This script connects to Gemini Flash
via the OpenRouter API and confirms your organisation key is working.

Run this first. If it works, proceed to Exercise 2.

Usage:
    python examples/starter-code/01_openrouter_hello.py
"""

import os
import time
from openai import OpenAI
from dotenv import load_dotenv

# Always load environment variables before anything else
load_dotenv()


def create_client() -> OpenAI:
    """Create an OpenRouter-compatible OpenAI client."""
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY not found in environment.\n"
            "Create a .env file in this directory with:\n"
            "  OPENROUTER_API_KEY=sk-or-your-key-here\n"
            "See quickstart.md for full setup instructions."
        )

    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        default_headers={
            "HTTP-Referer": "https://github.com/ZA-KIU-Classroom/AI-POWERED-SOFTWARE-DEV-SP26",
            "X-Title": "CS-AI-2025 Lab 2"
        }
    )


def call_model(client: OpenAI, prompt: str, model: str = "google/gemini-3.1-flash") -> dict:
    """
    Call the specified model and return the response with timing and usage.

    Returns a dict with:
        - text: the model's response text
        - input_tokens: tokens consumed by the prompt
        - output_tokens: tokens in the response
        - latency_ms: round-trip time in milliseconds
        - cost_usd: approximate cost in USD (paid-tier equivalent)
    """
    start_time = time.time()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=256
    )

    latency_ms = (time.time() - start_time) * 1000

    # Usage data — guard against None (some models omit it)
    input_tokens = response.usage.prompt_tokens if response.usage else 0
    output_tokens = response.usage.completion_tokens if response.usage else 0

    # Approximate cost for google/gemini-3.1-flash
    # $0.10 per 1M input tokens, $0.40 per 1M output tokens
    # These figures are approximate — check openrouter.ai for current pricing
    cost_usd = (input_tokens / 1_000_000 * 0.10) + (output_tokens / 1_000_000 * 0.40)

    return {
        "text": response.choices[0].message.content,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "latency_ms": latency_ms,
        "cost_usd": cost_usd,
        "model": model
    }


def main():
    print("=" * 60)
    print("CS-AI-2025 Lab 2 | Exercise 1: Hello OpenRouter")
    print("=" * 60)
    print()

    # Step 1: Create the client
    print("Connecting to OpenRouter...")
    try:
        client = create_client()
        print("Client created successfully.\n")
    except ValueError as e:
        print(f"ERROR: {e}")
        return

    # Step 2: Your prompt — change this to something related to your project idea
    prompt = (
        "Explain what a vision-language model is in exactly two sentences. "
        "Use plain language suitable for a first-year computer science student."
    )

    model = "google/gemini-3.1-flash"

    print(f"Model:  {model}")
    print(f"Prompt: {prompt}")
    print()
    print("Sending request...")
    print()

    # Step 3: Make the call
    try:
        result = call_model(client, prompt, model)
    except Exception as e:
        print(f"API call failed: {e}")
        print("\nCommon causes:")
        print("  - Invalid API key (check .env file)")
        print("  - Organisation invitation not accepted yet")
        print("  - Rate limit hit (wait 10 seconds and retry)")
        return

    # Step 4: Display results
    print("─" * 60)
    print("RESPONSE:")
    print(result["text"])
    print("─" * 60)
    print()
    print("USAGE:")
    print(f"  Input tokens:  {result['input_tokens']}")
    print(f"  Output tokens: {result['output_tokens']}")
    print(f"  Total tokens:  {result['input_tokens'] + result['output_tokens']}")
    print(f"  Latency:       {result['latency_ms']:.0f}ms")
    print(f"  Cost (approx): ${result['cost_usd']:.6f}")
    print()

    # Step 5: Interpretation guide
    print("─" * 60)
    print("WHAT TO NOTICE:")
    print()

    if result["latency_ms"] < 2000:
        print("  ✓ Latency is under 2 seconds — good for interactive UX")
    elif result["latency_ms"] < 5000:
        print("  ⚠ Latency is 2–5 seconds — acceptable for batch tasks, slow for interactive")
    else:
        print("  ✗ Latency is over 5 seconds — investigate: rate limiting or network issue?")

    if result["input_tokens"] > 0:
        print(f"  ✓ Token usage data received — your org key is billing correctly")
    else:
        print("  ⚠ Token usage data was None — model may not report usage; check OpenRouter dashboard")

    print(f"  ✓ Cost per call at this length: ~${result['cost_usd']:.6f}")
    print(f"    At 100 calls/day: ~${result['cost_usd'] * 100:.4f}/day")
    print(f"    At 10,000 calls/day: ~${result['cost_usd'] * 10000:.2f}/day")
    print()
    print("─" * 60)
    print()
    print("Exercise 1 complete.")
    print("Next: python examples/starter-code/02_image_analyser.py")
    print()

    # YOUR TASK — modify this exercise:
    print("=" * 60)
    print("YOUR TASK:")
    print("=" * 60)
    print("1. Change the prompt to ask something related to YOUR capstone idea")
    print("2. Run again and compare the response")
    print("3. Try changing the model to 'google/gemini-3.1-pro' — what changes?")
    print("   (Note: Pro costs ~16x more than Flash — is the quality difference worth it?)")
    print("4. Record your observations — you will reference these in your Design Review")


if __name__ == "__main__":
    main()
