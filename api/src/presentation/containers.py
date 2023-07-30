# 外部ライブラリ
from dependency_injector import containers
from dependency_injector.providers import Factory

# 独自ライブラリ
from src.application.film_record.command.interface import IFilmRecordCommandApplication
from src.application.film_record.query.interface import IFilmRecordQueryApplication
from src.presentation.film_record.command import FilmRecordCommandContainer
from src.presentation.film_record.query import FilmRecordQueryContainer

# from src.application.jumanpp.jumanpp_application import JumanppApplication
# from src.presentation.jumanpp.jumanpp_container import JumanppContainer


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            # ".jumanpp.jumanpp_route",
            ".film_record.query.film_record_query_route",
            ".film_record.command.film_record_command_route",
        ]
    )

    # jumanpp_application: Factory[JumanppApplication] = JumanppContainer.jumanpp_application

    film_record_query_application: Factory[
        IFilmRecordQueryApplication
    ] = FilmRecordQueryContainer.film_record_query_application

    film_record_command_application: Factory[
        IFilmRecordCommandApplication
    ] = FilmRecordCommandContainer.film_record_command_application
