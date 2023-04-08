# 標準ライブラリ
from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class FilmAppreciationIdObject:
    """映画鑑賞 ID を扱う値オブジェクト

    Attributes
    ----------
    value: str
        映画鑑賞 ID
    """

    value: str

    def __init__(self, value: str):
        if not value:
            raise ValueError("映画鑑賞IDがありません.")
        if type(value) is not str:
            raise ValueError("映画鑑賞IDがstr型ではありません.")

        object.__setattr__(self, "value", value)
