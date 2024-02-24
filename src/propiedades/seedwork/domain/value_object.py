from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject: ...


@dataclass(frozen=True)
class Coordenada(ABC, ObjetoValor):
    posicion_x: float
    posicion_y: float


@dataclass(frozen=True)
class Poligono(ABC, ObjetoValor):
    coordenadas: list[Coordenada]
