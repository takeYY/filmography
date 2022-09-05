from typing import List, Optional

from pydantic import BaseModel, Field, validator


class MovieWannaWatch(BaseModel):
    title: str = Field(example="ターミネーター3")
    cover: str = Field(example="https://image.tmdb.org/t/p/w600_and_h900_bestv2/oaA02LgAPk9SAMBfEEiGNbEnaAk.jpg")
    genres: List[str] = Field(example=["アクション", "SF", "サスペンス"])
    note: Optional[str] = Field(example="2作目を超えられるかな？")
    tmdb_id: int = Field(example=296)

    @validator("title")
    def vaildate_title(cls, v: str):
        if not v:
            raise ValueError("title is required.")

        return v

    @validator("tmdb_id")
    def validate_tmdb_id(cls, v: str):
        if not v:
            raise ValueError("tmdb_id is required.")

        return v
