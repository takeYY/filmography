# 標準ライブラリ
from abc import ABC, abstractmethod

# 独自ライブラリ
from .film_record_entity import FilmRecordEntity
from .film_record_id_object import FilmRecordIdObject


class IFilmRecordRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: FilmRecordIdObject) -> FilmRecordEntity | None:
        raise NotImplementedError

    @abstractmethod
    def get_film_records(self):
        raise NotImplementedError

    @abstractmethod
    def create(self, film_record: FilmRecordEntity) -> FilmRecordEntity:
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        film_record_id: FilmRecordIdObject,
        film_record: FilmRecordEntity,
    ) -> FilmRecordEntity:
        raise NotImplementedError
