from fastapi import APIRouter, Depends
from src.application.movie.query.movie_query_application import IMovieQueryApplication, ImplMovieQueryApplication
from src.domain.movie.movie_repository import IMovieRepository
from src.infrastructure.movie.inmemory_movie_repository import ImplInmemoryMovieRepository
from src.infrastructure.movie.movie_repository import ImplMovieRepository
from src.utils.setup_logger import setup_logger

movie_query_router = APIRouter()


def movie_query_application():
    movie_repository: IMovieRepository = ImplMovieRepository()

    return ImplMovieQueryApplication(
        movie_repository=movie_repository,
    )


def inmemory_movie_query_application():
    inmemory_movie_repository: IMovieRepository = ImplInmemoryMovieRepository()

    return ImplMovieQueryApplication(
        movie_repository=inmemory_movie_repository,
    )


@movie_query_router.get("/{movie_id}")
async def movie_query(
    movie_id: str,
    movie_query_application: IMovieQueryApplication = Depends(movie_query_application),
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
