import os
import re

from dotenv import load_dotenv
from groq import Groq

from config.settings import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)


def generate_explanation(score, matching):

    prompt = f"""
You are an HR resume screening assistant.

Candidate Score: {score}

Matched Skills:
{matching['skills']['matched']}

Missing Skills:
{matching['skills']['missing']}

Matched Tools:
{matching['tools']['matched']}

Missing Tools:
{matching['tools']['missing']}

Generate a concise explanation (3-5 sentences).

Rules:
- Mention strengths.
- Mention missing skills.
- Mention overall suitability.
- Return plain text only.
- Do not use markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Return only the explanation text."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content

    if not content:
        raise ValueError("Empty response received from LLM")

    content = content.strip()

    # Remove markdown code fences if model adds them
    content = re.sub(r"^```.*?\n", "", content, flags=re.DOTALL)
    content = re.sub(r"\n```$", "", content)

    return content.strip()