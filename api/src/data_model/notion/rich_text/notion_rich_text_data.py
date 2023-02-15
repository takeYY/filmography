from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionRichTextData:
    id: str
    type: Literal["NotionRichTextData"]
    rich_text: list
