from propiedades.config.uwo import UnitOfWorkASQLAlchemyFactory
from propiedades.modules.catastrales.application.commands.base import (
    CatastralBaseHandler,
)
from propiedades.modules.catastrales.application.dtos import InmuebleDTO, OficinaDTO, PisoDTO
from propiedades.modules.catastrales.application.mappers import CatastralMapper
from propiedades.seedwork.application.commands import Command, execute_command
from dataclasses import dataclass, field

from propiedades.seedwork.infrastructure.uow import UnitOfWorkPort
from propiedades.modules.catastrales.domain.repositories import RepositorioInmuebles


@dataclass
class CrearInmueble(Command):
    fecha_creacion: str
    id: str
    pisos: list[PisoDTO]


class CrearInmuebleHandler(CatastralBaseHandler):

    def handle(self, comando: CrearInmueble):
        inmueble_dto = InmuebleDTO(
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            pisos=comando.pisos,
        )

        inmueble = self.fabrica_catastrales.create(inmueble_dto, CatastralMapper())
        repositorio = self.fabrica_repositorio.create(RepositorioInmuebles.__class__)

        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        UnitOfWorkPort.register_batch(uowf, repositorio.append, inmueble)
        UnitOfWorkPort.commit(uowf)

@execute_command.register(CrearInmueble)
def comando_crear_inmueble(comando: CrearInmueble):
    CrearInmuebleHandler().handle(comando)