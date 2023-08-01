# 標準ライブラリ
from datetime import datetime

# 独自ライブラリ
from src.data_model.notion.film_record.notion_film_record_data import NotionFilmRecordData
from src.data_model.notion.genre.notion_genre_data import NotionGenreData
from src.data_model.notion.series.notion_series_data import NotionSeriesData
from src.data_model.notion.series.notion_series_result_data import NotionSeriesResultData
from src.data_model.notion.watch_history.notion_watch_history_data import NotionWatchHistoryData
from src.data_model.notion.watch_medium.notion_watch_medium_data import NotionWatchMediumData
from src.domain.film_record import FilmRecordEntity, FilmRecordIdObject
from src.domain.film_record.appreciation import AppreciationStatusEnum, FilmAppreciationEntity, FilmAppreciationIdObject
from src.domain.film_record.film import FilmEntity, TmdbIdObject
from src.domain.film_record.film.genre import FilmGenreDTO
from src.domain.film_record.film.poster import FilmPosterObject
from src.domain.film_record.film.series import FilmSeriesObject
from src.domain.film_record.watch_medium.watch_medium_dto import WatchMediumDTO


class FilmRecordDto:
    """映画記録のデータトランスファーオブジェクト"""

    @staticmethod
    def from_notion_film_record_data2film_record_entity(
        notion_film_record: NotionFilmRecordData,
        notion_film_genre: NotionGenreData,
        notion_film_series: NotionSeriesData,
        notion_film_watch_history: NotionWatchHistoryData,
        notion_watch_media: NotionWatchMediumData,
    ):
        film_records: list[FilmRecordEntity] = []
        for notion_film_record_result in notion_film_record.results:
            # 映画シリーズを定義
            series_relation: str | None = notion_film_record_result.properties.Series.get_relation_id()
            if series_relation:
                film_series_result: NotionSeriesResultData = notion_film_series.get_series(
                    relation_id=series_relation,
                )
                film_series = FilmSeriesObject(
                    name=film_series_result.properties.Name.get_title(),
                    poster=FilmPosterObject(
                        poster_url=film_series_result.properties.Poster.get_file_external_url(),
                    ),
                )
            else:
                film_series = None
            # 映画視聴履歴を定義
            film_appreciations: list[FilmAppreciationEntity] = [
                FilmAppreciationEntity(
                    film_appreciation_id=FilmAppreciationIdObject(
                        value=notion_film_watch_history_result.properties.Title.get_title()
                    ),
                    medium=WatchMediumDTO.from_notion_relation_id2watch_medium_enum(
                        notion_watch_media=notion_watch_media,
                        notion_relation=(
                            notion_film_watch_history_result.properties.Watching_Medium.get_notion_relation_id()
                        ),
                    ),
                    appreciation_date=notion_film_watch_history_result.properties.Watched_On.get_date(),
                )
                for notion_film_watch_history_result in notion_film_watch_history.results
            ]

            film_records.append(
                FilmRecordEntity(
                    film_record_id=FilmRecordIdObject(value=notion_film_record_result.id),
                    appreciation_status=(
                        AppreciationStatusEnum.WATCHED
                        if notion_film_record_result.properties.Status.select.name == "鑑賞済み"
                        else AppreciationStatusEnum.NOT_WATCHED
                    ),
                    note=notion_film_record_result.properties.Note.get_rich_text(),
                    film=FilmEntity(
                        tmdb_id=TmdbIdObject(
                            value=notion_film_record_result.properties.TMDb_ID.get_int(),
                        ),
                        title=notion_film_record_result.properties.Title.get_title(),
                        overview=notion_film_record_result.properties.Overview.get_rich_text(),
                        release_date=notion_film_record_result.properties.Release_Date.get_date(),
                        run_time=notion_film_record_result.properties.Run_Time.get_int(),
                        series=film_series,
                        poster=FilmPosterObject(
                            poster_url=notion_film_record_result.properties.Cover.get_file_external_url(),
                        ),
                        genres=FilmGenreDTO.from_notion_relation_id2film_genre_enum_set(
                            notion_film_genre=notion_film_genre,
                            notion_relations=notion_film_record_result.properties.Genre.relation,
                        ),
                    ),
                    evaluation=notion_film_record_result.properties.Rating.number,
                    film_appreciations=film_appreciations,
                )
            )

        return film_records

    @staticmethod
    def from_json2film_record_entity(json_data: dict) -> list[FilmRecordEntity]:
        results: list = json_data["results"]
        film_records: list[FilmRecordEntity] = []

        for result in results:
            # 映画シリーズを定義
            series: dict | None = result["film"].get("series", {})
            if series:
                film_series = FilmSeriesObject(
                    name=series.get("name", ""),
                    poster=FilmPosterObject(
                        poster_url=series.get("poster", {}).get("poster_url", ""),
                    ),
                )
            else:
                film_series = None
            # 映画視聴履歴を定義
            appreciations: list[dict] = result.get("film_appreciations", [{}])
            film_appreciations: list[FilmAppreciationEntity] = [
                FilmAppreciationEntity(
                    film_appreciation_id=FilmAppreciationIdObject(
                        value=appreciation.get("film_appreciation_id", {}).get("value", ""),
                    ),
                    medium=WatchMediumDTO.from_str2watch_medium_enum(medium_str=appreciation.get("medium", "")),
                    appreciation_date=datetime.strptime(appreciation.get("appreciation_date", ""), "%Y-%m-%d"),
                )
                for appreciation in appreciations
            ]
            film: dict = result["film"]
            film_records.append(
                FilmRecordEntity(
                    film_record_id=FilmRecordIdObject(value=result["film_record_id"]),
                    appreciation_status=(
                        AppreciationStatusEnum.WATCHED
                        if result["appreciation_status"] == "鑑賞済み"
                        else AppreciationStatusEnum.NOT_WATCHED
                    ),
                    note=result["note"],
                    film=FilmEntity(
                        tmdb_id=TmdbIdObject(
                            value=film["tmdb_id"]["value"],
                        ),
                        title=film["title"],
                        overview=film["overview"],
                        release_date=film["release_date"],
                        run_time=film["run_time"],
                        series=film_series,
                        poster=FilmPosterObject(
                            poster_url=film.get("poster", {}).get("poster_url", ""),
                        ),
                        genres=FilmGenreDTO.from_list2film_genre_enum_set(genre_str_list=film.get("genres", [])),
                    ),
                    evaluation=result["evaluation"],
                    film_appreciations=film_appreciations,
                )
            )

        return film_records
