from propiedades.modules.contratos.domain.value_objects import (
    TiposContrato,
    TipoMoneda
)
from propiedades.modules.contratos.domain.entities import Contrato
from propiedades.seedwork.domain.rules import CompundBusinessRule, BusinessRule


class ValidTipoContrato(BusinessRule):
    tipo_contrato: str

    def __init__(self, tipo_contrato: str, message="Tipo de contrato inválido"):
        super().__init__(message)
        self.tipo_contrato = tipo_contrato

    def is_valid(self) -> bool:
        return self.tipo_contrato in [tipo.value for tipo in TiposContrato]

class ValidTipoMoneda(BusinessRule):
    tipo_moneda: str

    def __init__(self, tipo_moneda: str, message="Tipo de moneda inválido"):
        super().__init__(message)
        self.tipo_moneda = tipo_moneda

    def is_valid(self) -> bool:
        return self.tipo_moneda in [tipo.value for tipo in TipoMoneda]

class ValidContrato(CompundBusinessRule):
    contrato: Contrato

    def __init__(self, contrato: Contrato, message="Contrato inválido"):
        self.contrato = contrato

        rules = [ValidTipoContrato(self.contrato.tipo_contrato), ValidTipoMoneda(self.contrato.pago.moneda)]

        super().__init__(message, rules)
