from abc import ABC, abstractmethod
from logging import getLogger

from src.domain.movie.movie_repository import IMovieRepository


class IMovieQueryApplication(ABC):
    movie_repository: IMovieRepository

    @abstractmethod
    async def fetch_movie_by_id(self, id: str):
        raise NotImplementedError

    async def fetch_movies(self):
        raise NotImplementedError


class ImplMovieQueryApplication(IMovieQueryApplication):
    def __init__(
        self,
        movie_repository: IMovieRepository,
    ):
        logger = getLogger(__name__)
        logger.info("movie query application init")
        self.movie_repository: IMovieRepository = movie_repository

    async def fetch_movie_by_id(self, id: str) -> dict[str, str]:
        logger = getLogger(__name__)
        try:
            logger.info(f"fetch movie by {id}: start")
            movie = self.movie_repository.find_by_id(id=id)
            logger.info(f"fetch movie by {id}: done")

            return dict(
                status="success",
                result=movie,
            )
        except Exception as e:
            print(e)
            return dict(
                status="error",
                result=str(e),
            )

    async def fetch_movies(self):
        pass
