# 標準ライブラリ
from logging import getLogger

# 独自ライブラリ
from src.application.film_record.query.interface import IFilmRecordQueryApplication, IFilmRecordQueryDomainService
from src.domain.film_record import FilmRecordEntity, FilmRecordIdObject, IFilmRecordRepository
from src.domain.film_record.film.genre import IFilmGenreRepository
from src.domain.film_record.film.series import IFilmSeriesRepository
from src.domain.film_record.watch_history import IFilmWatchHistoryRepository
from src.domain.film_record.watch_medium import IWatchMediumRepository

from .film_record_query_domain_service import ImplFilmRecordQueryDomainService


class ImplFilmRecordQueryApplication(IFilmRecordQueryApplication):
    def __init__(
        self,
        film_record_repository: IFilmRecordRepository,
        film_genre_repository: IFilmGenreRepository,
        film_series_repository: IFilmSeriesRepository,
        film_watch_history_repository: IFilmWatchHistoryRepository,
        watch_medium_repository: IWatchMediumRepository,
    ) -> None:
        logger = getLogger(__name__)
        logger.info("映画記録アプリケーションの初期化")
        self.film_record_repository: IFilmRecordRepository = film_record_repository
        self.film_record_domain_service: IFilmRecordQueryDomainService = ImplFilmRecordQueryDomainService(
            film_record_repository=film_record_repository,
            film_genre_repository=film_genre_repository,
            film_series_repository=film_series_repository,
            film_watch_history_repository=film_watch_history_repository,
            watch_medium_repository=watch_medium_repository,
        )

    async def fetch_film_record_by_id(self, id: str) -> dict[str, str | FilmRecordEntity | None]:
        logger = getLogger(__name__)
        try:
            logger.info(f"{id}に一致する映画記録をfetch: 開始")
            film_record_id = FilmRecordIdObject(value=id)
            film_record: FilmRecordEntity | None = self.film_record_repository.find_by_id(id=film_record_id)
            logger.info(f"{id}に一致する映画記録をfetch: 終了")

            return dict(
                status="success",
                result=film_record,
            )
        except Exception as e:
            logger.error(e)
            return dict(
                status="error",
                result=str(e),
            )

    async def fetch_film_records(self):
        logger = getLogger(__name__)
        try:
            logger.info("映画記録を一括取得: 開始")
            film_records = self.film_record_domain_service.get_film_records()
            logger.info("映画記録を一括取得: 終了")

            return dict(
                status="success",
                result=film_records,
            )
        except Exception as e:
            logger.error(e)
            return dict(
                status="error",
                result=str(e),
            )
