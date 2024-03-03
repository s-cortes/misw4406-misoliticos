from propiedades.seedwork.domain.repositories import Mapper
from propiedades.modules.contratos.domain.entities import Contrato, Pago
from .dto import Contrato as ContratoDTO
from .dto import Pago as PagoDTO

class MapperContratos(Mapper):
    def entity_to_dto(self, contrato: Contrato) -> ContratoDTO:
        contrato_dto = ContratoDTO()
        contrato_dto.id = contrato.id
        contrato_dto.tipoContrato = contrato.tipo_contrato
        contrato_dto.fechaInicio = contrato.fecha_inicio
        contrato_dto.fechaTerminacion = contrato.fecha_terminacion
        contrato_dto.pago = self._procesar_pago(contrato.pago)
        contrato_dto.informacionCatastral = contrato.informacion_catastral

        return contrato_dto

    def dto_to_entity(self, dto: ContratoDTO) -> Contrato:
        return Contrato(dto.id,
                        dto.tipoContrato,
                        dto.fechaInicio,
                        dto.fechaTerminacion,
                        self._procesar_pago_dto(dto.pago),
                        dto.informacionCatastral)

    def _procesar_pago(self, pago: Pago) -> PagoDTO:
        pago_dto = PagoDTO()
        pago_dto.valorPago = pago.valor_pago
        pago_dto.tipoMoneda = pago.moneda
        pago_dto.metodoPago = pago.metodo_pago

        return pago_dto

    def _procesar_pago_dto(self, dto: PagoDTO) -> Pago:
        return Pago(dto.valorPago,
                    dto.tipoMoneda,
                    dto.metodoPago)

    def type(self) -> type:
        return Contrato.__class__
