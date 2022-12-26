from src.domain.movie.series.movie_series_entity import MovieSeriesEntity
from src.domain.movie.series.movie_series_id_object import MovieSeriesIdObject
from src.domain.poster.poster_object import PosterObject


class TestMovieSeriesEntity:
    def test_constructor_should_create_instance(self):
        movie_series = MovieSeriesEntity(
            id=MovieSeriesIdObject(value=1),
            name="ターミネーターシリーズ",
            poster=PosterObject(poster_path="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg"),
        )
        assert movie_series.id == MovieSeriesIdObject(1)
        assert movie_series.name == "ターミネーターシリーズ"
        assert movie_series.poster == PosterObject("/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg")
