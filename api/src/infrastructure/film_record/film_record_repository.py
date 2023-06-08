# 標準ライブラリ
import os

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject
from notion_client import Client
from notion_client.typing import SyncAsync

# 独自ライブラリ
from src.domain.film_record import FilmRecordEntity, FilmRecordIdObject, IFilmRecordRepository


class ImplFilmRecordRepository(IFilmRecordRepository):
    def __init__(self) -> None:
        pass

    def find_by_id(self, id: FilmRecordIdObject) -> FilmRecordEntity | None:
        return None

    def get_film_records(self) -> SyncAsync[JSONObject]:
        notion_token = os.environ["NOTION_TOKEN"]
        notion = Client(auth=notion_token)
        div_film_record_id: str = os.environ["FILM_RECORD_DB_ID"]

        query: dict[str, str] = dict(database_id=div_film_record_id)
        return notion.databases.query(**query)

    def create(self, film_record: FilmRecordEntity) -> FilmRecordEntity | None:
        return None

    def update(self, film_record_id: FilmRecordIdObject, film_record: FilmRecordEntity) -> FilmRecordEntity | None:
        return None
