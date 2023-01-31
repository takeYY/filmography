import os

from dependency_injector import providers
from dependency_injector.providers import Factory
from src.application.film_record.command.film_record_command_application import ImplFilmRecordCommandApplication
from src.application.film_record.command.interface.film_record_command_application import IFilmRecordCommandApplication
from src.infrastructure.film_record.film_record_repository import ImplFilmRecordRepository
from src.infrastructure.film_record.inmemory.inmemory_film_record_repository import ImplInmemoryFilmRecordRepository


class FilmRecordCommandContainer:
    env = os.getenv("ENV")
    film_record_command_application: Factory[IFilmRecordCommandApplication]

    if env == "PROD":
        film_record_command_application = providers.Factory(
            ImplFilmRecordCommandApplication,
            film_record_repository=ImplFilmRecordRepository(),
        )
    else:
        film_record_command_application = providers.Factory(
            ImplFilmRecordCommandApplication,
            film_record_repository=ImplInmemoryFilmRecordRepository(),
        )
