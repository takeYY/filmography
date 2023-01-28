import re
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
        regex = r"^/[0-9a-zA-Z]{27}.jpg"
        pattern = re.compile(regex)

        if not poster_url:
            raise ValueError("poster_urlがありません.")
        if type(poster_url) is not str:
            raise ValueError("poster_urlがstr型ではありません.")
        if not pattern.match(poster_url):
            raise ValueError("poster_urlの形式が違います.")

        object.__setattr__(self, "poster_url", poster_url)

    def get_600x900(self):
        return f"https://image.tmdb.org/t/p/w600_and_h900_bestv2{self.poster_url}"
