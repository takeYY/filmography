from abc import ABC, abstractmethod

from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_id_object import FilmRecordIdObject


class IFilmRecordRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: FilmRecordIdObject) -> FilmRecordEntity | None:
        raise NotImplementedError
