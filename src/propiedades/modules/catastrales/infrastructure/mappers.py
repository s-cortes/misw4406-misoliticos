from propiedades.seedwork.domain.repositories import Mapper
from propiedades.modules.catastrales.domain.entities import Inmueble
from propiedades.modules.catastrales.domain.value_objects import Piso, UbicacionInterna, Area, Oficina
from .dto import Inmueble as InmuebleDTO
from .dto import Piso as PisoDTO
from .dto import Oficina as OficinaDTO

class MapperInmueble(Mapper):
    def entity_to_dto(self, entidad: Inmueble) -> InmuebleDTO:
        inmueble_dto = InmuebleDTO()
        inmueble_dto.id = entidad.id
        inmueble_dto.fechaCreacion = entidad.fecha_creacion

        pisos_dto = list()
        for piso in entidad.pisos:
            pisos_dto.extend(self._procesar_piso(piso))
        
        inmueble_dto.pisos = pisos_dto
        return inmueble_dto

    def dto_to_entity(self, dto: InmuebleDTO) -> Inmueble:
        inmueble = Inmueble(dto.id, dto.fechaCreacion)
        inmueble.pisos = list()

        pisos_dto: list[PisoDTO] = dto.pisos

        inmueble.pisos.extend(self._procesar_piso_dto(pisos_dto))
        return inmueble

    def _procesar_piso(self, piso: any) -> list[PisoDTO]:
        pisos_list = list()
        oficinas_list = list()
        for oficina in piso.oficinas:
            oficina_dto = OficinaDTO()
            oficina_dto.nombre = oficina.ubicacion.nombre
            oficina_dto.division = oficina.ubicacion.division_visible
            oficina_dto.telefono = oficina.ubicacion.telefono
            oficina_dto.unidadArea = oficina.area.unidad
            oficina_dto.valorArea = oficina.area.valor
            oficinas_list.append(oficina_dto)
        pisos_list.append(oficinas_list)
        return pisos_list
    
    def obtener_tipo(self) -> type:
        return Inmueble.__class__
    
    def _procesar_piso_dto(self, piso_dto: list[PisoDTO]) -> list[Piso]:
        piso_dict = list()

        for piso in piso_dto:
            pisoTrad = Piso()
            oficinas = list[Oficina]
            for oficina in piso.oficinas:
                area = Area()
                area.unidad = oficina.unidadArea
                area.valor = oficina.valorArea

                ubicacion = UbicacionInterna()
                ubicacion.nombre = oficina.nombre
                ubicacion.division_visible = oficina.division
                ubicacion.telefono = oficina.telefono

                oficinaTrad = Oficina()
                oficinaTrad.area = area
                oficinaTrad.ubicacion = ubicacion

                oficinas.append(oficinaTrad)
            pisoTrad.oficinas = oficinas
        piso_dict.append(pisoTrad)

        return piso_dict
                
                





