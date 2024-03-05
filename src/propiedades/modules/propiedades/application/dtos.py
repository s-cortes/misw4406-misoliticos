from dataclasses import dataclass, field

from propiedades.seedwork.application.dtos import DTO


@dataclass(frozen=True)
class FotografiaDTO(DTO):
    contenido: str = field(default_factory=str)
    tipo: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    nombre: str = field(default_factory=str)



@dataclass(frozen=True)
class PropiedadDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)

    fotografias: list[FotografiaDTO] = field(default_factory=list)
    tipo_construccion: str = field(default_factory=str)
    entidad: str = field(default_factory=str)
