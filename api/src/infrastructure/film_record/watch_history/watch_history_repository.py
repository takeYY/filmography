# 標準ライブラリ
import os

# 外部ライブラリ
from notion_client import Client

# 独自ライブラリ
from src.domain.film_record.watch_history import IFilmWatchHistoryRepository


class ImplFilmWatchHistoryRepository(IFilmWatchHistoryRepository):
    def __init__(self):
        pass

    def get_film_watch_history(self):
        notion_token = os.environ["NOTION_TOKEN"]
        notion = Client(auth=notion_token)
        notion_film_genre_id: str = os.environ["WATCH_HISTORY_DB_ID"]

        query: dict[str, str] = dict(database_id=notion_film_genre_id)
        return notion.databases.query(**query)
