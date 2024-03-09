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
    area: AreaDTO
    ubicacion: UbicacionInternaDTO
    id: str = field(default_factory=str)

@dataclass(frozen=True)
class PisoDTO(DTO):
    oficinas: List[OficinaDTO]


@dataclass(frozen=True)
class InmuebleDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)

    pisos: List[PisoDTO] = field(default_factory=list)
