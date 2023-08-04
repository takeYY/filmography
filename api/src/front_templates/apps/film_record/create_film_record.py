# 標準ライブラリ
from logging import getLogger

# 外部ライブラリ
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# 独自ライブラリ
from .. import client

logger = getLogger(__name__)

front_create_film_record_router = APIRouter(prefix="/front/film_record", tags=["front", "film_record"])

templates = Jinja2Templates(directory="src/front_templates/html/film_record")


@front_create_film_record_router.get("/{tmdb_id}", response_class=HTMLResponse)
async def create(request: Request, tmdb_id: str):
    # TODO: 下記 API を作る
    film_json: dict = client.get(f"/film/query/{tmdb_id}").json()
    logger.info(f"【front:create】{film_json=}")

    # TODO: dictをEntityに変換する
    film = ...

    return templates.TemplateResponse(
        "create.html",
        {"film": film},
    )
