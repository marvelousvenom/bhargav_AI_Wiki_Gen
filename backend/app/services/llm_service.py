import json
import re
from groq import Groq
from app.core.config import settings


# Initialize Groq client
client = Groq(api_key=settings.GROQ_API_KEY)


def extract_json(text: str) -> dict:
    """
    Safely extract JSON from LLM response
    """
    # Remove markdown code blocks if present
    text = re.sub(r"```json|```", "", text).strip()

    # Extract JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No valid JSON found in LLM response")

    return json.loads(match.group())


def generate_quiz_llm(context: str) -> dict:
    # Load prompt
    with open("app/prompts/quiz_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

    # Call Groq LLM
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ supported model
        messages=[
            {
                "role": "user",
                "content": prompt.format(context=context)
            }
        ],
        temperature=0.3
    )

    raw_output = response.choices[0].message.content

    # ✅ SAFE JSON PARSING
    return extract_json(raw_output)
