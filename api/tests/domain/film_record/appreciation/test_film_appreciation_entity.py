from datetime import date

import pytest
from src.domain.film_record.appreciation.film_appreciation_entity import FilmAppreciationEntity
from src.domain.film_record.appreciation.film_appreciation_id_object import FilmAppreciationIdObject


class TestFilmAppreciationEntity:
    @pytest.fixture
    def init_film_appreciation(self):
        self.prime_video = FilmAppreciationEntity(
            film_appreciation_id=FilmAppreciationIdObject(1),
            medium="Amazon Prime Video",
            appreciation_date=date(2022, 12, 25),
        )
        self.netflix = FilmAppreciationEntity(
            film_appreciation_id=FilmAppreciationIdObject(2),
            medium="Netflix",
            appreciation_date=date(2023, 1, 1),
        )

    def test_constructor_should_create_instance(self, init_film_appreciation):
        assert self.prime_video.film_appreciation_id == FilmAppreciationIdObject(1)
        assert self.prime_video.medium == "Amazon Prime Video"
        assert self.prime_video.appreciation_date == date(2022, 12, 25)

    @pytest.mark.parametrize(
        "medium",
        [
            ("Amazon Prime Video"),
            ("Netflix"),
            ("U-NEXT"),
        ],
    )
    def test_medium_setter_should_update_value(self, medium):
        film_appreciation = FilmAppreciationEntity(
            film_appreciation_id=FilmAppreciationIdObject(2),
            medium="Disney+",
            appreciation_date=date(2023, 1, 1),
        )
        film_appreciation.medium = medium

        assert film_appreciation.medium == medium
