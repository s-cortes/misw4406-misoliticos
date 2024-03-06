import logging
import traceback

import _pulsar
import pulsar
from pulsar.schema import *

# from propiedades.modules.propiedades.infrastructure.schema.v1.commands import
from propiedades.modules.propiedades.infrastructure.schema.v1.events import \
    EventoPropiedadCreada
from propiedades.seedwork.infrastructure import utils


def subscribe_to_events():
    cliente = None
    try:
        logging.error("[Propiedades] Inicinando Subscripcion")
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650",connection_timeout_ms=5000)
        consumidor = cliente.subscribe(
            "propiedad-events",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="propiedades-sub-eventos",
            schema=AvroSchema(EventoPropiedadCreada),
        )

        logging.error("[Propiedades] Inicinando consumo")

        while True:
            mensaje = consumidor.receive()
            logging.error(f"[Propiedades] Evento Recibido Subscripcion {mensaje.value().data}")

            print(f"[Propiedades] Evento recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)

        cliente.close()
    except Exception as error:
        logging.error("[Propiedades] ERROR: Suscribiendose al tópico de eventos!")
        logging.error(error)
        traceback.print_exc()
        if cliente:
            cliente.close()


def subscribe_to_commands():
    pass
    # cliente = None
    # try:
    #     cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
    #     consumidor = cliente.subscribe(
    #         "propiedad-commands",
    #         consumer_type=_pulsar.ConsumerType.Shared,
    #         subscription_name="propiedades-sub-comandos",
    #         schema=AvroSchema(ComandoCrearReserva),
    #     )

    #     while True:
    #         mensaje = consumidor.receive()
    #         print(f"Comando recibido: {mensaje.value().data}")

    #         consumidor.acknowledge(mensaje)

    #     cliente.close()
    # except:
    #     logging.error("ERROR: Suscribiendose al tópico de comandos!")
    #     traceback.print_exc()
    #     if cliente:
    #         cliente.close()
