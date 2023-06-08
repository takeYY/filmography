# 標準ライブラリ
import os
from logging import getLogger

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject
from notion_client import Client
from notion_client.typing import SyncAsync

# 独自ライブラリ
from src.domain.film_record.watch_history import IFilmWatchHistoryRepository

# 定数
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
WATCH_HISTORY_DB_ID = os.environ["WATCH_HISTORY_DB_ID"]

logger = getLogger(__name__)


class ImplFilmWatchHistoryRepository(IFilmWatchHistoryRepository):
    def __init__(self):
        # Notionの設定
        self.notion = Client(auth=NOTION_TOKEN)
        self.notion_film_watch_history_id = WATCH_HISTORY_DB_ID

    def get_film_watch_history(self) -> SyncAsync[JSONObject]:
        logger.info("Notionから映画視聴履歴を取得する処理: 開始")
        query: dict[str, str] = dict(database_id=self.notion_film_watch_history_id)
        logger.info("Notionから映画視聴履歴を取得する処理: 終了")

        return self.notion.databases.query(**query)
