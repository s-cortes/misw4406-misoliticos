from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
from propiedades.seedwork.domain.value_object import ValueObject

class TiposContrato(Enum):
    ARRENDAMIENTO = "Arrendamiento"
    COMPRA = "Compra"

class TipoMoneda(Enum):
    COP = "COP"
    ARS = "ARS"
    USD = "USD"
    EUR = "EUR"

class TipoMetodoPago(Enum):
    EFECTIVO = "Efectivo"
    HIPOTECA = "Hipoteca"
    PERMUTA = "Permuta"
    HIBRIDO = "Hibrido"

@dataclass(frozen=True)
class TipoContrato(ValueObject):
    tipo: TiposContrato

@dataclass(frozen=True)
class FechaInicio(ValueObject):
    fecha: datetime

@dataclass(frozen=True)
class FechaTerminacion(ValueObject):
    fecha: datetime

@dataclass(frozen=True)
class ValorPago(ValueObject):
    valor: float

@dataclass(frozen=True)
class Moneda(ValueObject):
    moneda: TipoMoneda

@dataclass(frozen=True)
class MetodoPago(ValueObject):
    metodo: TipoMetodoPago
