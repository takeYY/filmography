from datetime import date
from enum import Enum

from pydantic import BaseModel, Field, validator


class MovieStatus(Enum):
    WATCHED = "Watched"
    WANNA_WATCH = "Wanna Watch"


class Movie(BaseModel):
    title: str = Field(example="ターミネーター")
    cover: str = Field(example="https://image.tmdb.org/t/p/w600_and_h900_bestv2/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg")
    status: MovieStatus = Field(example=MovieStatus.WATCHED)
    notion_id: str = Field(example="12341234123412341234123412341234")
    tmdb_id: int = Field(example=218)
    created_at: date = Field(example="2016-12-25", default=date.today())

    @validator("title")
    def vaildate_title(cls, v: str):
        if not v:
            raise ValueError("title is required.")

        return v

    @validator("notion_id")
    def validate_notion_id(cls, v: str):
        if not v:
            raise ValueError("notion_id is required.")

        if len(v) != 32:
            raise ValueError("notion_id must be 32 characters.")

        return v

    @validator("tmdb_id")
    def validate_tmdb_id(cls, v: str):
        if not v:
            raise ValueError("tmdb_id is required.")

        return v
