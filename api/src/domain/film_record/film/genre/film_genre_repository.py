# 標準ライブラリ
from abc import ABC, abstractmethod


class IFilmGenreRepository(ABC):
    @abstractmethod
    def get_genres(self):
        raise NotImplementedError
