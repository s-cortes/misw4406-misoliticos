from dataclasses import dataclass, field
import uuid

from propiedades.seedwork.infrastructure.uow import UnitOfWorkPort
from propiedades.seedwork.application.commands import Command, execute_command
from propiedades.config.uwo import UnitOfWorkASQLAlchemyFactory

from propiedades.modules.geoespacial.application.dtos import DireccionDTO, PoligonoDTO, EdificioDTO, LoteDTO
from propiedades.modules.geoespacial.application.mappers import TestMapper
from propiedades.modules.geoespacial.application.commands.base import GeoespacialBaseHandler
from propiedades.modules.geoespacial.domain.repositories import RepositorioLotes
from propiedades.modules.geoespacial.domain.entities import TestLoteEntity

@dataclass
class CrearTestCommand(Command):
    ...

class CrearTestCommandHandler(GeoespacialBaseHandler):
    def handle(self, comando: CrearTestCommand):
        lote: TestLoteEntity = self.fabrica_geoespacial.create(TestMapper())
        lote.create()
        repositorio = self.fabrica_repositorio.create(RepositorioLotes.__class__)
        

        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        #try:
        UnitOfWorkPort.register_batch(uowf, repositorio.insert, lote)
        UnitOfWorkPort.commit(uowf)
        #except:
        #    print("rollback")
        #   UnitOfWorkPort.rollback(uowf)
    
    @execute_command.register(CrearTestCommand)
    def comando_crear_lote(comando: CrearTestCommand):
        return CrearTestCommandHandler().handle(comando)