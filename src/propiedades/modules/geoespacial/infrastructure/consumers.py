import logging
import traceback

import _pulsar
import pulsar
from pulsar.schema import *

from propiedades.modules.geoespacial.infrastructure.schema.v1.commands import ComandoCrearLote
from propiedades.modules.geoespacial.infrastructure.schema.v1.events import \
    EventoLoteCreado
from propiedades.seedwork.infrastructure import utils
from propiedades.modules.geoespacial.application.commands.crear_lote import CrearLote
from propiedades.seedwork.application.commands import execute_command
from propiedades.modules.geoespacial.infrastructure.schema.v1.mappers import CrearLoteCommandMapper


def subscribe_to_events():
    cliente = None
    try:
        logging.error("[Lotes] Inicinando Subscripcion")
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650",connection_timeout_ms=5000)
        consumidor = cliente.subscribe(
            "geoespacial-events",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="geoespacial-sub-eventos",
            schema=AvroSchema(EventoLoteCreado),
        )

        logging.error("[Lotes] Inicinando consumo")

        while True:
            mensaje = consumidor.receive()
            logging.error(f"[Lotes] Evento Recibido Subscripcion {mensaje.value().data}")

            print(f"[Lotes] Evento recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)

        cliente.close()
    except Exception as error:
        logging.error("[Lotes] ERROR: Suscribiendose al tópico de eventos!")
        logging.error(error)
        traceback.print_exc()
        if cliente:
            cliente.close()


def subscribe_to_commands(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "geoespacial-commands",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="propiedades-sub-comandos",
            schema=AvroSchema(ComandoCrearLote),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido: {mensaje.value().data}")
            map_lote = CrearLoteCommandMapper()
            lote_dto = map_lote.message_to_dto(mensaje.value().data)
            with app.context():
                command = CrearLote(
                    lote_dto.id, lote_dto.direccion, lote_dto.poligono, lote_dto.edificio, lote_dto.id_propiedad
                )
                execute_command(command)
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
