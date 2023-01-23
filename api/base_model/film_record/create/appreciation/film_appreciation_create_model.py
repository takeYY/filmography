from datetime import date

from pydantic import BaseModel, Field, validator


class FilmAppreciationCreateModel(BaseModel):
    medium: str = Field(
        default=None,
        example="Amazon Prime Video",
        description="鑑賞媒体. Enumにしても良さそう",
    )
    appreciation_date: date = Field(
        default=date(2016, 12, 25),
        example=date(2022, 12, 25),
        description="鑑賞日",
    )

    @validator("medium")
    def validate_medium(cls, v: str):
        if not v:
            raise ValueError("medium is required.")

        return v

    @validator("appreciation_date")
    def validate_appreciation_date(cls, v: date):
        if not v:
            raise ValueError("appreciation_date is required.")

        return v
