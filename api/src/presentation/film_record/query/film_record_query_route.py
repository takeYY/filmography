# 外部ライブラリ
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

# 独自ライブラリ
from src.application.film_record.query.interface import IFilmRecordQueryApplication
from src.presentation.containers import Container
from src.utils.setup_logger import setup_logger

film_record_query_router = APIRouter()


@film_record_query_router.get("/{film_record_id}")
@inject
async def film_record_query(
    film_record_id: str,
    film_record_query_application: IFilmRecordQueryApplication = Depends(
        Provide[
            Container.film_record_query_application,
        ]
    ),
):
    logger = setup_logger(__name__)
    try:
        logger.info("映画記録のクエリ: 開始")

        if not film_record_id:
            raise ValueError("film_record_id がありません。")

        response = await film_record_query_application.fetch_film_record_by_id(id=film_record_id)

        logger.info("映画記録のクエリ: 終了")

        return response
    except Exception as e:
        logger.error(f"映画記録のクエリでエラー. LOG: {e}", exc_info=True)
        return dict(
            status="error",
            result=e,
        )


@film_record_query_router.get("/")
@inject
async def film_records(
    film_record_query_application: IFilmRecordQueryApplication = Depends(
        Provide[
            Container.film_record_query_application,
        ]
    ),
):
    logger = setup_logger(__name__)
    try:
        logger.info("映画記録のクエリ: 開始")
        responses = await film_record_query_application.fetch_film_records()
        logger.info("映画記録のクエリ: 終了")

        return responses
    except Exception as e:
        logger.error(f"映画記録のクエリでエラー. LOG: {e}", exc_info=True)
        return dict(
            status="error",
            result=e,
        )
