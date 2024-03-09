from abc import ABC, abstractmethod
import traceback

import pulsar
from pulsar.schema import *
import logging

from .utils import brocker_host
from pulsar.schema import AvroSchema
from .utils import broker_host


class Dispatcher(ABC):

    def _publish_message(self, topic, message, schema: AvroSchema):
        client = None
        try:
            client = pulsar.Client(f"pulsar://{broker_host()}:6650") 
            publicador = client.create_producer(topic, schema=schema)
            publicador.send(message)
            client.close()
        except:
            logging.error('ERROR: Publicando al tópico de eventos!')
            traceback.print_exc()
            if client:
                client.close() 

    @abstractmethod
    def publish(self, topic):
        raise NotImplementedError       