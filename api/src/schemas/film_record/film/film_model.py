# 標準ライブラリ
from datetime import date

# 外部ライブラリ
from pydantic import BaseModel, Field

# 独自ライブラリ
from src.domain.film_record.film.genre import FilmGenreEnum
from src.schemas.film_record.film.poster import FilmPosterModel
from src.schemas.film_record.film.series import FilmSeriesModel


class TmdbIdModel(BaseModel):
    value: str = Field(description="TMDbのID", example="218")


class FilmModel(BaseModel):
    tmdb_id: TmdbIdModel
    title: str = Field(description="タイトル", example="ターミネーター")
    overview: str = Field(description="概要", example="アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる...")
    release_date: date = Field(description="公開日", example=date(1985, 5, 4))
    run_time: int = Field(description="上映時間", example="108")
    series: FilmSeriesModel
    poster: FilmPosterModel
    genres: list[FilmGenreEnum]
