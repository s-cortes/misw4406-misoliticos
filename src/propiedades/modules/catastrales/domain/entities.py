import uuid
import propiedades.modules.catastrales.domain.value_objects as vo
from propiedades.seedwork.domain.entities import Entity, RootAggregation
from dataclasses import dataclass, field

@dataclass
class Oficina(Entity):
    area: vo.Area = field(default_factory=vo.Area)
    ubicacion: vo.UbicacionInterna = field(default_factory=vo.UbicacionInterna)

@dataclass
class Inmueble(RootAggregation):
    id: uuid.UUID = field(hash=True, default=None)
    pisos: list[vo.Piso] = field(default_factory=vo.Piso)
