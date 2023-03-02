from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionSelectDetailData:
    id: str
    name: str
    color: str


@dataclass
class NotionSelectData:
    id: str
    type: Literal["select"]
    select: NotionSelectDetailData
