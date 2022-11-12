from logging import getLogger

from src.domain.movie.movie_repository import IMovieRepository


class ImplInmemoryMovieRepository(IMovieRepository):
    def __init__(self) -> None:
        logger = getLogger(__name__)
        logger.info("inmemory movie repository: init")
        self.movies: list[dict[str, str | list[str]]] = [
            {
                "id": "1",
                "title": "ターミネーター",
                "genre": ["SF", "アクション"],
            },
            {
                "id": "2",
                "title": "ターミネーター2",
                "genre": ["SF", "アクション"],
            },
        ]

    def find_by_id(self, id: str):
        logger = getLogger(__name__)
        logger.info(f"find by {id}")

        for movie in self.movies:
            if movie["id"] == id:
                logger.info(f"founded movie: {movie}")
                return movie

        logger.warning("not found movie")
        return None
