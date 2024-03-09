import datetime

from propiedades.modules.catastrales.domain.events import InmuebleCreado
from propiedades.modules.catastrales.infrastructure.schema.v1.events import (
    EventoInmuebleCreado, InmuebleCreadoPayload
)
from propiedades.seedwork.infrastructure.schema.v1.mappers import \
    IntegrationMapper
from propiedades.seedwork.infrastructure.schema.v1.messages import IntegrationMessage

class EventoInmuebleCreadoMapper(IntegrationMapper):
    epoch = datetime.datetime.utcfromtimestamp(0)

    def _unix_time_millis(self, dt):
        return (dt - self.epoch).total_seconds() * 1000.0
    
    def external_to_message(self, external: InmuebleCreado) -> EventoInmuebleCreado:
        tiempo = int(self._unix_time_millis(external.fecha_creacion))
        payload: InmuebleCreadoPayload = InmuebleCreadoPayload(
            id_inmueble=str(external.id_inmueble),
            fecha_creacion=tiempo,
        )
        return EventoInmuebleCreado(data=payload)