# HW01: Gemini API Model Comparison

This project demonstrates a Python-based implementation for interacting with multiple Google Gemini models. The script compares response accuracy, token usage, latency, and estimated costs for a standard logic puzzle.

## Project Structure

- `main.py`: The Python script that calls the Gemini API and processes the data.
- `.env.example`: A template for the environment variables (contains GEMINI_API_KEY).
- `README.md`: This file, containing the project analysis and reflection.

## API Model Comparison Table

| Call | Model                      | Input Tokens | Output Tokens | Total Tokens | Latency (ms) | Cost (paid equiv.) |
|------|----------------------------|--------------|---------------|--------------|--------------|--------------------|
| 1    | gemini-3-flash-preview     | 38          | 150          | 473         | 3410        | $0.00006380       |
| 2    | gemini-3.1-flash-lite-preview | 38       | 134          | 172         | 3910        | $0.00005740       |

## Reflection

Both models correctly identified that the answer to the logic puzzle remains 3 minutes because the cats work simultaneously. I was surprised to see that the gemini-3-flash-preview model had a significantly higher total token count than the sum of its input and output. Interestingly, the 3.1-flash-lite-preview model had a higher latency than the standard flash model, even though it is a "lite" version. Both models provided very clear step-by-step reasoning that broke down the individual rate of a single cat. Ultimately, while both were successful, the lite-preview model proved to be slightly more cost-effective based on the output results.
