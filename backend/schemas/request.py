from pydantic import BaseModel


class ScreeningRequest(BaseModel):
    job_description: str
    resume: str