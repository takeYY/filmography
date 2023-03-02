from dataclasses import dataclass
from typing import Literal

from src.data_model.notion.database.notion_database_data import NotionDatabaseData
from src.data_model.notion.number.notion_number_data import NotionNumberData
from src.data_model.notion.relation.notion_relation_data import NotionRelationData
from src.data_model.notion.title.notion_title_data import NotionTitleData
from src.data_model.notion.user.notion_user_data import NotionUserData


@dataclass
class NotionGenrePropertyData:
    Film_Record: NotionRelationData
    TMDb_Genre_ID: NotionNumberData
    Name: NotionTitleData


@dataclass
class NotionIconData:
    """Notion のアイコンを扱うデータクラス

    Attributes
    ----------
    type: Literal["emoji"]
        emoji 一択 (?)
    emoji: str
        絵文字, ex) ✨
    """

    # TODO: 専用のディレクトリに入れる
    type: Literal["emoji"]
    emoji: str


@dataclass
class NotionGenreResultData:
    object: str
    id: str
    created_time: str
    last_edited_time: str
    created_by: NotionUserData
    last_edited_by: NotionUserData
    cover: None
    icon: NotionIconData | None
    parent: NotionDatabaseData
    archived: bool
    properties: NotionGenrePropertyData
    url: str
