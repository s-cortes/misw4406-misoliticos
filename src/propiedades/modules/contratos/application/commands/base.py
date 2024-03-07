from propiedades.seedwork.application.commands import CommandHandler
from propiedades.modules.contratos.infrastructure.factories import RepositoryFactory
from propiedades.modules.contratos.domain.factories import ContratoFactory

class ContratoBaseHandler(CommandHandler):
    def __init__(self):
        self._fabrica_repositorio: RepositoryFactory = RepositoryFactory()
        self._fabrica_contratos: ContratoFactory = ContratoFactory()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos    
    