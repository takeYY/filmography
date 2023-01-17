from abc import ABC, abstractmethod

from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_id_object import FilmRecordIdObject
from src.domain.film_record.film_record_repository import IFilmRecordRepository


class IFilmRecordCommandApplication(ABC):
    film_record_repository: IFilmRecordRepository

    @abstractmethod
    async def create_film_record(
        self,
        film_record: FilmRecordEntity,
    ):
        raise NotImplementedError

    @abstractmethod
    async def update_film_record(
        self,
        film_record_id: FilmRecordIdObject,
        film_record: FilmRecordEntity,
    ):
        raise NotImplementedError
