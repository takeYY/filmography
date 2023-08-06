# 標準ライブラリ
from logging import getLogger

# 外部ライブラリ
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# 独自ライブラリ
from src.domain.film_record.film.dto import FilmDto
from src.domain.film_record.film.genre import FilmGenreEnum

from .. import client

logger = getLogger(__name__)

front_create_film_record_router = APIRouter(prefix="/front/film_record", tags=["front", "film_record"])

templates = Jinja2Templates(directory="src/front_templates/html/film_record")


@front_create_film_record_router.get("/{tmdb_id}", response_class=HTMLResponse)
async def create(request: Request, tmdb_id: str):
    film_json: dict = client.get(f"/film/query/{tmdb_id}").json()
    logger.info(f"【front:create】{film_json=}")

    # Entityに変換
    film = FilmDto.from_json2_film_entity(json_data=film_json)
    logger.info(f"【front:create】{film=}")

    # genres
    genres = {
        12: FilmGenreEnum.ADVENTURE,
        14: FilmGenreEnum.FANTASY,
        16: FilmGenreEnum.ANIMATION,
        18: FilmGenreEnum.DRAMA,
        27: FilmGenreEnum.HORROR,
        28: FilmGenreEnum.ACTION,
        35: FilmGenreEnum.COMEDY,
        36: FilmGenreEnum.HISTORY,
        37: FilmGenreEnum.WESTERN,
        53: FilmGenreEnum.THRILLER,
        80: FilmGenreEnum.CRIME,
        99: FilmGenreEnum.DOCUMENTARY,
        878: FilmGenreEnum.SF,
        9648: FilmGenreEnum.MYSTERY,
        10402: FilmGenreEnum.MUSIC,
        10749: FilmGenreEnum.ROMANCE,
        10751: FilmGenreEnum.FAMILY,
        10752: FilmGenreEnum.WAR,
        10770: FilmGenreEnum.TV,
    }

    return templates.TemplateResponse(
        "create.html",
        {
            "request": request,
            "genres": genres,
            "film": film,
        },
    )
