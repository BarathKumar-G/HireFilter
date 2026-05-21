from fastapi import APIRouter

from schemas.request import ScreeningRequest

from services.screening_service import (
    screen_candidate
)

router = APIRouter()


@router.post("/screen")
def screen_resume(
    payload: ScreeningRequest
):

    result = screen_candidate(
        payload.job_description,
        payload.resume
    )

    return result