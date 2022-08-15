class NotionNumber:
    """Notionの整数型の数値項目を扱うクラス

    Attributes
    ----------
    number: int
        数値
    """

    def __init__(self, number: int):
        self.number = number

    def create_number_prop(self):
        """Notionの整数型数値項目を作成

        Returns
        -------
        dict
            数値項目
        """
        return {
            "number": self.number,
        }
