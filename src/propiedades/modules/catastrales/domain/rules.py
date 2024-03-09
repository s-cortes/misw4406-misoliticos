from propiedades.modules.catastrales.domain.value_objects import (
    Area,
    Piso,
    UbicacionInterna,
    Oficina,
)
from propiedades.modules.catastrales.domain.entities import Inmueble
from propiedades.seedwork.domain.rules import CompundBusinessRule, BusinessRule


class ValidArea(BusinessRule):
    area: Area

    def __init__(self, area: Area, message="area invalida"):
        super().__init__(message)
        self.area = area

    def is_valid(self) -> bool:
        return self.area is not None and self.area.valor > 0 and self.area.unidad


class ValidUbicacionInterna(BusinessRule):
    ubicacion: UbicacionInterna

    def __init__(self, ubicacion: UbicacionInterna, message="ubicacion invalida"):
        super().__init__(message)
        self.ubicacion = ubicacion

    def is_valid(self) -> bool:

        return self.ubicacion is not None and self.ubicacion.nombre


class ValidOficina(CompundBusinessRule):
    oficina: Oficina

    def __init__(self, oficina: Oficina, message="Oficina invalida"):
        self.oficina = oficina
        rules = [
            ValidArea(self.oficina.area),
            ValidUbicacionInterna(self.oficina.ubicacion),
        ]
        super().__init__(message, rules)


class _AtLeastOneOficina(BusinessRule):
    oficinas: List[Oficina]

    def __init__(
        self, oficinas: List[Oficina], message="Al menos una oficina en el piso"
    ):
        super().__init__(message)
        self.oficinas = oficinas

    def is_valid(self) -> bool:
        return len(self.oficinas) > 0 and all(
            [isinstance(o, Oficina) for o in self.oficinas]
        )


class ValidPiso(CompundBusinessRule):
    piso: Piso

    def __init__(self, piso: Piso, message="Piso invalido en inmueble"):
        self.piso = piso

        rules = [_AtLeastOneOficina(self.piso.oficinas)]
        rules.extend([ValidOficina(o) for o in self.piso.oficinas])

        super().__init__(message, rules)


class _AtLeastOnePiso(BusinessRule):
    pisos: List[Piso]

    def __init__(self, pisos: List[Piso], message="Al menos un piso en el inmueble"):
        super().__init__(message)
        self.pisos = pisos

    def is_valid(self) -> bool:
        return len(self.pisos) > 0 and all([isinstance(o, Piso) for o in self.pisos])


class ValidInmueble(CompundBusinessRule):
    inmueble: Inmueble

    def __init__(self, inmueble: Inmueble, message="inmueble invalido"):
        self.inmueble = inmueble

        rules = [_AtLeastOnePiso(self.inmueble.pisos)]
        rules.extend([ValidPiso(o) for o in self.inmueble.pisos])

        super().__init__(message, rules)
        