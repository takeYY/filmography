# 標準ライブラリ
import os
from logging import getLogger

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject
from notion_client import Client
from notion_client.typing import SyncAsync

# 独自ライブラリ
from src.domain.film_record.film.series.film_series_repository import IFilmSeriesRepository

# 定数
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
FILM_SERIES_DB_ID = os.environ["FILM_SERIES_DB_ID"]

logger = getLogger(__name__)


class ImplFilmSeriesRepository(IFilmSeriesRepository):
    def __init__(self):
        # Notionの設定
        self.notion = Client(auth=NOTION_TOKEN)
        self.notion_film_series_id = FILM_SERIES_DB_ID

    def get_series(self) -> SyncAsync[JSONObject]:
        """Notionから映画ジャンルデータを取得する"""
        logger.info("Notionから映画シリーズを取得する処理: 開始")
        query: dict[str, str] = dict(database_id=self.notion_film_series_id)
        logger.info("Notionから映画シリーズを取得する処理: 終了")

        return self.notion.databases.query(**query)
