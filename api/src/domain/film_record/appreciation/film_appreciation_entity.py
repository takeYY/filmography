from datetime import date

from src.domain.film_record.appreciation.film_appreciation_id_object import FilmAppreciationIdObject


class FilmAppreciationEntity:
    """映画鑑賞を扱うエンティティ

    Attributes
    ----------
    film_appreciation_id: FilmAppreciationIdObject
        映画鑑賞 ID を扱う値オブジェクト
    medium: str
        鑑賞媒体
    appreciation_date: date
        鑑賞日
    """

    def __init__(
        self,
        film_appreciation_id: FilmAppreciationIdObject,
        medium: str,
        appreciation_date: date,
    ):
        self.film_appreciation_id: FilmAppreciationIdObject = film_appreciation_id
        self.medium: str = medium
        self.appreciation_date: date = appreciation_date

    def __eq__(self, o: object) -> bool:
        if isinstance(o, FilmAppreciationEntity):
            return self.film_appreciation_id == o.film_appreciation_id

        return False
