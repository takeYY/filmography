from fastapi import APIRouter

default_router = APIRouter(tags=["defaults"])


@default_router.get("/")
async def default():
    return {"status": "success", "message": "Hello, world!"}
