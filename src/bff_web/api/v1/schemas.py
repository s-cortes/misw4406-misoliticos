import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime

PROPIEDADES_HOST = os.getenv("PROPIEDADES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_propiedades(root) -> typing.List["Propiedad"]:
    reservas_json = requests.get(f'http://{AEROALPES_HOST}:5000/vuelos/reserva').json()
    reservas = []

    for reserva in reservas_json:
        reservas.append(
            Reserva(
                fecha_creacion=datetime.strptime(reserva.get('fecha_creacion'), FORMATO_FECHA), 
                fecha_actualizacion=datetime.strptime(reserva.get('fecha_actualizacion'), FORMATO_FECHA), 
                id=reserva.get('id'), 
                id_usuario=reserva.get('id_usuario', '')
            )
        )

    return reservas

@strawberry.type
class Propiedad:
    id: str
    id_usuario: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    #itinerarios: typing.List[Itinerario]

@strawberry.type
class ReservaRespuesta:
    mensaje: str
    codigo: int





