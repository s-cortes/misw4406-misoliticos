from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infrastructure.schema.v1.comands import CommandIntegration

class ComandCreateConsultaPayload(CommandIntegration):
    id_inmueble = String()
    id_usuario = String()
    fecha_consulta= Date()

class ComandCreateConsulta(CommandIntegration):
    data = ComandCreateConsultaPayload