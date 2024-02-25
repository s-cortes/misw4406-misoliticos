from dataclasses import dataclass

from propiedades.seedwork.domain.factories import Factory
from propiedades.modules.catastrales.domain.repositories import RepositorioInmuebles
from propiedades.modules.catastrales.infrastructure.repositories import RepositorioInmueblesSQLite

@dataclass
class RepositoryFactory(Factory):
    def crear_objeto(self, obj: type):
        if obj == RepositorioInmuebles.__class__:
            return RepositorioInmueblesSQLite()
        else:
            pass