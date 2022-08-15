from .movie import Movie
from .notion.notion_date import NotionDate
from .notion.notion_multi_select import NotionMultiSelect
from .notion.notion_number import NotionNumber
from .notion.notion_select import NotionSelect
from .notion.notion_text import NotionText


class WatchedMovie(Movie):
    """鑑賞済みの映画を扱うクラス

    Attributes
    ----------
    notion_title: NotionTitle
        タイトル
    notion_cover: NotionFilesMedia
        映画ポスターURL
    notion_rating: NotionSelect
        評価
    notion_viewed: NotionNumber
        鑑賞回数
    notion_genres: NotionMultiSelect
        ジャンル
    notion_first_watched_at: NotionDate
        初鑑賞日
    notion_last_watched_at: NotionDate
        最後の鑑賞日
    notion_note: NotionText
        備考や感想
    notion_tmdb_id: NotionNumber
        TMDbのID
    """

    def __init__(self, props: dict):
        super().__init__(props)
        self.notion_rating = NotionSelect(props.get("rating"))
        self.notion_viewed = NotionNumber(props.get("viewed"))
        self.notion_genres = NotionMultiSelect(props.get("genres"))
        self.notion_first_watched_at = NotionDate(
            props.get("first_watched_at"),
        )
        self.notion_last_watched_at = NotionDate(
            props.get("last_watched_at"),
        )
        self.notion_note = NotionText(props.get("note"))
