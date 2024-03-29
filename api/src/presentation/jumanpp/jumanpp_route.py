# 外部ライブラリ
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# 独自ライブラリ
from src.application.jumanpp.jumanpp_application import JumanppApplication
from src.presentation import Container
from src.schemas.jumanpp import JumanppResponse, JumanppSystemError, WordRequest
from src.utils import setup_logger

jumanpp_router = APIRouter(prefix="/jumanpp")
logger = setup_logger(__name__)


@jumanpp_router.post(
    "/",
    response_model=JumanppResponse,
    response_description="形態素解析の結果",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "システムエラー",
            "model": JumanppSystemError,
        },
    },
)
@inject
async def jumanpp(
    word: WordRequest,
    jumanpp_application: JumanppApplication = Depends(Provide[Container.jumanpp_application]),
):
    try:
        # TODO: このエンドポイントのログを修正したい
        logger.info("jumanpp router start")

        logger.info(f"target: {word.target}")
        return_response = await jumanpp_application.morphological_analysis(word)
        logger.info(f"jumanpp results: {return_response}")

        return JSONResponse(
            content=dict(
                status="success",
                results=jsonable_encoder(return_response),
            )
        )

    except Exception as e:
        logger.exception(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=dict(
                status="error",
                result="システムエラー",
            ),
        )
