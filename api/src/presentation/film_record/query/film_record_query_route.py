# 外部ライブラリ
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

film_record_query_router = APIRouter(prefix="/film_record/query")

# 独自ライブラリ
from src.application.film_record.query.interface import IFilmRecordQueryApplication
from src.presentation import Container
from src.schemas.film_record import FilmRecordResponse, FilmRecordsResponse, FilmRecordSystemError
from src.utils import setup_logger

logger = setup_logger(__name__)


@film_record_query_router.get(
    "/{film_record_id}",
    response_model=FilmRecordResponse,
    response_description="映画記録の単一レスポンス",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "システムエラー",
            "model": FilmRecordSystemError,
        },
    },
)
@inject
async def film_record_query(
    film_record_id: str,
    film_record_query_application: IFilmRecordQueryApplication = Depends(
        Provide[Container.film_record_query_application]
    ),
):
    try:
        logger.info("映画記録のクエリ: 開始")

        if not film_record_id:
            raise ValueError("film_record_id がありません。")

        film_record = await film_record_query_application.fetch_film_record_by_id(id=film_record_id)

        logger.info("映画記録のクエリ: 終了")

        return JSONResponse(
            content=dict(
                status="success",
                result=jsonable_encoder(film_record),
            )
        )

    except Exception as e:
        logger.exception(f"映画記録のクエリでエラー. LOG: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=dict(
                status="error",
                error="システムエラー",
            ),
        )


@film_record_query_router.get(
    "/",
    response_model=FilmRecordsResponse,
    response_description="映画記録の複数レスポンス",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "システムエラー",
            "model": FilmRecordSystemError,
        },
    },
)
@inject
async def film_records(
    film_record_query_application: IFilmRecordQueryApplication = Depends(
        Provide[Container.film_record_query_application]
    ),
):
    try:
        logger.info("映画記録のクエリ: 開始")
        film_records = await film_record_query_application.fetch_film_records()
        logger.info("映画記録のクエリ: 終了")

        return JSONResponse(
            content=dict(
                status="success",
                results=jsonable_encoder(film_records),
            )
        )

    except Exception as e:
        logger.exception(f"映画記録のクエリでエラー. LOG: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=dict(
                status="error",
                error="システムエラー",
            ),
        )
