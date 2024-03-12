from pydispatch import dispatcher

from propiedades.modules.contratos.domain.events import ContratoCreado

from .handlers import ContratoCreadoIntegrationMessageHandler

print("[Contratos] Consumiendo ContratoCreadoIntegracion")
dispatcher.connect(
    ContratoCreadoIntegrationMessageHandler.handle,
    signal=f"{ContratoCreado.__name__}Integracion",
)
