import uuid
import propiedades.modules.contratos.domain.value_objects as vo
from propiedades.seedwork.domain.entities import Entity, RootAggregation
from dataclasses import dataclass, field

@dataclass
class Pago(Entity):
    valor_pago: float = field(default_factory=float)
    moneda: str = field(default_factory=str)
    metodo_pago: str = field(default_factory=str)

@dataclass
class Contrato(RootAggregation):
    id: uuid.UUID = field(hash=True, default=None)
    tipo_contrato: vo.TipoContrato = field(default_factory=vo.TipoContrato)
    fecha_inicio: vo.FechaInicio = field(default=None)
    fecha_terminacion: vo.FechaTerminacion = field(default=None)
    pago: Pago = field(default=None)
    informacion_catastral: str = field(default=None)
