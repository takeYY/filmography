from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionTextData:
    content: str
    link: None


@dataclass
class NotionAnnotationData:
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: str


@dataclass
class NotionTitleDetailData:
    type: Literal["text"]
    text: NotionTextData
    annotations: NotionAnnotationData
    plain_text: str
    href: None


@dataclass
class NotionTitleData:
    id: str
    type: Literal["NotionTitleData"]
    title: list[NotionTitleDetailData]
