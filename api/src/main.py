from fastapi import FastAPI

from src.presentation.containers import Container
from src.presentation.default.default_route import default_router
from src.presentation.jumanpp.jumanpp_route import jumanpp_router
from src.presentation.movie.query.movie_query_route import movie_query_router

app = FastAPI()
app.container = Container()


app.include_router(default_router, tags=["default"])
app.include_router(jumanpp_router, prefix="/jumanpp", tags=["jumanpp"])
app.include_router(movie_query_router, prefix="/movie/query", tags=["movie"])
