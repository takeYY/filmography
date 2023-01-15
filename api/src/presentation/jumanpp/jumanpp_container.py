from dependency_injector.providers import Factory
from src.application.jumanpp.jumanpp_application import ImplJumanppApplication, JumanppApplication


class JumanppContainer:
    jumanpp_application: Factory[JumanppApplication] = Factory(
        ImplJumanppApplication,
    )
