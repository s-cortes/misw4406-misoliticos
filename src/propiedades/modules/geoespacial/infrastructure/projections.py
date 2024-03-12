
from abc import ABC, abstractmethod
import logging
import traceback
import uuid
from propiedades.modules.geoespacial.application.commands.crear_lote import CrearLote
from propiedades.modules.geoespacial.infrastructure.schema.v1.commands import ComandoCrearLote
from propiedades.modules.geoespacial.infrastructure.schema.v1.mappers import CrearLoteCommandMapper
from propiedades.seedwork.infrastructure.projections import Projection, ProjectionHandler, execute_projection
from propiedades.seedwork.application.commands import execute_command
from propiedades.modules.geoespacial.application.dtos import LoteDTO



class LoteCreateProjection(Projection):

    mapper = CrearLoteCommandMapper()

    def __init__(self, command: ComandoCrearLote) -> None:
        self.dto: LoteDTO = self.mapper.message_to_dto(command.data)

    def execute(self):

        comando = CrearLote(
            id=self.dto.id,
            direccion=self.dto.direccion,
            poligono=self.dto.poligono,
            edificio=self.dto.edificio,
            id_propiedad=self.dto.id_propiedad,
            correlation_id=self.dto.correlation_id
        )
        execute_command(comando)


class LoteCreateProjectionHandler(ProjectionHandler):
    def handle(self, projection: LoteCreateProjection):
        projection.execute()


@execute_projection.register(LoteCreateProjection)
def ejecutar_proyeccion_reserva(proyeccion: LoteCreateProjection, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.test_request_context():
            from flask import request
            handler = LoteCreateProjectionHandler()
            handler.handle(proyeccion)  
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')