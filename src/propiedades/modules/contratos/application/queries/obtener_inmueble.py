from propiedades.seedwork.application.queries import Query, QueryResult
from propiedades.seedwork.application.queries import execute_query as query
from propiedades.modules.contratos.domain.repositories import RepositorioInmuebles
from dataclasses import dataclass
from .base import InmuebleQueryBaseHandler
from propiedades.modules.contratos.infrastructure.mappers import MapperInmueble
import uuid

@dataclass
class ObtenerInmueble(Query):
    id: uuid.UUID

class ObtenerInmuebleHandler(InmuebleQueryBaseHandler):

    def handle(self, query: ObtenerInmueble) -> QueryResult:
        repositorio = self.fabrica_repositorio.create(RepositorioInmuebles.__class__)
        reserva =  self.fabrica_contratos.create(repositorio.get(query.id), MapperInmueble())
        return QueryResult(resultado=reserva)

@query.register(ObtenerInmueble)
def ejecutar_query_obtener_reserva(query: ObtenerInmueble):
    handler = ObtenerInmuebleHandler()
    return handler.handle(query)