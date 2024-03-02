from flask import (Blueprint, Response, redirect, render_template, request, session, url_for)
import propiedades.seedwork.presentation.api as api
from propiedades.modules.geoespacial.application.mappers import LoteDTOJsonMapper
from propiedades.modules.geoespacial.application.commands.crear_lote import CrearLote 
from propiedades.seedwork.application.commands import execute_command

bp: Blueprint = api.create_blueprint("geoespacial", "/geoespacial")

@bp.route("lote", methods=("POST",))
def crear_lote():
    lote_dict = request.json
    map_lote = LoteDTOJsonMapper()
    lote_dto = map_lote.external_to_dto(lote_dict)
    comando = CrearLote(
        lote_dto.id, lote_dto.direccion, lote_dto.poligono, lote_dto.edificio
    )
    execute_command(comando) 
    return Response({}, status=200, mimetype="application/json")

@bp.route("lote/<id>", methods=("GET",))
def obtener_lote(id=None):
    #response = 
    return Response("{}", status=200, mimetype="application/json")