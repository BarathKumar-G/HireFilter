from Skill_Extraction.extractor import extract_entities
from matching.matcher import match_entities
from scoring.scorer import calculate_score
from explanation.explainor import generate_explanation
jd_text = '''
Looking for a Python developer.

Required:
Python
SQL
Docker

Minimum 3 years experience.
'''
resume_text = '''
Python Developer

Skills:
Python
SQL

3 years experience.
'''

jd_data = extract_entities(jd_text)

resume_data = extract_entities(
    resume_text
)

matching = match_entities(
    jd_data,
    resume_data
)

score = calculate_score(
    jd_data,
    resume_data,
    matching
)

explanation = generate_explanation(
    score,
    matching
)

print("\nScore:", score)
print("\nMatching:", matching)
print("\nExplanation:")
print(explanation)