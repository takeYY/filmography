from dataclasses import dataclass
from datetime import date
from typing import Literal


@dataclass
class NotionDateDetailData:
    start: str
    end: None
    time_zone: None


@dataclass
class NotionDateData:
    id: str
    type: Literal["date"]
    date: NotionDateDetailData

    def get_date(self):
        year, month, day = self.date.start.split("-")

        return date(int(year), int(month), int(day))
