import datetime

from propiedades.modules.propiedades.domain.events import PropiedadCreada
from propiedades.modules.propiedades.infrastructure.schema.v1.events import (
    PropiedadCreatedEvent, PropiedadCreadaPayload)
from propiedades.seedwork.infrastructure.schema.v1.mappers import \
    IntegrationMapper


class PropiedadCreatedEventMapper(IntegrationMapper):
    epoch = datetime.datetime.utcfromtimestamp(0)

    def _unix_time_millis(self, dt):
        return (dt - self.epoch).total_seconds() * 1000.0

    def external_to_message(self, external: PropiedadCreada) -> PropiedadCreatedEvent:
        tiempo = int(self._unix_time_millis(external.fecha_creacion))
        payload: PropiedadCreadaPayload = PropiedadCreadaPayload(
            id_propiedad=str(external.id_propiedad),
            fecha_creacion=tiempo,
        )
        return PropiedadCreatedEvent(data=payload)
