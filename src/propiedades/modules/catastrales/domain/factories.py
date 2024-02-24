from dataclasses import dataclass

from exceptions import InvalidCatastralFactoryException
from propiedades.modules.catastrales.domain.rules import ValidInmueble
from .entities import Inmueble, Oficina
from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.events import DomainEvent
from propiedades.seedwork.domain.factories import Factory
from propiedades.seedwork.domain.repositories import Mapper, Repository


@dataclass
class _InmuebleFactory(Factory):

    def create(self, obj: any, mapper: Mapper = None) -> any:
        if isinstance(obj, Entity) or isinstance(obj, DomainEvent):
            return mapper.entity_to_dto(obj)

        inmueble: Inmueble = mapper.dto_to_entity(obj)
        self.validate_rule(ValidInmueble(inmueble))

        return inmueble

@dataclass
class CatastralFactory(Factory):
    def create(self, obj: any, mapper: Mapper) -> any:
        if mapper.obtener_tipo() == Inmueble.__class__:
            inmueble_factory = _InmuebleFactory()
            return inmueble_factory.create(obj, mapper)
        else:
            raise InvalidCatastralFactoryException()
