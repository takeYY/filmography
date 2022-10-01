from src.domain.movie.movie_repository import IMovieRepository


class ImplMovieRepository(IMovieRepository):
    def __init__(self) -> None:
        pass

    def find_by_id(self, id: str):
        return None
