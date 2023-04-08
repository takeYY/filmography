# 標準ライブラリ
import os

# 外部ライブラリ
from dependency_injector import providers
from dependency_injector.providers import Factory

# 独自ライブラリ
from src.application.film_record.query import ImplFilmRecordQueryApplication
from src.application.film_record.query.interface import IFilmRecordQueryApplication
from src.infrastructure.film_record.film_record_repository import ImplFilmRecordRepository
from src.infrastructure.film_record.genre.film_genre_repository import ImplFilmGenreRepository
from src.infrastructure.film_record.genre.inmemory.inmemory_film_genre_repository import ImplInmemoryFilmGenreRepository
from src.infrastructure.film_record.inmemory.inmemory_film_record_repository import ImplInmemoryFilmRecordRepository
from src.infrastructure.film_record.series.film_series_repository import ImplFilmSeriesRepository
from src.infrastructure.film_record.series.inmemory.inmemory_film_series_repository import (
    ImplInmemoryFilmSeriesRepository,
)
from src.infrastructure.film_record.watch_history.inmemory.inmemory_watch_history_repository import (
    ImplInmemoryFilmWatchHistoryRepository,
)
from src.infrastructure.film_record.watch_history.watch_history_repository import ImplFilmWatchHistoryRepository
from src.infrastructure.film_record.watch_medium.inmemory.inmemory_watch_medium_repository import (
    ImplInmemoryWatchMediumRepository,
)
from src.infrastructure.film_record.watch_medium.watch_medium_repository import ImplWatchMediumRepository


class FilmRecordQueryContainer:
    env = os.getenv("ENV")
    film_record_query_application: Factory[IFilmRecordQueryApplication]

    if env == "PROD":
        film_record_query_application = providers.Factory(
            ImplFilmRecordQueryApplication,
            film_record_repository=ImplFilmRecordRepository(),
            film_genre_repository=ImplFilmGenreRepository(),
            film_series_repository=ImplFilmSeriesRepository(),
            film_watch_history_repository=ImplFilmWatchHistoryRepository(),
            watch_medium_repository=ImplWatchMediumRepository(),
        )
    else:
        film_record_query_application = providers.Factory(
            ImplFilmRecordQueryApplication,
            film_record_repository=ImplInmemoryFilmRecordRepository(),
            film_genre_repository=ImplInmemoryFilmGenreRepository(),
            film_series_repository=ImplInmemoryFilmSeriesRepository(),
            film_watch_history_repository=ImplInmemoryFilmWatchHistoryRepository(),
            watch_medium_repository=ImplInmemoryWatchMediumRepository(),
        )
