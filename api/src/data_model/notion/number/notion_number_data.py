from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionNumberData:
    id: str
    type: Literal["NotionNumberData"]
    number: float
