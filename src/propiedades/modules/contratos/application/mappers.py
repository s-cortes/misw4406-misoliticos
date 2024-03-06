from propiedades.modules.contratos.application.dtos import (
    AreaDTO,
    ContratoDTO,
    OficinaDTO,
    PagoDTO,
    UbicacionInternaDTO,
)
from propiedades.modules.contratos.domain.entities import Contrato
from propiedades.modules.contratos.domain.value_objects import (
    Area,
    Pago,
    UbicacionInterna,
    Oficina,
)
from propiedades.seedwork.application.dtos import Mapper as ApplicationMapper
from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.repositories import Mapper as RepositoryMapper


class ContratoDTOJsonMapper(ApplicationMapper):

    def _procesar_pagos(self, pago: dict) -> PagoDTO:
        oficinas_dto: list[OficinaDTO] = list()
        for oficina in pago.get("oficinas", list()):
            area: dict = oficina.get("area")
            area_dto: AreaDTO = AreaDTO(area.get("valor"), area.get("unidad"))

            ubicacion = oficina.get("ubicacion")
            ubicacion_dto: UbicacionInternaDTO = UbicacionInternaDTO(
                ubicacion.get("nombre"),
                ubicacion.get("division_visible"),
                ubicacion.get("telefono"),
            )

            oficinas_dto.append(OficinaDTO(area_dto, ubicacion_dto))

        return PagoDTO(oficinas_dto)

    def external_to_dto(self, external: any) -> ContratoDTO:
        contrato_dto = ContratoDTO()

        for itin in external.get("pagos", list()):
            contrato_dto.pagos.append(self._procesar_pagos(itin))

        return contrato_dto

    def dto_to_external(self, dto: ContratoDTO) -> any:
        return dto.__dict__


class ContratoMapper(RepositoryMapper):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def _procesar_pagos(self, pago: PagoDTO) -> Pago:
        oficinas: list[Oficina] = list()
        for oficina in pago.oficinas:
            area_dto: dict = oficina.area
            area: Area = Area(area_dto.valor, area_dto.unidad)

            ubicacion_dto = oficina.ubicacion
            ubicacion: UbicacionInterna = UbicacionInterna(
                ubicacion_dto.nombre,
                ubicacion_dto.division_visible,
                ubicacion_dto.telefono,
            )

            oficinas.append(Oficina(area, ubicacion))

        return Pago(oficinas)

    def entity_to_dto(self, entity: Contrato) -> ContratoDTO:
        fecha_creacion = entity.fecha_creacion.strftime(self._FORMATO_FECHA)
        _id = str(entity.id)
        pagos: list[PagoDTO] = list()

        for pago in entity.pagos:
            oficinas: list[OficinaDTO] = list()
            for oficina in pago.oficinas:
                _id_oficina = str(oficina.id)
                area: AreaDTO = AreaDTO(oficina.area.valor, oficina.area.unidad)
                ubicacion: UbicacionInternaDTO = UbicacionInternaDTO(
                    oficina.ubicacion.nombre,
                    oficina.ubicacion.division_visible,
                    oficina.ubicacion.telefono,
                )
                oficinas.append(OficinaDTO(_id_oficina, area, ubicacion))
            pagos.append(PagoDTO(oficinas))

        return ContratoDTO(_id, fecha_creacion, pagos)

    def dto_to_entity(self, dto: ContratoDTO) -> Contrato:
        pagos = list()
        pagos.extend([self._procesar_pagos(p) for p in dto.pagos])

        return Contrato(pagos=pagos)

    def type(self) -> type:
        return Contrato.__class__