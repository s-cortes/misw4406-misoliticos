import uuid
from dataclasses import dataclass, field

from propiedades.seedwork.domain.entities import Entity, RootAggregation
import propiedades.modules.geoespacial.domain.value_objects as vo

@dataclass
class Edificio(RootAggregation):
    id: uuid.UUID = field(hash=True, default=None)
    poligono: vo.Poligono = field(default_factory=vo.Poligono)
@dataclass
class Lote(Entity):
    id: uuid.UUID = field(hash=True, default=None)
    direccion: list[vo.Direccion] = field(default_factory=vo.Direccion)
    poligono: vo.Poligono = field(default_factory=vo.Poligono)
    edificio: list[Edificio] = field(default_factory=Edificio)
