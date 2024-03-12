from propiedades.modules.contratos.infrastructure.dispatchers import \
    ContratoDispatcher
from propiedades.seedwork.application.handlers import Handler


class ContratoCreadoIntegrationMessageHandler(Handler):

    @staticmethod
    def handle(event):
        dispatcher = ContratoDispatcher(event)
        dispatcher.publish("contrato-events")
