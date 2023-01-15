from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class TmdbIdObject:
    """TMDb ID を扱う値オブジェクト

    Attributes
    ----------
    value: int
        TMDb ID
    """

    value: int

    def __init__(self, value: int):
        if not value:
            raise ValueError("tmdb ID がありません.")

        object.__setattr__(self, "value", value)
