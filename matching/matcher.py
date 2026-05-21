def match_entities(jd, resume):

    jd_skills = set(
        skill.lower()
        for skill in jd.get("technical_skills", [])
    )

    resume_skills = set(
        skill.lower()
        for skill in resume.get("technical_skills", [])
    )

    jd_tools = set(
        tool.lower()
        for tool in jd.get("tools", [])
    )

    resume_tools = set(
        tool.lower()
        for tool in resume.get("tools", [])
    )

    return {
        "skills": {
            "matched": list(jd_skills & resume_skills),
            "missing": list(jd_skills - resume_skills),
            "extra": list(resume_skills - jd_skills)
        },
        "tools": {
            "matched": list(jd_tools & resume_tools),
            "missing": list(jd_tools - resume_tools),
            "extra": list(resume_tools - jd_tools)
        }
    }