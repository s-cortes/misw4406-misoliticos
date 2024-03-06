from propiedades.config.uwo import UnitOfWorkASQLAlchemyFactory
from propiedades.modules.contratos.application.commands.base import (
    ContratoBaseHandler,
)
from propiedades.modules.contratos.application.dtos import ContratoDTO
from propiedades.modules.contratos.application.mappers import ContratoMapper
from propiedades.seedwork.application.commands import Command, execute_command
from dataclasses import dataclass, field

from propiedades.seedwork.infrastructure.uow import UnitOfWorkPort
from propiedades.modules.contratos.domain.repositories import RepositorioContratos


@dataclass
class CrearContrato(Command):
    fecha_creacion: str
    id: str
    tipo_contrato: str
    fecha_inicio: str
    fecha_terminacion: str
    catastral_id: str
    compania_id: str
#    pagos: list[PagoDTO]


class CrearContratoHandler(ContratoBaseHandler):

    def handle(self, comando: CrearContrato):
        contrato_dto = ContratoDTO(
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            tipo_contrato=comando.tipo_contrato,
            fecha_inicio=comando.fecha_inicio,
            fecha_terminacion=comando.fecha_terminacion,
            catastral_id=comando.catastral_id,
            compania_id=comando.compania_id,
        )

        contrato = self.fabrica_contratos.create(contrato_dto, ContratoMapper())
        repositorio = self.fabrica_repositorio.create(RepositorioContratos.__class__)

        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        UnitOfWorkPort.register_batch(uowf, repositorio.append, contrato)
        UnitOfWorkPort.commit(uowf)

@execute_command.register(CrearContrato)
def comando_crear_contrato(comando: CrearContrato):
    CrearContratoHandler().handle(comando)