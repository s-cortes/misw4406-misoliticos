from dataclasses import dataclass

from propiedades.seedwork.domain.factories import Factory
from propiedades.modules.contratos.domain.repositories import RepositorioInmuebles
from propiedades.modules.contratos.infrastructure.repositories import RepositorioInmueblesSQLite
from propiedades.modules.contratos.infrastructure.exceptions import InvalidRepositoryFactoryException

@dataclass
class RepositoryFactory(Factory):
    def create(self, obj: type):
        if obj == RepositorioInmuebles.__class__:
            return RepositorioInmueblesSQLite()
        else:
            raise InvalidRepositoryFactoryException