import pytest
from src.domain.film_record.film.poster.film_poster_object import FilmPosterObject


class TestFilmPosterObject:
    @pytest.mark.parametrize(
        "poster_url",
        [
            ("/4RYFIwAhR4YHz8JjhvHpq07DSmv.jpg"),
            ("/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg"),
            ("/ghKQ6it5j7KjdYghT5EDthVNXlD.jpg"),
        ],
    )
    def test_constructor_should_create_instance(self, poster_url):
        film_poster_object = FilmPosterObject(poster_url=poster_url)

        assert film_poster_object.poster_url == poster_url

    @pytest.mark.parametrize(
        "poster_url",
        [
            ("invalid-params"),
            (False),
            (1024),
            ("1024"),
            (3.14),
            ("/4RYFIwAhR4YHz8JjhvHpq07DSmv"),
            ("4RYFIwAhR4YHz8JjhvHpq07DSmv.jpg"),
            ("/4RYFIwAhR4YHz8JjhvHpq07DSmv.png"),
            ("/4RYFIwAhR4YHz8JjhvHpq07DSmv.jpeg"),
            ("/4RYFIwAhR4YHz8JjhvHpq07DSmv.svg"),
        ],
    )
    def test_constructor_should_throw_value_error_when_params_are_invalid(self, poster_url):
        with pytest.raises(ValueError):
            FilmPosterObject(poster_url)
