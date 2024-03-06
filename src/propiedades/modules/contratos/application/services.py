from propiedades.seedwork.application.services import Service

from propiedades.modules.contratos.domain.repositories import RepositorioContratos
from propiedades.modules.contratos.infrastructure.factories import RepositoryFactory
from propiedades.modules.contratos.domain.factories import ContratoFactory

from .dtos import ContratoDTO
from .mappers import ContratoMapper
class ContratoService(Service):

    def __init__(self):
        self._fabrica_repositorio: RepositoryFactory = RepositoryFactory()
        self._fabrica_Contrato: ContratoFactory = ContratoFactory()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_Contrato(self):
        return self._fabrica_Contrato

    def obtener_contrato_por_id(self, id) -> ContratoDTO:
        repositorio = self.fabrica_repositorio.create(RepositorioContratos.__class__)
        return self.fabrica_Contrato.create(repositorio.get(id), ContratoMapper())