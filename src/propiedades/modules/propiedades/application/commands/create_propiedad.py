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
    id: uuid.UUID
    fecha_creacion: str

    tipo_construccion: str
    entidad: str
    fotografias: list[FotografiaDTO]


class CreatePropiedadHandler(PropiedadBaseCommandHanlder):

    def handle(self, command: CreatePropiedadCommand):
        propiedad_dto = PropiedadDTO(
            id=command.id,
            fecha_creacion=command.fecha_creacion,
            fotografias=command.fotografias,
            tipo_construccion=command.tipo_construccion,
            entidad=command.entidad,
        )

        propiedad = self.propiedad_factory.create(propiedad_dto, PropiedadMapper())
        propiedad.create()

        repository: PropiedadesRepository = self.repository_factory.create(
            PropiedadesRepository.__class__
        )
        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        
        try:
            UnitOfWorkPort.register_batch(uowf, repository.append, propiedad)
            UnitOfWorkPort.commit(uowf)
        except:
            UnitOfWorkPort.rollback(uowf)


@execute_command.register(CreatePropiedadCommand)
def execute_get_propiedad_command(command: CreatePropiedadCommand):
    handler = CreatePropiedadHandler()
    return handler.handle(command)
