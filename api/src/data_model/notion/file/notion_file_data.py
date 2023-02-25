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
    type: Literal["files"]
    files: list[NotionFileDetailData]

    def get_file_external_url(self):
        return self.files[0].external.url if self.files else ""
