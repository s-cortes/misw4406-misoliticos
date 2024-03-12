import datetime

from propiedades.modules.geoespacial.domain.events import LoteCreado
from propiedades.modules.geoespacial.infrastructure.schema.v1.events import (
    EventoLoteCreado, LoteCreadoPayload)
from propiedades.seedwork.infrastructure.schema.v1.mappers import \
    IntegrationMapper
from propiedades.seedwork.infrastructure.schema.v1.messages import IntegrationMessage
from propiedades.modules.geoespacial.application.dtos import LoteDTO , EdificioDTO, PoligonoDTO, DireccionDTO, CoordenadasDTO
from propiedades.modules.geoespacial.infrastructure.schema.v1.commands import ComandoCrearLotePayload, DireccionesPayload, EdificiosPayload, CoordenadaPayload, PoligonoPayload 


class EventoLoteCreadoMapper(IntegrationMapper):
    epoch = datetime.datetime.utcfromtimestamp(0)

    def _unix_time_millis(self, dt):
        return (dt - self.epoch).total_seconds() * 1000.0

    def external_to_message(self, external: LoteCreado) -> EventoLoteCreado:
        #tiempo = int(self._unix_time_millis(external.fecha_creacion))
        payload: LoteCreadoPayload = LoteCreadoPayload(
            id_lote=str(external.id_lote),
            #fecha_creacion=tiempo,
            id_propiedad=str(external.id_propiedad),
            correlation_id=str(external.correlation_id),
            mensaje=str(external.mensaje)
        )
        return EventoLoteCreado(data=payload)
    
class CrearLoteCommandMapper(IntegrationMapper):

    def _procesar_edificio_entity(self, edificio: any) -> EdificiosPayload :
        return EdificiosPayload(
            poligono=self._procesar_poligono_entity(edificio.poligono)
            )

    def _procesar_poligono_entity(self, poligono: any) -> PoligonoPayload :
        coordenadas_dto : list[CoordenadaPayload] = list()

        for coordenada in poligono.coordenadas:
            coordenada_out = CoordenadaPayload(
                latitud=coordenada.latitud, longitud=coordenada.longitud
                )
            coordenadas_dto.append(coordenada_out)
        return PoligonoPayload(coordenadas=coordenadas_dto)

    def _procesar_direccion_entity(self, direccion: any) -> DireccionesPayload:
        return DireccionesPayload(direccion.valor)

    def external_to_message(self, entity:any) -> ComandoCrearLotePayload:
        id_propiedad = str(entity.id_propiedad)
        correlation_id = str(entity.correlation_id)
        direccions_list : list[DireccionesPayload] = list()
        edificios_list : list[EdificiosPayload] = list()
        for direccion in entity.direccion:
            direccions_list.append(self._procesar_direccion_entity(direccion))

        poligono = self._procesar_poligono_entity(entity.poligono)

        for edificio in entity.edificio:
            edificios_list.append(self._procesar_edificio_entity(edificio))

        return ComandoCrearLotePayload(
            id_propiedad=id_propiedad,
            direcciones=direccions_list,
            poligono=poligono,
            edificios=edificios_list,
            correlation_id=correlation_id
        )

    def _procesar_direccion_message(self, direccion: DireccionesPayload) -> DireccionDTO :
        return DireccionDTO(direccion.valor)

    def _procesar_poligono_message(self, poligono: PoligonoPayload) -> PoligonoDTO :
        coordenadas_dto : list[CoordenadasDTO] = list()

        for coordenada in poligono.coordenadas:
            coordenada_out = CoordenadasDTO(coordenada.latitud, coordenada.longitud)
            coordenadas_dto.append(coordenada_out)
        return PoligonoDTO(coordenadas_dto)

    def _procesar_edificio_message(self, edificio: EdificiosPayload) -> EdificioDTO :
        return EdificioDTO(edificio.id, self._procesar_poligono_message(edificio.poligono))

    def message_to_dto(self, external: ComandoCrearLotePayload) -> LoteDTO:
        direccion_dto : list[DireccionDTO] = list()
        
        for direccion in external.direcciones:
            direccion_dto.append(self._procesar_direccion_message(direccion))
        poligono = self._procesar_poligono_message(external.poligono)

        edificio_dto = list[EdificioDTO] = list()
        for edificio in external.edificios:
            edificio_dto.append(self._procesar_edificio_message(edificio))

        return LoteDTO(direccion_dto,poligono,edificio_dto,external.id_propiedad,external.correlation_id)