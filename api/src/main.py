# 外部ライブラリ
from fastapi import FastAPI

# 独自ライブラリ
from src.presentation import Container
from src.presentation.default.default_route import default_router
from src.presentation.film.query.film_query_route import film_query_router
from src.presentation.film_record.command.film_record_command_route import film_record_command_router
from src.presentation.film_record.query.film_record_query_route import film_record_query_router

# from src.presentation.jumanpp.jumanpp_route import jumanpp_router

app = FastAPI(
    title="Filmography API",
    description="FilmographyのAPI",
    version="0.2.2.2",
)
Container()

app.include_router(default_router, tags=["default"])
# app.include_router(jumanpp_router, tags=["jumanpp"])
app.include_router(film_record_query_router, tags=["film_record"])
app.include_router(film_record_command_router, prefix="/film_record/command", tags=["film_record"])
app.include_router(film_query_router, tags=["film"])


# フロントのテンプレ
from fastapi.staticfiles import StaticFiles
from src.front_templates.apps.film_record.create_film_record import front_create_film_record_router
from src.front_templates.apps.index import front_index_router

app.mount("/src/front_templates/static", StaticFiles(directory="src/front_templates/static"), name="static")
app.include_router(front_index_router)
app.include_router(front_create_film_record_router)
