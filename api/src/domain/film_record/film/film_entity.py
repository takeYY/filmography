from datetime import date

from src.domain.film_record.film.genre.film_genre_enum import FilmGenreEnum
from src.domain.film_record.film.poster.film_poster_object import FilmPosterObject
from src.domain.film_record.film.series.film_series_object import FilmSeriesObject
from src.domain.film_record.film.tmdb_id_object import TmdbIdObject


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
        series: FilmSeriesObject,
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
        self.series: FilmSeriesObject = series
        self.poster: FilmPosterObject = poster
        self.genres: set[FilmGenreEnum] = genres
