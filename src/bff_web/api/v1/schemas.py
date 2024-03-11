import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime

PROPIEDADES_HOST = os.getenv("PROPIEDADES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_propiedades(root) -> typing.List["Propiedad"]:
    propiedades_json = requests.get(f'http://{PROPIEDADES_HOST}:5000/propiedades').json()
    propiedades = []

    for propiedad in propiedades_json:
        propiedades.append(
            Propiedad(
                fecha_creacion=datetime.strptime(propiedad.get('fecha_creacion'), FORMATO_FECHA), 
                fecha_actualizacion=datetime.strptime(propiedad.get('fecha_actualizacion'), FORMATO_FECHA), 
                id=propiedad.get('id'), 
                id_usuario=propiedad.get('id_usuario', '')
            )
        )

    return propiedades

@strawberry.type
class Propiedad:
    id: str
    id_usuario: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    #itinerarios: typing.List[Itinerario]

@strawberry.type
class PropiedadRespuesta:
    mensaje: str
    codigo: int





