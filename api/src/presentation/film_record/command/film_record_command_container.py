# 標準ライブラリ
import os

# 外部ライブラリ
from dependency_injector import providers
from dependency_injector.providers import Factory

# 独自ライブラリ
from src.application.film_record.command import ImplFilmRecordCommandApplication
from src.application.film_record.command.interface import IFilmRecordCommandApplication
from src.infrastructure.film_record import ImplFilmRecordRepository
from src.infrastructure.film_record.inmemory import ImplInmemoryFilmRecordRepository


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
