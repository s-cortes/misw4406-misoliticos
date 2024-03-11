from strawberry.fastapi import GraphQLRouter
from .consults import Query
from .mutations import Mutation

import strawberry

from .subscriptions import Suscripcion

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Suscripcion)
router = GraphQLRouter(schema)
