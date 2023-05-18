# 外部ライブラリ
from fastapi import APIRouter

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
    return dict(
        status="success",
        message="Hello, world!",
    )
