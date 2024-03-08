import pulsar
from pulsar.schema import *

from propiedades.modules.contratos.infrastructure.factories import (
    IntegrationMessageFactory,
)
from propiedades.seedwork.infrastructure.dispatchers import Dispatcher
from propiedades.seedwork.infrastructure.schema.v1.messages import IntegrationMessage


class ContratoDispatcher(Dispatcher):
    def __init__(self, event):
        self._integration_factory = IntegrationMessageFactory()
        self._message: IntegrationMessage = self._integration_factory.create(event)

    def publish(self, topic):
        schema: AvroSchema = AvroSchema(self._message.__class__)
        self._publish_message(topic, self._message, schema)
        print("[Contratos] Mensaje Publicado")
