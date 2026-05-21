from scorer import calculate_score

jd = {
    "technical_skills":
    ["Python", "SQL", "Docker"],

    "experience_years":
    3
}

resume = {
    "technical_skills":
    ["Python", "SQL"],

    "experience_years":
    3
}

matching = {
    "matched":
    ["Python", "SQL"]
}

print(
    calculate_score(
        jd,
        resume,
        matching
    )
)