import datetime

from propiedades.modules.contratos.domain.events import ContratoCreado
from propiedades.modules.contratos.infrastructure.schema.events import (
    EventoContratoCreado, ContratoCreadoPayload)
from propiedades.seedwork.infrastructure.schema.v1.mappers import IntegrationMapper


class EventoContratoCreadoMapper(IntegrationMapper):
    epoch = datetime.datetime.utcfromtimestamp(0)

    def _unix_time_millis(self, dt):
        return (dt - self.epoch).total_seconds() * 1000.0

    def external_to_message(self, external: ContratoCreado) -> EventoContratoCreado:
        tiempo = int(self._unix_time_millis(external.fecha_creacion))
        payload: ContratoCreadoPayload = ContratoCreadoPayload(
            id_contrato=str(external.id_propiedad),
            fecha_creacion=tiempo,
        )
        return EventoContratoCreado(data=payload)
