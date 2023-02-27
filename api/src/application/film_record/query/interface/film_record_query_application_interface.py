from abc import ABC, abstractmethod

from src.domain.film_record.film.genre.film_genre_repository import IFilmGenreRepository
from src.domain.film_record.film.series.film_series_repository import IFilmSeriesRepository
from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_repository import IFilmRecordRepository


class IFilmRecordQueryApplication(ABC):
    film_record_repository: IFilmRecordRepository
    film_genre_repository: IFilmGenreRepository
    film_series_repository: IFilmSeriesRepository

    @abstractmethod
    async def fetch_film_record_by_id(
        self,
        id: str,
    ) -> dict[str, str | FilmRecordEntity | None]:
        raise NotImplementedError

    @abstractmethod
    async def fetch_film_records(self):
        raise NotImplementedError
