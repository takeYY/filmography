from dataclasses import dataclass

from src.data_model.notion.database.notion_database_data import NotionDatabaseData
from src.data_model.notion.number.notion_number_data import NotionNumberData
from src.data_model.notion.relation.notion_relation_data import NotionRelationData
from src.data_model.notion.title.notion_title_data import NotionTitleData
from src.data_model.notion.user.notion_user_data import NotionUserData


@dataclass
class NotionWatchMediumPropertyData:
    Medium_ID: NotionNumberData
    Medium: NotionTitleData
    Watch_History: NotionRelationData


@dataclass
class NotionWatchMediumResultData:
    object: str
    id: str
    created_time: str
    last_edited_time: str
    created_by: NotionUserData
    last_edited_by: NotionUserData
    cover: None
    icon: None
    parent: NotionDatabaseData
    archived: bool
    properties: NotionWatchMediumPropertyData
    url: str
