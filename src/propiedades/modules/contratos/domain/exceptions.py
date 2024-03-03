from propiedades.seedwork.domain.exceptions import FactoryException


class InvalidContratoFactoryException(FactoryException):
    def __init__(self, mensaje="Tipo inválido"):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)
