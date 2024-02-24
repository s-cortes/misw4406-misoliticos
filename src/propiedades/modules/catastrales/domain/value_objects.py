
from dataclasses import dataclass, field
import propiedades.modules.catastrales.domain.entities as ent
from propiedades.seedwork.domain.value_object import ValueObject


@dataclass(frozen=True)
class Piso(ValueObject):
    oficinas: list[ent.Oficina] = field(default_factory=ent.Oficina)


@dataclass(frozen=True)
class UbicacionInterna(ValueObject):
    nombre: str
    division_visible: str
    telefono: str


@dataclass(frozen=True)
class Area(ValueObject):
    valor: float
    unidad: str

