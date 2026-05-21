from pydantic import BaseModel


class ScreeningResponse(BaseModel):
    score: float
    matching: dict
    explanation: str