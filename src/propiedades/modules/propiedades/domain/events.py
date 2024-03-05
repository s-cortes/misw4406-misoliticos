from dataclasses import dataclass
import datetime
import uuid

from propiedades.seedwork.domain.events import DomainEvent


@dataclass
class PropiedadCreada(DomainEvent):
    id_propiedad: uuid.UUID = None
    fecha_creacion: datetime = None
