from propiedades.config.uwo import UnitOfWorkASQLAlchemyFactory
from propiedades.modules.contratos.application.commands.base import (
    ContratoBaseHandler,
)
from propiedades.modules.contratos.application.dtos import InmuebleDTO, OficinaDTO, PisoDTO
from propiedades.modules.contratos.application.mappers import ContratoMapper
from propiedades.seedwork.application.commands import Command, execute_command
from dataclasses import dataclass, field

from propiedades.seedwork.infrastructure.uow import UnitOfWorkPort
from propiedades.modules.contratos.domain.repositories import RepositorioInmuebles


@dataclass
class CrearInmueble(Command):
    fecha_creacion: str
    id: str
    pisos: list[PisoDTO]


class CrearInmuebleHandler(ContratoBaseHandler):

    def handle(self, comando: CrearInmueble):
        inmueble_dto = InmuebleDTO(
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            pisos=comando.pisos,
        )

        inmueble = self.fabrica_contratos.create(inmueble_dto, ContratoMapper())
        repositorio = self.fabrica_repositorio.create(RepositorioInmuebles.__class__)

        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        UnitOfWorkPort.register_batch(uowf, repositorio.append, inmueble)
        UnitOfWorkPort.commit(uowf)

@execute_command.register(CrearInmueble)
def comando_crear_inmueble(comando: CrearInmueble):
    CrearInmuebleHandler().handle(comando)