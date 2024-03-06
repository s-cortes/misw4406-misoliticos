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

        return contrato_dto

    def dto_to_entity(self, dto: ContratoDTO) -> Contrato:
        return Contrato(dto.id, dto.fechaCreacion)

    def _procesar_pago(self, piso: any) -> list[PisoDTO]:
        pass
    
    def type(self) -> type:
        return Contrato.__class__
    
    def _procesar_pago_dto(self, pago_dto: list[PagoDTO]) -> list[Pago]:
        pago_dict = list()

        for pago in pago_dto:
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
        pago_dict.append(pisoTrad)

        return pago_dict
                
                





