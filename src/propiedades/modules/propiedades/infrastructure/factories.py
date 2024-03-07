from dataclasses import dataclass

from propiedades.modules.propiedades.domain.events import PropiedadCreada
from propiedades.modules.propiedades.domain.repositories import \
    PropiedadesRepository
from propiedades.modules.propiedades.infrastructure.exceptions import \
    InvalidRepositoryFactoryException
from propiedades.modules.propiedades.infrastructure.repositories import \
    PropiedadesRepositorySQLite
from propiedades.modules.propiedades.infrastructure.schema.v1.mappers import \
    PropiedadCreatedEventMapper
from propiedades.seedwork.domain.factories import Factory
from propiedades.seedwork.domain.repositories import Mapper
from propiedades.seedwork.infrastructure.schema.v1.mappers import \
    IntegrationMapper


@dataclass
class RepositoryFactory(Factory):
    def create(self, obj: type):
        if obj == PropiedadesRepository.__class__:
            return PropiedadesRepositorySQLite()
        else:
            raise InvalidRepositoryFactoryException


class IntegrationMessageFactory(Factory):
    def create(self, event: any) -> any:
        if type(event) is PropiedadCreada:
            mapper = PropiedadCreatedEventMapper()
            return mapper.external_to_message(event)
        else:
            print("[Propiedades] Error en IntegrationMessageFactory")
            raise InvalidRepositoryFactoryException()
