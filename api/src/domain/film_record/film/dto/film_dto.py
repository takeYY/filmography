# 標準ライブラリ
from datetime import date

# 独自ライブラリ
from src.domain.film_record.film import FilmEntity
from src.domain.film_record.film.genre import FilmGenreDTO
from src.domain.film_record.film.poster import FilmPosterObject
from src.domain.film_record.film.series import FilmSeriesObject


class FilmDto:
    """映画のデータトランスファーオブジェクト"""

    @staticmethod
    def from_json2_film_entity(json_data: dict) -> FilmEntity:
        result: dict = json_data.get("result", {})
        if not result:
            raise ValueError("resultがありません")

        series = result.get("series")
        if not series:
            film_series = None
        else:
            film_series = FilmSeriesObject(
                name=series.get("name", ""),
                poster=FilmPosterObject(
                    poster_url=series.get("poster", {}).get("poster_url", ""),
                ),
            )

        return FilmEntity(
            tmdb_id=result["tmdb_id"]["value"],
            title=result["title"],
            overview=result["overview"],
            release_date=date.fromisoformat(result["release_date"]),
            run_time=result["run_time"],
            series=film_series,
            poster=FilmPosterObject(
                poster_url=result.get("poster", {}).get("poster_url", ""),
            ),
            genres=FilmGenreDTO.from_list2film_genre_enum_set(
                genre_str_list=result.get("genres", []),
            ),
        )
