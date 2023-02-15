from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionExternalData:
    url: str


@dataclass
class NotionFileDetailData:
    name: str
    type: Literal["external"]
    external: NotionExternalData


@dataclass
class NotionFileData:
    id: str
    type: Literal["NotionFileData"]
    files: list[NotionFileDetailData]
