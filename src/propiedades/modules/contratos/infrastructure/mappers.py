from propiedades.seedwork.domain.repositories import Mapper
from propiedades.modules.contratos.domain.entities import Contrato
#from propiedades.modules.contratos.domain.value_objects import Pago
from .dto import Contrato as ContratoDTO
from .dto import Pago as PagoDTO
# from .dto import Oficina as OficinaDTO

class MapperContrato(Mapper):
    def entity_to_dto(self, entidad: Contrato) -> ContratoDTO:
        contrato_dto = ContratoDTO()
        contrato_dto.id = entidad.id
        contrato_dto.fechaCreacion = entidad.fecha_creacion

        return contrato_dto

    def dto_to_entity(self, dto: ContratoDTO) -> Contrato:
        return Contrato(dto.id, dto.fechaCreacion)

    def _procesar_pago(self, pago: any) -> list[PagoDTO]:
        pass
    
    def type(self) -> type:
        return Contrato.__class__
    
    #def _procesar_pago_dto(self, pago_dto: list[PagoDTO]) -> list[Pago]:
     #   pago_dict = list()



      #  return pago_dict
                
                





