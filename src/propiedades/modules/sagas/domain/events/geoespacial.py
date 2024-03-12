from dataclasses import dataclass

from propiedades.seedwork.domain.events import DomainEvent


@dataclass
class GeoespacialCreado(DomainEvent):
    id_propiedad: str= None
    correlation_id: str = None
    id_lote: str = None
    mensaje: str = None