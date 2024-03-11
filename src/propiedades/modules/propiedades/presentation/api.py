from flask import Blueprint, request
import logging

import propiedades.seedwork.presentation.api as api
from propiedades.modules.propiedades.application.commands.request_create_propiedad import \
    RequestCreatePropiedadCommand
from propiedades.modules.propiedades.application.mappers import \
    PropiedadDTOJsonMapper
from propiedades.modules.propiedades.application.queries.get_propiedad import \
    GetPropiedadQuery
from propiedades.modules.propiedades.application.queries.get_propiedades import \
    GetPropiedadesQuery
from propiedades.seedwork.application.commands import execute_command
from propiedades.seedwork.application.queries import execute_query

bp_prefix = "propiedades"
bp: Blueprint = api.create_blueprint(bp_prefix, "/propiedades")


@bp.route("/", methods=("POST",))
def create():
    propiedad_dict = request.json

    map_propiedad = PropiedadDTOJsonMapper()
    propiedad_dto = map_propiedad.external_to_dto(propiedad_dict)

    logging.error("[Propiedades] create")
    comando = RequestCreatePropiedadCommand(
        id=propiedad_dto.id,
        fecha_creacion=propiedad_dto.fecha_creacion,
        tipo_construccion=propiedad_dto.tipo_construccion,
        entidad=propiedad_dto.entidad, 
        fotografias=propiedad_dto.fotografias,
        geoespacial=propiedad_dto.geoespacial,
        catastral=propiedad_dto.catastral
    )
    logging.error("[Propiedades] create execute")
    execute_command(comando)

    return {}, 202


@bp.route("/", methods=("GET",))
@bp.route("/<id>", methods=("GET",))
def retrieve(id=None):
    map_propiedad = PropiedadDTOJsonMapper()
    query_resultado = None
    if not id:
        query_resultado = execute_query(GetPropiedadesQuery())
        query_resultado = [map_propiedad.dto_to_external(p) for p in query_resultado.result]
    else:
        query_resultado = execute_query(GetPropiedadQuery(id))
        query_resultado = map_propiedad.dto_to_external(query_resultado.result)

    return query_resultado
