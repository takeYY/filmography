from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class FilmPosterObject:
    """映画ポスターを扱う値オブジェクト

    Attributes
    ----------
    poster_url: str
        ポスター URL
    """

    poster_url: str

    def __init__(self, poster_url: str):
        if not poster_url:
            raise ValueError("poster_urlがありません.")

        object.__setattr__(self, "poster_url", poster_url)
