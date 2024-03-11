from propiedades.modules.propiedades.infrastructure.dispartchers import (
    PropiedadCommandDispatcher,
    PropiedadEventDispatcher,
)
from propiedades.seedwork.application.handlers import Handler


class PropiedadCreadaIntegrationMessageHandler(Handler):

    @staticmethod
    def handle(event):
        dispatcher = PropiedadEventDispatcher(event)
        dispatcher.publish("propiedades-events")


class PropiedadCommandMessageHandler(Handler):

    @staticmethod
    def handle(event):
        dispatcher = PropiedadCommandDispatcher(event)
        dispatcher.publish("propiedades-commands")
