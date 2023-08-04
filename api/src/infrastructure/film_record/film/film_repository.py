# 標準ライブラリ
import os
from datetime import date
from logging import getLogger

# 外部ライブラリ
import requests

# 独自ライブラリ
from src.domain.film_record.film import AbstractFilmRepository, FilmEntity, TmdbIdObject
from src.domain.film_record.film.genre import FilmGenreDTO, FilmGenreEnum
from src.domain.film_record.film.poster import FilmPosterObject
from src.domain.film_record.film.series import FilmSeriesObject

logger = getLogger(__name__)


TMDB_KEY = os.environ["TMDB_KEY"]


class ImplFilmRepository(AbstractFilmRepository):
    def __init__(self) -> None:
        logger.debug("FilmRepo: init")

    def find_by_tmdb_id(self, id: TmdbIdObject) -> FilmEntity | None:
        url = f"https://api.themoviedb.org/3/movie/{id.value}"
        params = dict(
            api_key=TMDB_KEY,
            language="ja-JP",
        )

        res = requests.get(
            url=url,
            params=params,
            timeout=30,
        )
        res.raise_for_status()

        res_json = res.json()

        # series
        belongs_to_collection = res_json.get("belongs_to_collection")
        series: FilmSeriesObject | None = None
        if belongs_to_collection:
            series = FilmSeriesObject(
                name=belongs_to_collection["name"],
                poster=FilmPosterObject(
                    poster_url=belongs_to_collection["poster_path"],
                ),
            )
        # genres
        tmdb_genres = res_json.get("genres")
        genres: set[FilmGenreEnum] = set()
        if tmdb_genres:
            tmdb_genres_ids = list(map(lambda x: x["id"], tmdb_genres))
            genres = set(
                [
                    FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=tmdb_genre_id)
                    for tmdb_genre_id in tmdb_genres_ids
                ]
            )

        return FilmEntity(
            tmdb_id=id,
            title=res_json["title"],
            overview=res_json["overview"],
            release_date=date.fromisoformat(res_json["release_date"]),
            run_time=res_json["runtime"],
            series=series,
            poster=FilmPosterObject(
                poster_url=res_json["poster_path"],
            ),
            genres=genres,
        )
