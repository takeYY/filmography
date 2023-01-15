from dataclasses import dataclass

from src.domain.film_record.film.poster.film_poster_object import FilmPosterObject


@dataclass(init=False, eq=True, frozen=True)
class FilmSeriesObject:
    """映画シリーズを扱う値オブジェクト

    Attributes
    ----------
    name: str
        シリーズ名
    poster: FilmPosterObject
        映画ポスターを扱う値オブジェクト
    """

    name: str
    poster: FilmPosterObject

    def __init__(self, name: str, poster: FilmPosterObject):
        if not name:
            raise ValueError("nameがありません.")
        if not poster:
            raise ValueError("posterがありません.")

        object.__setattr__(self, "name", name)
        object.__setattr__(self, "poster", poster)
