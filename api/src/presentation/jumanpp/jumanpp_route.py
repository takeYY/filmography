from base_model.word.word import Word
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from src.application.jumanpp.jumanpp_application import JumanppApplication
from src.presentation.containers import Container

jumanpp_router = APIRouter()


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
