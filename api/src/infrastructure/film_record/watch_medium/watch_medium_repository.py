# 標準ライブラリ
import os
from logging import getLogger

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject
from notion_client import Client
from notion_client.typing import SyncAsync

# 独自ライブラリ
from src.domain.film_record.watch_medium import IWatchMediumRepository

# 定数
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
WATCH_MEDIUM_DB_ID = os.environ["WATCH_MEDIUM_DB_ID"]

logger = getLogger(__name__)


class ImplWatchMediumRepository(IWatchMediumRepository):
    def __init__(self):
        # Notionの設定
        self.notion = Client(auth=NOTION_TOKEN)
        self.notion_watch_medium_id = WATCH_MEDIUM_DB_ID

    def get_watch_media(self) -> SyncAsync[JSONObject]:
        logger.info("Notionから視聴媒体を取得する処理: 開始")
        query: dict[str, str] = dict(database_id=self.notion_watch_medium_id)
        logger.info("Notionから視聴媒体を取得する処理: 終了")

        return self.notion.databases.query(**query)
