from pydispatch import dispatcher
from .handlers import HandlerInmuebleIntegracion
from modules.catastrales.domain.events import InmuebleCreado

dispatcher.connect(HandlerInmuebleIntegracion().handle, signal=f'{InmuebleCreado.__name__}Integracion')