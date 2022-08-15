from typing import List


class NotionMultiSelect:
    """Notionのタグ項目を扱うクラス

    Attributes
    ----------
    tags: List[str]
        タグ
    """

    def __init__(self, tags: List[str]):
        self.tags = tags

    def create_multi_select_prop(self):
        """Notionのタグ項目を作成

        Returns
        -------
        dict
            タグ項目
        """
        return {
            "multi_select": [
                {
                    "name": tag,
                }
                for tag in self.tags
            ],
        }
