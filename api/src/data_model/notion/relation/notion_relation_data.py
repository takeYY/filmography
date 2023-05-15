from dataclasses import dataclass
from typing import Literal


@dataclass
class NotionRelationIdData:
    id: str


@dataclass
class NotionRelationData:
    id: str
    type: Literal["relation"]
    relation: list[NotionRelationIdData]
    has_more: bool

    def get_relation_id(self) -> str | None:
        if 1 < len(self.relation):
            raise ValueError("relationが複数あります。")

        if not self.relation:
            return None

        return self.relation[0].id

    def get_relation_ids(self) -> list[str]:
        return [relation.id for relation in self.relation]

    def get_notion_relation_id(self) -> NotionRelationIdData:
        if 1 < len(self.relation):
            raise ValueError("relationが複数あります。")

        return self.relation[0]
