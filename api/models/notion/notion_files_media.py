class NotionFilesMedia:
    """Notionのファイルやメディア項目を扱うクラス

    Attributes
    ----------
    media_url: str
        メディアのURL
    """

    def __init__(self, media_url: str):
        self.media_url = media_url

    def create_files_media_prop(self):
        """Notionのファイルやメディアの項目を作成

        Returns
        -------
        dict
            ファイルやメディアの項目
        """
        return {
            "files": [
                {
                    "name": self.media_url,
                    "type": "external",
                    "external": {
                        "url": self.media_url,
                    },
                },
            ],
        }
