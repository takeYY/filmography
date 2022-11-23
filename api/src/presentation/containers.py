from dependency_injector import containers
from src.application.jumanpp.jumanpp_application import JumanppApplication
from src.application.movie.query.movie_query_application import IMovieQueryApplication
from src.presentation.jumanpp.jumanpp_container import JumanppContainer
from src.presentation.movie.query.movie_query_container import MovieQueryContainer


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            ".jumanpp.jumanpp_route",
            ".movie.query.movie_query_route",
        ]
    )

    jumanpp_application: JumanppApplication = JumanppContainer.jumanpp_application
    movie_query_application: IMovieQueryApplication = MovieQueryContainer.movie_query_application
