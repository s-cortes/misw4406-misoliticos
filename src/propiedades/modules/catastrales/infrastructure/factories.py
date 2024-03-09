from dataclasses import dataclass

from propiedades.seedwork.domain.factories import Factory
from propiedades.seedwork.domain.repositories import Mapper
from propiedades.seedwork.infrastructure.schema.v1.mappers import \
    IntegrationMapper
from propiedades.modules.catastrales.domain.repositories import \
    RepositorioInmuebles
from propiedades.modules.catastrales.infrastructure.repositories import RepositorioInmueblesSQLite
from propiedades.modules.catastrales.infrastructure.exceptions import InvalidRepositoryFactoryException
from propiedades.modules.catastrales.domain.events import InmuebleCreado
from propiedades.modules.catastrales.infrastructure.schema.v1.mapper import \
    EventoInmuebleCreadoMapper

@dataclass
class RepositoryFactory(Factory):
    def create(self, obj: type):
        if obj == RepositorioInmuebles.__class__:
            return RepositorioInmueblesSQLite()
        else:
            raise InvalidRepositoryFactoryException
        
class IntegrationMessageFactory(Factory):
    def create(self, event: any) -> any:
        if type(event) is InmuebleCreado:
            mapper = EventoInmuebleCreadoMapper()
            return mapper.external_to_message(event)
        else:
            print("[Propiedades] Error en IntegrationMessageFactory")
            raise InvalidRepositoryFactoryException()