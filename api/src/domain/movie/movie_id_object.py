from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class MovieIdObject:
    """映画 ID を扱う値オブジェクト

    Attributes
    ----------
    value: int
        映画 ID
    """

    value: int

    def __init__(self, value: int):
        if not value:
            raise ValueError("movie ID is empty.")

        object.__setattr__(self, "value", value)
