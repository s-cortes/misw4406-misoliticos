from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
from propiedades.seedwork.domain.value_object import ValueObject

class TipoContrato(str, Enum):
    ARRENDAMIENTO = "Arrendamiento"
    COMPRA = "Compra"

@dataclass(frozen=True)
class FechaInicio():
    fecha: datetime

@dataclass(frozen=True)
class FechaTerminacion():
    fecha: datetime