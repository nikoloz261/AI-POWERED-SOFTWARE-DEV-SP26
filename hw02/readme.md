# HW2 Audio Pipeline

This script demonstrates a complete audio processing pipeline using Text-to-Speech (TTS) and Speech-to-Text (STT) via OpenRouter. It takes text input, generates speech in two different voices, transcribes one back to text, and compares the results.

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up your API key:
   - Copy `.env.example` to `.env`
   - Add your OpenRouter API key to `.env`:
     ```
     OPENROUTER_API_KEY=your_actual_api_key_here
     ```

## Usage

Run the script with default text:
```
python hw2-audio-pipeline.py
```

Or provide custom text:
```
python hw2-audio-pipeline.py --text "Your custom text here."
```

## Expected Output

```
$ python hw2-audio-pipeline.py

=== HW2 Audio Pipeline ===

[1/4] Generating speech with voice: nova
  Text: "Machine learning models learn patterns from data..."
  Generated in 2.14s
  File: audio-output/voice_nova_sample.mp3 (47.3 KB)
  Cost: $0.0021

[2/4] Generating speech with voice: alloy
  Text: "Machine learning models learn patterns from data..."
  Generated in 1.98s
  File: audio-output/voice_alloy_sample.mp3 (45.8 KB)
  Cost: $0.0021

[3/4] Transcribing audio-output/voice_nova_sample.mp3
  Transcript: "Machine learning models learn patterns from data..."
  Transcribed in 1.52s
  Audio duration: 8.3s
  Cost: $0.0008

[4/4] Comparing original vs transcribed text
  Original:    "Machine learning models learn patterns from data..."
  Transcribed: "Machine learning models learn patterns from data..."
  Word overlap accuracy: 100.0%

=== Cost and Latency Summary ===
  TTS calls:  2 | Total cost: $0.0042 | Avg latency: 2.06s
  STT calls:  1 | Total cost: $0.0008 | Avg latency: 1.52s
  Pipeline total: $0.0050

=== Pipeline complete ===
```
