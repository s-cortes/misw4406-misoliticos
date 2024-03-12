from dataclasses import dataclass, field
import datetime
import uuid

from propiedades.seedwork.domain.events import DomainEvent


@dataclass
class PropiedadCreada(DomainEvent):
    id_propiedad: uuid.UUID = None
    fecha_creacion: datetime = None

    geoespacial: dict = None
    catastral: dict = None


@dataclass
class CreacionPropiedadSolicitada(DomainEvent):
    id_propiedad: uuid.UUID = None
    fecha_creacion: datetime = None
    tipo_construccion: str = None
    entidad: str = None
    fotografias: list = None
    geoespacial: dict = None
    catastral: dict = None

class CreacionPropiedadRecibida(DomainEvent):
    id_propiedad: uuid.UUID = None
    fecha_creacion: datetime = None
    tipo_construccion: str = None
    entidad: str = None
    fotografias: list = None
    geoespacial: dict = None
    catastral: dict = None
