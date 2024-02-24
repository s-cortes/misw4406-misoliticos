from propiedades.modules.catastrales.application.dtos import (
    AreaDTO,
    InmuebleDTO,
    OficinaDTO,
    PisoDTO,
    UbicacionInternaDTO,
)
from propiedades.modules.catastrales.domain.entities import Inmueble, Oficina
from propiedades.modules.catastrales.domain.value_objects import (
    Area,
    Piso,
    UbicacionInterna,
)
from propiedades.seedwork.application.dtos import Mapper as ApplicationMapper
from propiedades.seedwork.domain.entities import Entity
from propiedades.seedwork.domain.repositories import Mapper as RepositoryMapper


class CatastralDTOJsonMapper(ApplicationMapper):

    def _procesar_pisos(piso: dict) -> PisoDTO:
        oficinas_dto: list[OficinaDTO] = list()
        for oficina in piso.get("oficinas", list()):
            area: dict = oficina.get("area")
            area_dto: AreaDTO = AreaDTO(area.get("valor"), area.get("unidad"))

            ubicacion = oficina.get("ubicacion")
            ubicacion_dto: UbicacionInternaDTO = UbicacionInternaDTO(
                ubicacion.get("nombre"),
                ubicacion.get("division_visible"),
                ubicacion.get("telefono"),
            )

            oficinas_dto.append(OficinaDTO(area_dto, ubicacion_dto))

        return PisoDTO(oficinas_dto)

    def external_to_dto(self, external: any) -> InmuebleDTO:
        inmueble_dto = InmuebleDTO()

        for itin in external.get("pisos", list()):
            inmueble_dto.pisos.append(self._procesar_pisos(itin))

        return inmueble_dto

    def dto_to_external(self, dto: InmuebleDTO) -> any:
        return dto.__dict__


class CatastralMapper(RepositoryMapper):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def _procesar_pisos(piso: PisoDTO) -> Piso:
        oficinas: list[Oficina] = list()
        for oficina in piso.oficinas:
            area_dto: dict = oficina.area
            area: Area = Area(area_dto.valor, area_dto.unidad)

            ubicacion_dto = oficina.ubicacion
            ubicacion: UbicacionInterna = UbicacionInterna(
                ubicacion_dto.nombre,
                ubicacion_dto.division_visible,
                ubicacion_dto.telefono,
            )

            oficinas.append(Oficina(area, ubicacion))

        return Piso(oficinas)

    def entity_to_dto(self, entity: Inmueble) -> InmuebleDTO:
        fecha_creacion = entity.fecha_creacion.strftime(self._FORMATO_FECHA)
        _id = str(entity.id)
        pisos: list[PisoDTO] = list()

        for piso in entity.pisos:
            oficinas: list[OficinaDTO] = list()
            for oficina in piso.oficinas:
                _id_oficina = str(oficina.id)
                area: AreaDTO = AreaDTO(oficina.area.valor, oficina.area.unidad)
                ubicacion: UbicacionInternaDTO = UbicacionInternaDTO(
                    oficina.ubicacion.nombre,
                    oficina.ubicacion.division_visible,
                    oficina.ubicacion.telefono,
                )
                oficinas.append(OficinaDTO(_id_oficina, area, ubicacion))
            pisos.append(PisoDTO(oficinas))

        return InmuebleDTO(_id, fecha_creacion, pisos)

    def dto_to_entity(self, dto: InmuebleDTO) -> Inmueble:
        inmueble: Inmueble = Inmueble()

        inmueble.pisos = list()
        inmueble.pisos.extend([self._procesar_pisos(p) for p in dto.pisos])

        return inmueble
