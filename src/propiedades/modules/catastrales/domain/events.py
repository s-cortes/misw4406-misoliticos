import datetime
import uuid
from attr import dataclass
from propiedades.seedwork.domain.events import DomainEvent


@dataclass
class InmuebleCreado(DomainEvent):
    id_inmueble: uuid.UUID = None
    fecha_creacion: datetime = None
