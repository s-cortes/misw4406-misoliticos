from propiedades.seedwork.domain.repositories import Mapper
from propiedades.modules.contratos.domain.entities import Contrato
from propiedades.modules.contratos.domain.value_objects import Piso, UbicacionInterna, Area, Oficina
from .dto import Contrato as ContratoDTO
from .dto import Piso as PisoDTO
from .dto import Oficina as OficinaDTO

class MapperContrato(Mapper):
    def entity_to_dto(self, entidad: Contrato) -> ContratoDTO:
        contrato_dto = ContratoDTO()
        contrato_dto.id = entidad.id
        contrato_dto.fechaCreacion = entidad.fecha_creacion

        pisos_dto = list()
        for piso in entidad.pisos:
            pisos_dto.extend(self._procesar_piso(piso))
        
        contrato_dto.pisos = pisos_dto
        return contrato_dto

    def dto_to_entity(self, dto: ContratoDTO) -> Contrato:
        pisos_dto: list[PisoDTO] = dto.pisos

        return Contrato(dto.id, dto.fechaCreacion, pisos = [self._procesar_piso_dto(p) for p in pisos_dto])

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
    
    def type(self) -> type:
        return Contrato.__class__
    
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
                
                





