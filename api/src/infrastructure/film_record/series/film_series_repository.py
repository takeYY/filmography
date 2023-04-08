# 標準ライブラリ
import os

# 外部ライブラリ
from notion_client import Client

# 独自ライブラリ
from src.domain.film_record.film.series.film_series_repository import IFilmSeriesRepository


class ImplFilmSeriesRepository(IFilmSeriesRepository):
    def __init__(self):
        pass

    def get_series(self):
        """Notionから映画ジャンルデータを取得する"""

        notion_token = os.environ["NOTION_TOKEN"]
        notion = Client(auth=notion_token)
        notion_film_series_id: str = os.environ["FILM_SERIES_DB_ID"]

        query: dict[str, str] = dict(database_id=notion_film_series_id)
        return notion.databases.query(**query)
