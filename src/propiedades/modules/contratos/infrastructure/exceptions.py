from propiedades.seedwork.domain.exceptions import FactoryException


class InvalidRepositoryFactoryException(FactoryException):
    def __init__(self, mensaje="Tipo inválido para el repositorio"):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)
