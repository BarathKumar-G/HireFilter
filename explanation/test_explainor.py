from explainor import generate_explanation

matching = {
    "matched": ["Python", "SQL"],
    "missing": ["Docker"]
}

result = generate_explanation(
    score=86,
    matching=matching
)

print(result)