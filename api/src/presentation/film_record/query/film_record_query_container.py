# 標準ライブラリ
import os

# 外部ライブラリ
from dependency_injector.providers import Factory

# 独自ライブラリ
from src.application.film_record.query import ImplFilmRecordQueryApplication
from src.application.film_record.query.interface import IFilmRecordQueryApplication
from src.infrastructure.film_record import (
    ImplFilmGenreRepository,
    ImplFilmRecordRepository,
    ImplFilmSeriesRepository,
    ImplFilmWatchHistoryRepository,
    ImplInmemoryFilmGenreRepository,
    ImplInmemoryFilmRecordRepository,
    ImplInmemoryFilmSeriesRepository,
    ImplInmemoryFilmWatchHistoryRepository,
    ImplInmemoryWatchMediumRepository,
    ImplWatchMediumRepository,
)


class FilmRecordQueryContainer:
    env = os.getenv("ENV")
    film_record_query_application: Factory[IFilmRecordQueryApplication]

    if env == "PROD":
        film_record_query_application = Factory(
            ImplFilmRecordQueryApplication,
            film_record_repository=ImplFilmRecordRepository(),
            film_genre_repository=ImplFilmGenreRepository(),
            film_series_repository=ImplFilmSeriesRepository(),
            film_watch_history_repository=ImplFilmWatchHistoryRepository(),
            watch_medium_repository=ImplWatchMediumRepository(),
        )
    else:
        film_record_query_application = Factory(
            ImplFilmRecordQueryApplication,
            film_record_repository=ImplInmemoryFilmRecordRepository(),
            film_genre_repository=ImplInmemoryFilmGenreRepository(),
            film_series_repository=ImplInmemoryFilmSeriesRepository(),
            film_watch_history_repository=ImplInmemoryFilmWatchHistoryRepository(),
            watch_medium_repository=ImplInmemoryWatchMediumRepository(),
        )
