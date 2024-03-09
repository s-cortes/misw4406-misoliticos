import datetime

from propiedades.modules.geoespacial.domain.events import LoteCreado
from propiedades.modules.geoespacial.infrastructure.schema.v1.events import (
    EventoLoteCreado, LoteCreadoPayload)
from propiedades.seedwork.infrastructure.schema.v1.mappers import \
    IntegrationMapper


class EventoLoteCreadoMapper(IntegrationMapper):
    epoch = datetime.datetime.utcfromtimestamp(0)

    def _unix_time_millis(self, dt):
        return (dt - self.epoch).total_seconds() * 1000.0

    def external_to_message(self, external: LoteCreado) -> EventoLoteCreado:
        tiempo = int(self._unix_time_millis(external.fecha_creacion))
        payload: LoteCreadoPayload = LoteCreadoPayload(
            id_lote=str(external.id_lote),
            fecha_creacion=tiempo,
        )
        return EventoLoteCreado(data=payload)