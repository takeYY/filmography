# 標準ライブラリ
from logging import getLogger

# 独自ライブラリ
from src.application.film.query.interface import AbstractFilmQueryApplication
from src.domain.film_record.film import AbstractFilmRepository, FilmEntity, TmdbIdObject

logger = getLogger(__name__)


class ImplFilmQueryApplication(AbstractFilmQueryApplication):
    def __init__(self, film_repository: AbstractFilmRepository) -> None:
        logger.info("filmアプリケーションの初期化")
        self.film_repo = film_repository

    async def fetch_film_by_tmdb_id(self, id: str) -> FilmEntity:
        try:
            logger.info(f"{id}に一致する映画をfetch: 開始")
            tmdb_id = TmdbIdObject(value=int(id))
            film: FilmEntity | None = self.film_repo.find_by_tmdb_id(id=tmdb_id)
            logger.info(f"{id}に一致する映画をfetch: 終了")

            if not film:
                raise ValueError("映画がありません。")

            return film

        except Exception:
            raise
