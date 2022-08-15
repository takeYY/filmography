class NotionSelect:
    """Notionのラベル項目を扱うクラス

    Attributes
    ----------
    label : str
        ラベル
    """

    def __init__(self, label: str):
        self.label = label

    def create_select_prop(self):
        """Notionのラベル項目を作成

        Returns
        -------
        dict
            ラベル項目
        """
        return {
            "select": {
                "name": self.label,
            },
        }
