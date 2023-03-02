from dataclasses import dataclass

from src.data_model.notion.database.notion_database_data import NotionDatabaseData
from src.data_model.notion.date.notion_date_data import NotionDateData
from src.data_model.notion.relation.notion_relation_data import NotionRelationData
from src.data_model.notion.title.notion_title_data import NotionTitleData
from src.data_model.notion.user.notion_user_data import NotionUserData


@dataclass
class NotionWatchHistoryPropertyData:
    Film_Record: NotionRelationData
    Watched_On: NotionDateData
    Watching_Medium: NotionRelationData
    Title: NotionTitleData


@dataclass
class NotionWatchHistoryResultData:
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
    properties: NotionWatchHistoryPropertyData
    url: str
