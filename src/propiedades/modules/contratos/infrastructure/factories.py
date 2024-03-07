from dataclasses import dataclass

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