from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionDatabaseData:
    type: Literal["database_id"]
    database_id: str
