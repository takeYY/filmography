# 外部ライブラリ
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

jumanpp_router = APIRouter()

# 独自ライブラリ
from schemas.word.word import Word
from src.application.jumanpp.jumanpp_application import JumanppApplication
from src.presentation import Container


@jumanpp_router.get("/")
@inject
async def jumanpp(
    word: Word,
    jumanpp_application: JumanppApplication = Depends(
        Provide[
            Container.jumanpp_application,
        ]
    ),
):
    try:
        print("router start")
        return_response = await jumanpp_application.morphological_analysis(word)

        return return_response
    except Exception as e:
        print(e)
        return dict(
            status="error",
            result=e,
        )
