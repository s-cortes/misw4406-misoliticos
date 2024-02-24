import uuid
from dataclasses import dataclass, field
from datetime import datetime

from .events import DomainEvent
from .exceptions import MutableEntityIdExcepcion
from .mixins import RuleValidationMixin
from .rules import ImmutableEntityIdRule
from entities import Entity

@dataclass
class Entity:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    fecha_creacion: datetime = field(default=datetime.now())
    fecha_actualizacion: datetime = field(default=datetime.now())

    @classmethod
    def next_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not ImmutableEntityIdRule(self).is_valid():
            raise MutableEntityIdExcepcion()
        self._id = self.next_id()


@dataclass
class RootAggregation(Entity, RuleValidationMixin):
    events: list[DomainEvent] = field(default_factory=list)

    def append_event(self, evento: DomainEvent):
        self.events.append(evento)

    def clear_events(self):
        self.events = list()
