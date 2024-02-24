from propiedades.config.uwo import UnitOfWorkASQLAlchemyFactory
from propiedades.modules.catastrales.application.commands.base import (
    CatastralBaseHandler,
)
from propiedades.modules.catastrales.application.dtos import InmuebleDTO, OficinaDTO
from propiedades.modules.catastrales.application.mappers import CatastralMapper
from propiedades.seedwork.application.commands import Command, execute_command
from dataclasses import dataclass, field

from propiedades.seedwork.infrastructure.uow import UnitOfWorkPort


@dataclass
class CrearInmueble(Command):
    fecha_creacion: str
    id: str
    oficinas: list[OficinaDTO]


class CrearInmuebleHandler(CatastralBaseHandler):

    def handle(self, comando: CrearInmueble):
        inmueble_dto = InmuebleDTO(
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            oficinas=comando.oficinas,
        )

        inmueble = self.fabrica_catastrales.create(inmueble_dto, CatastralMapper)
        # repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)

        # uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        # UnitOfWorkPort.register_batch(uowf, repositorio.agregar, inmueble)
        # UnitOfWorkPort.commit(uowf)

@execute_command.register(CrearInmueble)
def comando_crear_inmueble(comando: CrearInmueble):
    CrearInmuebleHandler().handle(comando)