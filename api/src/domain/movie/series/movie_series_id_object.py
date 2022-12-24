from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class MovieSeriesIdObject:
    """映画シリーズ ID を扱う値オブジェクト

    Attributes
    ---------
    value: str
        シリーズ ID
    """

    value: int

    def __init__(self, value: int):
        if not value:
            raise ValueError("movie series ID is empty.")

        object.__setattr__(self, "value", value)
