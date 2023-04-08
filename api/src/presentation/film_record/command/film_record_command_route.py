from base_model.film_record.create.film_record_create_model import FilmRecordCreateModel
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from src.application.film_record.command.interface import IFilmRecordCommandApplication
from src.presentation.containers import Container
from src.utils.setup_logger import setup_logger

film_record_command_router = APIRouter()


@film_record_command_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
@inject
async def film_record_command(
    film_record: FilmRecordCreateModel,
    film_record_command_application: IFilmRecordCommandApplication = Depends(
        Provide[
            Container.film_record_command_application,
        ]
    ),
):
    logger = setup_logger(__name__)
    try:
        logger.info("映画記録のコマンド: 開始")

        response = await film_record_command_application.create_film_record(film_record_model=film_record)

        logger.info("映画記録のクエリ: 終了")

        return response
    except Exception as e:
        logger.error(f"映画記録のクエリでエラー. LOG: {e}", exc_info=True)
        return dict(
            status="error",
            result=e,
        )
