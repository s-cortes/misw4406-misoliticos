import logging
import traceback

import _pulsar
import pulsar
from pulsar.schema import *

from propiedades.modules.contratos.infrastructure.schema.events import EventoContratoCreado
from propiedades.seedwork.infrastructure import utils


def subscribe_to_events():
    cliente = None
    try:
        logging.error("[Contratos] Inicinando Subscripcion")
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650",connection_timeout_ms=5000)
        consumidor = cliente.subscribe(
            "contrato-events",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="contratos-sub-eventos",
            schema=AvroSchema(EventoContratoCreado),
        )

        logging.error("[Contratos] Inicinando consumo")

        while True:
            mensaje = consumidor.receive()
            logging.error(f"[Contratos] Evento Recibido Subscripcion {mensaje.value().data}")

            print(f"[Contratos] Evento recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)

            cliente.close()
    except Exception as error:
        logging.error("[Contratos] ERROR: Suscribiendose al tópico de eventos!")
        logging.error(error)
        traceback.print_exc()
        if cliente:
            cliente.close()


def subscribe_to_commands():
    pass
