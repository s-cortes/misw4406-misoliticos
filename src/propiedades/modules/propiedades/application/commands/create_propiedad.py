import logging
import uuid
from dataclasses import dataclass

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
class CreatePropiedadCommand(Command):
    correlation_id: uuid.UUID
    id: uuid.UUID
    fecha_creacion: str

    tipo_construccion: str
    entidad: str
    fotografias: list[FotografiaDTO]
    geoespacial: dict
    catastral: dict


class CreatePropiedadHandler(PropiedadBaseCommandHanlder):

    def handle(self, command: CreatePropiedadCommand):
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
        propiedad.create(command.correlation_id)

        repository: PropiedadesRepository = self.repository_factory.create(
            PropiedadesRepository.__class__
        )
        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        
        try:
            UnitOfWorkPort.register_batch(uowf, repository.append, propiedad)
            UnitOfWorkPort.commit(uowf)
        except Exception as ex:
            logging.error("[Propiedades] error creando propiedad")
            logging.exception(ex)
            UnitOfWorkPort.rollback(uowf)


@execute_command.register(CreatePropiedadCommand)
def execute_create_propiedad_command(command: CreatePropiedadCommand):
    logging.error("[Propiedades] execute_create_propiedad_command")
    handler = CreatePropiedadHandler()
    return handler.handle(command)
