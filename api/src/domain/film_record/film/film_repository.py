# 標準ライブラリ
from abc import ABC, abstractmethod

# 独自ライブラリ
from .film_entity import FilmEntity
from .tmdb_id_object import TmdbIdObject


class AbstractFilmRepository(ABC):
    @abstractmethod
    def find_by_tmdb_id(self, id: TmdbIdObject) -> FilmEntity | None:
        raise NotImplementedError
