from dataclasses import dataclass
import datetime
import uuid

from propiedades.seedwork.domain.events import DomainEvent


@dataclass
class LoteCreado(DomainEvent):
    id_lote: uuid.UUID = None
    fecha_creacion: datetime = None
    id_propiedad: str = None
    correlation_id: str = None
    mensaje : str = None

@dataclass
class CreacionLoteFallida(DomainEvent):
    fecha_creacion: datetime = None
    id_propiedad: uuid.UUID = None

"""@dataclass
class ComandoCrearLote(DomainEvent):
    pass"""
