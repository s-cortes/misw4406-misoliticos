import pulsar
from pulsar.schema import *

from modules.catastrales.infrastructure.schema.v1.events import ConsultaCreadaPayload, EventConsultaCreada
from modules.catastrales.infrastructure.schema.v1.comandos import ComandCreateConsultaPayload, ComandCreateConsulta
from seedwork.infrastructure import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventConsultaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ConsultaCreadaPayload(
            id=str(evento.id),
            oficinas=str(evento.oficinas), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventConsultaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventConsultaCreada))
    
    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandCreateConsultaPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandCreateConsulta(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandCreateConsulta))