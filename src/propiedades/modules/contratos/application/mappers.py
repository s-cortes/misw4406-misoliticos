from propiedades.modules.contratos.application.dtos import *
from propiedades.modules.contratos.domain.entities import Contrato, Pago
from propiedades.modules.contratos.domain.value_objects import *
from propiedades.seedwork.application.dtos import Mapper as ApplicationMapper
from propiedades.seedwork.domain.repositories import Mapper as RepositoryMapper


class ContratosDTOJsonMapper(ApplicationMapper):

    def _procesar_pago(self, pago: dict) -> PagoDTO:
        valor_pago = ValorPagoDTO(pago.get("valor_pago"))
        moneda = MonedaDTO(pago.get("moneda"))
        metodo_pago = MetodoPagoDTO(pago.get("metodo_pago"))

        return PagoDTO(valor_pago, moneda, metodo_pago)

    def external_to_dto(self, external: dict) -> ContratoDTO:
        pago = self._procesar_pago(external.get("pago"))
        contrato_dto = ContratoDTO(external.get("id"),
                                    TipoContratoDTO(external.get("tipo_contrato")),
                                    FechaInicioDTO(external.get("fecha_inicio")),
                                    FechaTerminacionDTO(external.get("fecha_terminacion")),
                                    pago,
                                    InformacionCatastralDTO(external.get("informacion_catastral"))
                                )

        return contrato_dto

    def dto_to_external(self, dto: ContratoDTO) -> any:
        return dto.__dict__

class ContratosMapper(RepositoryMapper):
    _FORMATO_FECHA = "%Y-%m-%d"

    def _procesar_pago(self, pago: PagoDTO) -> Pago:
        valor_pago = pago.valor_pago.valor
        moneda = pago.moneda.moneda
        metodo_pago = pago.metodo_pago.metodo

        return Pago(valor_pago, moneda, metodo_pago)

    def entity_to_dto(self, entity: Contrato) -> ContratoDTO:
     #   fecha_creacion = entity.fecha_creacion.strftime(self._FORMATO_FECHA)
        _id = str(entity.id)
        tipo_contrato = TipoContratoDTO(entity.tipo_contrato.tipo)
        fecha_inicio = FechaInicioDTO(entity.fecha_inicio.fecha)
        fecha_terminacion = FechaTerminacionDTO(entity.fecha_terminacion.fecha)
        pago = PagoDTO(entity.pago.valor_pago, entity.pago.moneda, entity.pago.metodo_pago)
        informacion_catastral = InformacionCatastralDTO(entity.informacion_catastral)

        return ContratoDTO(_id, tipo_contrato, fecha_inicio, fecha_terminacion, pago, informacion_catastral)

    def dto_to_entity(self, dto: ContratoDTO) -> Contrato:
        tipo_contrato = dto.tipo_contrato.tipo
        fecha_inicio = dto.fecha_inicio.fecha #datetime.strptime(dto.fecha_inicio.fecha, self._FORMATO_FECHA)
        fecha_terminacion = datetime.strptime(dto.fecha_terminacion.fecha, self._FORMATO_FECHA)
        pago = self._procesar_pago(dto.pago)
        informacion_catastral = dto.informacion_catastral.id

        return Contrato(tipo_contrato, fecha_inicio, fecha_terminacion, pago, informacion_catastral)

    def type(self) -> type:
        return Contrato.__class__