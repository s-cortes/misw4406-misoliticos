from uuid import UUID

from propiedades.config.db import db
from propiedades.modules.propiedades.domain.entities import Propiedad
from propiedades.modules.propiedades.domain.factories import PropiedadFactory
from propiedades.modules.propiedades.domain.repositories import PropiedadesRepository
from propiedades.modules.propiedades.infrastructure.mappers import PropiedadMapper

from .dtos import Propiedad as PropiedadDTO


class PropiedadesRepositorySQLite(PropiedadesRepository):
    def __init__(self):
        self._propiedad_factory: PropiedadFactory = PropiedadFactory()

    @property
    def fabrica_propiedades(self):
        return self._propiedad_factory

    def get_all(self) -> list[Propiedad]:
        propiedades_dto = db.session.query(PropiedadDTO).all()
        return [
            self.fabrica_propiedades.create(dto, PropiedadMapper())
            for dto in propiedades_dto
        ]

    def get(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.create(propiedad_dto, PropiedadMapper())

    def append(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedades.create(propiedad, PropiedadMapper())
        db.session.add(propiedad_dto)

    def delete(self):
        pass

    def update(self):
        pass
