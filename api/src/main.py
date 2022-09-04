from fastapi import FastAPI

app = FastAPI()

from src.presentation.default.default_route import default_router
from src.presentation.jumanpp.jumanpp_route import jumanpp_router

app.include_router(default_router, tags=["default"])
app.include_router(jumanpp_router, prefix="/jumanpp", tags=["jumanpp"])
