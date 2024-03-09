from dataclasses import dataclass, field

from propiedades.seedwork.application.dtos import DTO

@dataclass(frozen=True)
class PagoDTO(DTO):
    valor_pago: float = field(default_factory=float)
    moneda: str = field(default_factory=str)
    metodo_pago: str = field(default_factory=str)

@dataclass(frozen=True)
class ContratoDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    tipo_contrato: str = field(default_factory=str)
    fecha_inicio: str = field(default_factory=str)
    fecha_terminacion: str = field(default_factory=str)
    catastral_id: str = field(default_factory=str)
    compania_id: str = field(default_factory=str)
    pagos: list[PagoDTO] = field(default_factory=list)
