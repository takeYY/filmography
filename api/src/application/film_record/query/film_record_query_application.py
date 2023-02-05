from logging import getLogger

from src.application.film_record.query.interface.film_record_query_application_interface import (
    IFilmRecordQueryApplication,
)
from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_id_object import FilmRecordIdObject
from src.domain.film_record.film_record_repository import IFilmRecordRepository


class ImplFilmRecordQueryApplication(IFilmRecordQueryApplication):
    def __init__(
        self,
        film_record_repository: IFilmRecordRepository,
    ) -> None:
        logger = getLogger(__name__)
        logger.info("映画記録アプリケーションの初期化")
        self.film_record_repository: IFilmRecordRepository = film_record_repository

    async def fetch_film_record_by_id(self, id: str) -> dict[str, str | FilmRecordEntity | None]:
        logger = getLogger(__name__)
        try:
            logger.info(f"{id}に一致する映画記録をfetch: 開始")
            film_record_id = FilmRecordIdObject(value=int(id))
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
            # TODO: ドメインサービスで、Notion APIから取得したデータを整形する
            film_records = self.film_record_repository.get_film_records()
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
