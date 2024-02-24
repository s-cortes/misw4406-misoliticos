
from dataclasses import dataclass, field
from propiedades.seedwork.domain.value_object import ValueObject


@dataclass(frozen=True)
class UbicacionInterna(ValueObject):
    nombre: str
    division_visible: str
    telefono: str


@dataclass(frozen=True)
class Area(ValueObject):
    valor: float
    unidad: str

