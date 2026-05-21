import json
import os
import re

from dotenv import load_dotenv
from groq import Groq

from config.settings import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)



def extract_entities(text: str):

    prompt = f"""
You are an expert resume parser.

Extract:

1. technical_skills
2. tools
3. certifications
4. education
5. experience_years

Rules:
- Return ONLY valid JSON.
- Do not explain your answer.
- Do not use markdown.
- Do not include additional text.
- Use empty lists if information is missing.
- Use null if education is missing.
- Use 0 if experience is missing.

Example:

Input:
Python developer skilled in Python and SQL.
Worked with Docker.
3 years experience.
AWS Cloud Practitioner certified.

Output:
{{
    "technical_skills": ["Python", "SQL"],
    "tools": ["Docker"],
    "certifications": ["AWS Cloud Practitioner"],
    "education": null,
    "experience_years": 3
}}

Text:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Return only valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content.strip()

    try:
        result = json.loads(content)

    except json.JSONDecodeError:

        # Fallback if model still returns extra text
        match = re.search(r"\{.*\}", content, re.DOTALL)

        if not match:
            raise ValueError("No JSON object found in LLM response")

        result = json.loads(match.group())

    required_keys = {
        "technical_skills",
        "tools",
        "certifications",
        "education",
        "experience_years"
    }

    missing_keys = required_keys - result.keys()

    if missing_keys:
        raise ValueError(
            f"Missing required fields: {missing_keys}"
        )

    return result