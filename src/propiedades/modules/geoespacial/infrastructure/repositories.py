from uuid import UUID
import logging
from propiedades.config.db import db
from propiedades.modules.geoespacial.domain.repositories import RepositorioLotes
from propiedades.modules.geoespacial.domain.factories import GeoespacialFactory
from propiedades.modules.geoespacial.domain.entities import Lote, TestLoteEntity
from propiedades.modules.geoespacial.infrastructure.mappers import MapperLote
from propiedades.modules.geoespacial.infrastructure.dto import Lote as LoteDTO

class RepositorioLotesSQLite(RepositorioLotes):
    def __init__(self):
        self._fabrica_geoespacial: GeoespacialFactory = GeoespacialFactory()
    
    @property
    def fabrica_geoespacial(self):
        return self._fabrica_geoespacial
    
    def get_all(self) -> list[Lote]:
        pass

    def get(self, id: UUID) -> Lote:
        lote_dto = db.session.query(LoteDTO).filter_by(id=str(id)).one()
        return self._fabrica_geoespacial.create(lote_dto, MapperLote())

    def append(self, lote: Lote):
        lote_dto = self.fabrica_geoespacial.create(lote, MapperLote())
        db.session.add(lote_dto)

    def insert(self, lote: TestLoteEntity):
        pass
    
    def delete(self):
        pass

    def update(self):
        pass