from pulsar.schema import *
from dataclasses import dataclass, field
from propiedades.seedwork.infrastructure.schema.v1.commands import \
    IntegrationCommand


class ComandoCrearLotePayload(Record):
    id_propiedad = String()
    direcciones = String()
    poligono = String()
    edificios = String()



class EventoLoteCreado(IntegrationCommand):
    data = ComandoCrearLotePayload()