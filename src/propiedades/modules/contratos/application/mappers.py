from propiedades.modules.contratos.application.dtos import (
    ContratoDTO,
    PagoDTO
)
from propiedades.modules.contratos.domain.entities import Contrato, Pago
# from propiedades.modules.contratos.domain.value_objects import 
from propiedades.seedwork.application.dtos import Mapper as ApplicationMapper
from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.repositories import Mapper as RepositoryMapper


class ContratoDTOJsonMapper(ApplicationMapper):

    def _procesar_pagos(self, pago: dict) -> PagoDTO:
        return PagoDTO(pago.get("valor_pago"), pago.get("moneda"), pago.get("metodo_pago"))

    def external_to_dto(self, external: any) -> ContratoDTO:
        contrato_dto = ContratoDTO(tipo_contrato=external.get("tipo_contrato"),
                                    fecha_inicio=external.get("fecha_inicio"),
                                    fecha_terminacion=external.get("fecha_terminacion"),
                                    catastral_id=external.get("catastral_id"),
                                    compania_id=external.get("compania_id"))

        for pago in external.get("pagos", list()):
            contrato_dto.pagos.append(self._procesar_pagos(pago))

        return contrato_dto

    def dto_to_external(self, dto: ContratoDTO) -> any:
        return dto.__dict__


class ContratoMapper(RepositoryMapper):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def _procesar_pagos(self, pago: PagoDTO) -> Pago:
        return Pago(pago.valor_pago, pago.moneda, pago.metodo_pago)

    def entity_to_dto(self, entity: Contrato) -> ContratoDTO:
        fecha_creacion = entity.fecha_creacion.strftime(self._FORMATO_FECHA)
        _id = str(entity.id)
        fecha_inicio = entity.fecha_inicio.strftime(self._FORMATO_FECHA)
        fecha_terminacion = entity.fecha_terminacion.strftime(self._FORMATO_FECHA)
        pagos: list[PagoDTO] = list()

        for pago in entity.pagos:
            pagos.append(PagoDTO(pago.valor_pago, pago.moneda, pago.metodo_pago))

        return ContratoDTO(_id,
                            fecha_creacion,
                            entity.tipo_contrato,
                            fecha_inicio,
                            fecha_terminacion,
                            entity.catastral_id,
                            entity.compania_id,
                            pagos
        )

    def dto_to_entity(self, dto: ContratoDTO) -> Contrato:
        pagos = list()
        pagos.extend([self._procesar_pagos(p) for p in dto.pagos])

        return Contrato(tipo_contrato=dto.tipo_contrato,
                        fecha_inicio=dto.fecha_inicio,
                        fecha_terminacion=dto.fecha_terminacion,
                        catastral_id=dto.catastral_id,
                        compania_id=dto.compania_id,
                        pagos=pagos
        )

    def type(self) -> type:
        return Contrato.__class__