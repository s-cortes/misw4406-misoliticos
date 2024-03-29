from pydispatch import dispatcher

from propiedades.modules.propiedades.domain.events import PropiedadCreada
from propiedades.modules.sagas.domain.events.geoespacial import GeoespacialCreado
from .propiedades_saga import handle_saga_messages

dispatcher.connect(
    handle_saga_messages,
    signal=f"{PropiedadCreada.__name__}Domain",
)

dispatcher.connect(
    handle_saga_messages,
    signal=f"{GeoespacialCreado.__name__}Integracion",
)

