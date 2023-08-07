# 標準ライブラリ
from datetime import date

# 独自ライブラリ
from src.domain.film_record.film.genre import FilmGenreEnum
from src.domain.film_record.film.poster import FilmPosterObject
from src.domain.film_record.film.series import FilmSeriesObject

from .tmdb_id_object import TmdbIdObject


class FilmEntity:
    """映画情報を扱うエンティティ

    Attributes
    ----------
    tmdb_id: TmdbIdObject
        TMDb ID を扱う値オブジェクト
    title: str
        タイトル
    overview: str
        概要
    release_date: date
        公開日
    run_time: int
        上映時間
    series: FilmSeriesObject
        映画シリーズを扱う値オブジェクト
    poster: FilmPosterObject
        映画ポスターを扱う値オブジェクト
    genres: set[FilmGenreEnum]
        映画ジャンルを扱う Enumの集合
    """

    def __init__(
        self,
        tmdb_id: TmdbIdObject,
        title: str,
        overview: str,
        release_date: date,
        run_time: int,
        series: FilmSeriesObject | None,
        poster: FilmPosterObject,
        genres: set[FilmGenreEnum],
    ):
        if not title:
            raise ValueError("titleがありません.")

        self.tmdb_id: TmdbIdObject = tmdb_id
        self.title: str = title
        self.overview: str = overview
        self.release_date: date = release_date
        self.run_time: int = run_time
        self.series: FilmSeriesObject | None = series
        self.poster: FilmPosterObject = poster
        self.genres: set[FilmGenreEnum] = genres

    def get_title(self):
        return self.title

    def get_overview(self):
        return self.overview

    def get_release_date_form(self) -> str:
        return self.release_date.strftime("%Y/%m/%d")

    def get_run_time_form(self):
        return f"{self.run_time}分"

    def get_poster_image(self):
        return self.poster.get_600x900()

    def get_genres(self):
        return self.genres
