class NotionTitle:
    """Notionのタイトル項目を扱うクラス

    Attributes
    ----------
    title: str
        タイトル
    """

    def __init__(self, title: str):
        self.title = title

    def create_title_prop(self):
        """Notionのタイトル項目を作成

        テキスト項目とは別で削除できない項目

        Returns
        -------
        dict
            タイトルの項目
        """
        return {
            "title": [
                {
                    "text": {
                        "content": self.title,
                    },
                },
            ],
        }
