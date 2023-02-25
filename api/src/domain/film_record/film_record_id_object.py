from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class FilmRecordIdObject:
    """映画記録 ID を扱う値オブジェクト

    Attributes
    ----------
    value: str
        映画記録 ID
    """

    value: str

    def __init__(self, value: str):
        if not value:
            raise ValueError("film record ID がありません.")

        object.__setattr__(self, "value", value)
