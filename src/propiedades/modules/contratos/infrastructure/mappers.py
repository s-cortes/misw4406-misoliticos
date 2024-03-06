from propiedades.seedwork.domain.repositories import Mapper
from propiedades.modules.contratos.domain.entities import Contrato
from .dto import Contrato as ContratoDTO
from .dto import Pago as PagoDTO

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

