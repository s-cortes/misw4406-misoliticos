
from abc import ABC, abstractmethod
import logging
import traceback
import uuid
from propiedades.modules.propiedades.application.commands.create_propiedad import CreatePropiedadCommand
from propiedades.modules.propiedades.infrastructure.schema.v1.commands import PropiedadCreateCommand
from propiedades.modules.propiedades.infrastructure.schema.v1.mappers import PropiedadCreateCommandMapper
from propiedades.seedwork.infrastructure.projections import Projection, ProjectionHandler, execute_projection
from propiedades.seedwork.application.commands import execute_command
from propiedades.modules.propiedades.application.dtos import PropiedadDTO



class PropiedadCreateProjection(Projection):

    mapper = PropiedadCreateCommandMapper()

    def __init__(self, command: PropiedadCreateCommand) -> None:
        self.dto: PropiedadDTO = self.mapper.message_to_dto(command)
        self.correlation_id = uuid.uuid4()

    def execute(self):

        comando = CreatePropiedadCommand(
            correlation_id=self.correlation_id,
            id=self.dto.id,
            fecha_creacion=self.dto.fecha_creacion,
            tipo_construccion=self.dto.tipo_construccion,
            entidad=self.dto.entidad, 
            fotografias=self.dto.fotografias
        )
        execute_command(comando)


class PropiedadCreateProjectionHandler(ProjectionHandler):
    def handle(self, projection: PropiedadCreateProjection):
        projection.execute()


@execute_projection.register(PropiedadCreateProjection)
def ejecutar_proyeccion_reserva(proyeccion: PropiedadCreateProjection, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.test_request_context():
            from flask import request
            handler = PropiedadCreateProjectionHandler()
            handler.handle(proyeccion)  
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')