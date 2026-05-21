def calculate_score(
        jd,
        resume,
        matching
):

    total_jd_skills = len(
        jd["technical_skills"]
    )

    matched_skills = len(
        matching["matched"]
    )

    if total_jd_skills == 0:
        skill_score = 0
    else:
        skill_score = (
            matched_skills /
            total_jd_skills
        ) * 70

    exp_score = 0

    if resume["experience_years"] >= jd["experience_years"]:
        exp_score = 20

    edu_score = 10

    final_score = (
        skill_score +
        exp_score +
        edu_score
    )

    return round(final_score, 2)