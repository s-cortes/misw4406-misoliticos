from pulsar.schema import *

from propiedades.seedwork.infrastructure.schema.v1.events import \
    IntegrationEvent


class InmuebleCreadoPayload(Record):
    id_inmueble = String()
    fecha_creacion = long()

class EventoInmuebleCreado(IntegrationEvent):
    data = InmuebleCreadoPayload()
