from propiedades.config.db import db
from propiedades.modules.contratos.domain.repositories import RepositorioContratos
from propiedades.modules.contratos.domain.factories import ContratosFactory
from propiedades.modules.contratos.domain.entities import Contrato
from propiedades.modules.contratos.infrastructure.mappers import MapperContratos
from .dto import Contrato as ContratoDTO
from uuid import UUID

class RepositorioContratosSQLite(RepositorioContratos):
    def __init__(self):
        self._fabrica_contratos: ContratosFactory = ContratosFactory()

    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos
    
    def get_all(self) -> list[Contrato]:
        contratos = db.session.query(ContratoDTO).one()

    def get(self, id: UUID) -> Contrato:
        contrato_dto = db.session.query(ContratoDTO).one()
        return self.fabrica_contratos.create(contrato_dto, MapperContratos())
    
    def append(self, contrato: Contrato):
        contrato_dto = self.fabrica_contratos.create(contrato, MapperContratos())
        db.session.add(contrato_dto)

    def delete(self):
        pass
    
    def update(self):
        pass
