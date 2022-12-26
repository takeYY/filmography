import pytest
from src.domain.movie.series.movie_series_id_object import MovieSeriesIdObject


class TestMovieSeriesIdObject:
    @pytest.mark.parametrize(
        "value",
        [
            (1),
            (144),
            (2001),
        ],
    )
    def test_constructor_should_create_instance(self, value):
        movie_series_id = MovieSeriesIdObject(value=value)

        assert movie_series_id.value == value
