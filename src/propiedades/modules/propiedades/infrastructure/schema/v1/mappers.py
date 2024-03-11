import datetime
from propiedades.modules.propiedades.application.dtos import FotografiaDTO, PropiedadDTO

from propiedades.modules.propiedades.domain.events import (
    CreacionPropiedadSolicitada,
    PropiedadCreada,
)
from propiedades.modules.propiedades.domain.value_objects import Contenido
from propiedades.modules.propiedades.infrastructure.schema.v1.commands import (
    ContenidoPayload,
    PropiedadCreateCommand,
    CreatePropiedadPayload,
    FotografiaPayload,
)
from propiedades.modules.propiedades.infrastructure.schema.v1.events import (
    PropiedadCreadaPayload,
    PropiedadCreatedEvent,
)
from propiedades.seedwork.infrastructure.schema.v1.mappers import IntegrationMapper
from propiedades.seedwork.infrastructure.schema.v1.messages import IntegrationMessage


class PropiedadCreatedEventMapper(IntegrationMapper):
    epoch = datetime.datetime.utcfromtimestamp(0)

    def _unix_time_millis(self, dt):
        return (dt - self.epoch).total_seconds() * 1000.0

    def external_to_message(self, external: PropiedadCreada) -> PropiedadCreatedEvent:
        tiempo = int(self._unix_time_millis(external.fecha_creacion))
        payload: PropiedadCreadaPayload = PropiedadCreadaPayload(
            correlation_id=str(external.correlation_id),
            id_propiedad=str(external.id_propiedad),
            fecha_creacion=tiempo,
        )
        return PropiedadCreatedEvent(data=payload)


class PropiedadCreateCommandMapper(IntegrationMapper):
    epoch = datetime.datetime.utcfromtimestamp(0)

    def _unix_time_millis(self, dt):
        return (dt - self.epoch).total_seconds() * 1000.0

    def external_to_message(
        self, external: CreacionPropiedadSolicitada
    ) -> PropiedadCreateCommand:

        fotografias: list[FotografiaPayload] = list()
        for foto in external.fotografias:
            fotografias.append(
                FotografiaPayload(
                    contenido=ContenidoPayload(
                        valor=foto.contenido.valor,
                        tipo=foto.contenido.tipo,
                    ),
                    descripcion=foto.descripcion,
                    nombre=foto.nombre,
                )
            )

        tiempo = int(self._unix_time_millis(external.fecha_creacion))
        payload = CreatePropiedadPayload(
            id=str(external.id_propiedad),
            fecha_creacion=tiempo,
            tipo_construccion=external.tipo_construccion,
            entidad=external.entidad,
            fotografias=fotografias,
            
        )
        return PropiedadCreateCommand(data=payload)

    def message_to_dto(self, message: PropiedadCreateCommand) -> PropiedadDTO:
        fotografias = list()
        fotografias.extend([self._procesar_fotografias(p) for p in message.data.fotografias])

        return PropiedadDTO(
            fotografias=fotografias,
            entidad=message.data.entidad,
            tipo_construccion=message.data.tipo_construccion,
        )
    
    def _procesar_fotografias(self, payload: FotografiaPayload):
        return FotografiaDTO(
            contenido=payload.contenido.valor,
            tipo=payload.contenido.tipo,
            descripcion=payload.descripcion,
            nombre=payload.nombre,
        )
