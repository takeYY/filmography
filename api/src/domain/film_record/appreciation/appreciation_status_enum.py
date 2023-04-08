# 標準ライブラリ
from enum import Enum


class AppreciationStatusEnum(Enum):
    """鑑賞状況を扱う Enum"""

    WATCHED = "鑑賞済み"
    NOT_WATCHED = "未鑑賞"
