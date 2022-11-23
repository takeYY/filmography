import os

from dependency_injector import providers
from src.application.movie.query.movie_query_application import IMovieQueryApplication, ImplMovieQueryApplication
from src.infrastructure.movie.inmemory_movie_repository import ImplInmemoryMovieRepository
from src.infrastructure.movie.movie_repository import ImplMovieRepository


class MovieQueryContainer:
    env = os.getenv("ENV")
    movie_query_application: IMovieQueryApplication
    if env == "PROD":
        movie_query_application = providers.Factory(
            ImplMovieQueryApplication,
            movie_repository=ImplMovieRepository(),
        )
    else:
        movie_query_application = providers.Factory(
            ImplMovieQueryApplication,
            movie_repository=ImplInmemoryMovieRepository(),
        )
