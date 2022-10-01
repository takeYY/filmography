from src.domain.movie.movie_repository import IMovieRepository


class ImplInmemoryMovieRepository(IMovieRepository):
    def __init__(self) -> None:
        self.movies = [
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
        for movie in self.movies:
            if movie["id"] == id:
                return movie

        return None
