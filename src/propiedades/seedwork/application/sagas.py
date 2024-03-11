import datetime
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
    def build_command(self, event: DomainEvent, command_type: str) -> Command: ...

    def publish_command(self, event: DomainEvent, command_type: str):
        command = self.build_command(event, command_type)
        execute_command(command)

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
        step = self.get_step(event)
        
        if self.is_start_transaction(step) and not isinstance(event, step.error):
            self.start(event, step)
        if self.is_end_transaction(step) and not isinstance(event, step.error):
            self.complete(event, step)
        
        if isinstance(event, step.error):
            self.publish_command(event, step.compensation)
        elif isinstance(event, step.event):
            self.publish_command(event, step.command)
