# 標準ライブラリ
from abc import ABC, abstractmethod

# 外部ライブラリ
from dataclass_wizard.type_def import JSONObject


class IWatchMediumRepository(ABC):
    @abstractmethod
    def get_watch_media(self) -> JSONObject:
        raise NotImplementedError
