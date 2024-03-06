import uuid
import propiedades.modules.contratos.domain.value_objects as vo
from propiedades.seedwork.domain.entities import Entity, RootAggregation
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Pago(vo.ValueObject):
    valor_pago: vo.ValorPago = field(default_factory=vo.ValorPago)
    moneda: vo.Moneda = field(default_factory=vo.Moneda)
    metodo_pago: vo.MetodoPago = field(default_factory=vo.MetodoPago)

@dataclass
class Contrato(RootAggregation):
    id: uuid.UUID = field(hash=True, default=None)
    tipo_contrato: vo.TipoContrato = field(default_factory=vo.TipoContrato)
    fecha_inicio: vo.FechaInicio = field(default_factory=vo.FechaInicio)
    fecha_terminacion: vo.FechaTerminacion = field(default_factory=vo.FechaTerminacion)
    catastral_id: str = field(default_factory=str)
    compania_id: str = field(default_factory=str)
    pagos: list[Pago] = field(default_factory=list[Pago])