import datetime
import logging
import uuid


from propiedades.modules.sagas.infrastructure.dtos import Saga as SagaDTO
from propiedades.modules.sagas.infrastructure.dtos import Transaction as TransactionDTO
from propiedades.modules.sagas.infrastructure.repositories import (
    SagaRepository,
    TransactionRepository,
)

from propiedades.seedwork.application.commands import Command
from propiedades.seedwork.application.sagas import OrchestrationCoordinator
from propiedades.seedwork.application.sagas import End, Start, Step, Transaction
from propiedades.seedwork.domain.events import DomainEvent


class CoordinadorReservas(OrchestrationCoordinator):
    __saga_id = 1

    def start(self, event: DomainEvent, step: SagaDTO):
        created_at = datetime.datetime.utcnow()
        self.persist(Step(event.correlation_id, created_at, step.command, step.id), status='PROCESSED')

    def complete(self, event: DomainEvent, step: SagaDTO):
        created_at = datetime.datetime.utcnow()
        self.persist(Step(event.correlation_id, created_at, step.command, step.id), status='COMPLETED')

    def is_start_transaction(self, step: SagaDTO):
        return step.step == 0

    def is_end_transaction(self, step: SagaDTO):
        return step.is_last

    def get_step(self, event: DomainEvent):
        sagas: list[SagaDTO] = SagaRepository().get_all(self.__saga_id)
        event_name: str = type(event).__name__

        for step in enumerate(sagas):
            if event_name in (step.event, step.error):
                return step

    def persist(self, step: Step, status=None):
        transaction: TransactionDTO = TransactionDTO(
            id=step.saga_id,
            step=step.index,
            correlation_id=step.correlation_id,
            created_at=step.event_date,
            status=status,
        )
        TransactionRepository().append(transaction)

    def build_command(self, event: DomainEvent, tipo_command: type):
        # TODO Transforma un event en la entrada de un command
        # Por ejemplo si el event que llega es ReservaCreada y el tipo_command es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el command PagarReserva
        ...


def handle_saga_messages(event):
    if isinstance(event, DomainEvent):
        logging.error("[Saga] Domain Event received----------------------------------------------------------")
        coordinador = CoordinadorReservas()
        coordinador.process_event(event)
    else:
        raise NotImplementedError("El mensaje no es event de Dominio")
