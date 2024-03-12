from pydispatch import dispatcher

from propiedades.modules.geoespacial.domain.events import LoteCreado

from .handlers import LoteCreadoIntegrationMessageHandler

print("[Propiedades] Consumiendo LoteCreadoIntegracion")
dispatcher.connect(
    LoteCreadoIntegrationMessageHandler.handle,
    signal=f"{LoteCreado.__name__}Integracion",
)