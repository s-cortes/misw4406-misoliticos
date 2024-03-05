from dataclasses import dataclass, field

from propiedades.seedwork.infrastructure.uow import UnitOfWorkPort
from propiedades.seedwork.application.commands import Command, execute_command
from propiedades.config.uwo import UnitOfWorkASQLAlchemyFactory

from propiedades.modules.geoespacial.application.dtos import DireccionDTO, PoligonoDTO, EdificioDTO, LoteDTO
from propiedades.modules.geoespacial.application.mappers import GeoespacialMapper
from propiedades.modules.geoespacial.application.commands.base import GeoespacialBaseHandler
from propiedades.modules.geoespacial.domain.repositories import RepositorioLotes

@dataclass
class CrearLote(Command):
    #fecha_creacion: str #evaluar si insertar y una para actualizar
    id: str
    direccion: list[DireccionDTO]
    poligono: PoligonoDTO
    edificio: list[EdificioDTO]

class CrearLoteHandler(GeoespacialBaseHandler):
    def handle(self, comando: CrearLote):
        lote_dto = LoteDTO(
            id=comando.id,
            direccion=comando.direccion,
            poligono=comando.poligono,
            edificio=comando.edificio
        )

        lote = self.fabrica_geoespacial.create(lote_dto, GeoespacialMapper())
        repositorio = self.fabrica_repositorio.create(RepositorioLotes.__class__)

        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        UnitOfWorkPort.register_batch(uowf, repositorio.append, lote)
        UnitOfWorkPort.commit(uowf)
    
    @execute_command.register(CrearLote)
    def comando_crear_lote(comando: CrearLote):
        CrearLoteHandler().handle(comando)