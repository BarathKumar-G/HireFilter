from extractor import extract_entities

resume = """
Python
SQL
Docker
"""

result = extract_entities(resume)

print(result)