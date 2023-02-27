from dataclasses import dataclass
from typing import Literal

from dataclass_wizard import JSONWizard
from src.data_model.notion.series.notion_series_result_data import NotionSeriesResultData


@dataclass
class NotionSeriesData(JSONWizard):
    object: str
    results: list[NotionSeriesResultData]
    next_cursor: str | None
    has_more: bool
    type: Literal["page"]
    page: dict

    def get_series(self, relation_id: str) -> NotionSeriesResultData:
        for result in self.results:
            if result.id == relation_id:
                return result

        raise ValueError(f"{relation_id}は存在しません。")
