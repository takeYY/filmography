# 標準ライブラリ
from abc import ABC, abstractmethod

# 独自ライブラリ
from base_model.film_record.create.film_record_create_model import FilmRecordCreateModel
from src.domain.film_record import FilmRecordEntity, FilmRecordIdObject, IFilmRecordRepository


class IFilmRecordCommandApplication(ABC):
    film_record_repository: IFilmRecordRepository

    @abstractmethod
    async def create_film_record(
        self,
        film_record_model: FilmRecordCreateModel,
    ):
        raise NotImplementedError

    @abstractmethod
    async def update_film_record(
        self,
        film_record_id: FilmRecordIdObject,
        film_record: FilmRecordEntity,
    ):
        raise NotImplementedError
