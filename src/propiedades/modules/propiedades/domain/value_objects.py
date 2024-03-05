from dataclasses import dataclass, field
from enum import Enum

from propiedades.seedwork.domain.value_object import ValueObject


@dataclass(frozen=True)
class Contenido(ValueObject):
    valor: str = field(default_factory=str)
    tipo: str = field(default_factory=str)

class TipoContruccion(Enum):
    RESIDENCIAL = "Residencial"
    COMERCIAL = "Comercial"
    INDUSTRIAL = "Industrial"
    INSTITUCIONAL = "Institucional"


class Entidad(Enum):
    MINORISTA = "Minorista"
    INDUSTRIAL = "Industrial"
    OFICINA = "Oficina"
    ESPECIALISTA = "Especialista"
