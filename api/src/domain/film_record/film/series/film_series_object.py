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
        self.__validate_name(name)
        self.__validate_poster(poster)

        object.__setattr__(self, "name", name)
        object.__setattr__(self, "poster", poster)

    def __validate_name(self, name: str):
        if not name:
            raise ValueError("nameがありません.")
        if type(name) is not str:
            raise ValueError("nameがstr型ではありません.")

    def __validate_poster(self, poster: FilmPosterObject):
        if not poster:
            raise ValueError("posterがありません.")
        if type(poster) is not FilmPosterObject:
            raise ValueError("posterがFilmPosterObject型ではありません.")
