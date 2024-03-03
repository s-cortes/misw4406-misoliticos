from flask import (Blueprint, Response, request)

import propiedades.seedwork.presentation.api as api
from propiedades.modules.contratos.application.commands.crear_contrato import \
    CrearContrato
from propiedades.modules.contratos.application.mappers import \
    ContratosDTOJsonMapper
from propiedades.seedwork.application.commands import execute_command

bp: Blueprint = api.create_blueprint("contratos", "/contratos")


@bp.route("contrato", methods=("POST",))
def crear_contrato():
    contrato_dict = request.json

    map_contrato = ContratosDTOJsonMapper()
    contrato_dto = map_contrato.external_to_dto(contrato_dict)

    comando = CrearContrato(
        contrato_dto.id,
        contrato_dto.tipo_contrato,
        contrato_dto.fecha_inicio,
        contrato_dto.fecha_terminacion,
        contrato_dto.pago,
        contrato_dto.informacion_catastral
    )
    execute_command(comando)

    return Response("{}", status=202, mimetype="application/json")
