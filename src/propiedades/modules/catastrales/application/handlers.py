from propiedades.modules.catastrales.domain.events import InmuebleCreado
from propiedades.seedwork.application.handlers import Handler
from propiedades.modules.catastrales.infrastructure.despachadores import Despachador

class HandlerInmuebleIntegracion(Handler):
    @staticmethod
    def handle_inmueble_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-inmueble')

    

