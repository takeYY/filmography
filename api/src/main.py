# 外部ライブラリ
from fastapi import FastAPI

# 独自ライブラリ
from src.presentation import Container
from src.presentation.default.default_route import default_router
from src.presentation.film_record.command.film_record_command_route import film_record_command_router
from src.presentation.film_record.query.film_record_query_route import film_record_query_router
from src.presentation.jumanpp.jumanpp_route import jumanpp_router

app = FastAPI()
Container()

app.include_router(default_router, tags=["default"])
app.include_router(jumanpp_router, prefix="/jumanpp", tags=["jumanpp"])
app.include_router(film_record_query_router, prefix="/film_record/query", tags=["film_record"])
app.include_router(film_record_command_router, prefix="/film_record/command", tags=["film_record"])
