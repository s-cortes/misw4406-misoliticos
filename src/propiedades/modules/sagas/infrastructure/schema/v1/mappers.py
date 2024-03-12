from propiedades.modules.geoespacial.infrastructure.schema.v1.commands import (
    ComandoCrearLotePayload,
    CoordenadaPayload,
    DireccionesPayload,
    EdificiosPayload,
    PoligonoPayload,
)
from propiedades.seedwork.infrastructure.schema.v1.mappers import IntegrationMapper


class CrearLoteSagaCommandMapper(IntegrationMapper):

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
                coordenada_dict = dict(
                    latitud=str(coordenada.latitud), longitud=str(coordenada.longitud)
                )
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
