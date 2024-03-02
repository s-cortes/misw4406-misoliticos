from propiedades.seedwork.domain.repositories import Mapper
from propiedades.modules.geoespacial.domain.entities import Lote, Edificio
from propiedades.modules.geoespacial.domain.value_objects import Coordenada, Direccion, Poligono
from .dto import Lote as LoteDTO
from .dto import Edificio as EdificioDTO

class MapperLote(Mapper):
    def entity_to_dto(self, entidad: Lote) -> LoteDTO:
        lote_dto = LoteDTO()
        lote_dto.id = entidad.id

        edificios_dto = list()
        for edificio in entidad.edificio:
            edificios_dto.extend(self._procesar_edificio(edificio))
        
        lote_dto.edificio = edificios_dto
        return lote_dto

    def dto_to_entity(self, dto: LoteDTO) -> Lote:
        pass

    def type(self) -> type:
        return Lote.__class__
    
    def _procesar_edificio(self, edificio: Edificio) -> EdificioDTO:
        edificio_dto = EdificioDTO()
        edificio_dto.id = edificio.id
        