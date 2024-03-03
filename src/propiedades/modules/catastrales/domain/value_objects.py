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

@dataclass(frozen=True)
class Oficina(ValueObject):
    ubicacion: UbicacionInterna = field(default_factory=UbicacionInterna)
    area: Area = field(default_factory=Area)

@dataclass(frozen=True)
class Piso(ValueObject):
    oficinas: list[Oficina] = field(default_factory=Oficina)
