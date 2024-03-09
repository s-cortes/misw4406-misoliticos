from dataclasses import dataclass

from propiedades.modules.geoespacial.infrastructure.schema.v1.mappers import \
    EventoLoteCreadoMapper
from propiedades.seedwork.domain.factories import Factory
from propiedades.modules.geoespacial.domain.repositories import RepositorioLotes
from propiedades.modules.geoespacial.infrastructure.repositories import RepositorioLotesSQLite
from propiedades.modules.geoespacial.infrastructure.exceptions import InvalidRepositoryFactoryException

@dataclass
class RepositoryFactory(Factory):
    def create(self, obj: type):
        if obj == RepositorioLotes.__class__:
            return RepositorioLotesSQLite()
        else:
            raise InvalidRepositoryFactoryException

class IntegrationMessageFactory(Factory):
    def create(self, event: any) -> any:
        if type(event) is LoteCreado:
            mapper = EventoPropiedadCreadaMapper()
            return mapper.external_to_message(event)
        else:
            print("[Propiedades] Error en IntegrationMessageFactory")
            raise InvalidRepositoryFactoryException()