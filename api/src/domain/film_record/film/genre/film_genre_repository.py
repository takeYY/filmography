# 標準ライブラリ
from abc import ABC, abstractmethod

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject


class IFilmGenreRepository(ABC):
    @abstractmethod
    def get_genres(self) -> JSONObject:
        raise NotImplementedError
