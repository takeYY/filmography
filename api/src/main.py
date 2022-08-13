from fastapi import FastAPI
from pydantic import BaseModel
from pyknp import Juman

app = FastAPI()


class Keyword(BaseModel):
    name: str


@app.get("/")
async def default():
    return {"status": "success", "message": "Hello, world!"}


@app.post("/jumanpp")
async def get_juman(keyword: Keyword):
    try:
        juman = Juman()
        result = juman.analysis(keyword.name)
        result_list = result.mrph_list()

        return {"status": "success", "result": result_list}
    except Exception as e:
        print(e)
        return {"status": "error", "result": e}
