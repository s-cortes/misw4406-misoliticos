from propiedades.seedwork.application.commands import CommandHandler
from propiedades.modules.geoespacial.infrastructure.factories import RepositoryFactory
from propiedades.modules.geoespacial.domain.factories import GeoespacialFactory

class GeoespacialBaseHandler(CommandHandler):
    def __init__(self):
        self._fabrica_repositorio: RepositoryFactory = RepositoryFactory()
        self._fabrica_geoespacial: GeoespacialFactory = GeoespacialFactory()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_geoespacial(self):
        return self._fabrica_geoespacial