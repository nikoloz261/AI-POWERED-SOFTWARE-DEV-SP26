import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Task 1 & 3: Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not set in .env. Check Task 3!")

client = genai.Client(api_key=api_key)

prompt = "Solve this logic puzzle: If 3 cats can catch 3 mice in 3 minutes, how long will it take 6 cats to catch 6 mice? Explain your reasoning."

# Task 4: Use the specific models from your assignment
models = [
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite-preview"
]

print("\n=== Gemini Model Comparisons ===\n")

for model_id in models:
    start_time = time.time()
    
    try:
        # Task 4: Call the model
        response = client.models.generate_content(
            model=model_id,
            contents=prompt
        )
        
        end_time = time.time()
        latency_ms = int((end_time - start_time) * 1000)

        # Task 4: Extract response and metadata
        text = response.text
        usage = response.usage_metadata
        
        input_tokens = usage.prompt_token_count
        output_tokens = usage.candidates_token_count
        total_tokens = usage.total_token_count

        # Task 4: Cost calculation (using the assignment's logic)
        cost_estimate = (
            (input_tokens * 0.0001 / 1000) + 
            (output_tokens * 0.0004 / 1000)
        )

        # Output for Task 4
        print(f"Model: {model_id}")
        print(f"Response: {text.strip()}")
        print(f"Input Tokens: {input_tokens}")
        print(f"Output Tokens: {output_tokens}")
        print(f"Total Tokens: {total_tokens}")
        print(f"Latency: {latency_ms} ms")
        print(f"Paid‑tier cost equiv.: ${cost_estimate:.8f}")
        
    except errors.ClientError as e:
        print(f"Error calling {model_id}: {e}")
        print("Note: If you get a 429 with 'limit: 0', the model might not be enabled for your key yet.")

    print("\n" + "-"*50 + "\n")
    time.sleep(5)