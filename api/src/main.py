from fastapi import FastAPI
from pydantic import BaseModel
from pyknp import Juman

app = FastAPI()

from src.default.route import default_router


class Keyword(BaseModel):
    name: str


app.include_router(default_router)


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
