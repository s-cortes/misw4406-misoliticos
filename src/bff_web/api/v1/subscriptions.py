import asyncio
import strawberry

from .schemas import *

@strawberry.type
class Suscripcion:
    @strawberry.subscription
    async def eventos_propiedades(self, id_correlacion: str) -> Propiedad:
