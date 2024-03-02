from dataclasses import dataclass, field
from propiedades.seedwork.domain.value_object import ValueObject

@dataclass(frozen=True)
class Coordenada(ValueObject):
    latitud: float
    longitud: float

@dataclass(frozen=True)
class Direccion(ValueObject):
    valor: str

@dataclass(frozen=True)
class Poligono(ValueObject):
    coordenadas: list[Coordenada]