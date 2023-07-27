# 標準ライブラリ
from abc import ABC, abstractmethod

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject


class IFilmSeriesRepository(ABC):
    @abstractmethod
    def get_series(self) -> JSONObject:
        raise NotImplementedError
