from abc import ABC, abstractmethod


class IFilmRecordQueryDomainService(ABC):
    @abstractmethod
    def get_film_records(self):
        raise NotImplementedError
