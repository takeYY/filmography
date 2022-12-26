from datetime import date

from src.domain.genre.genre_id_object import GenreIdObject
from src.domain.movie.movie_entity import MovieEntity
from src.domain.movie.movie_id_object import MovieIdObject
from src.domain.movie.series.movie_series_entity import MovieSeriesEntity
from src.domain.movie.series.movie_series_id_object import MovieSeriesIdObject
from src.domain.movie.tmdb_id_object import TmdbIdObject
from src.domain.poster.poster_object import PosterObject


class TestMovieEntity:
    def test_constructor_should_create_instance(self):
        movie = MovieEntity(
            movie_id=MovieIdObject(value=1),
            title="ターミネーター",
            overview="アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる。同じくして放電の中からもう一人の男カイル・リースが現れる。...",
            poster=PosterObject(poster_path="/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg"),
            release_date=date(1984, 10, 26),
            run_time=108,
            series=MovieSeriesEntity(
                id=MovieSeriesIdObject(value=528),
                name="ターミネーター シリーズ",
                poster=PosterObject(poster_path="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg"),
            ),
            genres=[
                GenreIdObject(18),
                GenreIdObject(28),
                GenreIdObject(53),
                GenreIdObject(10752),
            ],
            tmdb_id=TmdbIdObject(value=218),
            created_on=date(2016, 12, 25),
            updated_on=date(2016, 12, 25),
        )
        assert movie.movie_id == MovieIdObject(1)
        assert movie.title == "ターミネーター"
        assert movie.overview == "アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる。同じくして放電の中からもう一人の男カイル・リースが現れる。..."
        assert movie.poster == PosterObject(poster_path="/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg")
        assert movie.release_date == date(1984, 10, 26)
        assert movie.run_time == 108
        assert movie.series == MovieSeriesEntity(
            id=MovieSeriesIdObject(value=528),
            name="ターミネーター シリーズ",
            poster=PosterObject(poster_path="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg"),
        )
        assert movie.tmdb_id == TmdbIdObject(218)
        assert movie.created_on == date(2016, 12, 25)
        assert movie.updated_on == date(2016, 12, 25)

    def test_created_on_is_automatically_set2today(self):
        movie = MovieEntity(
            movie_id=MovieIdObject(value=1),
            title="ターミネーター",
            overview="アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる。同じくして放電の中からもう一人の男カイル・リースが現れる。...",
            poster=PosterObject(poster_path="/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg"),
            release_date=date(1984, 10, 26),
            run_time=108,
            series=MovieSeriesEntity(
                id=MovieSeriesIdObject(value=528),
                name="ターミネーター シリーズ",
                poster=PosterObject(poster_path="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg"),
            ),
            genres=[
                GenreIdObject(18),
                GenreIdObject(28),
                GenreIdObject(53),
                GenreIdObject(10752),
            ],
            tmdb_id=TmdbIdObject(value=218),
        )
        assert movie.movie_id == MovieIdObject(1)
        assert movie.title == "ターミネーター"
        assert movie.overview == "アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる。同じくして放電の中からもう一人の男カイル・リースが現れる。..."
        assert movie.poster == PosterObject(poster_path="/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg")
        assert movie.release_date == date(1984, 10, 26)
        assert movie.run_time == 108
        assert movie.series == MovieSeriesEntity(
            id=MovieSeriesIdObject(value=528),
            name="ターミネーター シリーズ",
            poster=PosterObject(poster_path="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg"),
        )
        assert movie.tmdb_id == TmdbIdObject(218)
        assert movie.created_on == date.today()
        assert movie.updated_on == date.today()
