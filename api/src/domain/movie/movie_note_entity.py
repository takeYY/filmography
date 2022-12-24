from src.domain.movie.movie_id_object import MovieIdObject
from src.domain.status.appreciation_status_enum import AppreciationStatus


class MovieNoteEntity:
    """映画の感想などを扱うエンティティ

    Attributes
    ----------
    movie_id: MovieIdObject
        映画 ID を扱う値オブジェクト
    appreciation_status: AppreciationStatus
        鑑賞状況を扱う Enum
    evaluation: str
        評価
    note: str
        感想
    """

    def __init__(
        self,
        movie_id: MovieIdObject,
        appreciation_status: AppreciationStatus,
        evaluation: str,
        note: str,
    ):
        self.movie_id: MovieIdObject = movie_id
        self.appreciation_status: AppreciationStatus = appreciation_status
        self.evaluation: str = evaluation
        self.note: str = note

    def __eq__(self, o: object) -> bool:
        if isinstance(o, MovieNoteEntity):
            return self.movie_id == o.movie_id

        return False
