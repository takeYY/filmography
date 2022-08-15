from .notion.notion_files_media import NotionFilesMedia
from .notion.notion_number import NotionNumber
from .notion.notion_title import NotionTitle


class Movie:
    """映画データを扱う基底クラス

    Attributes
    ----------
    notion_title: NotionTitle
        映画タイトルを扱うタイトルクラス
    notion_cover_url: NotionFilesMedia
        映画ポスターを扱うファイルメディアクラス
    notion_tmdb_id: NotionNumber
        TMDbのIDを扱う数値クラス
    """

    def __init__(self, props: dict):
        self.notion_title = NotionTitle(props.get("title"))
        self.notion_cover = NotionFilesMedia(props.get("cover"))
        self.notion_tmdb_id = NotionNumber(props.get("tmdb_id"))
