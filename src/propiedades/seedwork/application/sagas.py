import datetime
import logging
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass

from propiedades.seedwork.application.commands import Command, execute_command
from propiedades.seedwork.domain.events import DomainEvent


class Step:
    correlation_id: uuid.UUID
    event_date: datetime.datetime
    index: int
    saga_id: int


@dataclass
class Start(Step):
    index: int = 0


@dataclass
class End(Step): ...


@dataclass
class Transaction(Step):

    command: Command
    event: DomainEvent
    error: DomainEvent
    compensation: Command
    exitosa: bool


class SagaCoordinator(ABC):
    correlation_id: uuid.UUID

    @abstractmethod
    def start(event, step): ...

    @abstractmethod
    def persist(self, step): ...

    @abstractmethod
    def publish_command(self, event: DomainEvent, command_type: str, topic: str): ...

    @abstractmethod
    def process_event(self, event: DomainEvent): ...

    @abstractmethod
    def complete(event, step): ...


class OrchestrationCoordinator(SagaCoordinator, ABC):
    steps: list[Step]
    index: int

    @abstractmethod
    def get_step(self, event: DomainEvent):
        raise NotImplementedError()

    @abstractmethod
    def is_start_transaction(self, step):
        raise NotImplementedError()
    
    @abstractmethod
    def is_end_transaction(self, step):
        raise NotImplementedError()

    def process_event(self, event: DomainEvent):
        logging.error("[Sagas] processing event")
        event_type = event.__class__.__name__
        step = self.get_step(event)
        logging.error(step.__dict__)

        
        if self.is_start_transaction(step) and event_type != step.error:
            self.start(event, step)
        if self.is_end_transaction(step) and event_type != step.error:
            self.complete(event, step)
            return
        
        if event_type == step.error:
            self.publish_command(event, step.compensation, step.topic)
        elif event_type == step.event:
            self.publish_command(event, step.command, step.topic)
