from dataclasses import dataclass, field
import uuid

from propiedades.seedwork.infrastructure.uow import UnitOfWorkPort
from propiedades.seedwork.application.commands import Command, execute_command
from propiedades.config.uwo import UnitOfWorkASQLAlchemyFactory

from propiedades.modules.geoespacial.application.dtos import DireccionDTO, PoligonoDTO, EdificioDTO, LoteDTO
from propiedades.modules.geoespacial.application.mappers import GeoespacialMapper
from propiedades.modules.geoespacial.application.commands.base import GeoespacialBaseHandler
from propiedades.modules.geoespacial.domain.repositories import RepositorioLotes
from propiedades.modules.geoespacial.domain.entities import Lote

@dataclass
class CrearLote(Command):
    #fecha_creacion: str #evaluar si insertar y una para actualizar
    id: uuid.UUID
    direccion: list[DireccionDTO]
    poligono: PoligonoDTO
    edificio: list[EdificioDTO]
    id_propiedad: str
    id_coorelacion: str

class CrearLoteHandler(GeoespacialBaseHandler):
    def handle(self, comando: CrearLote):
        lote_dto = LoteDTO(
            id=comando.id,
            direccion=comando.direccion,
            poligono=comando.poligono,
            edificio=comando.edificio,
            id_propiedad=comando.id_propiedad,
            id_coorelacion=comando.id_coorelacion
        )

        lote: Lote = self.fabrica_geoespacial.create(lote_dto, GeoespacialMapper())
        lote.create()
        repositorio = self.fabrica_repositorio.create(RepositorioLotes.__class__)
        

        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        #try:
        UnitOfWorkPort.register_batch(uowf, repositorio.append, lote)
        UnitOfWorkPort.commit(uowf)
        #except:
        #    print("rollback")
        #   UnitOfWorkPort.rollback(uowf)
    
    @execute_command.register(CrearLote)
    def comando_crear_lote(comando: CrearLote):
        return CrearLoteHandler().handle(comando)