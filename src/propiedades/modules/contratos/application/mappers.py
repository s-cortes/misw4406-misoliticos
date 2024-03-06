from propiedades.modules.contratos.application.dtos import (
    ContratoDTO,
)
from propiedades.modules.contratos.domain.entities import Contrato
# from propiedades.modules.contratos.domain.value_objects import 
from propiedades.seedwork.application.dtos import Mapper as ApplicationMapper
from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.repositories import Mapper as RepositoryMapper


class ContratoDTOJsonMapper(ApplicationMapper):

  #  def _procesar_pagos(self, pago: dict) -> PagoDTO:
   #     oficinas_dto: list[OficinaDTO] = list()
    #    for oficina in pago.get("oficinas", list()):

#            oficinas_dto.append(OficinaDTO(area_dto, ubicacion_dto))

 #       return PagoDTO(oficinas_dto)

    def external_to_dto(self, external: any) -> ContratoDTO:
        contrato_dto = ContratoDTO(tipo_contrato=external.get("tipo_contrato"),
                                    fecha_inicio=external.get("fecha_inicio"),
                                    fecha_terminacion=external.get("fecha_terminacion"))

       # for itin in external.get("pagos", list()):
       #     contrato_dto.pagos.append(self._procesar_pagos(itin))

        return contrato_dto

    def dto_to_external(self, dto: ContratoDTO) -> any:
        return dto.__dict__


class ContratoMapper(RepositoryMapper):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

  #  def _procesar_pagos(self, pago: PagoDTO) -> Pago:
   #     oficinas: list[Oficina] = list()
    #    for oficina in pago.oficinas:
      #      oficinas.append(Oficina(area, ubicacion))

       # return Pago(oficinas)

    def entity_to_dto(self, entity: Contrato) -> ContratoDTO:
        fecha_creacion = entity.fecha_creacion.strftime(self._FORMATO_FECHA)
        _id = str(entity.id)
        fecha_inicio = entity.fecha_inicio.strftime(self._FORMATO_FECHA)
        fecha_terminacion = entity.fecha_terminacion.strftime(self._FORMATO_FECHA)
     #   pagos: list[PagoDTO] = list()

        return ContratoDTO(_id, fecha_creacion, entity.tipo_contrato, fecha_inicio, fecha_terminacion)

    def dto_to_entity(self, dto: ContratoDTO) -> Contrato:
        #pagos = list()
       # pagos.extend([self._procesar_pagos(p) for p in dto.pagos])

        #return Contrato(pagos=pagos)
        return Contrato(tipo_contrato=dto.tipo_contrato, fecha_inicio=dto.fecha_inicio, fecha_terminacion=dto.fecha_terminacion)

    def type(self) -> type:
        return Contrato.__class__