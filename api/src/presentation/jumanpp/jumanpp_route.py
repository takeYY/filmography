from fastapi import APIRouter, Depends

jumanpp_router = APIRouter()

from base_model.word.word import Word
from src.application.jumanpp.jumanpp_application import ImplJumanppApplication, JumanppApplication


def jumanpp_application():
    return ImplJumanppApplication()


@jumanpp_router.get("/")
async def jumanpp(
    word: Word,
    jumanpp_application: JumanppApplication = Depends(jumanpp_application),
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
