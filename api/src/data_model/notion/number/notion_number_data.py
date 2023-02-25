from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionNumberData:
    id: str
    type: Literal["number"]
    number: float

    def get_int(self) -> int:
        return int(self.number)
