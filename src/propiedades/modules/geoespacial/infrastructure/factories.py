from dataclasses import dataclass

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