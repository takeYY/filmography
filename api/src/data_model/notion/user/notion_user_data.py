from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionUserData:
    object: Literal["user"]
    id: str
