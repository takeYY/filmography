# 標準ライブラリ
import dataclasses

# 外部ライブラリ
import pytest

# 独自ライブラリ
from src.domain.film_record.appreciation import FilmAppreciationIdObject


class TestFilmAppreciationIdObject:
    @pytest.mark.parametrize(
        "value",
        [
            ("1"),
            ("144"),
            ("1024"),
        ],
    )
    def test_constructor_should_create_instance(self, value: str):
        film_appreciation_id_object = FilmAppreciationIdObject(value)

        assert film_appreciation_id_object.value == value

    @pytest.mark.parametrize(
        "value",
        [
            (False),
            (1024),
            (3.14),
        ],
    )
    def test_constructor_should_throw_value_error_when_params_are_invalid(self, value):
        with pytest.raises(ValueError):
            FilmAppreciationIdObject(value)

    def test_film_appreciation_id_object_should_be_frozen(self):
        with pytest.raises(dataclasses.FrozenInstanceError):
            film_appreciation_id_object = FilmAppreciationIdObject("1024")
            film_appreciation_id_object.value = "1"  # type: ignore
