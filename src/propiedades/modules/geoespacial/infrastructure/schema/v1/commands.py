import pulsar.schema as schema
from propiedades.seedwork.infrastructure.schema.v1.commands import \
    IntegrationCommand

class CoordenadaPayload(schema.Record):
    latitud = schema.Float()
    longitud = schema.Float()

class PoligonoPayload(schema.Record):
    coordenadas = schema.Array(array_type=CoordenadaPayload())

class DireccionesPayload(schema.Record):
    valor = schema.String()

class EdificiosPayload(schema.Record):
    poligono = PoligonoPayload()

class ComandoCrearLotePayload(schema.Record):
    correlation_id = schema.String()
    id_propiedad = schema.String()
    direcciones = schema.Array(array_type=DireccionesPayload())
    poligono = PoligonoPayload()
    edificios = schema.Array(array_type=EdificiosPayload())
    
class ComandoCrearLote(IntegrationCommand):
    data = ComandoCrearLotePayload()