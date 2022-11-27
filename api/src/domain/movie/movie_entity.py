from datetime import date

from src.domain.movie.movie_status_enum import MovieStatus
from src.domain.movie.tmdb_id_object import TmdbIdObject


class MovieEntity:
    """全ての映画情報を扱うエンティティ

    Attributes
    ----------
    tmdb_id: TmdbIdObject
        TMDb ID を扱う値オブジェクト
    title: str
        映画タイトル
    cover: str
        映画カバーのURL
    status: MovieStatus
        鑑賞済みか否か TODO: もう少しわかりやすい名称にしたい
    notion_id: str
        Notion ID
    created_on: date
        作成日, default=date.today()
    """

    def __init__(
        self,
        tmdb_id: TmdbIdObject,
        title: str,
        cover: str,
        status: MovieStatus,
        notion_id: str,
        created_on: date = date.today(),
    ):
        self.tmdb_id: TmdbIdObject = tmdb_id
        self.title: str = title
        self.cover: str = cover
        self.status: MovieStatus = status
        self.notion_id: str = notion_id
        self.created_on: date = created_on

    def __eq__(self, o: object) -> bool:
        if isinstance(o, MovieEntity):
            return self.tmdb_id == o.tmdb_id

        return False
