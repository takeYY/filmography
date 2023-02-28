from abc import ABC, abstractmethod


class IFilmWatchHistoryRepository(ABC):
    @abstractmethod
    def get_film_watch_history(self):
        raise NotImplementedError
