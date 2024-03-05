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
class GetPropiedadesQuery(Query): ...


class GetPropiedadesHandler(PropiedadBaseQueryHandler):

    def handle(self, query: GetPropiedadesQuery) -> QueryResult:
        repositorio: PropiedadesRepository = self.repository_factory.create(
            PropiedadesRepository.__class__
        )
        propiedades = [
            self.propiedad_factory.create(p, PropiedadMapper())
            for p in repositorio.get_all()
        ]
        return QueryResult(result=propiedades)


@execute_query.register(GetPropiedadesQuery)
def execute_get_propiedades_query(query: GetPropiedadesQuery):
    handler = GetPropiedadesHandler()
    return handler.handle(query)