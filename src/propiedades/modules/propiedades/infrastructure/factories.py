from dataclasses import dataclass
import logging

from propiedades.modules.propiedades.domain.events import (
    CreacionPropiedadSolicitada, PropiedadCreada)
from propiedades.modules.propiedades.domain.repositories import \
    PropiedadesRepository
from propiedades.modules.propiedades.infrastructure.exceptions import \
    InvalidRepositoryFactoryException
from propiedades.modules.propiedades.infrastructure.repositories import \
    PropiedadesRepositorySQLite
from propiedades.modules.propiedades.infrastructure.schema.v1.mappers import (
    PropiedadCreateCommandMapper, PropiedadCreatedIntegrationEventMapper)
from propiedades.seedwork.domain.factories import Factory


@dataclass
class RepositoryFactory(Factory):
    def create(self, obj: type):
        if obj == PropiedadesRepository.__class__:
            return PropiedadesRepositorySQLite()
        else:
            raise InvalidRepositoryFactoryException


class IntegrationMessageFactory(Factory):
    def create(self, event: any) -> any:
        logging.error("[Propiedades] creando IntegrationMessageFactory")

        if type(event) is PropiedadCreada:
            mapper = PropiedadCreatedIntegrationEventMapper()
            return mapper.external_to_message(event)
        else:
            logging.error("[Propiedades] Error en IntegrationMessageFactory")
            raise InvalidRepositoryFactoryException()


class CommandMessageFactory(Factory):
    def create(self, event: any) -> any:
        logging.error("[Propiedades] creando CommandMessageFactory")
        if type(event) is CreacionPropiedadSolicitada:
            try:
                mapper = PropiedadCreateCommandMapper()
                return mapper.external_to_message(event)
            except Exception as e:
                logging.error("[Propiedades] CommandMessageFactory exception")
                logging.exception(e)
                
        else:
            logging.error("[Propiedades] Error en CommandMessageFactory")
            raise InvalidRepositoryFactoryException()
