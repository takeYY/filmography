from dataclasses import dataclass
from typing import Literal

from src.data_model.notion.database.notion_database_data import NotionDatabaseData
from src.data_model.notion.file.notion_file_data import NotionExternalData, NotionFileData
from src.data_model.notion.relation.notion_relation_data import NotionRelationData
from src.data_model.notion.title.notion_title_data import NotionTitleData
from src.data_model.notion.user.notion_user_data import NotionUserData


@dataclass
class NotionSeriesPropertyData:
    Poster: NotionFileData
    Film_Record: NotionRelationData
    Name: NotionTitleData


@dataclass
class NotionIconData:
    """Notion のアイコンを扱うデータクラス

    Attributes
    ----------
    type: Literal["external"]
        external 一択 (?)
    external: str
        外部ファイル
    """

    # TODO: 専用のディレクトリに入れる
    type: Literal["external"]
    external: NotionExternalData


@dataclass
class NotionSeriesResultData:
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
    properties: NotionSeriesPropertyData
    url: str
