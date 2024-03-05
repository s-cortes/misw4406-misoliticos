from pydispatch import dispatcher

from propiedades.modules.propiedades.domain.events import PropiedadCreada

from .handlers import PropiedadCreadaIntegrationMessageHandler

print("[Propiedades] Consumiendo PropiedadCreadaIntegracion")
dispatcher.connect(
    PropiedadCreadaIntegrationMessageHandler.handle,
    signal=f"{PropiedadCreada.__name__}Integracion",
)
