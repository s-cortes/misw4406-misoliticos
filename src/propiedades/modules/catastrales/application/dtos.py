from dataclasses import dataclass, field

from propiedades.seedwork.application.dtos import DTO


@dataclass(frozen=True)
class UbicacionInternaDTO(DTO):
    nombre: str
    division_visible: str
    telefono: str


@dataclass(frozen=True)
class AreaDTO(DTO):
    valor: float
    unidad: str


@dataclass(frozen=True)
class OficinaDTO(DTO):
    id: str = field(default_factory=str)
    area: AreaDTO
    ubicacion: UbicacionInternaDTO


@dataclass(frozen=True)
class PisoDTO(DTO):
    oficinas: list[OficinaDTO]


@dataclass(frozen=True)
class InmuebleDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)

    pisos: list[PisoDTO] = field(default_factory=list)
