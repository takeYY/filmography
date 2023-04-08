# 標準ライブラリ
from enum import Enum


class FilmGenreEnum(Enum):
    """映画ジャンルを扱う Enum"""

    ACTION = "アクション"
    ADVENTURE = "アドベンチャー"
    ANIMATION = "アニメーション"
    COMEDY = "コメディ"
    CRIME = "クライム"
    DOCUMENTARY = "ドキュメンタリー"
    DRAMA = "ドラマ"
    FAMILY = "ファミリー"
    FANTASY = "ファンタジー"
    HISTORY = "ヒストリー"
    HORROR = "ホラー"
    MUSIC = "音楽"
    MYSTERY = "ミステリー"
    ROMANCE = "ロマンス"
    SF = "SF"
    TV = "TV"
    THRILLER = "スリラー"
    WAR = "戦争"
    WESTERN = "西部劇"
