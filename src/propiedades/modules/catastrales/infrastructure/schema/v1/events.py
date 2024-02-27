from pulsar.schema import *
from seedwork.infrastructure.schema.v1.events import EventIntegration

class ConsultaCreadaPayload(Record):
    fecha_creacion = String()
    id = String()
    oficinas = Array(str)

class EventConsultaCreada(EventIntegration):
    data = ConsultaCreadaPayload