import pulsar.schema as schema
from propiedades.modules.geoespacial.infrastructure.schema.v1.commands import ComandoCrearLotePayload

from propiedades.seedwork.infrastructure.schema.v1.commands import \
    IntegrationCommand


class ContenidoPayload(schema.Record):
    valor = schema.String()
    tipo = schema.String()

class FotografiaPayload(schema.Record):
    contenido = ContenidoPayload()
    descripcion = schema.String()
    nombre = schema.String()


class CreatePropiedadPayload(schema.Record):
    id = schema.String()
    fecha_creacion = schema.Long()

    tipo_construccion = schema.String()
    entidad = schema.String()
    fotografias = schema.Array(array_type=FotografiaPayload())
    geoespacial = ComandoCrearLotePayload()

class PropiedadCreateCommand(IntegrationCommand):
    data = CreatePropiedadPayload()
