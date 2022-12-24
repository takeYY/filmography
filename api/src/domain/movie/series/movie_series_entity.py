from src.domain.movie.series.movie_series_id_object import MovieSeriesIdObject
from src.domain.poster.poster_object import PosterObject


class MovieSeriesEntity:
    """映画シリーズを扱うエンティティ

    Attributes
    ---------
    id: MovieSeriesIdObject
        映画シリーズ ID を扱う値オブジェクト
    name: str
        シリーズ名
    poster: PosterObject
        ポスター画像を扱う値オブジェクト
    """

    def __init__(
        self,
        id: MovieSeriesIdObject,
        name: str,
        poster: PosterObject,
    ):
        self.id: MovieSeriesIdObject = id
        self.name: str = name
        self.poster: PosterObject = poster

    def __eq__(self, o: object) -> bool:
        if isinstance(o, MovieSeriesEntity):
            return self.id == o.id

        return False
