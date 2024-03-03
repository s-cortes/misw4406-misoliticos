from propiedades.seedwork.application.services import Service

from propiedades.modules.catastrales.domain.repositories import RepositorioInmuebles
from propiedades.modules.catastrales.infrastructure.factories import RepositoryFactory
from propiedades.modules.catastrales.domain.factories import CatastralFactory

from .dtos import InmuebleDTO
from .mappers import CatastralMapper

class CompaniaService(Service):

    def __init__(self):
        self._fabrica_repositorio: RepositoryFactory = RepositoryFactory()
        self._fabrica_catastral: CatastralFactory = CatastralFactory()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_catastral(self):
        return self._fabrica_catastral

    def obtener_inmueble_por_id(self, id) -> InmuebleDTO:
        repositorio = self.fabrica_repositorio.create(RepositorioInmuebles.__class__)
        return self.fabrica_catastral.create(repositorio.get(id), CatastralMapper())