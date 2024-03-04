from propiedades.config.uwo import UnitOfWorkASQLAlchemyFactory
from propiedades.modules.contratos.application.commands.base import ContratosBaseHandler
from propiedades.modules.contratos.application.dtos import *
from propiedades.modules.contratos.application.mappers import ContratosMapper
from propiedades.seedwork.application.commands import Command, execute_command
from dataclasses import dataclass
from propiedades.seedwork.infrastructure.uow import UnitOfWorkPort
from propiedades.modules.contratos.domain.repositories import RepositorioContratos


@dataclass
class CrearContrato(Command):
    id: str
    tipo_contrato: TipoContratoDTO
    fecha_inicio: FechaInicioDTO
    fecha_terminacion: FechaTerminacionDTO
    pago: PagoDTO
    informacion_catastral: InformacionCatastralDTO

class CrearContratosHandler(ContratosBaseHandler):

    def handle(self, comando: CrearContrato):
        contrato_dto = ContratoDTO(
            comando.id,
            comando.tipo_contrato,
            comando.fecha_inicio,
            comando.fecha_terminacion,
            comando.pago,
            comando.informacion_catastral
        )

        contrato = self._fabrica_contratos.create(contrato_dto, ContratosMapper())
        repositorio = self.fabrica_repositorio.create(RepositorioContratos.__class__)

        uowf: UnitOfWorkASQLAlchemyFactory = UnitOfWorkASQLAlchemyFactory()
        UnitOfWorkPort.register_batch(uowf, repositorio.append, contrato)
        UnitOfWorkPort.commit(uowf)

@execute_command.register(CrearContrato)
def comando_crear_contrato(comando: CrearContrato):
    CrearContratosHandler().handle(comando)