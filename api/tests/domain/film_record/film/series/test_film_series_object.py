import pytest
from src.domain.film_record.film.poster.film_poster_object import FilmPosterObject
from src.domain.film_record.film.series.film_series_object import FilmSeriesObject


class TestFilmSeriesObject:
    @pytest.mark.parametrize(
        "name, poster_url",
        [
            ("ターミネーターシリーズ", "/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg"),
            ("ハリー・ポッターシリーズ", "/eVPs2Y0LyvTLZn6AP5Z6O2rtiGB.jpg"),
            ("ワイルド・スピードシリーズ", "/yvr1Ziehgps1VJyug8nnezTJRJW.jpg"),
        ],
    )
    def test_constructor_should_create_instance(self, name, poster_url):
        film_poster_object = FilmPosterObject(poster_url=poster_url)
        film_series_object = FilmSeriesObject(
            name=name,
            poster=film_poster_object,
        )

        assert film_series_object.name == name
        assert film_poster_object == FilmPosterObject(poster_url=poster_url)

    @pytest.mark.parametrize(
        "name",
        [
            (False),
            (1024),
            (3.14),
        ],
    )
    def test_constructor_name_should_throw_value_error_when_params_are_invalid(self, name):
        poster_url = "/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg"
        with pytest.raises(ValueError):
            FilmSeriesObject(
                name=name,
                poster=FilmPosterObject(poster_url=poster_url),
            )
