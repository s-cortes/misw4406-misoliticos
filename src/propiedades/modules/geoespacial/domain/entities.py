import uuid
from dataclasses import dataclass, field
from propiedades.modules.geoespacial.domain.events import LoteCreado
from propiedades.seedwork.domain.entities import Entity, RootAggregation
import propiedades.modules.geoespacial.domain.value_objects as vo

@dataclass
class Edificio(Entity):
    poligono: vo.Poligono = field(default_factory=vo.Poligono)
@dataclass
class Lote(RootAggregation):
    direccion: list[vo.Direccion] = field(default_factory=vo.Direccion)
    poligono: vo.Poligono = field(default_factory=vo.Poligono)
    edificio: list[Edificio] = field(default_factory=Edificio)
    id_propiedad: str = field(default_factory=str)
    id_coorelacion: str = field(default_factory=str)

    def create(self):
        self.append_event(
            LoteCreado(
                id_lote=self.id,
                id_propiedad=self.id_propiedad,
                id_coorelacion=self.id_coorelacion,
            )
        )
