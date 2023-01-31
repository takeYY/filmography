import os
from datetime import date

import requests
from base_model.film_record.create.film_record_create_model import FilmRecordCreateModel
from src.application.film_record.command.interface.film_record_command_domain_service import (
    IFilmRecordCommandDomainService,
)
from src.domain.film_record.appreciation.film_appreciation_entity import FilmAppreciationEntity
from src.domain.film_record.appreciation.film_appreciation_id_object import FilmAppreciationIdObject
from src.domain.film_record.film.film_entity import FilmEntity
from src.domain.film_record.film.genre.film_genre_dto import FilmGenreDTO
from src.domain.film_record.film.poster.film_poster_object import FilmPosterObject
from src.domain.film_record.film.series.film_series_object import FilmSeriesObject
from src.domain.film_record.film.tmdb_id_object import TmdbIdObject
from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_id_object import FilmRecordIdObject
from src.domain.film_record.film_record_repository import IFilmRecordRepository


class ImplFilmRecordCommandDomainService(IFilmRecordCommandDomainService):
    def __init__(self, film_record_repository: IFilmRecordRepository):
        self.film_record_repository: IFilmRecordRepository = film_record_repository

    def create_film_record(self, film_record_model: FilmRecordCreateModel) -> FilmRecordEntity:
        # TODO: リファクタリングする
        # TODO: TMDb APIを叩いて、失敗した時のリトライとエラーハンドリングを追加する
        movie_detail_url = "https://api.themoviedb.org/3/movie/"
        tmdb_id: int = film_record_model.film.tmdb_id
        params = dict(
            api_key=os.environ.get("TMDB_KEY"),
            language="ja-JP",
        )

        res = requests.get(
            url=f"{movie_detail_url}{tmdb_id}",
            params=params,
        )
        res.raise_for_status()
        res_json = res.json()

        title: str = res_json.get("title", "")
        overview: str = res_json.get("overview", "")

        year, month, day = self.__get_release_year_month_day(res_json.get("release_date", "2016-12-25"))
        release_date: date = date(year, month, day)
        run_time: int = res_json.get("run_time")
        collection: dict[str, str] = res_json.get("belongs_to_collection")
        series_name: str = collection.get("name", "")
        series_poster: str = collection.get("poster_path", "")
        poster: str = res_json.get("poster_path", "")
        genres: list[dict[str, int]] = res_json.get("genres")

        film_record = FilmRecordEntity(
            film_record_id=FilmRecordIdObject(tmdb_id),
            appreciation_status=film_record_model.appreciation_status,
            note=film_record_model.note,
            film=FilmEntity(
                tmdb_id=TmdbIdObject(tmdb_id),
                title=title,
                overview=overview,
                release_date=release_date,
                run_time=run_time,
                series=FilmSeriesObject(
                    name=series_name,
                    poster=FilmPosterObject(poster_url=series_poster),
                ),
                poster=FilmPosterObject(poster_url=poster),
                genres=set(
                    [
                        FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=genre.get("id", 144))
                        for genre in genres
                    ]
                ),
            ),
            evaluation=film_record_model.evaluation,
            film_appreciations=[
                FilmAppreciationEntity(
                    film_appreciation_id=FilmAppreciationIdObject(tmdb_id),
                    medium=film_appreciation_model.medium,
                    appreciation_date=film_appreciation_model.appreciation_date,
                )
                for film_appreciation_model in film_record_model.appreciations
            ],
        )

        return self.film_record_repository.create(film_record=film_record)

    def __get_release_year_month_day(self, release_date_str: str) -> tuple[int, int, int]:
        year, month, day = release_date_str.split("-")
        return int(year), int(month), int(day)
