# 標準ライブラリ
from datetime import date
from typing import List, Optional

# 外部ライブラリ
from pydantic import BaseModel, Field, validator


class MovieWatched(BaseModel):
    title: str = Field(example="ターミネーター2")
    cover: str = Field(example="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ghKQ6it5j7KjdYghT5EDthVNXlD.jpg")
    rating: str = Field(example="★★★★★")
    viewed: int = Field(example=3)
    genres: List[str] = Field(example=["アクション", "SF", "サスペンス"])
    first_watched_at: date = Field(example="2016-12-25")
    last_watched_at: date = Field(example="2020-12-25")
    note: Optional[str] = Field(example="最高峰の映画")
    tmdb_id: int = Field(example=280)

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
