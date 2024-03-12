
import logging
from propiedades.modules.geoespacial.infrastructure.schema.v1.commands import ComandoCrearLote
from propiedades.modules.sagas.infrastructure.exceptions import InvalidRepositoryFactoryException
from propiedades.modules.sagas.infrastructure.schema.v1.mappers import CrearLoteSagaCommandMapper
from propiedades.seedwork.domain.factories import Factory
from propiedades.modules.propiedades.domain.events import PropiedadCreada


class CommandMessageSagaFactory(Factory):
    def create(self, event: any, command: str) -> any:
        logging.error("[Sagas] creando PropiedadCreatedSagaEventMapper")
        if type(event) is PropiedadCreada and command == "CreateGeoespacialCommand":
            try:
                mapper = CrearLoteSagaCommandMapper()
                logging.error("----------*-------------------*----------------")
                logging.error(event.geoespacial)
                payload =  mapper.external_to_message(event.geoespacial)
                return ComandoCrearLote(data=payload)
            except Exception as e:
                logging.error("[Sagas] CommandMessageFactory exception")
                logging.exception(e)
                
        else:
            logging.error("[Sagas] Error en CommandMessageFactory")
            raise InvalidRepositoryFactoryException()
