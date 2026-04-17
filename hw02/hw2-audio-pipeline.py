import os
import time
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from pydub import AudioSegment

# Load API key
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

AUDIO_DIR = "audio-output"
os.makedirs(AUDIO_DIR, exist_ok=True)

logs = []

# COST FUNCTIONS
def tts_cost(text):
    return (len(text) / 1000) * 0.015

def stt_cost(seconds):
    return (seconds / 60) * 0.006

# TEXT COMPARISON

def word_overlap(a, b):
    a_words = set(a.lower().split())
    b_words = set(b.lower().split())
    return (len(a_words & b_words) / max(len(a_words), 1)) * 100

# TTS FUNCTION
def text_to_speech(text, voice, filename):
    path = os.path.join(AUDIO_DIR, filename)
    for attempt in range(2):
        try:
            start = time.time()
            response = client.audio.speech.create(
                model="openai/gpt-4o-mini-tts",
                voice=voice,
                input=text
            )
            with open(path, "wb") as f:
                f.write(response.content)
            latency = time.time() - start
            size_kb = os.path.getsize(path) / 1024
            cost = tts_cost(text)
            logs.append(("TTS", latency, cost))
            return path, latency, size_kb, cost
        except Exception as e:
            if attempt == 0:
                print(f"[TTS RETRY] {e}")
                time.sleep(1)
            else:
                print(f"[TTS ERROR] {e}")
                return None


# STT FUNCTION

def speech_to_text(filepath):
    if not os.path.exists(filepath):
        print("[ERROR] File not found")
        return None

    if not filepath.lower().endswith((".mp3", ".wav")):
        print("[ERROR] Unsupported format")
        return None

    duration = AudioSegment.from_file(filepath).duration_seconds

    for attempt in range(2):
        try:
            start = time.time()
            with open(filepath, "rb") as f:
                result = client.audio.transcriptions.create(
                    model="openai/whisper-1",
                    file=f
                )
            latency = time.time() - start
            cost = stt_cost(duration)
            logs.append(("STT", latency, cost))
            return result.text, latency, duration, cost
        except Exception as e:
            if attempt == 0:
                print(f"[STT RETRY] {e}")
                time.sleep(1)
            else:
                print(f"[STT ERROR] {e}")
                return None


def main():
    parser = argparse.ArgumentParser(description="HW2 Audio Pipeline")
    parser.add_argument("--text", default="Machine learning models learn patterns from data.", help="Text to process")
    args = parser.parse_args()
    text = args.text

    print("=== HW2 Audio Pipeline ===")

    # TTS 1
    print("\n[1/4] Generating speech with voice: nova")
    result1 = text_to_speech(text, "nova", "voice_nova_sample.mp3")
    if result1:
        path1, lat1, size1, cost1 = result1
        print(f"  Text: \"{text}\"")
        print(f"  Generated in {lat1:.2f}s")
        print(f"  File: {path1} ({size1:.1f} KB)")
        print(f"  Cost: ${cost1:.4f}")

    # TTS 2
    print("\n[2/4] Generating speech with voice: alloy")
    result2 = text_to_speech(text, "alloy", "voice_alloy_sample.mp3")
    if result2:
        path2, lat2, size2, cost2 = result2
        print(f"  Text: \"{text}\"")
        print(f"  Generated in {lat2:.2f}s")
        print(f"  File: {path2} ({size2:.1f} KB)")
        print(f"  Cost: ${cost2:.4f}")

    # STT on first
    if result1:
        print(f"\n[3/4] Transcribing {path1}")
        stt_result = speech_to_text(path1)
        if stt_result:
            transcript, stt_lat, duration, stt_cost = stt_result
            print(f"  Transcript: \"{transcript}\"")
            print(f"  Transcribed in {stt_lat:.2f}s")
            print(f"  Audio duration: {duration:.1f}s")
            print(f"  Cost: ${stt_cost:.4f}")

            # Compare
            print("\n[4/4] Comparing original vs transcribed text")
            score = word_overlap(text, transcript)
            print(f"  Original:    \"{text}\"")
            print(f"  Transcribed: \"{transcript}\"")
            print(f"  Word overlap accuracy: {score:.1f}%")

    # Summary
    tts_logs = [l for l in logs if l[0] == "TTS"]
    stt_logs = [l for l in logs if l[0] == "STT"]
    tts_cost_total = sum(l[2] for l in tts_logs)
    stt_cost_total = sum(l[2] for l in stt_logs)
    tts_latencies = [l[1] for l in tts_logs]
    stt_latencies = [l[1] for l in stt_logs]
    avg_tts_lat = sum(tts_latencies) / len(tts_latencies) if tts_latencies else 0
    avg_stt_lat = sum(stt_latencies) / len(stt_latencies) if stt_latencies else 0

    print("\n=== Cost and Latency Summary ===")
    print(f"  TTS calls:  {len(tts_logs)} | Total cost: ${tts_cost_total:.4f} | Avg latency: {avg_tts_lat:.2f}s")
    print(f"  STT calls:  {len(stt_logs)} | Total cost: ${stt_cost_total:.4f} | Avg latency: {avg_stt_lat:.2f}s")
    print(f"  Pipeline total: ${tts_cost_total + stt_cost_total:.4f}")

    print("\n=== Pipeline complete ===")


if __name__ == "__main__":
    main()