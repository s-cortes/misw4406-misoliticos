import logging
import traceback

import _pulsar
import pulsar
from pulsar.schema import *

from propiedades.modules.catastrales.infrastructure.schema.v1.events import \
    EventoInmuebleCreado
from propiedades.seedwork.infrastructure import utils
from pulsar.schema import AvroSchema

def subscribe_to_events():
    cliente = None
    try:
        logging.error("[Inmueble] Inicinando Subscripcion")
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650",connection_timeout_ms=5000)
        consumidor = cliente.subscribe(
            "inmueble-events",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="inmueble-sub-eventos",
            schema=AvroSchema(EventoInmuebleCreado),
        )

        logging.error("[Inmuebles] Inicinando consumo")

        while True:
            mensaje = consumidor.receive()
            logging.error(f"[Inmuebles] Evento Recibido Subscripcion {mensaje.value().data}")

            print(f"[Inmuebles] Evento recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)

        cliente.close()
    except Exception as error:
        logging.error("[Inmuebles] ERROR: Suscribiendose al tópico de eventos!")
        logging.error(error)
        traceback.print_exc()
        if cliente:
            cliente.close()

def subscribe_to_commands():
    pass
