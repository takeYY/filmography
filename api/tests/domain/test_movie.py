from datetime import date

import pytest
from src.domain.movie.movie_entity import MovieEntity
from src.domain.movie.movie_status_enum import MovieStatus
from src.domain.movie.tmdb_id_object import TmdbIdObject


class TestMovie:
    def test_constructor_should_create_instance(self):
        movie = MovieEntity(
            tmdb_id=TmdbIdObject(1),
            title="ターミネーター",
            cover="https://image.tmdb.org/t/p/w600_and_h900_bestv2/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg",
            status=MovieStatus.WATCHED,
            notion_id="12341234123412341234123412341234",
            created_on=date(2016, 12, 25),
        )

        assert movie.tmdb_id == TmdbIdObject(1)
        assert movie.title == "ターミネーター"
        assert movie.cover == "https://image.tmdb.org/t/p/w600_and_h900_bestv2/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg"
        assert movie.status == MovieStatus.WATCHED
        assert movie.notion_id == "12341234123412341234123412341234"
        assert movie.created_on == date(2016, 12, 25)

    def test_created_on_is_automatically_set2today(self):
        movie = MovieEntity(
            tmdb_id=TmdbIdObject(1),
            title="ターミネーター",
            cover="https://image.tmdb.org/t/p/w600_and_h900_bestv2/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg",
            status=MovieStatus.WATCHED,
            notion_id="12341234123412341234123412341234",
        )

        assert movie.tmdb_id == TmdbIdObject(1)
        assert movie.title == "ターミネーター"
        assert movie.cover == "https://image.tmdb.org/t/p/w600_and_h900_bestv2/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg"
        assert movie.status == MovieStatus.WATCHED
        assert movie.notion_id == "12341234123412341234123412341234"
        assert movie.created_on == date.today()

    @pytest.mark.parametrize(
        "watch_status",
        [
            (MovieStatus.WANNA_WATCH),
            (MovieStatus.WATCHED),
        ],
    )
    def test_status_setter_should_update_value(self, watch_status):
        movie = MovieEntity(
            tmdb_id=TmdbIdObject(1),
            title="ターミネーター",
            cover="https://image.tmdb.org/t/p/w600_and_h900_bestv2/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg",
            status=watch_status,
            notion_id="12341234123412341234123412341234",
            created_on=date(2016, 12, 25),
        )

        assert movie.status == watch_status
