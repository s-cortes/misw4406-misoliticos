import uuid

from pulsar.schema import *
from seedwork.infrastructure.utils import datetime

class Message(Record):
    id: str = String(default=str(uuid.uuid4()))
    created_at: datetime = DateTime()
