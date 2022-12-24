from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class PosterObject:
    """ポスター画像を扱う値オブジェクト

    Attributes
    ---------
    poster_path: str
        ポスター画像のパス
    """

    poster_path: str

    def __init__(self, poster_path: str):
        if not poster_path:
            raise ValueError("poster path is empty.")

        object.__setattr__(self, "poster_path", poster_path)

    def get_600x900(self):
        return f"https://image.tmdb.org/t/p/w600_and_h900_bestv2{self.poster_path}"
