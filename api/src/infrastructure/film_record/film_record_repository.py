import os

from notion_client import Client
from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_id_object import FilmRecordIdObject
from src.domain.film_record.film_record_repository import IFilmRecordRepository


class ImplFilmRecordRepository(IFilmRecordRepository):
    def __init__(self) -> None:
        pass

    def find_by_id(self, id: FilmRecordIdObject) -> FilmRecordEntity | None:
        return None

    def get_film_records(self):
        notion_token = os.environ["NOTION_TOKEN"]
        notion = Client(auth=notion_token)
        div_film_record_id: str = os.environ["FILM_RECORD_DB_ID"]

        query: dict[str, str] = dict(database_id=div_film_record_id)
        return notion.databases.query(**query)

    def create(self, film_record: FilmRecordEntity) -> FilmRecordEntity | None:
        return None

    def update(self, film_record_id: FilmRecordIdObject, film_record: FilmRecordEntity) -> FilmRecordEntity | None:
        return None
