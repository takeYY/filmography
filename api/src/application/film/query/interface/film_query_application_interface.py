# 標準ライブラリ
from abc import ABC, abstractmethod

# 独自ライブラリ
from src.domain.film_record.film import AbstractFilmRepository, FilmEntity


class AbstractFilmQueryApplication(ABC):
    film_repository: AbstractFilmRepository

    @abstractmethod
    async def fetch_film_by_tmdb_id(
        self,
        id: str,
    ) -> FilmEntity:
        raise NotImplementedError
