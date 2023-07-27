# 標準ライブラリ
from abc import ABC, abstractmethod

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject


class IFilmWatchHistoryRepository(ABC):
    @abstractmethod
    def get_film_watch_history(self) -> JSONObject:
        raise NotImplementedError
