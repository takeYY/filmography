# 標準ライブラリ
import os

# 外部ライブラリ
from dependency_injector.providers import Factory

# 独自ライブラリ
from src.application.film_record.query import ImplFilmRecordQueryApplication
from src.application.film_record.query.interface import IFilmRecordQueryApplication
from src.infrastructure.film_record import ImplFilmRecordRepository
from src.infrastructure.film_record.genre import ImplFilmGenreRepository
from src.infrastructure.film_record.genre.inmemory import ImplInmemoryFilmGenreRepository
from src.infrastructure.film_record.inmemory import ImplInmemoryFilmRecordRepository
from src.infrastructure.film_record.series import ImplFilmSeriesRepository
from src.infrastructure.film_record.series.inmemory import ImplInmemoryFilmSeriesRepository
from src.infrastructure.film_record.watch_history import ImplFilmWatchHistoryRepository
from src.infrastructure.film_record.watch_history.inmemory import ImplInmemoryFilmWatchHistoryRepository
from src.infrastructure.film_record.watch_medium import ImplWatchMediumRepository
from src.infrastructure.film_record.watch_medium.inmemory import ImplInmemoryWatchMediumRepository


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
