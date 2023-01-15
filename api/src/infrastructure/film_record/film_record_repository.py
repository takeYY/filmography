from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_id_object import FilmRecordIdObject
from src.domain.film_record.film_record_repository import IFilmRecordRepository


class ImplFilmRecordRepository(IFilmRecordRepository):
    def __init__(self) -> None:
        pass

    def find_by_id(self, id: FilmRecordIdObject) -> FilmRecordEntity | None:
        return None
