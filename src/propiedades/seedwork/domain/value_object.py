from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject: ...


@dataclass(frozen=True)
class Coordenada(ABC, ValueObject):
    posicion_x: float
    posicion_y: float


@dataclass(frozen=True)
class Poligono(ABC, ValueObject):
    coordenadas: 'list[Coordenada]'
