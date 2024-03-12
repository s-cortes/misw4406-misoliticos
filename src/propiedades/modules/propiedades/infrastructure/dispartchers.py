import pulsar
from pulsar.schema import *
import logging


from propiedades.modules.propiedades.infrastructure.factories import (
    CommandMessageFactory,
    IntegrationMessageFactory,
)
from propiedades.seedwork.domain.events import DomainEvent
from propiedades.seedwork.infrastructure.dispatchers import Dispatcher
from propiedades.seedwork.infrastructure.schema.v1.messages import IntegrationMessage


class PropiedadEventDispatcher(Dispatcher):
    def __init__(self, event):
        self._integration_factory = IntegrationMessageFactory()
        self._message: IntegrationMessage = self._integration_factory.create(event)

    def publish(self, topic):
        schema: AvroSchema = AvroSchema(self._message.__class__)
        self._publish_message(topic, self._message, schema)
        logging.error(f"[Propiedades] Mensaje Publicado {self._message}")


class PropiedadCommandDispatcher(Dispatcher):
    def __init__(self, event):
        self._integration_factory = CommandMessageFactory()
        self._message: IntegrationMessage = self._integration_factory.create(event)

    def publish(self, topic):
        schema: AvroSchema = AvroSchema(self._message.__class__)
        self._publish_message(topic, self._message, schema)
        logging.error("[Propiedades] Comando Publicado")
