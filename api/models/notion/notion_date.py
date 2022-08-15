class NotionDate:
    """Notionの日付項目を扱うクラス

    Attributes
    ----------
    start_date: str
        日付, YYYY-MM-DD
    """

    def __init__(self, start_date: str):
        self.start_date = start_date

    def create_date_prop(self):
        """Notionの日付項目を作成

        Returns
        -------
        dict
            日付の項目
        """
        return {
            "date": {
                "start": self.start_date,
            },
        }
