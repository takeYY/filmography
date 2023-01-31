from src.domain.film_record.film.genre.film_genre_dto import FilmGenreDTO
from src.domain.film_record.film.genre.film_genre_enum import FilmGenreEnum


class TestFilmGenreDto:
    def test_to_tmdb_genre_should_create_film_genre_enum(self):
        adventure = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=12)
        fantasy = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=14)
        animation = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=16)
        drama = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=18)
        horror = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=27)
        action = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=28)
        comedy = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=35)
        history = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=36)
        western = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=37)
        thriller = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=53)
        crime = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=80)
        documentary = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=99)
        sf = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=878)
        mystery = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=9648)
        music = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=10402)
        romance = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=10749)
        family = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=10751)
        war = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=10752)
        tv = FilmGenreDTO.from_tmdb_genre2film_genre_enum(tmdb_genre_id=10770)

        assert adventure == FilmGenreEnum.ADVENTURE
        assert fantasy == FilmGenreEnum.FANTASY
        assert animation == FilmGenreEnum.ANIMATION
        assert drama == FilmGenreEnum.DRAMA
        assert horror == FilmGenreEnum.HORROR
        assert action == FilmGenreEnum.ACTION
        assert comedy == FilmGenreEnum.COMEDY
        assert history == FilmGenreEnum.HISTORY
        assert western == FilmGenreEnum.WESTERN
        assert thriller == FilmGenreEnum.THRILLER
        assert crime == FilmGenreEnum.CRIME
        assert documentary == FilmGenreEnum.DOCUMENTARY
        assert sf == FilmGenreEnum.SF
        assert mystery == FilmGenreEnum.MYSTERY
        assert music == FilmGenreEnum.MUSIC
        assert romance == FilmGenreEnum.ROMANCE
        assert family == FilmGenreEnum.FAMILY
        assert war == FilmGenreEnum.WAR
        assert tv == FilmGenreEnum.TV
