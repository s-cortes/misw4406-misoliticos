from dataclasses import dataclass

from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.events import DomainEvent
from propiedades.seedwork.domain.factories import Factory
from propiedades.seedwork.domain.repositories import Mapper, Repository

from propiedades.modules.geoespacial.domain.exceptions import InvalidGeoespacialFactoryException
#from propiedades.modules.geoespacial.domain.rules import ValidLote
from propiedades.modules.geoespacial.domain.entities import Lote


@dataclass
class _LoteFactory(Factory):
    def create(self, obj:any, mapper:Mapper = None) -> any:
        if isinstance(obj, Entity) or isinstance(obj, DomainEvent):
            return mapper.entity_to_dto(obj)
        
        lote: Lote = mapper.dto_to_entity(obj)
        #self.validate_rules(ValidLote(lote))
        print("fa:" + str(lote))
        return lote

@dataclass
class GeoespacialFactory(Factory):
    def create(self, obj:any, mapper: Mapper) -> any:
        if mapper.type() == Lote.__class__:
            lote_factory = _LoteFactory()
            return lote_factory.create(obj, mapper)
        else:
            raise InvalidGeoespacialFactoryException()