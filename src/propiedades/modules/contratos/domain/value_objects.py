from enum import Enum
from dataclasses import dataclass, field
from propiedades.seedwork.domain.value_object import ValueObject

class TipoContrato(str, Enum):
    ARRENDAMIENTO = "Arrendamiento"
    COMPRA = "Compra"