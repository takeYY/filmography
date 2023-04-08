# 標準ライブラリ
from datetime import date

# 外部ライブラリ
from pydantic import BaseModel, Field, validator

# 独自ライブラリ
from src.domain.film_record.watch_medium import WatchMediumEnum


class FilmAppreciationCreateModel(BaseModel):
    medium: WatchMediumEnum = Field(
        default=None,
        example=WatchMediumEnum.AMAZON_PRIME_VIDEO,
        description="鑑賞媒体",
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
