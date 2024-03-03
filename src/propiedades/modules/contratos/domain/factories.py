from dataclasses import dataclass

from .exceptions import InvalidContratoFactoryException
from propiedades.modules.contratos.domain.rules import ValidContrato
from .entities import Contrato
from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.events import DomainEvent
from propiedades.seedwork.domain.factories import Factory
from propiedades.seedwork.domain.repositories import Mapper


@dataclass
class _ContratoFactory(Factory):
    def create(self, obj: any, mapper: Mapper = None) -> any:
        if isinstance(obj, Entity) or isinstance(obj, DomainEvent):
            return mapper.entity_to_dto(obj)

        contrato: Contrato = mapper.dto_to_entity(obj)
        self.validate_rule(ValidContrato(Contrato))

        return contrato

@dataclass
class ContratoFactory(Factory):
    def create(self, obj: any, mapper: Mapper) -> any:
        if mapper.type() == Contrato.__class__:
            contrato_factory = _ContratoFactory()
            return contrato_factory.create(obj, mapper)
        else:
            raise InvalidContratoFactoryException()
