from flask import (Blueprint, Response, redirect, render_template, request,
                   session, url_for)

import propiedades.seedwork.presentation.api as api
from propiedades.seedwork.application.queries import execute_query as query
from propiedades.modules.contratos.application.commands.crear_contrato import \
    CrearContrato
from propiedades.modules.contratos.application.mappers import \
    ContratoDTOJsonMapper
from propiedades.seedwork.application.commands import execute_command
from propiedades.modules.contratos.application.services import ContratoService

from propiedades.modules.contratos.application.queries.obtener_contrato import ObtenerContrato

bp: Blueprint = api.create_blueprint("Contrato", "/contratos")


@bp.route("contrato", methods=("POST",))
def crear_contrato():
    contrato_dict = request.json

    map_contrato = ContratoDTOJsonMapper()
    contrato_dto = map_contrato.external_to_dto(contrato_dict)

    comando = CrearContrato(
        contrato_dto.fecha_creacion, contrato_dto.id, contrato_dto.pagos
    )
    execute_command(comando)

    return Response("{}", status=202, mimetype="application/json")

@bp.route("contrato/<id>", methods=("GET",))
def obtener_contrato_id(id=None):
    
    if id:
        query_resultado = query(ObtenerContrato(id))
        map_contrato = ContratoDTOJsonMapper()
        
        return map_contrato.dto_to_external(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
