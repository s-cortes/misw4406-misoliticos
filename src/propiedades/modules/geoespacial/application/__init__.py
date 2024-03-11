from pydispatch import dispatcher

from propiedades.modules.geoespacial.domain.events import LoteCreado

from .handlers import LoteCreadoIntegrationMessageHandler, LoteCreadoIntegrationCommandsHandler

print("[Propiedades] Consumiendo LoteCreadoIntegracion")
dispatcher.connect(
    LoteCreadoIntegrationMessageHandler.handle,
    signal=f"{LoteCreado.__name__}Integracion",
)

dispatcher.connect(
    LoteCreadoIntegrationCommandsHandler.handle,
    signal=f"{LoteCreado.__name__}Integracion",
)