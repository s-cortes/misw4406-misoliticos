from propiedades.config.db import db
from propiedades.modules.contratos.domain.repositories import RepositorioInmuebles
from propiedades.modules.contratos.domain.factories import ContratoFactory
from propiedades.modules.contratos.domain.entities import Inmueble
from propiedades.modules.contratos.infrastructure.mappers import MapperInmueble
from .dto import Inmueble as InmuebleDTO
from uuid import UUID

class RepositorioInmueblesSQLite(RepositorioInmuebles):
    def __init__(self):
        self._fabrica_contratos: ContratoFactory = ContratoFactory()

    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos
    
    def get_all(self) -> list[Inmueble]:
        inmuebles = db.session.query(InmuebleDTO).one()

    def get(self, id: UUID) -> Inmueble:
        inmueble_dto = db.session.query(InmuebleDTO).one()
        return self.fabrica_contratos.create(inmueble_dto, MapperInmueble())
    
    def append(self, inmueble: Inmueble):
        inmueble_dto = self.fabrica_contratos.create(inmueble, MapperInmueble())
        db.session.add(inmueble_dto)

    def delete(self):
        pass
    
    def update(self):
        pass