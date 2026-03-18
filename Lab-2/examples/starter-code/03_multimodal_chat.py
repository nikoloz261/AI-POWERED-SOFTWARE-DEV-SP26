"""
Exercise 3: Multimodal Multi-Turn Chat
CS-AI-2025 Lab 2 | Spring 2026

This exercise demonstrates multi-turn conversation with image context —
a pattern many capstone projects will use. The user can ask follow-up
questions about an image without re-uploading it on every turn.

This is a terminal-based chat loop. In your capstone, this pattern
maps to a chat UI where the user uploads an image once and then
asks questions about it.

Usage:
    python examples/starter-code/03_multimodal_chat.py
"""

import os
import base64
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

MODEL = "google/gemini-3.1-flash"

# ─────────────────────────────────────────────────────────────
# Client
# ─────────────────────────────────────────────────────────────

def create_client() -> OpenAI:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in .env file. See quickstart.md.")
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        default_headers={
            "HTTP-Referer": "https://github.com/ZA-KIU-Classroom/AI-POWERED-SOFTWARE-DEV-SP26",
            "X-Title": "CS-AI-2025 Lab 2"
        }
    )


# ─────────────────────────────────────────────────────────────
# Image preparation
# ─────────────────────────────────────────────────────────────

def image_content_from_url(url: str) -> dict:
    return {"type": "image_url", "image_url": {"url": url}}


def image_content_from_file(path: str) -> dict:
    ext = path.lower().split(".")[-1]
    media_types = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp"}
    media_type = media_types.get(ext, "image/jpeg")
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    return {"type": "image_url", "image_url": {"url": f"data:{media_type};base64,{b64}"}}


# ─────────────────────────────────────────────────────────────
# Chat session
# ─────────────────────────────────────────────────────────────

class MultimodalChatSession:
    """
    Maintains a conversation history that includes an initial image.

    Key insight: The image is sent only in the FIRST message.
    Subsequent messages are text-only, but the model retains the
    visual context from the first message within the conversation.

    This is the pattern you will implement in your capstone backend.
    """

    def __init__(self, client: OpenAI, system_prompt: str, model: str = MODEL):
        self.client = client
        self.model = model
        self.system_prompt = system_prompt
        self.conversation_history: list[dict] = []
        self.image_attached = False
        self.total_tokens = 0
        self.total_cost = 0.0
        self.turn_count = 0

    def attach_image(self, image_content: dict, initial_message: str) -> str:
        """
        Start the conversation with an image and an initial question.
        The image is sent once and retained in context for the session.
        """
        if self.image_attached:
            return "Image already attached. Continue the conversation with text."

        # First message: image + text combined
        user_message = {
            "role": "user",
            "content": [
                image_content,
                {"type": "text", "text": initial_message}
            ]
        }

        self.conversation_history.append(user_message)
        response_text = self._send()
        self.image_attached = True
        return response_text

    def chat(self, user_message: str) -> str:
        """Send a follow-up text message. The model retains image context."""
        if not self.image_attached:
            return "No image attached yet. Call attach_image() first."

        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        return self._send()

    def _send(self) -> str:
        """Send the current conversation history to the model."""
        self.turn_count += 1
        start_time = time.time()

        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        messages.extend(self.conversation_history)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=512
        )

        latency_ms = (time.time() - start_time) * 1000
        response_text = response.choices[0].message.content

        # Track usage
        if response.usage:
            self.total_tokens += response.usage.total_tokens
            cost = (
                (response.usage.prompt_tokens / 1_000_000 * 0.10) +
                (response.usage.completion_tokens / 1_000_000 * 0.40)
            )
            self.total_cost += cost
            token_info = f"[{response.usage.total_tokens} tokens | {latency_ms:.0f}ms | ${cost:.6f}]"
        else:
            token_info = f"[{latency_ms:.0f}ms]"

        # Add assistant response to history for next turn
        self.conversation_history.append({
            "role": "assistant",
            "content": response_text
        })

        return f"{response_text}\n\n{token_info}"

    def session_summary(self) -> str:
        return (
            f"Session: {self.turn_count} turns | "
            f"{self.total_tokens} total tokens | "
            f"${self.total_cost:.5f} total cost"
        )


# ─────────────────────────────────────────────────────────────
# Main exercise
# ─────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("CS-AI-2025 Lab 2 | Exercise 3: Multimodal Chat")
    print("=" * 60)
    print()
    print("This exercise demonstrates multi-turn conversation with")
    print("image context — a pattern your capstone will likely use.")
    print()
    print("You will attach an image once, then ask follow-up questions")
    print("without re-uploading the image each time.")
    print()

    client = create_client()

    # System prompt — this sets the assistant's persona for the session
    # In your capstone, this would reflect your specific use case
    system_prompt = (
        "You are a helpful visual analysis assistant. "
        "When given an image, analyse it carefully and answer questions about it. "
        "Be concise and specific. "
        "If you are uncertain about something you see, say so explicitly."
    )

    session = MultimodalChatSession(client, system_prompt)

    # The sample image — replace with something relevant to your project
    IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/640px-Camponotus_flavomarginatus_ant.jpg"

    print("─" * 60)
    print("ATTACHING IMAGE:")
    print(f"  {IMAGE_URL[:70]}...")
    print()
    print("Sending first message to the model...")
    print()

    image_content = image_content_from_url(IMAGE_URL)

    # First message: describe what you see
    initial_message = "Please describe what you see in this image in detail."
    response = session.attach_image(image_content, initial_message)

    print("You:       ", initial_message)
    print()
    print("Assistant: ", response)
    print()

    # Now demonstrate multi-turn follow-up without re-uploading the image
    follow_ups = [
        "What colour is the primary subject?",
        "What is the background of the image?",
        "If you had to classify this image into one category (nature / technology / document / people / food / other), which would you choose and why?"
    ]

    for question in follow_ups:
        input(f"Press Enter to ask: '{question}'\n")
        print(f"You:       {question}")
        print()
        response = session.chat(question)
        print(f"Assistant: {response}")
        print()

    # Interactive mode — let the student ask their own questions
    print("─" * 60)
    print("INTERACTIVE MODE — Ask your own questions about the image.")
    print("Type 'quit' to end the session.")
    print("─" * 60)
    print()

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            break
        print()
        response = session.chat(user_input)
        print(f"Assistant: {response}")
        print()

    print()
    print("─" * 60)
    print("SESSION SUMMARY:")
    print(f"  {session.session_summary()}")
    print("─" * 60)
    print()

    print("=" * 60)
    print("YOUR TASKS:")
    print("=" * 60)
    print()
    print("1. Change IMAGE_URL to an image relevant to your project.")
    print("   Ask follow-up questions that a user of YOUR app would ask.")
    print()
    print("2. Change the system_prompt to reflect your capstone use case.")
    print("   Example for a receipt tracker:")
    print('   "You are an expense tracking assistant. When given a receipt,')
    print('    extract the vendor, date, total amount, and itemised costs.')
    print('    Always respond in JSON format."')
    print()
    print("3. Notice the token count per turn.")
    print("   Multi-turn chat sends the full history each time.")
    print("   After 10 turns, how much context are you sending?")
    print("   This is why context window management matters in production.")
    print()
    print("4. Discuss with your team: which of these three exercises")
    print("   (01, 02, 03) is most relevant to your capstone architecture?")
    print("   The answer informs which starter code you should build from.")


if __name__ == "__main__":
    main()
