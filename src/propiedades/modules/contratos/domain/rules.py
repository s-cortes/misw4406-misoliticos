from propiedades.modules.contratos.domain.value_objects import (
    Area,
    Pago,
    UbicacionInterna,
    Oficina,
)
from propiedades.modules.contratos.domain.entities import Contrato
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
    oficinas: list[Oficina]

    def __init__(
        self, oficinas: list[Oficina], message="Al menos una oficina en el pago"
    ):
        super().__init__(message)
        self.oficinas = oficinas

    def is_valid(self) -> bool:
        return len(self.oficinas) > 0 and all(
            [isinstance(o, Oficina) for o in self.oficinas]
        )


class ValidPago(CompundBusinessRule):
    pago: Pago

    def __init__(self, pago: Pago, message="Pago invalido en contrato"):
        self.pago = pago

        rules = [_AtLeastOneOficina(self.pago.oficinas)]
        rules.extend([ValidOficina(o) for o in self.pago.oficinas])

        super().__init__(message, rules)


class _AtLeastOnePago(BusinessRule):
    pagos: list[Pago]

    def __init__(self, pagos: list[Pago], message="Al menos un pago en el contrato"):
        super().__init__(message)
        self.pagos = pagos

    def is_valid(self) -> bool:
        return len(self.pagos) > 0 and all([isinstance(o, Pago) for o in self.pagos])


class ValidContrato(CompundBusinessRule):
    contrato: Contrato

    def __init__(self, contrato: Contrato, message="contrato invalido"):
        self.contrato = contrato

        rules = [_AtLeastOnePago(self.contrato.pagos)]
        rules.extend([ValidPago(o) for o in self.contrato.pagos])

        super().__init__(message, rules)
        