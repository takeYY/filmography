# 標準ライブラリ
from abc import ABC, abstractmethod

# 独自ライブラリ
from src.domain.film_record import FilmRecordEntity


class IFilmRecordQueryDomainService(ABC):
    @abstractmethod
    def get_film_records(self) -> list[FilmRecordEntity]:
        raise NotImplementedError
