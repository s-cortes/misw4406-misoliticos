from pulsar.schema import *
from dataclasses import dataclass, field
from propiedades.seedwork.infrastructure.schema.v1.commands import \
    IntegrationCommand


class CoordenadaPayload(Record):
    latitud: Float()
    longitud: Float()

class PoligonoPayload(Record):
    coordenadas = Array(array_type=CoordenadaPayload())

class DireccionesPayload(Record):
    valor = String()

class EdificiosPayload(Record):
    poligono = PoligonoPayload()

class ComandoCrearLotePayload(Record):
    id_propiedad = String()
    direcciones = Array(array_type=DireccionesPayload())
    poligono = PoligonoPayload()
    edificios = Array(array_type=EdificiosPayload())
    id_coorelacion = String()

class ComandoCrearLote(IntegrationCommand):
    data = ComandoCrearLotePayload()