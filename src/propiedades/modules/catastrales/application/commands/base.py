from propiedades.seedwork.application.commands import CommandHandler
from propiedades.modules.catastrales.infrastructure.factories import RepositoryFactory
from propiedades.modules.catastrales.domain.factories import CatastralFactory

class CatastralBaseHandler(CommandHandler):
    def __init__(self):
        self._fabrica_repositorio: RepositoryFactory = RepositoryFactory()
        self._fabrica_catastrales: CatastralFactory = CatastralFactory()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_catastrales(self):
        return self._fabrica_catastrales    
    