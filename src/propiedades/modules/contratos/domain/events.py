import datetime
import uuid
from dataclasses import dataclass
from propiedades.seedwork.domain.events import DomainEvent


@dataclass
class ContratoCreado(DomainEvent):
    id_contrato: uuid.UUID = None
    fecha_creacion: datetime = None
