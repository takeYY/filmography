from abc import ABC, abstractmethod

from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_repository import IFilmRecordRepository


class IFilmRecordQueryApplication(ABC):
    film_record_repository: IFilmRecordRepository

    @abstractmethod
    async def fetch_film_record_by_id(self, id: str) -> dict[str, str | FilmRecordEntity | None]:
        raise NotImplementedError

    async def fetch_film_records(self):
        raise NotImplementedError
