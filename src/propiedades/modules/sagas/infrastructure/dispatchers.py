import logging

from pulsar.schema import *

from propiedades.modules.sagas.infrastructure.factories import \
    CommandMessageSagaFactory
from propiedades.seedwork.infrastructure.dispatchers import Dispatcher
from propiedades.seedwork.infrastructure.schema.v1.messages import \
    IntegrationMessage


class SagaCommandDispatcher(Dispatcher):
    def __init__(self, event, command: str):
        self._integration_factory = CommandMessageSagaFactory()
        self._message: IntegrationMessage = self._integration_factory.create(event, command)

    def publish(self, topic):
        schema: AvroSchema = AvroSchema(self._message.__class__)
        logging.error(f"[Sagas] publicando comando {topic}")
        self._publish_message(topic, self._message, schema)
        logging.error("[Sagas] Comando Publicado")
