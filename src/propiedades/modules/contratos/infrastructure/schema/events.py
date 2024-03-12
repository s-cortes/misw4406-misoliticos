from pulsar.schema import *

from propiedades.seedwork.infrastructure.schema.v1.events import IntegrationEvent


class ContratoCreadoPayload(Record):
    id_contrato = String()
    fecha_creacion = Long()


class EventoContratoCreado(IntegrationEvent):
    data = ContratoCreadoPayload()
