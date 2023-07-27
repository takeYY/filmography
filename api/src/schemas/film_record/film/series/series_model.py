# 外部ライブラリ
from pydantic import BaseModel, Field


class FilmSeriesPosterModel(BaseModel):
    poster_url: str = Field(description="映画シリーズのポスターURL", example="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg")


class FilmSeriesModel(BaseModel):
    name: str = Field(description="映画シリーズ名", example="ターミネーターシリーズ")
    poster: FilmSeriesPosterModel
