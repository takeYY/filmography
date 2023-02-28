import os
from logging import getLogger

from notion_client import Client
from src.domain.film_record.watch_history.watch_history_repository import IFilmWatchHistoryRepository

logger = getLogger(__name__)


class ImplInmemoryFilmWatchHistoryRepository(IFilmWatchHistoryRepository):
    def __init__(self) -> None:
        pass

    def get_film_watch_history(self):
        logger.info("【inmemory】Notionから映画視聴履歴を取得する処理: 開始")
        # Notionの設定
        notion_token = os.environ["NOTION_TOKEN"]
        self.notion = Client(auth=notion_token)
        self.notion_dev_film_watch_history_id: str = os.environ["DEV_WATCH_HISTORY_DB_ID"]

        query: dict[str, str] = dict(database_id=self.notion_dev_film_watch_history_id)
        logger.info("【inmemory】Notionから映画視聴履歴を取得する処理: 終了")
        return self.notion.databases.query(**query)
