class NotionText:
    """Notionのテキスト項目を扱うクラス

    Attributes
    ----------
    text: str
        テキスト
    """

    def __init__(self, text: str):
        self.text = text

    def create_text_prop(self):
        """Notionのテキスト項目を作成

        Returns
        -------
        dict
            テキスト項目
        """
        return {
            "rich_text": [
                {
                    "text": {
                        "content": self.text,
                    },
                },
            ],
        }
