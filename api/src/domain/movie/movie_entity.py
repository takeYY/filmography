from datetime import date

from src.domain.genre.genre_id_object import GenreIdObject
from src.domain.movie.movie_id_object import MovieIdObject
from src.domain.movie.series.movie_series_entity import MovieSeriesEntity
from src.domain.movie.tmdb_id_object import TmdbIdObject
from src.domain.poster.poster_object import PosterObject


class MovieEntity:
    """映画情報を扱うエンティティ

    Attributes
    ----------
    movie_id: MovieIdObject
        映画 ID を扱う値オブジェクト
    title: str
        映画タイトル
    overview: str
        映画概要
    poster: PosterObject
        ポスター画像を扱う値オブジェクト
    release_date: date
        公開日
    run_time: int
        上映時間
    series: MovieSeriesEntity
        映画シリーズを扱うエンティティ
    genres: list[GenreIdObject]
        ジャンル ID を扱う値オブジェクトのリスト
    tmdb_id: TmdbIdObject
        TMDb ID を扱う値オブジェクト
    created_on: date
        作成日, default=date.today()
    updated_on: date
        更新日, default=date.today()
    """

    def __init__(
        self,
        movie_id: MovieIdObject,
        title: str,
        overview: str,
        poster: PosterObject,
        release_date: date,
        run_time: int,
        series: MovieSeriesEntity,
        genres: list[GenreIdObject],
        tmdb_id: TmdbIdObject,
        created_on: date = date.today(),
        updated_on: date = date.today(),
    ):
        self.movie_id: MovieIdObject = movie_id
        self.title: str = title
        self.overview: str = overview
        self.poster: PosterObject = poster
        self.release_date: date = release_date
        self.run_time: int = run_time
        self.series: MovieSeriesEntity = series
        self.genres: list[GenreIdObject] = genres
        self.tmdb_id: TmdbIdObject = tmdb_id
        self.created_on: date = created_on
        self.updated_on: date = updated_on

    def __eq__(self, o: object) -> bool:
        if isinstance(o, MovieEntity):
            return self.movie_id == o.movie_id

        return False
