from abc import ABC, abstractmethod
from typing import Dict

from base_model.word.word import Word
from pyknp import Juman


class JumanppApplication(ABC):
    @abstractmethod
    async def morphological_analysis(self, target: Word) -> Dict[str, str]:
        raise NotImplementedError


class ImplJumanppApplication(JumanppApplication):
    def __init__(self):
        print("application init")

    async def morphological_analysis(self, word: Word) -> Dict[str, str]:
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
