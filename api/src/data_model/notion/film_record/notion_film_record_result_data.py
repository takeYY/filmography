from dataclasses import dataclass

from src.data_model.notion.database.notion_database_data import NotionDatabaseData
from src.data_model.notion.date.notion_date_data import NotionDateData
from src.data_model.notion.file.notion_file_data import NotionFileData
from src.data_model.notion.number.notion_number_data import NotionNumberData
from src.data_model.notion.relation.notion_relation_data import NotionRelationData
from src.data_model.notion.rich_text.notion_rich_text_data import NotionRichTextData
from src.data_model.notion.select.notion_select_data import NotionSelectData
from src.data_model.notion.title.notion_title_data import NotionTitleData
from src.data_model.notion.user.notion_user_data import NotionUserData


@dataclass
class NotionResultData:
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
    properties: dict[
        str,
        NotionRelationData
        | NotionDateData
        | NotionSelectData
        | NotionNumberData
        | NotionRichTextData
        | NotionTitleData
        | NotionFileData,
    ]
    url: str
