from abc import ABC, abstractmethod

from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_repository import IFilmRecordRepository


class IFilmRecordQueryApplication(ABC):
    film_record_repository: IFilmRecordRepository

    # NITS: 1行が長いので改行する
    @abstractmethod
    async def fetch_film_record_by_id(self, id: str) -> dict[str, str | FilmRecordEntity | None]:
        raise NotImplementedError

    # TODO: abstractmethodデコレータを追加する
    async def fetch_film_records(self):
        raise NotImplementedError
