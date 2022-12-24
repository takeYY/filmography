from dataclasses import dataclass

from src.domain.genre.genre import TmdbGenre


@dataclass(init=False, eq=True, frozen=True)
class GenreIdObject:
    """ジャンル ID を扱う値オブジェクト

    Attributes
    ----------
    value: int
        ジャンル ID
    """

    value: int

    def __init__(self, value: int):
        if not value:
            raise ValueError("genre ID is empty.")

        object.__setattr__(self, "value", value)

    def genre_name(self):
        return TmdbGenre.genre.get(str(self.value))
