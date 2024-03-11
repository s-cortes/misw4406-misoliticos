from pydispatch import dispatcher

from propiedades.modules.propiedades.domain.events import CreacionPropiedadSolicitada, PropiedadCreada

from .handlers import PropiedadCommandMessageHandler, PropiedadCreadaIntegrationMessageHandler


dispatcher.connect(
    PropiedadCreadaIntegrationMessageHandler.handle,
    signal=f"{PropiedadCreada.__name__}Integracion",
)

dispatcher.connect(
    PropiedadCommandMessageHandler.handle,
    signal=f"{CreacionPropiedadSolicitada.__name__}Domain",
)