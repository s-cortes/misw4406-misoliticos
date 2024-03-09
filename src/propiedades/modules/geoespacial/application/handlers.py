from propiedades.modules.geoespacial.infrastructure.dispatchers import \
    LotesDispatcher
from propiedades.seedwork.application.handlers import Handler


class LoteCreadoIntegrationMessageHandler(Handler):

    @staticmethod
    def handle(event):
        dispatcher = LotesDispatcher(event)
        dispatcher.publish("propiedad-events")