from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionAnnotationDetailData:
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: str


@dataclass
class NotionTextDetailData:
    content: str
    link: None


@dataclass
class NotionRichTextDetailData:
    type: Literal["text"]
    text: NotionTextDetailData
    annotations: NotionAnnotationDetailData
    plain_text: str
    href: None


@dataclass
class NotionRichTextData:
    id: str
    type: Literal["rich_text"]
    rich_text: list[NotionRichTextDetailData]

    def get_rich_text(self) -> str:
        return self.rich_text[0].plain_text if self.rich_text else ""
