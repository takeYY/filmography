from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionDateDetailData:
    start: str
    end: None
    time_zone: None


@dataclass
class NotionDateData:
    id: str
    type: Literal["NotionDateData"]
    date: NotionDateDetailData
