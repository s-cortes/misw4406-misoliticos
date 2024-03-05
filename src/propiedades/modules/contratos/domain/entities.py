import uuid
import propiedades.modules.contratos.domain.value_objects as vo
from propiedades.seedwork.domain.entities import Entity, RootAggregation
from dataclasses import dataclass, field

@dataclass
class Pago(Entity):
    valor_pago: vo.ValorPago = field(default_factory=vo.ValorPago)
    moneda: vo.Moneda = field(default_factory=vo.Moneda)
    metodo_pago: vo.MetodoPago = field(default_factory=vo.MetodoPago)

@dataclass
class Contrato(RootAggregation):
    id: uuid.UUID = field(hash=True, default=None)
    tipo_contrato: vo.TipoContrato = field(default_factory=vo.TipoContrato)
    fecha_inicio: vo.FechaInicio = field(default=None)
    fecha_terminacion: vo.FechaTerminacion = field(default=None)
    pago: Pago = field(default=None)
    informacion_catastral: str = field(default=None)
