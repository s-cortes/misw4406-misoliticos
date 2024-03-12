from pulsar.schema import *

from propiedades.seedwork.infrastructure.schema.v1.events import \
    IntegrationEvent


class PropiedadCreadaPayload(Record):
    correlation_id = String()
    id_propiedad = String()
    fecha_creacion = Long()


class PropiedadCreatedEvent(IntegrationEvent):
    data = PropiedadCreadaPayload()
