# 標準ライブラリ
from abc import ABC, abstractmethod

# 独自ライブラリ
from src.domain.film_record import FilmRecordEntity, IFilmRecordRepository

from .film_record_query_domain_service import IFilmRecordQueryDomainService


class IFilmRecordQueryApplication(ABC):
    film_record_repository: IFilmRecordRepository
    film_record_domain_service: IFilmRecordQueryDomainService

    @abstractmethod
    async def fetch_film_record_by_id(
        self,
        id: str,
    ) -> FilmRecordEntity:
        raise NotImplementedError

    @abstractmethod
    async def fetch_film_records(self) -> list[FilmRecordEntity]:
        raise NotImplementedError
