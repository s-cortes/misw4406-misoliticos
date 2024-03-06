# from propiedades.modules.contratos.domain.value_objects import
from propiedades.modules.contratos.domain.entities import Contrato
from propiedades.seedwork.domain.rules import CompundBusinessRule, BusinessRule


class ValidContrato(CompundBusinessRule):
    contrato: Contrato

    def __init__(self, contrato: Contrato, message="contrato invalido"):
        self.contrato = contrato

        rules = []

        super().__init__(message, rules)
        