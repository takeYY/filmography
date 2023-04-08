# 標準ライブラリ
from abc import ABC, abstractmethod

# 独自ライブラリ
from schemas.film_record.create.film_record_create_model import FilmRecordCreateModel
from src.domain.film_record import FilmRecordEntity


class IFilmRecordCommandDomainService(ABC):
    @abstractmethod
    def create_film_record(self, film_record_model: FilmRecordCreateModel) -> FilmRecordEntity:
        raise NotImplementedError
