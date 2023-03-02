import os
from logging import getLogger

from notion_client import Client
from src.domain.film_record.film.series.film_series_repository import IFilmSeriesRepository

logger = getLogger(__name__)


class ImplInmemoryFilmSeriesRepository(IFilmSeriesRepository):
    def __init__(self) -> None:
        pass

    def get_series(self):
        logger.info("【inmemory】Notionから映画シリーズを取得する処理: 開始")
        # Notionの設定
        notion_token = os.environ["NOTION_TOKEN"]
        self.notion = Client(auth=notion_token)
        self.notion_dev_film_series_id: str = os.environ["DEV_FILM_SERIES_DB_ID"]

        query: dict[str, str] = dict(database_id=self.notion_dev_film_series_id)
        logger.info("【inmemory】Notionから映画シリーズを取得する処理: 終了")
        return self.notion.databases.query(**query)
