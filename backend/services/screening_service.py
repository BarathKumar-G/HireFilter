from services.extractor import extract_entities
from services.matcher import match_entities
from services.scorer import calculate_score
from services.explainor import generate_explanation


def screen_candidate(
    job_description: str,
    resume: str
):

    jd_data = extract_entities(
        job_description
    )

    resume_data = extract_entities(
        resume
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

    return {
        "score": score,
        "matching": matching,
        "explanation": explanation
    }