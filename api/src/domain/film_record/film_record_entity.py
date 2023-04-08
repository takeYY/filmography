# 標準ライブラリ
from datetime import date

# 独自ライブラリ
from src.domain.film_record.appreciation import AppreciationStatusEnum, FilmAppreciationEntity
from src.domain.film_record.film import FilmEntity, TmdbIdObject
from src.domain.film_record.film.genre import FilmGenreEnum
from src.domain.film_record.film.poster import FilmPosterObject
from src.domain.film_record.film.series import FilmSeriesObject

from .film_record_id_object import FilmRecordIdObject


class FilmRecordEntity:
    """映画記録を扱うエンティティ

    Attributes
    ----------
    film_record_id: FilmRecordIdObject
        映画記録 ID を扱う値オブジェクト
    appreciation_status: AppreciationStatusEnum
        鑑賞状況を扱う Enum
    note: str | None
        ノート
    film: FilmEntity
        映画情報を扱うエンティティ
    evaluation: int
        評価
    film_appreciations: list[FilmAppreciationEntity]
        映画鑑賞を扱うエンティティ
    """

    def __init__(
        self,
        film_record_id: FilmRecordIdObject,
        appreciation_status: AppreciationStatusEnum,
        note: str | None,
        film: FilmEntity,
        evaluation: float = 0.0,
        film_appreciations: list[FilmAppreciationEntity] = [],
    ):
        if not isinstance(appreciation_status, AppreciationStatusEnum):
            raise ValueError("appreciation_statusの型が違います.")
        if not 0 <= evaluation <= 5:
            raise ValueError("evaluationは0-5の範囲で設定してください.")
        if not film:
            raise ValueError("filmがありません.")

        # 未鑑賞の場合はデフォルトを設定
        if appreciation_status == AppreciationStatusEnum.NOT_WATCHED:
            evaluation = 0
            film_appreciations = []

        self.film_record_id: FilmRecordIdObject = film_record_id
        self.appreciation_status: AppreciationStatusEnum = appreciation_status
        self.evaluation: float = evaluation
        self.note: str | None = note
        self.film: FilmEntity = film
        self.film_appreciations: list[FilmAppreciationEntity] = film_appreciations

    def __eq__(self, o: object) -> bool:
        if isinstance(o, FilmRecordEntity):
            return self.film_record_id == o.film_record_id

        return False

    def get_film_record_id_object(self) -> FilmRecordIdObject:
        return self.film_record_id

    def get_appreciation_status(self) -> AppreciationStatusEnum:
        return self.appreciation_status

    def get_note(self) -> str | None:
        return self.note

    def get_film_tmdb_id_object(self) -> TmdbIdObject:
        return self.film.tmdb_id

    def get_film_title(self) -> str:
        return self.film.title

    def get_film_overview(self) -> str:
        return self.film.overview

    def get_film_release_date(self) -> date:
        return self.film.release_date

    def get_film_run_time(self) -> int:
        return self.film.run_time

    def get_film_series_object(self) -> FilmSeriesObject:
        return self.film.series

    def get_film_poster_object(self) -> FilmPosterObject:
        return self.film.poster

    def get_film_genres(self) -> set[FilmGenreEnum]:
        return self.film.genres

    def get_evaluation(self) -> float:
        return self.evaluation

    def get_film_appreciations(self) -> list[FilmAppreciationEntity]:
        return self.film_appreciations
