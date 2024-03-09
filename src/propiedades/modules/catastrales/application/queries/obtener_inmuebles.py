from propiedades.seedwork.application.queries import Query, QueryResult
from propiedades.seedwork.application.queries import execute_query as query
from propiedades.modules.catastrales.infrastructure.repositories import RepositorioInmuebles
from dataclasses import dataclass
from .base import InmuebleQueryBaseHandler
from propiedades.modules.catastrales.application.mappers import MapperInmueble
import uuid

@dataclass
class ObtenerInmueblesQuery(Query): ...

class ObtenerInmueblesHandler(InmuebleQueryBaseHandler):

    def handle(self, query: ObtenerInmueblesQuery) -> QueryResult:
        repositorio: RepositorioInmuebles = self.fabrica_repositorios.create(RepositorioInmuebles.__class__)
        reservas =  [
            self.fabrica_catastrales.create(i, MapperInmueble()) 
            for i in repositorio.get_all()]
        return QueryResult(resultado=reservas)

@query.register(ObtenerInmueblesQuery)
def ejecutar_query_obtener_reservas(query: ObtenerInmueblesQuery):
    handler = ObtenerInmueblesHandler()
    return handler.handle(query)