from propiedades.seedwork.application.queries import Query, QueryResult
from propiedades.seedwork.application.queries import execute_query as query
from propiedades.modules.contratos.domain.repositories import RepositorioContratos
from dataclasses import dataclass
from .base import ContratoQueryBaseHandler
from propiedades.modules.contratos.infrastructure.mappers import MapperContrato
import uuid

@dataclass
class ObtenerContrato(Query):
    id: uuid.UUID

class ObtenerContratoHandler(ContratoQueryBaseHandler):

    def handle(self, query: ObtenerContrato) -> QueryResult:
        repositorio = self.fabrica_repositorio.create(RepositorioContratos.__class__)
        contrato =  self.fabrica_contratos.create(repositorio.get(query.id), MapperContrato())
        return QueryResult(resultado=contrato)

@query.register(ObtenerContrato)
def ejecutar_query_obtener_reserva(query: ObtenerContrato):
    handler = ObtenerContratoHandler()
    return handler.handle(query)