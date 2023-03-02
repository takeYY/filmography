from dataclasses import dataclass
from typing import Literal

from dataclass_wizard import JSONWizard
from src.data_model.notion.genre.notion_genre_result_data import NotionGenreResultData


@dataclass
class NotionGenreData(JSONWizard):
    object: str
    results: list[NotionGenreResultData]
    next_cursor: str | None
    has_more: bool
    type: Literal["page"]
    page: dict

    def get_tmdb_genre_id(self, relation_id: str) -> int:
        for result in self.results:
            if result.id == relation_id:
                return int(result.properties.TMDb_Genre_ID.number)

        raise ValueError(f"{relation_id}は存在しません。")
