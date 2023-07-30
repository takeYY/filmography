from dataclasses import dataclass
from typing import Literal

from dataclass_wizard import JSONWizard
from src.data_model.notion.film_record.notion_film_record_result_data import NotionResultData


@dataclass
class NotionFilmRecordData(JSONWizard):
    object: str
    results: list[NotionResultData]
    next_cursor: str | None
    has_more: bool
    type: Literal["page_or_database"]
    page_or_database: dict
