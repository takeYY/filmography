# 標準ライブラリ
from abc import ABC, abstractmethod
from logging import getLogger

# 外部ライブラリ
from pyknp import Juman

# 独自ライブラリ
from src.schemas.jumanpp import JumanppResult, WordRequest

logger = getLogger(__name__)


class JumanppApplication(ABC):
    @abstractmethod
    async def morphological_analysis(
        self,
        target: WordRequest,
    ) -> list[JumanppResult]:
        raise NotImplementedError


class ImplJumanppApplication(JumanppApplication):
    def __init__(self):
        logger.info("jumanpp application init")

    async def morphological_analysis(
        self,
        word: WordRequest,
    ) -> list[JumanppResult]:
        try:
            logger.info("application analysis")

            juman = Juman()
            result = juman.analysis(word.target)
            result_list: list[JumanppResult] = result.mrph_list()
            if not result_list:
                raise ValueError("形態素解析結果がありません.")

            return result_list

        except Exception:
            raise
