from propiedades.modules.propiedades.infrastructure.dispartchers import \
    PropiedadDispatcher
from propiedades.seedwork.application.handlers import Handler


class PropiedadCreadaIntegrationMessageHandler(Handler):

    @staticmethod
    def handle(event):
        dispatcher = PropiedadDispatcher(event)
        dispatcher.publish("propiedad-events")
