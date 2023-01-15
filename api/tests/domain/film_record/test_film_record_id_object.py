import pytest
from src.domain.film_record.film_record_id_object import FilmRecordIdObject


class TestFilmRecordIdObject:
    @pytest.mark.parametrize("value", [(1), (144), (2001)])
    def test_constructor_should_create_instance(self, value):
        film_record_id = FilmRecordIdObject(value=value)

        assert film_record_id.value == value
