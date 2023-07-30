from dataclasses import dataclass
from typing import Literal

from dataclass_wizard import JSONWizard
from src.data_model.notion.watch_history.notion_watch_history_result_data import NotionWatchHistoryResultData


@dataclass
class NotionWatchHistoryData(JSONWizard):
    object: str
    results: list[NotionWatchHistoryResultData]
    next_cursor: str | None
    has_more: bool
    type: Literal["page_or_database"]
    page_or_database: dict
