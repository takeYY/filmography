from .movie import Movie
from .notion.notion_date import NotionDate
from .notion.notion_number import NotionNumber


class AllMovie(Movie):
    """映画情報の作成日を扱うクラス

    Attributes
    ----------
    notion_title: NotionTitle
        タイトル
    notion_cover: NotionFilesMedia
        映画ポスターURL
    notion_id: NotionNumber
        NotionのID
    notion_tmdb_id: NotionNumber
        TMDbのID
    notion_created_at: NotionDate
        作成日
    """

    def __init__(self, props: dict):
        super().__init__(props)
        self.notion_id = NotionNumber(props.get("notion_id"))
        self.notion_created_at = NotionDate(props.get("created_at"))
