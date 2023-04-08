# 標準ライブラリ
import os
from logging import getLogger

# 外部ライブラリ
from notion_client import Client

# 独自ライブラリ
from src.domain.film_record.watch_medium import IWatchMediumRepository

logger = getLogger(__name__)


class ImplInmemoryWatchMediumRepository(IWatchMediumRepository):
    def __init__(self) -> None:
        pass

    def get_watch_media(self):
        logger.info("【inmemory】Notionから視聴媒体を取得する処理: 開始")
        # Notionの設定
        notion_token = os.environ["NOTION_TOKEN"]
        self.notion = Client(auth=notion_token)
        self.notion_dev_watch_medium_id: str = os.environ["DEV_WATCH_MEDIUM_DB_ID"]

        query: dict[str, str] = dict(database_id=self.notion_dev_watch_medium_id)
        logger.info("【inmemory】Notionから視聴媒体を取得する処理:: 終了")
        return self.notion.databases.query(**query)
