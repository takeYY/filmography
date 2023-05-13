# 外部ライブラリ
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# 独自ライブラリ
from src.domain.film_record import FilmRecordEntity
from src.domain.film_record.dto import FilmRecordDto

from . import client

front_index_router = APIRouter(prefix="/front", tags=["front"])


templates = Jinja2Templates(directory="src/front_templates/html")


@front_index_router.get("/index", response_class=HTMLResponse)
async def home(request: Request):
    json_data: dict = client.get("/film_record/query/").json()  # type: ignore

    film_records: list[FilmRecordEntity] = FilmRecordDto.from_json2film_record_entity(json_data=json_data)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "film_records": film_records},
    )
