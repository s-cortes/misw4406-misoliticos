from propiedades.seedwork.domain.repositories import Mapper
from propiedades.modules.propiedades.domain.entities import Propiedad, Fotografia
from propiedades.modules.propiedades.domain.value_objects import Contenido
from .dtos import Propiedad as PropiedadDTO
from .dtos import Fotografia as FotografiaDTO


class PropiedadMapper(Mapper):
    def entity_to_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        propiedad_dto.id = str(entidad.id)
        propiedad_dto.fecha_creacion = entidad.fecha_creacion
        propiedad_dto.fecha_actualizacion = entidad.fecha_actualizacion
        propiedad_dto.tipo_construccion = entidad.tipo_construccion
        propiedad_dto.entidad = entidad.entidad

        fotografias_dto: list[FotografiaDTO] = list()
        fotografias_dto.extend(
            [self._procesar_fotografia(f) for f in entidad.fotografias]
        )

        propiedad_dto.fotografias = fotografias_dto
        return propiedad_dto

    def dto_to_entity(self, dto: PropiedadDTO) -> Propiedad:
        fotografias_dto: list[FotografiaDTO] = [
            self._procesar_fotografia_dto(p) for p in dto.fotografias
        ]

        return Propiedad(
            id=str(dto.id),
            fecha_creacion=dto.fecha_creacion,
            tipo_construccion=dto.tipo_construccion,
            entidad=dto.entidad,
            fotografias=fotografias_dto,
        )

    def _procesar_fotografia(self, fotografia: Fotografia) -> FotografiaDTO:
        fotografia_dto = FotografiaDTO()
        fotografia_dto.id = fotografia.id
        fotografia_dto.fecha_creacion = fotografia.fecha_creacion
        fotografia_dto.fecha_actualizacion = fotografia.fecha_actualizacion

        fotografia_dto.nombre = fotografia.nombre
        fotografia_dto.descripcion = fotografia.descripcion

        fotografia_dto.valor_contenido = fotografia.contenido.valor
        fotografia_dto.tipo_contenido = fotografia.contenido.tipo

        return fotografia_dto

    def type(self) -> type:
        return Propiedad.__class__

    def _procesar_fotografia_dto(self, dto: FotografiaDTO) -> Fotografia:
        contenido: Contenido = Contenido(dto.valor_contenido, dto.tipo_contenido)

        return Fotografia(
            dto.id,
            dto.fecha_creacion,
            dto.fecha_actualizacion,
            contenido=contenido,
            descripcion=dto.descripcion,
            nombre=dto.nombre,
        )
