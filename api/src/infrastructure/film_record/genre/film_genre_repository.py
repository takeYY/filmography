# 標準ライブラリ
import os
from logging import getLogger

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject
from notion_client import Client
from notion_client.typing import SyncAsync

# 独自ライブラリ
from src.domain.film_record.film.genre import IFilmGenreRepository

# 定数
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
FILM_GENRE_DB_ID = os.environ["FILM_GENRE_DB_ID"]

logger = getLogger(__name__)


class ImplFilmGenreRepository(IFilmGenreRepository):
    def __init__(self):
        # Notionの設定
        self.notion = Client(auth=NOTION_TOKEN)
        self.notion_film_genre_id = FILM_GENRE_DB_ID

    def get_genres(self) -> SyncAsync[JSONObject]:
        """Notionから映画ジャンルデータを取得する"""
        logger.info("Notionから映画ジャンルを取得する処理: 開始")
        query: dict[str, str] = dict(database_id=self.notion_film_genre_id)
        logger.info("Notionから映画ジャンルを取得する処理: 終了")

        return self.notion.databases.query(**query)
