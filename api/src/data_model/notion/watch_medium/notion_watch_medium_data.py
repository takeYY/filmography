from dataclasses import dataclass
from typing import Literal

from dataclass_wizard import JSONWizard
from src.data_model.notion.watch_medium.notion_watch_medium_result_data import NotionWatchMediumResultData


@dataclass
class NotionWatchMediumData(JSONWizard):
    object: str
    results: list[NotionWatchMediumResultData]
    next_cursor: str | None
    has_more: bool
    type: Literal["page_or_database"]
    page_or_database: dict

    def get_medium_id(self, relation_id: str) -> int:
        for result in self.results:
            if result.id == relation_id:
                return int(result.properties.Medium_ID.number)

        raise ValueError(f"{relation_id}は存在しません。")
