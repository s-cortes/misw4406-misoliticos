import uuid
from dataclasses import dataclass

from propiedades.modules.propiedades.application.mappers import PropiedadMapper
from propiedades.modules.propiedades.infrastructure.repositories import (
    PropiedadesRepository,
)
from propiedades.seedwork.application.queries import Query, QueryResult
from propiedades.seedwork.application.queries import execute_query

from .base import PropiedadBaseQueryHandler


@dataclass
class GetPropiedadQuery(Query):
    id: uuid.UUID


class GetPropiedadHandler(PropiedadBaseQueryHandler):

    def handle(self, query: GetPropiedadQuery) -> QueryResult:
        repositorio: PropiedadesRepository = self.repository_factory.create(
            PropiedadesRepository.__class__
        )
        propiedad = self.propiedad_factory.create(
            repositorio.get(query.id), PropiedadMapper()
        )
        return QueryResult(result=propiedad)


@execute_query.register(GetPropiedadQuery)
def execute_get_propiedad_query(query: GetPropiedadQuery):
    handler = GetPropiedadHandler()
    return handler.handle(query)
