
import logging
from propiedades.modules.geoespacial.infrastructure.schema.v1.commands import ComandoCrearLote, ComandoCrearLotePayload
from propiedades.modules.sagas.domain.events.geoespacial import GeoespacialCreado
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
                payload: ComandoCrearLotePayload =  mapper.external_to_message(event.geoespacial)
                payload.correlation_id = str(event.correlation_id)
                return ComandoCrearLote(data=payload)
            except Exception as e:
                logging.error("[Sagas] CommandMessageFactory exception")
                logging.exception(e)

        elif type(event) is GeoespacialCreado and command == "CreateCatastralCommand":
            pass
        else:
            logging.error("[Sagas] Error en CommandMessageFactory")
            raise InvalidRepositoryFactoryException()
