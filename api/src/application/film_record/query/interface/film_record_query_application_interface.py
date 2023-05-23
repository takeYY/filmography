# 標準ライブラリ
from abc import ABC, abstractmethod

# 独自ライブラリ
from src.domain.film_record import FilmRecordEntity, IFilmRecordRepository
from src.domain.film_record.film.genre import IFilmGenreRepository
from src.domain.film_record.film.series import IFilmSeriesRepository
from src.domain.film_record.watch_history import IFilmWatchHistoryRepository
from src.domain.film_record.watch_medium import IWatchMediumRepository


class IFilmRecordQueryApplication(ABC):
    film_record_repository: IFilmRecordRepository
    film_genre_repository: IFilmGenreRepository
    film_series_repository: IFilmSeriesRepository
    film_watch_history_repository: IFilmWatchHistoryRepository
    watch_medium_repository: IWatchMediumRepository

    @abstractmethod
    async def fetch_film_record_by_id(
        self,
        id: str,
    ) -> FilmRecordEntity:
        raise NotImplementedError

    @abstractmethod
    async def fetch_film_records(self):
        raise NotImplementedError
