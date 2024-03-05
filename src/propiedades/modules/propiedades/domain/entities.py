from dataclasses import dataclass, field
import uuid
from propiedades.modules.propiedades.domain.events import PropiedadCreada

from propiedades.seedwork.domain.entities import Entity, RootAggregation
import propiedades.modules.propiedades.domain.value_objects as vo


@dataclass
class Fotografia(Entity):
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    contenido: vo.Contenido = field(default_factory=vo.Contenido)


@dataclass
class Propiedad(RootAggregation):
    tipo_construccion: vo.TipoContruccion = field(default_factory=vo.TipoContruccion)
    entidad: vo.Entidad = field(default_factory=vo.Entidad)
    fotografias: list[Fotografia] = field(default_factory=list[Fotografia])

    def create(self):
        self.append_event(
            PropiedadCreada(id_propiedad=self.id, fecha_creacion=self.fecha_creacion)
        )
