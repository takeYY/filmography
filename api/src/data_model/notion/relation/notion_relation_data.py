from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionRelationIdData:
    id: str


@dataclass
class NotionRelationData:
    id: str
    type: Literal["relation"]
    relation: list[NotionRelationIdData]
    has_more: bool
