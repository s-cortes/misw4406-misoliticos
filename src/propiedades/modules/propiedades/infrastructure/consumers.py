import logging

import _pulsar
import pulsar
from pulsar.schema import *

from propiedades.modules.propiedades.infrastructure.schema.v1.commands import \
    PropiedadCreateCommand
from propiedades.modules.propiedades.infrastructure.schema.v1.events import \
    PropiedadCreatedEvent
from propiedades.seedwork.infrastructure import utils
from propiedades.modules.propiedades.infrastructure.projections import PropiedadCreateProjection, execute_projection

def subscribe_to_events():
    client = None
    try:
        client = pulsar.Client(
            f"pulsar://{utils.broker_host()}:6650", connection_timeout_ms=5000
        )
        consumer = client.subscribe(
            "propiedades-events",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="propiedades-sub-eventos",
            schema=AvroSchema(PropiedadCreatedEvent),
        )

        logging.error("[Propiedades] Inicinando consumo")

        while True:
            mensaje = consumer.receive()
            logging.error(
                f"[Propiedades] Evento Recibido Subscripcion {mensaje.value().data}"
            )

            consumer.acknowledge(mensaje)

        client.close()
    except Exception as error:
        logging.error("[Propiedades] ERROR: Suscribiendose al tópico de eventos!")
        logging.exception(error)
        if client:
            client.close()


def subscribe_to_commands(app=None):
    client = None
    try:
        client = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        consumer = client.subscribe(
            "propiedades-commands",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="propiedades-sub-comandos",
            schema=AvroSchema(PropiedadCreateCommand),
        )

        while True:
            command = consumer.receive()
            logging.error(f"Comando recibido: {command.value().data}")
            execute_projection(PropiedadCreateProjection(command.value()), app=app)
            consumer.acknowledge(command)

        client.close()
    except Exception as error:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        logging.exception(error)
        if client:
            client.close()
