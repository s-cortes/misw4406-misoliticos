from flask import (Blueprint, Response, redirect, render_template, request,
                   session, url_for)

import propiedades.seedwork.presentation.api as api
from propiedades.modules.catastrales.application.commands.crear_inmueble import \
    CrearInmueble
from propiedades.modules.catastrales.application.mappers import \
    CatastralDTOJsonMapper
from propiedades.seedwork.application.commands import execute_command

bp: Blueprint = api.crear_blueprint("catastral", "/catastrales")


@bp.route("inmueble", methods=("POST",))
def crear_inmueble():
    inmueble_dict = request.json

    map_inmueble = CatastralDTOJsonMapper()
    inmueble_dto = map_inmueble.external_to_dto(inmueble_dict)

    comando = CrearInmueble(
        inmueble_dto.fecha_creacion, inmueble_dto.id, inmueble_dto.pisos
    )
    execute_command(comando)

    return Response("{}", status=202, mimetype="application/json")
