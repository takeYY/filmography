# 標準ライブラリ
import os

# 独自ライブラリ
from notion_client import Client
from src.domain.film_record.film.genre import IFilmGenreRepository


class ImplFilmGenreRepository(IFilmGenreRepository):
    def __init__(self):
        pass

    def get_genres(self):
        """Notionから映画ジャンルデータを取得する"""

        notion_token = os.environ["NOTION_TOKEN"]
        notion = Client(auth=notion_token)
        notion_film_genre_id: str = os.environ["FILM_GENRE_DB_ID"]

        query: dict[str, str] = dict(database_id=notion_film_genre_id)
        return notion.databases.query(**query)
