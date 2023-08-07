# 標準ライブラリ
import os

# 外部ライブラリ
from dependency_injector.providers import Factory

# 独自ライブラリ
from src.application.film.query import ImplFilmQueryApplication
from src.application.film.query.interface import AbstractFilmQueryApplication
from src.infrastructure.film_record.film import ImplFilmRepository
from src.infrastructure.film_record.film.inmemory import ImplInmemoryFilmRepository


class FilmQueryContainer:
    env = os.getenv("ENV")
    film_query_application: Factory[AbstractFilmQueryApplication]

    if env == "PROD":
        film_query_application = Factory(
            ImplFilmQueryApplication,
            film_repository=ImplFilmRepository(),
        )
    else:
        film_query_application = Factory(
            ImplFilmQueryApplication,
            film_repository=ImplInmemoryFilmRepository(),
        )
