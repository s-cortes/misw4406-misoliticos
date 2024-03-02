from propiedades.seedwork.application.dtos import Mapper as ApplicationMapper
from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.repositories import Mapper as RepositoryMapper

from propiedades.modules.geoespacial.application.dtos import LoteDTO, EdificioDTO, PoligonoDTO, DireccionDTO, CoordenadasDTO
from propiedades.modules.geoespacial.domain.entities import Lote

class LoteDTOJsonMapper():
    def _procesar_direccion(self, direccion: dict) -> DireccionDTO:
        direccion_dto = DireccionDTO()
        direccion_dto.valor = direccion.get("valor")
        return direccion_dto

    def _procesar_poligono(self, poligono: any) -> PoligonoDTO:
        coordenadas_dto = list[CoordenadasDTO()] = list()
        for coordenada in poligono.get("coordenadas"):
            coordenada_dto = CoordenadasDTO(
                coordenada.get("latitud"),
                coordenada.get("longitud")
                )
            coordenadas_dto.append(coordenada_dto)

        return PoligonoDTO(coordenadas_dto)
        

    def _procesar_edificio(self, edificio: any) -> EdificioDTO:
        return EdificioDTO(self._procesar_poligono(edificio.get("poligono")))

    def external_to_dto(self, external: any) -> LoteDTO:
        direcciones_dto = list[DireccionDTO] = list()
        poligono = PoligonoDTO()
        edificios_dto = list[EdificioDTO] = list()
        
        for direccion in external.get("direcciones"):
            direcciones_dto.append(self._procesar_direccion(direccion))
        
        for poligono in external.get("poligono"):
            poligono = self._procesar_poligono(poligono)
        
        for edificio in external.get("edificios", list()):
            edificios_dto.append(self._procesar_edificio(edificio))
        return LoteDTO(direcciones_dto, poligono, edificios_dto)

class GeoespacialMapper(RepositoryMapper):
    def _procesar_edificio(self, edificio:any) -> EdificioDTO:
        return EdificioDTO(edificio.id, self._procesar_poligono(edificio.poligono))

    def _procesar_direccion(self, direccion:any) -> DireccionDTO:
        return DireccionDTO(direccion.valor)
    
    def _procesar_poligono(self, poligono: any) -> PoligonoDTO:
        coordenadas_dto = list[CoordenadasDTO] = list()

        for coordenada in poligono.coordenadas:
            coordenada_out = CoordenadasDTO(coordenada.latitud, coordenada.longitud)
            coordenadas_dto.append(coordenada_out)
        return PoligonoDTO(coordenadas_dto)
    
    def entity_to_dto(self, entity: Lote) -> LoteDTO:
        _id = str(entity.id)
        direccion_dto = list[DireccionDTO] = list()
        
        for direccion in entity.direccion:
            direccion_dto.append(self._procesar_direccion(direccion))
        poligono = self._procesar_poligono(entity.poligono)

        edificio_dto = list[EdificioDTO] = list()
        for edificio in entity.edificio:
            edificio_dto.append(self._procesar_edificio(edificio))

        return LoteDTO(_id,direccion,poligono,edificio)
    def dto_to_entity(self, dto: any) -> Lote:
        pass
    def type(self) -> type:
        return Lote.__class__