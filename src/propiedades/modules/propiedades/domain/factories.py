from dataclasses import dataclass

from propiedades.modules.propiedades.domain.rules import ValidPropiedad
from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.events import DomainEvent
from propiedades.seedwork.domain.factories import Factory
from propiedades.seedwork.domain.repositories import Mapper

from .entities import Propiedad
from .exceptions import InvalidPropiedadFactoryException


@dataclass
class _PropiedadFactory(Factory):

    def create(self, obj: any, mapper: Mapper = None) -> Propiedad:
        if isinstance(obj, Entity) or isinstance(obj, DomainEvent):
            return mapper.entity_to_dto(obj)

        propiedad: Propiedad = mapper.dto_to_entity(obj)
        self.validate_rule(ValidPropiedad(propiedad))
        return propiedad


@dataclass
class PropiedadFactory(Factory):
    def create(self, obj: any, mapper: Mapper) -> Propiedad:
        if mapper.type() == Propiedad.__class__:
            propiedad_factory = _PropiedadFactory()
            return propiedad_factory.create(obj, mapper)
        else:
            raise InvalidPropiedadFactoryException()
