import datetime
import logging
from propiedades.modules.geoespacial.infrastructure.schema.v1.commands import (
    ComandoCrearLotePayload,
    CoordenadaPayload,
    DireccionesPayload,
    EdificiosPayload,
    PoligonoPayload,
)

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


class PropiedadCreatedIntegrationEventMapper(IntegrationMapper):
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

        geoespacial = CrearLoteFromDictCommandMapper().external_to_message(
            external.geoespacial
        )
        geoespacial.id_propiedad = str(external.id_propiedad)
        tiempo = int(self._unix_time_millis(external.fecha_creacion))

        payload = CreatePropiedadPayload(
            id=str(external.id_propiedad),
            fecha_creacion=tiempo,
            tipo_construccion=external.tipo_construccion,
            entidad=external.entidad,
            fotografias=fotografias,
            geoespacial=geoespacial,
        )
        logging.error("asdfasdfads----------------------------")
        logging.error(geoespacial.poligono.coordenadas[0].__dict__)
        return PropiedadCreateCommand(data=payload)

    def message_to_dto(self, message: PropiedadCreateCommand) -> PropiedadDTO:
        fotografias = list()
        fotografias.extend(
            [self._procesar_fotografias(p) for p in message.data.fotografias]
        )
        geoespacial = CrearLoteFromDictCommandMapper().message_to_dict(
            message.data.geoespacial
        )

        return PropiedadDTO(
            fotografias=fotografias,
            entidad=message.data.entidad,
            tipo_construccion=message.data.tipo_construccion,
            geoespacial=geoespacial,
        )

    def _procesar_fotografias(self, payload: FotografiaPayload):
        return FotografiaDTO(
            contenido=payload.contenido.valor,
            tipo=payload.contenido.tipo,
            descripcion=payload.descripcion,
            nombre=payload.nombre,
        )


class CrearLoteFromDictCommandMapper(IntegrationMapper):

    def external_to_message(self, external: dict) -> ComandoCrearLotePayload:
        id_propiedad = str(external.get("id_propiedad", ""))
        correlation_id = str(external.get("correlation_id"))
        direccions_list: list[DireccionesPayload] = list()
        edificios_list: list[EdificiosPayload] = list()
        for direccion in external.get("direcciones"):
            direccions_list.append(self._procesar_direccion_external(direccion))

        poligono = self._procesar_poligono_external(external.get("poligono"))

        for edificio in external.get("edificios"):
            edificios_list.append(self._procesar_edificio_external(edificio))

        return ComandoCrearLotePayload(
            id_propiedad=id_propiedad,
            direcciones=direccions_list,
            poligono=poligono,
            edificios=edificios_list,
            correlation_id=correlation_id,
        )

    def _procesar_poligono_external(self, poligono: dict) -> PoligonoPayload:
        coordenadas_dto: list[CoordenadaPayload] = list()

        for coordenada in poligono.get("coordenadas"):
            coordenada_out = CoordenadaPayload(
                latitud=float(coordenada.get("latitud")),
                longitud=float(coordenada.get("longitud")),
            )
            coordenadas_dto.append(coordenada_out)
        return PoligonoPayload(coordenadas=coordenadas_dto)

    def _procesar_direccion_external(self, direccion: dict) -> DireccionesPayload:
        return DireccionesPayload(direccion.get("valor"))

    def _procesar_edificio_external(self, edificio: dict) -> EdificiosPayload:
        return EdificiosPayload(
            poligono=self._procesar_poligono_external(edificio.get("poligono"))
        )

    def message_to_dict(self, message: ComandoCrearLotePayload):
        edificios: list = list()
        
        for e in message.edificios:
            coordenadas = list()
            for coordenada in e.poligono.coordenadas:
                coordenada_dict = dict(latitud=str(coordenada.latitud), longitud=str(coordenada.longitud))
                coordenadas.append(coordenada_dict)
            edificios.append(dict(poligono=dict(coordenadas=coordenadas)))

        poligono = dict(
            coordenadas=[
                dict(latitud=str(p.latitud), longitud=str(p.longitud))
                for p in message.poligono.coordenadas
            ]
        )

        return dict(
            id_propiedad=message.id_propiedad,
            correlation_id=message.correlation_id,
            direcciones=[dict(valor=e.valor) for e in message.direcciones],
            poligono=poligono,
            edificios=edificios,
        )
