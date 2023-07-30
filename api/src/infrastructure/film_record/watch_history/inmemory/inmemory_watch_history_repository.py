# 標準ライブラリ
import os
from logging import getLogger

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject
from notion_client import Client
from notion_client.typing import SyncAsync

# 独自ライブラリ
from src.domain.film_record import IFilmWatchHistoryRepository

# 定数
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DEV_WATCH_HISTORY_DB_ID = os.environ["DEV_WATCH_HISTORY_DB_ID"]

logger = getLogger(__name__)


class ImplInmemoryFilmWatchHistoryRepository(IFilmWatchHistoryRepository):
    def __init__(self) -> None:
        logger.debug("【inmemory】FilmWatchHistoryRepo: init")
        # Notionの設定
        self.notion_dev_film_watch_history_id = DEV_WATCH_HISTORY_DB_ID

    def get_film_watch_history(self) -> SyncAsync[JSONObject]:
        logger.info("【inmemory】Notionから映画視聴履歴を取得する処理: 開始")
        query: dict[str, str] = dict(database_id=self.notion_dev_film_watch_history_id)
        logger.info("【inmemory】Notionから映画視聴履歴を取得する処理: 終了")

        notion = Client(auth=NOTION_TOKEN)  # NOTE: initで定義してはいけない
        return notion.databases.query(**query)
