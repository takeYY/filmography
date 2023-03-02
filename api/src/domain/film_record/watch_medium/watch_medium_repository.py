from abc import ABC, abstractmethod


class IWatchMediumRepository(ABC):
    @abstractmethod
    def get_watch_media(self):
        raise NotImplementedError
