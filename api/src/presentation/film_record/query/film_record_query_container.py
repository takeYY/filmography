import os

from dependency_injector import providers
from dependency_injector.providers import Factory
from src.application.film_record.query.film_record_query_application import ImplFilmRecordQueryApplication
from src.application.film_record.query.interface.film_record_query_application_interface import (
    IFilmRecordQueryApplication,
)
from src.infrastructure.film_record.film_record_repository import ImplFilmRecordRepository
from src.infrastructure.film_record.genre.film_genre_repository import ImplFilmGenreRepository
from src.infrastructure.film_record.genre.inmemory.inmemory_film_genre_repository import ImplInmemoryFilmGenreRepository
from src.infrastructure.film_record.inmemory.inmemory_film_record_repository import ImplInmemoryFilmRecordRepository


class FilmRecordQueryContainer:
    env = os.getenv("ENV")
    film_record_query_application: Factory[IFilmRecordQueryApplication]

    if env == "PROD":
        film_record_query_application = providers.Factory(
            ImplFilmRecordQueryApplication,
            film_record_repository=ImplFilmRecordRepository(),
            film_genre_repository=ImplFilmGenreRepository(),
        )
    else:
        film_record_query_application = providers.Factory(
            ImplFilmRecordQueryApplication,
            film_record_repository=ImplInmemoryFilmRecordRepository(),
            film_genre_repository=ImplInmemoryFilmGenreRepository(),
        )
