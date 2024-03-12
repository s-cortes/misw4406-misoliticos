from flask import (Blueprint, Response, redirect, render_template, request, session, url_for)
import propiedades.seedwork.presentation.api as api
from propiedades.modules.geoespacial.application.mappers import LoteDTOJsonMapper, GeoespacialMapper
from propiedades.modules.geoespacial.application.commands.crear_lote import CrearLote 
from propiedades.modules.geoespacial.application.queries.obtener_lote import ObtenerLote
from propiedades.seedwork.application.commands import execute_command
from propiedades.seedwork.application.queries import execute_query as query

bp: Blueprint = api.create_blueprint("geoespacial", "/geoespacial")

@bp.route("lote", methods=("POST",))
def crear_lote():
    lote_dict = request.json
    map_lote = LoteDTOJsonMapper()
    lote_dto = map_lote.external_to_dto(lote_dict)
    comando = CrearLote(
        lote_dto.id, lote_dto.direccion, lote_dto.poligono, lote_dto.edificio, id_propiedad=None, correlation_id=None
    )
    execute_command(comando) 
    return Response({}, status=200, mimetype="application/json")

@bp.route("lote", methods=("GET",))
def obtener_todos_lotes():
    #query_resultado = query(ObtenerLotes())
    #map_lote = LoteDTOJsonMapper()
    #return map_lote.dto_to_external(query_resultado.resultado)
    return Response({}, status=501, mimetype="application/json")

@bp.route("lote/<id>", methods=("GET",))
def obtener_lote(id=None):
    if id:
        query_resultado = query(ObtenerLote(id))
        map_lote = LoteDTOJsonMapper()
        return map_lote.dto_to_external(query_resultado.result)
    else:
        return [{'message':'GET!'}]
