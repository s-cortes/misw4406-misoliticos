from dataclasses import dataclass
from .base import LoteQueryBaseHandler

from propiedades.seedwork.application.queries import Query, QueryResult
from propiedades.seedwork.application.queries import execute_query as query

from propiedades.modules.geoespacial.domain.repositories import RepositorioLotes
from propiedades.modules.geoespacial.infrastructure.mappers import MapperLote

@dataclass
class ObtenerLotes(Query):
    ...
class ObtenerLotesHandler(LoteQueryBaseHandler):

    def handle(self, query: ObtenerLotes) -> QueryResult:
        repositorio = self.fabrica_repositorio.create(RepositorioLotes.__class__)
        reserva =  self.fabrica_catastrales.create(repositorio.get(query.id), MapperLote())
        return QueryResult(resultado=reserva)

@query.register(ObtenerLotes)
def ejecutar_query_obtener_reserva(query: ObtenerLotes):
    handler = ObtenerLotesHandler()
    return handler.handle(query)