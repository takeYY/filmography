import os
from datetime import date
from logging import getLogger

from notion_client import Client
from src.domain.film_record.appreciation.appreciation_status_enum import AppreciationStatusEnum
from src.domain.film_record.appreciation.film_appreciation_entity import FilmAppreciationEntity
from src.domain.film_record.appreciation.film_appreciation_id_object import FilmAppreciationIdObject
from src.domain.film_record.film.film_entity import FilmEntity
from src.domain.film_record.film.genre.film_genre_enum import FilmGenreEnum
from src.domain.film_record.film.poster.film_poster_object import FilmPosterObject
from src.domain.film_record.film.series.film_series_object import FilmSeriesObject
from src.domain.film_record.film.tmdb_id_object import TmdbIdObject
from src.domain.film_record.film_record_entity import FilmRecordEntity
from src.domain.film_record.film_record_id_object import FilmRecordIdObject
from src.domain.film_record.film_record_repository import IFilmRecordRepository

logger = getLogger(__name__)


class ImplInmemoryFilmRecordRepository(IFilmRecordRepository):
    def __init__(self) -> None:
        logger.info("【inmemory】映画記録の初期化処理")

        # シリーズ作成
        terminator_series = FilmSeriesObject(
            name="ターミネーターシリーズ",
            poster=FilmPosterObject(
                poster_url="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg",
            ),
        )
        # 『ターミネーター』の映画記録を作成
        terminator_record = FilmRecordEntity(
            film_record_id=FilmRecordIdObject(value="1"),
            appreciation_status=AppreciationStatusEnum.WATCHED,
            note="あれやこれや",
            film=FilmEntity(
                tmdb_id=TmdbIdObject(value=218),
                title="ターミネーター",
                overview="アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる...",
                release_date=date(1985, 5, 4),
                run_time=108,
                series=terminator_series,
                poster=FilmPosterObject(
                    poster_url="/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg",
                ),
                genres=set(
                    [
                        FilmGenreEnum.ACTION,
                        FilmGenreEnum.THRILLER,
                        FilmGenreEnum.SF,
                    ]
                ),
            ),
            evaluation=5,
            film_appreciations=[
                FilmAppreciationEntity(
                    film_appreciation_id=FilmAppreciationIdObject(value=1),
                    medium="Amazon Prime Video",
                    appreciation_date=date(2020, 1, 1),
                ),
                FilmAppreciationEntity(
                    film_appreciation_id=FilmAppreciationIdObject(value=2),
                    medium="U-NEXT",
                    appreciation_date=date(2020, 2, 1),
                ),
            ],
        )
        # 『ターミネーター2』の映画記録を作成
        terminator2_record = FilmRecordEntity(
            film_record_id=FilmRecordIdObject(value="2"),
            appreciation_status=AppreciationStatusEnum.NOT_WATCHED,
            note="評価高いから観たいな〜♪",
            film=FilmEntity(
                tmdb_id=TmdbIdObject(value=280),
                title="ターミネーター2",
                overview="未来からの抹殺兵器ターミネーターを破壊し...",
                release_date=date(1991, 8, 24),
                run_time=137,
                series=terminator_series,
                poster=FilmPosterObject(
                    poster_url="/ghKQ6it5j7KjdYghT5EDthVNXlD.jpg",
                ),
                genres=set(
                    [
                        FilmGenreEnum.ACTION,
                        FilmGenreEnum.THRILLER,
                        FilmGenreEnum.SF,
                    ]
                ),
            ),
            evaluation=5,
            film_appreciations=[],
        )

        self.film_records: list[FilmRecordEntity] = [terminator_record, terminator2_record]

    def find_by_id(self, id: FilmRecordIdObject) -> FilmRecordEntity | None:
        logger.info(f"【inmemory】{id}に合致する映画記録を検索します")

        for film_record in self.film_records:
            if film_record.film_record_id == id:
                logger.info(f"映画記録が見つかりました. {film_record}")
                return film_record

        logger.warning(f"映画記録が見つかりませんでした. {id=}")
        return None

    def get_film_records(self):
        # Notionの設定
        notion_token = os.environ["NOTION_TOKEN"]
        self.notion = Client(auth=notion_token)
        self.div_film_record_id: str = os.environ["DEV_FILM_RECORD_DB_ID"]

        query: dict[str, str] = dict(database_id=self.div_film_record_id)
        return self.notion.databases.query(**query)

    def create(self, film_record: FilmRecordEntity) -> FilmRecordEntity:
        logger.info("【inmemory】映画記録を作成: 開始")
        self.film_records.append(film_record)
        logger.info("【inmemory】映画記録を作成: 終了")

        return film_record

    def update(
        self,
        film_record_id: FilmRecordIdObject,
        film_record: FilmRecordEntity,
    ) -> FilmRecordEntity | None:
        logger.info(f"【inmemory】{film_record_id}の映画記録を更新します")

        for idx, film_record in enumerate(self.film_records):
            if film_record.get_film_record_id_object() == film_record_id:
                self.film_records[idx] = film_record
                return film_record

        logger.warning(f"映画記録が見つかりませんでした. {film_record_id=}")
        return None
