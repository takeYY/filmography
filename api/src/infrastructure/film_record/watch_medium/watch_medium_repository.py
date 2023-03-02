import os

from notion_client import Client
from src.domain.film_record.watch_medium.watch_medium_repository import IWatchMediumRepository


class ImplWatchMediumRepository(IWatchMediumRepository):
    def __init__(self):
        pass

    def get_watch_media(self):
        notion_token = os.environ["NOTION_TOKEN"]
        notion = Client(auth=notion_token)
        notion_watch_medium_id: str = os.environ["WATCH_MEDIUM_DB_ID"]

        query: dict[str, str] = dict(database_id=notion_watch_medium_id)
        return notion.databases.query(**query)
