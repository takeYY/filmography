# 外部ライブラリ
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# 独自ライブラリ
from src.schemas.default import DefaultResponse

default_router = APIRouter()


@default_router.get(
    "/",
    responses={
        200: {
            "description": "デフォルトの結果",
            "model": DefaultResponse,
        },
    },
)
async def default():
    return JSONResponse(
        content=dict(
            status="success",
            message="Hello, world!",
        )
    )
