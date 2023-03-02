import os
from logging import getLogger

from notion_client import Client
from src.domain.film_record.film.genre.film_genre_repository import IFilmGenreRepository

logger = getLogger(__name__)


class ImplInmemoryFilmGenreRepository(IFilmGenreRepository):
    def __init__(self) -> None:
        pass

    def get_genres(self):
        logger.info("【inmemory】Notionから映画ジャンルを取得する処理: 開始")
        # Notionの設定
        notion_token = os.environ["NOTION_TOKEN"]
        self.notion = Client(auth=notion_token)
        self.notion_div_film_genre_id: str = os.environ["DEV_FILM_GENRE_DB_ID"]

        query: dict[str, str] = dict(database_id=self.notion_div_film_genre_id)
        logger.info("【inmemory】Notionから映画ジャンルを取得する処理: 終了")
        return self.notion.databases.query(**query)
