# 標準ライブラリ
from logging import getLogger

# 独自ライブラリ
from schemas.film_record.create.film_record_create_model import FilmRecordCreateModel
from src.application.film_record.command.interface import IFilmRecordCommandApplication, IFilmRecordCommandDomainService
from src.domain.film_record import FilmRecordEntity, FilmRecordIdObject, IFilmRecordRepository

from .film_record_command_domain_service import ImplFilmRecordCommandDomainService


class ImplFilmRecordCommandApplication(IFilmRecordCommandApplication):
    def __init__(
        self,
        film_record_repository: IFilmRecordRepository,
    ) -> None:
        logger = getLogger(__name__)
        logger.info("映画記録アプリケーションの初期化")
        self.film_record_repository: IFilmRecordRepository = film_record_repository
        self.film_record_command_domain_service: IFilmRecordCommandDomainService = ImplFilmRecordCommandDomainService(
            film_record_repository=film_record_repository,
        )

    async def create_film_record(self, film_record_model: FilmRecordCreateModel):
        logger = getLogger(__name__)
        try:
            logger.info("映画記録をcreate: 開始")

            # TMDb APIを利用して、映画情報を取得する
            film_record: FilmRecordEntity = self.film_record_command_domain_service.create_film_record(
                film_record_model=film_record_model,
            )
            logger.info("映画記録をcreate: 終了")

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

    async def update_film_record(
        self,
        film_record_id: FilmRecordIdObject,
        film_record: FilmRecordEntity,
    ):
        logger = getLogger(__name__)
        try:
            logger.info("映画記録をupdate: 開始")
            film_record = self.film_record_repository.update(
                film_record_id=film_record_id,
                film_record=film_record,
            )
            logger.info("映画記録をupdate: 終了")

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
