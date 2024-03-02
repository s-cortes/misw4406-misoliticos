from propiedades.seedwork.domain.exceptions import FactoryException

class InvalidGeoespacialFactoryException(FactoryException):
    def __init__(self, mensaje="invalid type for factory"):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)