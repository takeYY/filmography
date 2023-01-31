from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class FilmAppreciationIdObject:
    """映画鑑賞 ID を扱う値オブジェクト

    Attributes
    ----------
    value: int
        映画鑑賞 ID
    """

    value: int

    def __init__(self, value: int):
        if not value:
            raise ValueError("映画鑑賞IDがありません.")
        if type(value) is not int:
            raise ValueError("映画鑑賞IDがint型ではありません.")

        object.__setattr__(self, "value", value)
