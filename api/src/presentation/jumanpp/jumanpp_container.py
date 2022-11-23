from dependency_injector import providers
from src.application.jumanpp.jumanpp_application import ImplJumanppApplication, JumanppApplication


class JumanppContainer:
    jumanpp_application: JumanppApplication = providers.Factory(
        ImplJumanppApplication,
    )
