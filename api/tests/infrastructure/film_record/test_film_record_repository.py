# 標準ライブラリ
from datetime import date

# 外部ライブラリ
import pytest

# 独自ライブラリ
from src.domain.film_record import FilmRecordEntity, FilmRecordIdObject
from src.domain.film_record.appreciation import AppreciationStatusEnum, FilmAppreciationEntity, FilmAppreciationIdObject
from src.domain.film_record.film import FilmEntity, TmdbIdObject
from src.domain.film_record.film.genre import FilmGenreEnum
from src.domain.film_record.film.poster import FilmPosterObject
from src.domain.film_record.film.series import FilmSeriesObject
from src.domain.film_record.watch_medium import WatchMediumEnum


class TestFilmRecordRepository:
    @pytest.fixture
    def init_film_record(self):
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
                    film_appreciation_id=FilmAppreciationIdObject(value="1"),
                    medium=WatchMediumEnum.AMAZON_PRIME_VIDEO,
                    appreciation_date=date(2020, 1, 1),
                ),
                FilmAppreciationEntity(
                    film_appreciation_id=FilmAppreciationIdObject(value="2"),
                    medium=WatchMediumEnum.U_NEXT,
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

    def test_find_by_id(self, init_film_record):
        target_id = "1"
        film_record_id_object: FilmRecordIdObject = FilmRecordIdObject(target_id)

        is_found = False
        for idx, film_record in enumerate(self.film_records, start=1):
            if film_record.film_record_id == film_record_id_object:
                is_found = True
                assert str(idx) == target_id
                expected_target_id = int(target_id) - 1
                break

        assert is_found is True
        assert film_record.film_record_id == self.film_records[expected_target_id].film_record_id  # type: ignore
        assert (
            film_record.appreciation_status == self.film_records[expected_target_id].appreciation_status  # type: ignore
        )
        assert film_record.note == self.film_records[expected_target_id].note  # type: ignore
        assert film_record.film == self.film_records[expected_target_id].film  # type: ignore
        assert film_record.evaluation == self.film_records[expected_target_id].evaluation  # type: ignore
        assert (
            film_record.film_appreciations == self.film_records[expected_target_id].film_appreciations  # type: ignore
        )

    def test_create(self, init_film_record):
        new_film_record = FilmRecordEntity(
            film_record_id=FilmRecordIdObject("3"),
            appreciation_status=AppreciationStatusEnum.WATCHED,
            note="家政婦は三田",
            film=FilmEntity(
                tmdb_id=TmdbIdObject(296),
                title="ターミネーター3",
                overview="スカイネットを破壊、予見されていた最終戦争の日も過ぎたが、ジョンの心には...",
                release_date=date(2003, 7, 12),
                run_time=110,
                series=FilmSeriesObject(
                    name="ターミネーターシリーズ",
                    poster=FilmPosterObject(
                        poster_url="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg",
                    ),
                ),
                poster=FilmPosterObject(poster_url="/oaA02LgAPk9SAMBfEEiGNbEnaAk.jpg"),
                genres=set(
                    [
                        FilmGenreEnum.ACTION,
                        FilmGenreEnum.THRILLER,
                        FilmGenreEnum.SF,
                    ]
                ),
            ),
            evaluation=4,
            film_appreciations=[
                FilmAppreciationEntity(
                    film_appreciation_id=FilmAppreciationIdObject("3"),
                    medium=WatchMediumEnum.AMAZON_PRIME_VIDEO,
                    appreciation_date=date(2020, 3, 1),
                )
            ],
        )
        self.film_records.append(new_film_record)
        terminator3 = self.film_records[2]

        assert len(self.film_records) == 3
        assert terminator3 == new_film_record
