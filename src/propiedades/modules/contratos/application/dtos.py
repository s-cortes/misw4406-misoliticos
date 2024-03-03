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
    tipo_contrato: TipoContratoDTO = field(default_factory=TipoContratoDTO)
    fecha_inicio: FechaInicioDTO = field(default_factory=FechaInicioDTO)
    fecha_terminacion: FechaTerminacionDTO = field(default_factory=FechaTerminacionDTO)
    pago: PagoDTO = field(default_factory=PagoDTO)
    informacion_catastral: InformacionCatastralDTO = field(default_factory=InformacionCatastralDTO)
