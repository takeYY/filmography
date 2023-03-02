from datetime import date

from src.domain.film_record.appreciation.film_appreciation_id_object import FilmAppreciationIdObject
from src.domain.film_record.watch_medium.watch_medium_enum import WatchMediumEnum


class FilmAppreciationEntity:
    """映画鑑賞を扱うエンティティ

    Attributes
    ----------
    film_appreciation_id: FilmAppreciationIdObject
        映画鑑賞 ID を扱う値オブジェクト
    medium: WatchMediumEnum
        視聴媒体
    appreciation_date: date
        鑑賞日
    """

    def __init__(
        self,
        film_appreciation_id: FilmAppreciationIdObject,
        medium: WatchMediumEnum,
        appreciation_date: date,
    ):
        self.film_appreciation_id: FilmAppreciationIdObject = film_appreciation_id
        self.medium: WatchMediumEnum = medium
        self.appreciation_date: date = appreciation_date

    def __eq__(self, o: object) -> bool:
        if isinstance(o, FilmAppreciationEntity):
            return self.film_appreciation_id == o.film_appreciation_id

        return False
