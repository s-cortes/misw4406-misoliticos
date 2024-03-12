from pulsar.schema import *

from propiedades.seedwork.infrastructure.schema.v1.events import \
    IntegrationEvent


class LoteCreadoPayload(Record):
    id_lote = String()
    fecha_creacion = Long()
    id_propiedad = String()
    id_coorelacion = String()
    mensaje = String()


class EventoLoteCreado(IntegrationEvent):
    data = LoteCreadoPayload()
