
from pydantic import BaseModel, Field


class ResumeAnalysis(BaseModel):

    compatibility_score: int = Field(
        ge=0,
        le=100,
        description="Compatibilidade estimada entre currículo e vaga"
    )

    identified_skills: list[str]

    missing_skills: list[str]

    strengths: list[str]

    improvements: list[str]

    recommendations: list[str]

    summary: str
