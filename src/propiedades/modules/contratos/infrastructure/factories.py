from dataclasses import dataclass
from propiedades.modules.contratos.domain.events import ContratoCreado
from propiedades.modules.contratos.infrastructure.schema.mappers import EventoContratoCreadoMapper
from propiedades.seedwork.domain.factories import Factory
from propiedades.modules.contratos.domain.repositories import RepositorioContratos
from propiedades.modules.contratos.infrastructure.repositories import RepositorioContratosSQLite
from propiedades.modules.contratos.infrastructure.exceptions import InvalidRepositoryFactoryException

@dataclass
class RepositoryFactory(Factory):
    def create(self, obj: type):
        if obj == RepositorioContratos.__class__:
            return RepositorioContratosSQLite()
        else:
            raise InvalidRepositoryFactoryException

class IntegrationMessageFactory(Factory):
    def create(self, event: any) -> any:
        if type(event) is ContratoCreado:
            mapper = EventoContratoCreadoMapper()
            return mapper.external_to_message(event)
        else:
            print("[Contratos] Error en IntegrationMessageFactory")
            raise InvalidRepositoryFactoryException()
