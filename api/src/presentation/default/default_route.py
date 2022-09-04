from fastapi import APIRouter

default_router = APIRouter()


@default_router.get("/")
async def default():
    return dict(
        status="success",
        message="Hello, world!",
    )
