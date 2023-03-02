from abc import ABC, abstractmethod


class IFilmSeriesRepository(ABC):
    @abstractmethod
    def get_series(self):
        raise NotImplementedError
