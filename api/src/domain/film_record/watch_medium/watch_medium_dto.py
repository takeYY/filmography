# 独自ライブラリ
from src.data_model.notion.relation.notion_relation_data import NotionRelationIdData
from src.data_model.notion.watch_medium.notion_watch_medium_data import NotionWatchMediumData

from .watch_medium_enum import WatchMediumEnum


class WatchMediumDTO:
    """鑑賞媒体に関するデータトランスファーオブジェクト"""

    @staticmethod
    def from_medium_id2watch_medium_enum(medium_id: int) -> WatchMediumEnum:
        """媒体IDを鑑賞媒体に変換する"""
        medium_mapping = {
            "1": "AMAZON_PRIME_VIDEO",
            "2": "NETFLIX",
            "3": "DISNEY",
            "4": "U_NEXT",
            "5": "THEATER",
            "6": "D_ANIME",
        }
        medium = medium_mapping.get(str(medium_id))

        if not medium:
            raise ValueError(f"{medium_id}に合致する鑑賞媒体が存在しません。")

        return WatchMediumEnum[medium]

    @staticmethod
    def from_notion_relation_id2watch_medium_enum(
        notion_watch_media: NotionWatchMediumData,
        notion_relation: NotionRelationIdData,
    ) -> WatchMediumEnum:
        watch_medium_id = notion_watch_media.get_medium_id(relation_id=notion_relation.id)
        return WatchMediumDTO.from_medium_id2watch_medium_enum(medium_id=watch_medium_id)

    @staticmethod
    def from_str2watch_medium_enum(medium_str: str) -> WatchMediumEnum:
        for medium in WatchMediumEnum:
            if medium_str == medium.value:
                return medium

        raise ValueError(f"{medium_str}に合致する鑑賞媒体が存在しません。")
