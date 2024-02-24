from propiedades.modules.catastrales.application.dtos import (
    AreaDTO, InmuebleDTO, OficinaDTO, PisoDTO, UbicacionInternaDTO
)
from propiedades.seedwork.application.dtos import Mapper as ApplicationMapper


class CatastroDTOJsonMapper(ApplicationMapper):

    def _procesar_pisos(piso: dict) -> PisoDTO:
        oficinas_dto: list[OficinaDTO] = list()
        for oficina in piso.get("oficinas", list()):
            area: dict = oficina.get("area")
            area_dto: AreaDTO = AreaDTO(area.get("valor"), area.get("unidad"))

            ubicacion = oficina.get("ubicacion")
            ubicacion_dto: UbicacionInternaDTO = UbicacionInternaDTO(
                ubicacion.get("valor"),
                ubicacion.get("division_visible"),
                ubicacion.get("division_visible"),
            )

            oficinas_dto.append(OficinaDTO(area_dto, ubicacion_dto))

        return PisoDTO(oficinas_dto)

    def external_to_dto(self, external: any) -> InmuebleDTO:
        reserva_dto = InmuebleDTO()

        for itin in external.get("pisos", list()):
            reserva_dto.pisos.append(self._procesar_itinerario(itin))

        return reserva_dto

    def dto_to_external(self, dto: InmuebleDTO) -> any:
        return dto.__dict__
