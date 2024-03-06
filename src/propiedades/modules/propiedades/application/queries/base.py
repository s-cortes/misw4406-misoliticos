from propiedades.modules.propiedades.domain.factories import PropiedadFactory
from propiedades.modules.propiedades.infrastructure.factories import RepositoryFactory
from propiedades.seedwork.application.queries import QueryHandler


class PropiedadBaseQueryHandler(QueryHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._propiedad_factory: PropiedadFactory = PropiedadFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def propiedad_factory(self):
        return self._propiedad_factory
