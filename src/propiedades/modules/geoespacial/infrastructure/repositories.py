from uuid import UUID
from propiedades.config.db import db
from propiedades.modules.geoespacial.domain.repositories import RepositorioLotes
from propiedades.modules.geoespacial.domain.factories import GeoespacialFactory
from propiedades.modules.geoespacial.domain.entities import Lote
from propiedades.modules.geoespacial.infrastructure.mappers import MapperLote
from propiedades.modules.geoespacial.infrastructure.dto import MapperLote

class RepositorioLotesSQLite(RepositorioLotes):
    def __init__(self):
        self._fabrica_geoespacial: GeoespacialFactory = GeoespacialFactory()
    
    @property
    def fabrica_geoespacial(self):
        return self._fabrica_geoespacial
    
    def get_all(self) -> list[Lote]:
        pass

    def get(self, id: UUID) -> Lote:
        inmueble_dto = db.session.query(InmuebleDTO).one()
        return self.fabrica_catastrales.create(inmueble_dto, MapperLote())

    def append(self, lote: Lote):
        lote_dto = self.fabrica_geoespacial.create(lote, MapperLote())
        db.session.add(lote_dto)
    
    def delete(self):
        pass

    def update(self):
        pass