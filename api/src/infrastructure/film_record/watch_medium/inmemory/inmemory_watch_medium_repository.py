# 標準ライブラリ
import os
from logging import getLogger

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject
from notion_client import Client
from notion_client.typing import SyncAsync

# 独自ライブラリ
from src.domain.film_record import IWatchMediumRepository

# 定数
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DEV_WATCH_MEDIUM_DB_ID = os.environ["DEV_WATCH_MEDIUM_DB_ID"]

logger = getLogger(__name__)


class ImplInmemoryWatchMediumRepository(IWatchMediumRepository):
    def __init__(self) -> None:
        logger.debug("【inmemory】WatchMediumRepo: init")
        # Notionの設定
        self.notion_dev_watch_medium_id = DEV_WATCH_MEDIUM_DB_ID

    def get_watch_media(self) -> SyncAsync[JSONObject]:
        logger.info("【inmemory】Notionから視聴媒体を取得する処理: 開始")
        query: dict[str, str] = dict(database_id=self.notion_dev_watch_medium_id)
        logger.info("【inmemory】Notionから視聴媒体を取得する処理:: 終了")

        notion = Client(auth=NOTION_TOKEN)  # NOTE: initで定義してはいけない
        return notion.databases.query(**query)
