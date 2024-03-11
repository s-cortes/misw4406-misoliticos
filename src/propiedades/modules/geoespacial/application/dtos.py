from dataclasses import dataclass, field
from propiedades.seedwork.application.dtos import DTO

@dataclass(frozen = True)
class CoordenadasDTO(DTO):
    latitud: float
    longitud: float

@dataclass(frozen = True)
class PoligonoDTO(DTO):
    coordenadas: list[CoordenadasDTO]

@dataclass(frozen = True)
class DireccionDTO(DTO):
    valor: str

@dataclass(frozen = True)
class EdificioDTO(DTO):
    poligono: PoligonoDTO
    id: str = field(default_factory=str)

@dataclass(frozen = True)
class LoteDTO(DTO):
    direccion: list[DireccionDTO]
    poligono: PoligonoDTO
    edificio: list[EdificioDTO]
    id_propiedad: str = field(default_factory=str)
    id: str = field(default_factory=str)