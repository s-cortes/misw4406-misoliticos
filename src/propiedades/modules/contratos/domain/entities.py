import uuid
import propiedades.modules.contratos.domain.value_objects as vo
from propiedades.seedwork.domain.entities import Entity, RootAggregation
from dataclasses import dataclass, field


@dataclass
class Contrato(RootAggregation):
    id: uuid.UUID = field(hash=True, default=None)
