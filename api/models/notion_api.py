import os

from notion_client import Client


class NotionAPI:
    """Notion APIを扱うクラス

    Attributes
    ----------
    notion
        notion_client
    """

    def __init__(self):
        self.notion = Client(auth=os.environ["NOTION_TOKEN"])

    def create2watched_movie(self, props):
        """鑑賞済みの映画をNotionに追加する処理

        Parameters
        ----------
        props : dict
            作成する項目

        Returns
        -------
        create_result: dict
            Notion APIで作成した結果
        """
        create_props = {
            "parent": {
                "database_id": os.environ.get("WATCHED_DB_ID"),
            },
            "properties": props,
        }

        return self.__create_data2notion(create_props)

    def create2wanna_watch_movie(self, props):
        """観たい映画をNotionに追加する処理

        Parameters
        ----------
        props : dict
            作成する項目

        Returns
        -------
        create_result: dict
            Notion APIで作成した結果
        """
        create_props = {
            "parent": {
                "database_id": os.environ.get("WANNA_WATCH_DB_ID"),
            },
            "properties": props,
        }

        return self.__create_data2notion(create_props)

    def create2all_movies_db(self, props: dict):
        """Notionの映画DBに映画を追加する処理

        Parameters
        ----------
        props : dict
            作成する項目

        Returns
        -------
        create_result: dict
            Notion APIで作成した結果
        """
        create_props = {
            "parent": {
                "database_id": os.environ.get("ALL_MOVIES_DB_ID"),
            },
            "properties": props,
        }

        return self.__create_data2notion(create_props)

    def __create_data2notion(self, create_props: dict):
        create_result = self.notion.pages.create(create_props)

        return create_result
