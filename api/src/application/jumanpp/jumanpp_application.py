# 標準ライブラリ
from abc import ABC, abstractmethod

# 外部ライブラリ
from pyknp import Juman

# 独自ライブラリ
from schemas.word.word import Word


class JumanppApplication(ABC):
    @abstractmethod
    async def morphological_analysis(self, target: Word) -> dict[str, str]:
        raise NotImplementedError


class ImplJumanppApplication(JumanppApplication):
    def __init__(self):
        print("application init")

    async def morphological_analysis(self, word: Word) -> dict[str, str]:
        try:
            print("application analysis")
            juman = Juman()
            result = juman.analysis(word.target)
            result_list = result.mrph_list()

            return dict(
                status="success",
                result=result_list,
            )
        except Exception as e:
            print(e)
            return dict(
                status="error",
                result=str(e),
            )
