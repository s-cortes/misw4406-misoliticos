import uuid
from dataclasses import dataclass
import logging

from propiedades.config.uwo import UnitOfWorkASQLAlchemyFactory
from propiedades.modules.propiedades.application.dtos import FotografiaDTO, PropiedadDTO
from propiedades.modules.propiedades.application.mappers import PropiedadMapper
from propiedades.modules.propiedades.infrastructure.repositories import (
    PropiedadesRepository,
)
from propiedades.seedwork.application.commands import Command, execute_command
from propiedades.seedwork.infrastructure.uow import UnitOfWorkPort

from .base import PropiedadBaseCommandHanlder


@dataclass
class RequestCreatePropiedadCommand(Command):
    id: uuid.UUID
    fecha_creacion: str

    tipo_construccion: str
    entidad: str
    fotografias: list[FotografiaDTO]
    geoespacial: dict
    catastral: dict


class RequestCreatePropiedadHandler(PropiedadBaseCommandHanlder):

    def handle(self, command: RequestCreatePropiedadCommand):
        propiedad_dto = PropiedadDTO(
            id=command.id,
            fecha_creacion=command.fecha_creacion,
            fotografias=command.fotografias,
            tipo_construccion=command.tipo_construccion,
            entidad=command.entidad,
            geoespacial=command.geoespacial,
            catastral=command.catastral,
        )

        propiedad = self.propiedad_factory.create(propiedad_dto, PropiedadMapper())
        propiedad.request()

        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        UnitOfWorkPort.register_batch(uowf, None, propiedad)


@execute_command.register(RequestCreatePropiedadCommand)
def execute_request_propiedad_command(command: RequestCreatePropiedadCommand):
    handler = RequestCreatePropiedadHandler()
    return handler.handle(command)
