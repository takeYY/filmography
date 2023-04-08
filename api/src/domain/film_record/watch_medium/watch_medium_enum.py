# 標準ライブラリ
from enum import Enum


class WatchMediumEnum(Enum):
    """視聴媒体を扱う Enum"""

    AMAZON_PRIME_VIDEO = "Amazon Prime Video"
    NETFLIX = "Netflix"
    DISNEY = "Disney+"
    U_NEXT = "U-NEXT"
    THEATER = "Theater"
    D_ANIME = "dアニメストア"
