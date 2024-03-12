from pulsar.schema import *

from propiedades.seedwork.infrastructure.schema.v1.events import \
    IntegrationEvent


class LoteCreadoPayload(Record):
    correlation_id = String()
    id_lote = String()
    fecha_creacion = Long()
    id_propiedad = String()
    correlation_id = String()
    mensaje = String()


class EventoLoteCreado(IntegrationEvent):
    data = LoteCreadoPayload()
