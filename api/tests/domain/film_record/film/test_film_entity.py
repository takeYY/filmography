from datetime import date

import pytest
from src.domain.film_record.film.film_entity import FilmEntity
from src.domain.film_record.film.genre.film_genre_enum import FilmGenreEnum
from src.domain.film_record.film.poster.film_poster_object import FilmPosterObject
from src.domain.film_record.film.series.film_series_object import FilmSeriesObject
from src.domain.film_record.film.tmdb_id_object import TmdbIdObject


class TestFilmEntity:
    @pytest.fixture
    def init_film_series(self):
        """映画シリーズのテストデータ生成"""

        self.terminator_series = FilmSeriesObject(
            name="ターミネーターシリーズ",
            poster=FilmPosterObject(
                poster_url="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg",
            ),
        )

    @pytest.fixture
    def init_film(self, init_film_series):
        self.terminator = FilmEntity(
            tmdb_id=TmdbIdObject(value=218),
            title="ターミネーター",
            overview="アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる...",
            release_date=date(1985, 5, 4),
            run_time=108,
            series=self.terminator_series,
            poster=FilmPosterObject(
                poster_url="/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg",
            ),
            genres=set(
                [
                    FilmGenreEnum.ACTION,
                    FilmGenreEnum.THRILLER,
                    FilmGenreEnum.SF,
                ]
            ),
        )

    def test_constructor_should_create_instance(self, init_film):
        assert self.terminator.tmdb_id == TmdbIdObject(218)
        assert self.terminator.title == "ターミネーター"
        assert self.terminator.overview == "アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる..."
        assert self.terminator.release_date == date(1985, 5, 4)
        assert self.terminator.run_time == 108
        assert self.terminator.series == FilmSeriesObject(
            name="ターミネーターシリーズ",
            poster=FilmPosterObject(
                poster_url="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg",
            ),
        )
        assert self.terminator.poster == FilmPosterObject(
            poster_url="/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg",
        )
        assert self.terminator.genres == set(
            [
                FilmGenreEnum.ACTION,
                FilmGenreEnum.THRILLER,
                FilmGenreEnum.SF,
            ]
        )
