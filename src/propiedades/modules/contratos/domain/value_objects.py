from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
from propiedades.seedwork.domain.value_object import ValueObject

class TipoContrato(str, Enum):
    ARRENDAMIENTO = "Arrendamiento"
    COMPRA = "Compra"

class Moneda(str, Enum):
    COP = "COP"
    ARS = "ARS"
    USD = "USD"
    EUR = "EUR"

class MetodoPago(Enum):
    EFECTIVO = "Efectivo"
    HIPOTECA = "Hipoteca"
    PERMUTA = "Permuta"
    HIBRIDO = "Hibrido"

@dataclass(frozen=True)
class ValorPago():
    valor: float

@dataclass(frozen=True)
class FechaInicio():
    fecha: datetime

@dataclass(frozen=True)
class FechaTerminacion():
    fecha: datetime