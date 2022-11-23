from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from src.application.movie.query.movie_query_application import IMovieQueryApplication
from src.presentation.containers import Container
from src.utils.setup_logger import setup_logger

movie_query_router = APIRouter()


@movie_query_router.get("/{movie_id}")
@inject
async def movie_query(
    movie_id: str,
    movie_query_application: IMovieQueryApplication = Depends(
        Provide[
            Container.movie_query_application,
        ]
    ),
):
    logger = setup_logger(__name__)
    try:
        logger.info("movie query start")
        if not movie_id:
            raise ValueError("movie_id がありません。")
        response = await movie_query_application.fetch_movie_by_id(id=movie_id)

        return response
    except Exception as e:
        logger.error(f"movie query error. LOG: {e}", exc_info=True)
        return dict(
            status="error",
            result=e,
        )
