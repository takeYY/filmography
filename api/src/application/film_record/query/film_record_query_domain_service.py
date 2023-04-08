# 標準ライブラリ
from __future__ import annotations

# 独自ライブラリ
from src.application.film_record.query.interface import IFilmRecordQueryDomainService
from src.data_model.notion.film_record.notion_film_record_data import NotionFilmRecordData
from src.data_model.notion.genre.notion_genre_data import NotionGenreData
from src.data_model.notion.series.notion_series_data import NotionSeriesData
from src.data_model.notion.watch_history.notion_watch_history_data import NotionWatchHistoryData
from src.data_model.notion.watch_medium.notion_watch_medium_data import NotionWatchMediumData
from src.domain.film_record import FilmRecordEntity, IFilmRecordRepository
from src.domain.film_record.dto import FilmRecordDto
from src.domain.film_record.film.genre import IFilmGenreRepository
from src.domain.film_record.film.series import IFilmSeriesRepository
from src.domain.film_record.watch_history import IFilmWatchHistoryRepository
from src.domain.film_record.watch_medium import IWatchMediumRepository


class ImplFilmRecordQueryDomainService(IFilmRecordQueryDomainService):
    def __init__(
        self,
        film_record_repository: IFilmRecordRepository,
        film_genre_repository: IFilmGenreRepository,
        film_series_repository: IFilmSeriesRepository,
        film_watch_history_repository: IFilmWatchHistoryRepository,
        watch_medium_repository: IWatchMediumRepository,
    ):
        self.film_record_repository: IFilmRecordRepository = film_record_repository
        self.film_genre_repository: IFilmGenreRepository = film_genre_repository
        self.film_series_repository: IFilmSeriesRepository = film_series_repository
        self.film_watch_history_repository: IFilmWatchHistoryRepository = film_watch_history_repository
        self.watch_medium_repository: IWatchMediumRepository = watch_medium_repository

    def get_film_records(self):
        # 映画記録をNotionから取得し、データクラスに変換
        notion_film_records = self.film_record_repository.get_film_records()
        notion_film_record_data = NotionFilmRecordData.from_dict(notion_film_records)
        # 映画ジャンルをNotionから取得し、データクラスに変換
        notion_film_genres = self.film_genre_repository.get_genres()
        notion_film_genres_data = NotionGenreData.from_dict(notion_film_genres)
        # 映画シリーズをNotionから取得し、データクラスに変換
        notion_film_series = self.film_series_repository.get_series()
        notion_film_series_data = NotionSeriesData.from_dict(notion_film_series)
        # 映画視聴履歴をNotionから取得し、データクラスに変換
        notion_film_watch_history = self.film_watch_history_repository.get_film_watch_history()
        notion_film_watch_history_data = NotionWatchHistoryData.from_dict(notion_film_watch_history)
        # 視聴媒体をNotionから取得し、データクラスに変換
        notion_watch_media = self.watch_medium_repository.get_watch_media()
        notion_watch_media_data = NotionWatchMediumData.from_dict(notion_watch_media)

        film_records: list[FilmRecordEntity] = FilmRecordDto.from_notion_film_record_data2film_record_entity(
            notion_film_record=notion_film_record_data,
            notion_film_genre=notion_film_genres_data,
            notion_film_series=notion_film_series_data,
            notion_film_watch_history=notion_film_watch_history_data,
            notion_watch_media=notion_watch_media_data,
        )

        return film_records
