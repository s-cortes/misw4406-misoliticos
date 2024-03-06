from propiedades.modules.propiedades.application.dtos import FotografiaDTO, PropiedadDTO
from propiedades.modules.propiedades.domain.entities import Propiedad, Fotografia
from propiedades.modules.propiedades.domain.value_objects import Contenido
from propiedades.seedwork.application.dtos import Mapper as ApplicationMapper
from propiedades.seedwork.domain.repositories import Mapper as RepositoryMapper


class PropiedadDTOJsonMapper(ApplicationMapper):

    def _procesar_fotografias(self, fotografia) -> FotografiaDTO:
        contenido = fotografia.get("contenido")
        tipo = fotografia.get("tipo")
        descripcion = fotografia.get("descripcion")
        nombre = fotografia.get("nombre")

        return FotografiaDTO(contenido, tipo, descripcion, nombre)

    def external_to_dto(self, external: any) -> PropiedadDTO:
        fotografias_dto: list[FotografiaDTO] = list()
        for foto in external.get("fotografias", list()):
            fotografias_dto.append(self._procesar_fotografias(foto))

        propiedad_dto = PropiedadDTO(
            id=external.get("id"),
            fecha_creacion=external.get("fecha_creacion"),
            tipo_construccion=external.get("tipo_construccion"),
            entidad=external.get("entidad"),
            fotografias=fotografias_dto,
        )
        return propiedad_dto

    def dto_to_external(self, dto: PropiedadDTO) -> any:
        return dto.__dict__


class PropiedadMapper(RepositoryMapper):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def _procesar_fotografias(self, dto: FotografiaDTO):
        return Fotografia(
            contenido=Contenido(dto.contenido, dto.tipo),
            descripcion=dto.descripcion,
            nombre=dto.nombre,
        )

    def entity_to_dto(self, entity: Propiedad) -> PropiedadDTO:
        fecha_creacion = entity.fecha_creacion.strftime(self._FORMATO_FECHA)
        _id = str(entity.id)
        fotografias: list[FotografiaDTO] = list()

        for foto in entity.fotografias:
            fotografias.append(
                FotografiaDTO(
                    contenido=foto.contenido.valor,
                    tipo=foto.contenido.tipo,
                    descripcion=foto.descripcion,
                    nombre=foto.nombre,
                )
            )

        return PropiedadDTO(_id, fecha_creacion, fotografias)

    def dto_to_entity(self, dto: PropiedadDTO) -> Propiedad:
        fotografias = list()
        fotografias.extend([self._procesar_fotografias(p) for p in dto.fotografias])

        return Propiedad(
            fotografias=fotografias,
            entidad=dto.entidad,
            tipo_construccion=dto.tipo_construccion,
        )

    def type(self) -> type:
        return Propiedad.__class__
