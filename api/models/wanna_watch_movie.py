from .movie import Movie
from .notion.notion_multi_select import NotionMultiSelect
from .notion.notion_text import NotionText


class WannaWatchMovie(Movie):
    """観たい映画を扱うクラス

    Attributes
    ----------
    notion_title: NotionTitle
        タイトル
    notion_cover: NotionFilesMedia
        映画ポスターURL
    notion_genres: NotionMultiSelect
        ジャンル
    notion_note: NotionText
        備考や感想
    notion_tmdb_id: NotionNumber
        TMDbのID
    """

    def __init__(self, props: dict):
        super().__init__(props)
        self.notion_genres = NotionMultiSelect(props.get("genres"))
        self.notion_note = NotionText(props.get("note"))
