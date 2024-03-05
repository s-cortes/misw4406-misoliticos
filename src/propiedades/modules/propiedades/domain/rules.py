from propiedades.modules.propiedades.domain.entities import Propiedad, Fotografia
from propiedades.seedwork.domain.rules import BusinessRule, CompundBusinessRule


class _AtLeastOneFotografia(BusinessRule):
    fotografias: list[Fotografia]

    def __init__(self, fotografias: list[Fotografia], message="Al menos una fotografia en la propiedad"):
        super().__init__(message)
        self.fotografias = fotografias

    def is_valid(self) -> bool:
        return len(self.fotografias) > 0 and all([isinstance(o, Fotografia) for o in self.fotografias])


class ValidPropiedad(CompundBusinessRule):
    propiedad: Propiedad

    def __init__(self, propiedad: Propiedad, message="propiedad invalida"):
        self.propiedad = propiedad

        rules = [_AtLeastOneFotografia(self.propiedad.fotografias)]
        

        super().__init__(message, rules)
        