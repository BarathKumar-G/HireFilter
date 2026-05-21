def calculate_score(
    jd,
    resume,
    matching
):

    # ---------- Skills (50%) ----------

    total_skills = len(
        jd.get("technical_skills", [])
    )

    matched_skills = len(
        matching["skills"]["matched"]
    )

    if total_skills:
        skill_score = (
            matched_skills /
            total_skills
        ) * 50
    else:
        skill_score = 50

    # ---------- Tools (20%) ----------

    total_tools = len(
        jd.get("tools", [])
    )

    matched_tools = len(
        matching["tools"]["matched"]
    )

    if total_tools:
        tool_score = (
            matched_tools /
            total_tools
        ) * 20
    else:
        tool_score = 20

    # ---------- Experience (20%) ----------

    if resume.get("experience_years", 0) >= jd.get("experience_years", 0):
        experience_score = 20
    else:
        experience_score = 0

    # ---------- Education (10%) ----------

    if (
        jd.get("education")
        and resume.get("education")
    ):
        education_score = 10
    else:
        education_score = 0

    final_score = (
        skill_score
        + tool_score
        + experience_score
        + education_score
    )

    return round(final_score, 2)