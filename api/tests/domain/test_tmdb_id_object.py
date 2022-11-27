import pytest
from src.domain.movie.tmdb_id_object import TmdbIdObject


class TestTmdbIdObject:
    @pytest.mark.parametrize(
        "value",
        [
            (1),
            (144),
            (2001),
        ],
    )
    def test_constructor_should_create_instance(self, value):
        tmdb_id = TmdbIdObject(value=value)

        assert tmdb_id.value == value
