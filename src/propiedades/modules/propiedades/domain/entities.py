import uuid
from dataclasses import dataclass, field
import logging

import propiedades.modules.propiedades.domain.value_objects as vo
from propiedades.modules.propiedades.domain.events import (
    CreacionPropiedadSolicitada,
    PropiedadCreada,
)
from propiedades.seedwork.domain.entities import Entity, RootAggregation


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

    geoespacial: dict = field(default_factory=dict)
    catastral: dict = field(default_factory=dict)

    def create(self, correlation_id):
        self.append_event(
            PropiedadCreada(
                correlation_id=correlation_id,
                id_propiedad=self.id,
                fecha_creacion=self.fecha_creacion,
                geoespacial=self.geoespacial,
                catastral=self.catastral,
            )
        )

    def request(self):
        logging.error("[Propiedades] Agregando Evento")
        self.append_event(
            CreacionPropiedadSolicitada(
                id_propiedad=self.id,
                fecha_creacion=self.fecha_creacion,
                tipo_construccion=self.tipo_construccion,
                entidad=self.entidad,
                fotografias=self.fotografias,
                geoespacial=self.geoespacial,
                catastral=self.catastral,
            )
        )
