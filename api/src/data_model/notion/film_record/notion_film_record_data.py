from dataclasses import dataclass
from typing import Literal

from dataclass_wizard import JSONWizard
from src.data_model.notion.film_record.notion_film_record_result_data import NotionResultData


@dataclass
class NotionFilmRecordData(JSONWizard):
    class __(JSONWizard.Meta):
        tag_key = "type"
        auto_assign_tags = True

    object: str
    results: list[NotionResultData]
    next_cursor: str | None
    has_more: bool
    type: Literal["page"]
    page: dict
