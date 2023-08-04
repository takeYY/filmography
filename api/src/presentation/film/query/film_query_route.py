# 外部ライブラリ
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

film_query_router = APIRouter(prefix="/film/query")


# 独自ライブラリ
from src.application.film.query.interface import AbstractFilmQueryApplication
from src.presentation import Container
from src.utils import setup_logger

logger = setup_logger(__name__)


@film_query_router.get(
    "/{tmdb_id}",
    # response_model=FilmRecordResponse,
    response_description="映画の単一レスポンス",
    status_code=status.HTTP_200_OK,
    # responses={
    #     status.HTTP_500_INTERNAL_SERVER_ERROR: {
    #         "description": "システムエラー",
    #         "model": FilmRecordSystemError,
    #     },
    # },
)
@inject
async def film_query(
    tmdb_id: str,
    film_query_application: AbstractFilmQueryApplication = Depends(Provide[Container.film_query_application]),
):
    try:
        logger.info("映画のクエリ: 開始")
        film = await film_query_application.fetch_film_by_tmdb_id(id=tmdb_id)
        logger.info("映画のクエリ: 終了")

        return JSONResponse(
            content=dict(
                status="success",
                result=jsonable_encoder(film),
            )
        )

    except Exception as e:
        logger.exception(f"映画のクエリでエラー. LOG: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=dict(
                status="error",
                error="システムエラー",
            ),
        )
