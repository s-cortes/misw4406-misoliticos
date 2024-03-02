from flask import (Blueprint, Response, redirect, render_template, request,
                   session, url_for)

import propiedades.seedwork.presentation.api as api
from propiedades.seedwork.application.queries import execute_query as query
from propiedades.modules.catastrales.application.commands.crear_inmueble import \
    CrearInmueble
from propiedades.modules.catastrales.application.mappers import \
    CatastralDTOJsonMapper
from propiedades.seedwork.application.commands import execute_command
from propiedades.modules.catastrales.application.services import InmuebleService

from propiedades.modules.catastrales.application.queries.obtener_inmueble import ObtenerInmueble

bp: Blueprint = api.create_blueprint("catastral", "/catastrales")


@bp.route("inmueble", methods=("POST",))
def crear_inmueble():
    inmueble_dict = request.json

    map_inmueble = CatastralDTOJsonMapper()
    inmueble_dto = map_inmueble.external_to_dto(inmueble_dict)

    comando = CrearInmueble(
        inmueble_dto.fecha_creacion, inmueble_dto.id, inmueble_dto.pisos
    )
    data = execute_command(comando)

    return Response(dict(data), status=202, mimetype="application/json")

@bp.route("inmueble/<id>", methods=("GET",))
def obtener_inmueble_id(id=None):
    
    if id:
        query_resultado = query(ObtenerInmueble(id))
        map_inmueble = CatastralDTOJsonMapper()
        
        return map_inmueble.dto_to_external(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]