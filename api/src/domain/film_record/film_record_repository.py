from abc import ABC, abstractmethod

from src.domain.film_record import FilmRecordEntity, FilmRecordIdObject


class IFilmRecordRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: FilmRecordIdObject) -> FilmRecordEntity | None:
        raise NotImplementedError

    @abstractmethod
    def get_film_records(self):
        raise NotImplementedError

    @abstractmethod
    def create(self, film_record: FilmRecordEntity) -> FilmRecordEntity:
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        film_record_id: FilmRecordIdObject,
        film_record: FilmRecordEntity,
    ) -> FilmRecordEntity:
        raise NotImplementedError
