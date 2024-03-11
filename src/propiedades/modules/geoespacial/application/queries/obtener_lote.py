from dataclasses import dataclass
from .base import LoteQueryBaseHandler
import uuid

from propiedades.seedwork.application.queries import Query, QueryResult
from propiedades.seedwork.application.queries import execute_query as query

from propiedades.modules.geoespacial.domain.repositories import RepositorioLotes
from propiedades.modules.geoespacial.infrastructure.mappers import MapperLote

@dataclass
class ObtenerLote(Query):
    id: uuid.UUID

class ObtenerLoteHandler(LoteQueryBaseHandler):

    def handle(self, query: ObtenerLote) -> QueryResult:
        repositorio = self.fabrica_repositorio.create(RepositorioLotes.__class__)
        lote =  repositorio.get(query.id)
        return QueryResult(result=lote)

@query.register(ObtenerLote)
def ejecutar_query_obtener_reserva(query: ObtenerLote):
    handler = ObtenerLoteHandler()
    return handler.handle(query)