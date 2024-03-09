from propiedades.modules.catastrales.infrastructure.dispartchers import \
    InmuebleDispatcher
from propiedades.seedwork.application.handlers import Handler

class InmuebleCreadoIntegrationMessageHandler(Handler):

    @staticmethod
    def handle(event):
        dispatcher = InmuebleDispatcher(event)
        dispatcher.publish("inmueble-events")

