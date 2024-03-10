import strawberry
from .schemas import *

@strawberry.type
class Query:
    propiedades: typing.List[Propiedad] = strawberry.field(resolver=obtener_propiedadas)
