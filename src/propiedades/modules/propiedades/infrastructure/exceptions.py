
from propiedades.seedwork.domain.exceptions import FactoryException


class InvalidRepositoryFactoryException(FactoryException):
    def __init__(self, mensaje="invalid type for repository"):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)

class InvalidIntegrationMessageException(FactoryException):
    def __init__(self, mensaje="invalid type for integration message"):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)
