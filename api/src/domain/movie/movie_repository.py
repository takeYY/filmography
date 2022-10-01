from abc import ABC, abstractmethod


class IMovieRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str):
        raise NotImplementedError
