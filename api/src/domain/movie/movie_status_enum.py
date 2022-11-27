from enum import Enum


class MovieStatus(Enum):
    """鑑賞状況を扱う Enum"""

    WATCHED = "Watched"
    WANNA_WATCH = "Wanna Watch"
