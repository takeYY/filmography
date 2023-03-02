from src.data_model.notion.genre.notion_genre_data import NotionGenreData
from src.data_model.notion.relation.notion_relation_data import NotionRelationIdData
from src.domain.film_record.film.genre.film_genre_enum import FilmGenreEnum


class FilmGenreDTO:
    """映画ジャンルに関するデータトランスファーオブジェクト"""

    tmdb_genre_id: int

    @staticmethod
    def from_tmdb_genre2film_genre_enum(tmdb_genre_id: int) -> FilmGenreEnum:
        """TMDb のジャンルIDを映画記録のジャンル名に変換する"""
        tmdb_genre_mapping = {
            "12": "ADVENTURE",
            "14": "FANTASY",
            "16": "ANIMATION",
            "18": "DRAMA",
            "27": "HORROR",
            "28": "ACTION",
            "35": "COMEDY",
            "36": "HISTORY",
            "37": "WESTERN",
            "53": "THRILLER",
            "80": "CRIME",
            "99": "DOCUMENTARY",
            "878": "SF",
            "9648": "MYSTERY",
            "10402": "MUSIC",
            "10749": "ROMANCE",
            "10751": "FAMILY",
            "10752": "WAR",
            "10770": "TV",
        }
        genre = tmdb_genre_mapping.get(str(tmdb_genre_id))

        if not genre:
            raise ValueError("ジャンルが存在しません.")

        return FilmGenreEnum[genre]

    @staticmethod
    def from_notion_relation_id2film_genre_enum_set(
        notion_film_genre: NotionGenreData,
        notion_relations: list[NotionRelationIdData],
    ) -> set[FilmGenreEnum]:
        film_genre_enum_set: set[FilmGenreEnum] = set()
        for notion_relation in notion_relations:
            tmdb_genre_id = notion_film_genre.get_tmdb_genre_id(relation_id=notion_relation.id)
            film_genre_enum: FilmGenreEnum = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=tmdb_genre_id)
            film_genre_enum_set.add(film_genre_enum)

        return film_genre_enum_set
