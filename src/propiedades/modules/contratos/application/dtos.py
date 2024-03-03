from dataclasses import dataclass, field
from propiedades.seedwork.application.dtos import DTO

@dataclass(frozen=True)
class TipoContratoDTO(DTO):
    tipo: str

@dataclass(frozen=True)
class FechaInicioDTO(DTO):
    fecha: str

@dataclass(frozen=True)
class FechaTerminacionDTO(DTO):
    fecha: str

@dataclass(frozen=True)
class ValorPagoDTO(DTO):
    valor: float

@dataclass(frozen=True)
class MonedaDTO(DTO):
    moneda: str

@dataclass(frozen=True)
class MetodoPagoDTO(DTO):
    metodo: str

@dataclass(frozen=True)
class PagoDTO(DTO):
    valor_pago: ValorPagoDTO
    moneda: MonedaDTO
    metodo_pago: MetodoPagoDTO


@dataclass(frozen=True)
class InformacionCatastralDTO(DTO):
    id: str

@dataclass(frozen=True)
class ContratoDTO(DTO):
    id: str = field(default_factory=str)
    tipo_contrato: TipoContratoDTO
    fecha_inicio: FechaInicioDTO
    fecha_terminacion: FechaTerminacionDTO
    pago: PagoDTO
    informacion_catastral: InformacionCatastralDTO
