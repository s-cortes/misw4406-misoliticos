from propiedades.config.db import db
from propiedades.modules.catastrales.domain.repositories import RepositorioInmuebles
from propiedades.modules.catastrales.domain.factories import CatastralFactory
from propiedades.modules.catastrales.domain.entities import Inmueble
from propiedades.modules.catastrales.infrastructure.mappers import MapperInmueble
from .dto import Inmueble as InmuebleDTO
from uuid import UUID

class RepositorioInmueblesSQLite(RepositorioInmuebles):
    def __init__(self):
        self._fabrica_catastrales: CatastralFactory = CatastralFactory()

    @property
    def fabrica_catastrales(self):
        return self._fabrica_catastrales
    
    def obtener_todos(self) -> list[Inmueble]:
        pass

    def obtener_por_id(self, id: UUID) -> Inmueble:
        inmueble_dto = db.session.query(InmuebleDTO).filter_by(id = str(id)).one()
        return self.fabrica_catastrales.create(inmueble_dto, MapperInmueble())
    
    def agregar(self, inmueble: Inmueble):
        inmueble_dto = self.fabrica_catastrales.create(inmueble, MapperInmueble())
        db.session.add(inmueble_dto)