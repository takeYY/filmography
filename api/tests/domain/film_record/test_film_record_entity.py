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


class TestFilmRecordEntity:
    @pytest.fixture
    def init_film_series(self):
        """映画シリーズのテストデータ生成"""

        self.terminator_series = FilmSeriesObject(
            name="ターミネーターシリーズ",
            poster=FilmPosterObject(
                poster_url="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg",
            ),
        )

    @pytest.fixture
    def init_film_record_with_appreciations(self, init_film_series):
        """鑑賞データがある映画記録のテストデータを生成"""

        # 『ターミネーター』の映画記録を作成
        self.terminator_record = FilmRecordEntity(
            film_record_id=FilmRecordIdObject(value="1"),
            appreciation_status=AppreciationStatusEnum.WATCHED,
            note="あれやこれや",
            film=FilmEntity(
                tmdb_id=TmdbIdObject(value=218),
                title="ターミネーター",
                overview="アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる...",
                release_date=date(1985, 5, 4),
                run_time=108,
                series=self.terminator_series,
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

    @pytest.fixture
    def init_film_record_without_appreciations(self, init_film_series):
        """鑑賞データがない映画記録のテストデータを生成"""

        # 『ターミネーター2』の映画記録を作成
        self.terminator2_record = FilmRecordEntity(
            film_record_id=FilmRecordIdObject(value="2"),
            appreciation_status=AppreciationStatusEnum.NOT_WATCHED,
            note="評価高いから観たいな〜♪",
            film=FilmEntity(
                tmdb_id=TmdbIdObject(value=280),
                title="ターミネーター2",
                overview="未来からの抹殺兵器ターミネーターを破壊し...",
                release_date=date(1991, 8, 24),
                run_time=137,
                series=self.terminator_series,
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
            film_appreciations=[
                FilmAppreciationEntity(
                    film_appreciation_id=FilmAppreciationIdObject(value="2"),
                    medium=WatchMediumEnum.U_NEXT,
                    appreciation_date=date(2020, 2, 1),
                ),
            ],
        )

    def test_constructor_should_create_instance(self, init_film_record_with_appreciations):
        """インスタンス生成テスト"""
        assert self.terminator_record.get_film_record_id_object() == FilmRecordIdObject("1")
        assert self.terminator_record.get_appreciation_status() == AppreciationStatusEnum.WATCHED
        assert self.terminator_record.get_note() == "あれやこれや"
        assert self.terminator_record.get_film_tmdb_id_object() == TmdbIdObject(218)
        assert self.terminator_record.get_film_title() == "ターミネーター"
        assert self.terminator_record.get_film_overview() == "アメリカのとある街、深夜突如奇怪な放電と共に屈強な肉体をもった男が現れる..."
        assert self.terminator_record.get_film_release_date() == date(1985, 5, 4)
        assert self.terminator_record.get_film_run_time() == 108
        assert self.terminator_record.get_film_series_object() == FilmSeriesObject(
            name="ターミネーターシリーズ",
            poster=FilmPosterObject(
                poster_url="/kpZxdNsAV7qTdTLwKM5NLqa7GEo.jpg",
            ),
        )
        assert self.terminator_record.get_film_poster_object() == FilmPosterObject(
            poster_url="/tAB6R81LkJjUMCS8aMFwt2CM2vS.jpg",
        )
        assert self.terminator_record.get_film_genres() == set(
            [
                FilmGenreEnum.ACTION,
                FilmGenreEnum.THRILLER,
                FilmGenreEnum.SF,
            ]
        )
        assert self.terminator_record.get_evaluation() == 5
        assert self.terminator_record.get_film_appreciations()[0] == FilmAppreciationEntity(
            film_appreciation_id=FilmAppreciationIdObject(value="1"),
            medium=WatchMediumEnum.AMAZON_PRIME_VIDEO,
            appreciation_date=date(2020, 1, 1),
        )
        assert self.terminator_record.get_film_appreciations()[1] == FilmAppreciationEntity(
            film_appreciation_id=FilmAppreciationIdObject(value="2"),
            medium=WatchMediumEnum.U_NEXT,
            appreciation_date=date(2020, 2, 1),
        )

    def test_not_watched_record(self, init_film_record_without_appreciations):
        """未鑑賞の映画記録テスト

        evaluationとfilm_appreciationsがデフォルト値になっていること
        """

        assert self.terminator2_record.get_evaluation() == 0
        assert self.terminator2_record.get_film_appreciations() == []
