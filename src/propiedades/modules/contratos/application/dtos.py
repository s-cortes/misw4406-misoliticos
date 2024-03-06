from dataclasses import dataclass, field

from propiedades.seedwork.application.dtos import DTO

#@dataclass(frozen=True)
#class PagoDTO(DTO):
#    oficinas: list[OficinaDTO]

@dataclass(frozen=True)
class ContratoDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    tipo_contrato: str = field(default_factory=str)
#    pagos: list[PagoDTO] = field(default_factory=list)
