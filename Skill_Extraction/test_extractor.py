from extractor import extract_entities

resume = """
Python developer.
SQL.
Docker.
AWS Cloud Practitioner.
3 years experience.
"""

result = extract_entities(resume)

print(result)