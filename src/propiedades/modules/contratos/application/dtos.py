from dataclasses import dataclass, field

from propiedades.seedwork.application.dtos import DTO


@dataclass(frozen=True)
class SampleDTO(DTO):
    tbd: str
