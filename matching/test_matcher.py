from matcher import match_entities

jd = {
    "technical_skills":
    ["Python", "SQL", "Docker"]
}

resume = {
    "technical_skills":
    ["Python", "SQL"]
}

print(match_entities(jd, resume))