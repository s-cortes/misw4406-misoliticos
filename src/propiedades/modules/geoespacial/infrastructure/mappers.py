from propiedades.seedwork.domain.repositories import Mapper
from propiedades.modules.geoespacial.domain.entities import Lote, Edificio
from propiedades.modules.geoespacial.domain.value_objects import Coordenada, Direccion, Poligono
from .dto import Lote as LoteDTO
from .dto import Edificio as EdificioDTO

class MapperLote(Mapper):
    def entity_to_dto(self, entidad: Lote) -> LoteDTO:
        lote_dto = LoteDTO()
        #lote_dto.id = str(entidad.id)

        # Direcciones
        direccion_dto = ""
        for direction in entidad.direccion:
            direccion_dto = direccion_dto + str(direction.valor) + ";"
        lote_dto.direcciones = direccion_dto 

        # Coordenadas
        coordenada_dto = ""
        for coordenada in entidad.poligono.coordenadas:
            coordenada_dto = coordenada_dto + str(coordenada.latitud) + ":" + str(coordenada.longitud) + ";"
        lote_dto.coordenadas_poligono = coordenada_dto

        #Edificios
        edificios_dto: list[EdificioDTO] = list()
        for edificio in entidad.edificio:
            edificios_dto.append(self._procesar_edificio(edificio))
        
        lote_dto.edificio = edificios_dto
        return lote_dto

    def dto_to_entity(self, dto: LoteDTO) -> Lote:
        pass

    def type(self) -> type:
        return Lote.__class__
    
    def _procesar_edificio(self, edificio: Edificio) -> EdificioDTO:
        edificio_dto = EdificioDTO()
        #edificio_dto.id = str(edificio.id)

        # Coordenadas
        coordenada_dto = ""
        for coordenada in edificio.poligono.coordenadas:
            coordenada_dto = coordenada_dto + str(coordenada.latitud) + ":" + str(coordenada.longitud) + ";"
        edificio_dto.coordenadas_poligono = coordenada_dto

        return edificio_dto

        