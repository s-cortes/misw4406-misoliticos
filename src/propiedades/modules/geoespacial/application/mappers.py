from propiedades.seedwork.application.dtos import Mapper as ApplicationMapper
from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.repositories import Mapper as RepositoryMapper

from propiedades.modules.geoespacial.application.dtos import LoteDTO, EdificioDTO, PoligonoDTO, DireccionDTO, CoordenadasDTO
from propiedades.modules.geoespacial.domain.entities import Lote, Edificio
from propiedades.modules.geoespacial.domain.value_objects import Direccion, Coordenada, Poligono

class LoteDTOJsonMapper(ApplicationMapper):
    def _procesar_direccion(self, direccion: dict) -> DireccionDTO:
        return DireccionDTO(direccion.get("valor"))

    def _procesar_poligono(self, poligono: any) -> PoligonoDTO:
        coordenadas_dto : list[CoordenadasDTO] = list()
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
        direcciones_dto: list[DireccionDTO] = list()
        edificios_dto : list[EdificioDTO] = list()
        
        for direccion in external.get("direcciones", list()):
            direcciones_dto.append(self._procesar_direccion(direccion))
        
        poligono_dto: PoligonoDTO = self._procesar_poligono(external.get("poligono"))
        
        for edificio in external.get("edificios", list()):
            edificios_dto.append(self._procesar_edificio(edificio))
        return LoteDTO(direcciones_dto, poligono_dto, edificios_dto)
    
    def procesar_edificio(self, edificio: EdificioDTO) -> dict:
        
        coord_pol_list = list()
        for coord in edificio.poligono.coordenadas:
            coord_out = {"latitud":coord.latitud,"longitud": coord.longitud}
            coord_pol_list.append(coord_out)
        poligono_edif = {"coordenadas": coord_pol_list}

        return dict(id=str(edificio.id), poligono=poligono_edif)

    def dto_to_external(self, dto: Lote) -> any:
        
        direcciones_out = list()
        for dir in dto.direccion:
            direcciones_out.append({"valor":dir})
        
        coord_pol_list = list()
        for coord in dto.poligono.coordenadas:
            coord_out = {"latitud":coord.latitud,"longitud": coord.longitud}
            coord_pol_list.append(coord_out)
        poligono = {"coordenadas": coord_pol_list}

        edificios = list()
        for edificacion in dto.edificio:
            edificios.append(self.procesar_edificio(edificacion))
        return dict(id=str(dto.id),direcciones=direcciones_out, poligono=poligono, edificios=edificios)
        #return dict(id=str(dto.id),direcciones=direcciones_out)
        #return dto.__dict__

class GeoespacialMapper(RepositoryMapper):
    def _procesar_edificio(self, edificio:any) -> EdificioDTO:
        return EdificioDTO(edificio.id, self._procesar_poligono(edificio.poligono))

    def _procesar_direccion(self, direccion:any) -> DireccionDTO:
        return DireccionDTO(direccion.valor)
    
    def _procesar_poligono(self, poligono: any) -> PoligonoDTO:
        coordenadas_dto : list[CoordenadasDTO] = list()

        for coordenada in poligono.coordenadas:
            coordenada_out = CoordenadasDTO(coordenada.latitud, coordenada.longitud)
            coordenadas_dto.append(coordenada_out)
        return PoligonoDTO(coordenadas_dto)
    
    def entity_to_dto(self, entity: Lote) -> LoteDTO:
        print(str(entity))
        _id = str(entity.id)
        direccion_dto : list[DireccionDTO] = list()
        
        for direccion in entity.direccion:
            direccion_dto.append(self._procesar_direccion(direccion))
        poligono = self._procesar_poligono(entity.poligono)

        edificio_dto = list[EdificioDTO] = list()
        for edificio in entity.edificio:
            edificio_dto.append(self._procesar_edificio(edificio))

        return LoteDTO(_id,direccion,poligono,edificio)
    
    def _procesar_poligono_dto(self, poligono:PoligonoDTO) -> Poligono:
        coordenadas : list[Coordenada] = list()

        for coordenada in poligono.coordenadas:
            coordenada_out = Coordenada(coordenada.latitud, coordenada.longitud)
            coordenadas.append(coordenada_out)
        return Poligono(coordenadas)

    def _procesar_direccion_dto(self, direccion:DireccionDTO) -> Direccion:
        return Direccion(direccion.valor)
    
    def _procesar_edificio_dto(self, edificio: EdificioDTO) -> Edificio:
        _id = str(edificio.id)
        poligono = self._procesar_poligono_dto(edificio.poligono)
        return Edificio(id=_id, poligono=poligono)
    
    def dto_to_entity(self, dto: LoteDTO) -> Lote:
        _id = str(dto.id)
        direcciones: list[Direccion] = list()
        for direccion in dto.direccion:
             direcciones.append(self._procesar_direccion_dto(direccion))
        poligono = self._procesar_poligono_dto(dto.poligono)

        edificios: list[Edificio] = list()
        for edificio in dto.edificio:
            edificios.append(self._procesar_edificio_dto(edificio))

        return Lote(id=_id,direccion=direcciones,poligono=poligono, edificio=edificios)

    def type(self) -> type:
        return Lote.__class__