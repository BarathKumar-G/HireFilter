def match_entities(jd, resume):

    jd_skills = set(
        skill.lower()
        for skill in jd["technical_skills"]
    )

    resume_skills = set(
        skill.lower()
        for skill in resume["technical_skills"]
    )

    matched = jd_skills & resume_skills

    missing = jd_skills - resume_skills

    extra = resume_skills - jd_skills

    return {
        "matched": list(matched),
        "missing": list(missing),
        "extra": list(extra)
    }