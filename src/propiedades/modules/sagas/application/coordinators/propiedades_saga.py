import datetime
import logging
import uuid
from propiedades.modules.sagas.infrastructure.dispatchers import SagaCommandDispatcher


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
        new_step = Step()
        new_step.correlation_id = event.correlation_id
        new_step.event_date = datetime.datetime.utcnow()
        new_step.saga_id = step.id
        new_step.index = step.step
        self.persist(new_step, status=event.__class__.__name__)

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

        for step in sagas:
            if event_name in (step.event, step.error):
                return step

    def persist(self, step: Step, status=None):
        transaction: TransactionDTO = TransactionDTO(
            id=step.saga_id,
            step=step.index,
            correlation_id=step.correlation_id,
            created_at=step.event_date,
            updated_at=step.event_date,
            status=status,
        )
        TransactionRepository().append(transaction)

    def publish_command(self, event: DomainEvent, command_type: str, topic: str):
        dispatcher = SagaCommandDispatcher(event, command_type)
        dispatcher.publish(topic)
        ...


def handle_saga_messages(event):
    if isinstance(event, DomainEvent):
        logging.error("[Saga] Domain Event received----------------------------------------------------------")
        coordinador = CoordinadorReservas()
        coordinador.process_event(event)
    else:
        raise NotImplementedError("El mensaje no es event de Dominio")
