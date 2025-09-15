from typing import Any

class Octonion_generic(AlgebraElement):
    def conjugate(self: Any) -> Any:
        ...
    def imag_part(self: Any) -> Any:
        ...

class Octonion(Octonion_generic):
    ...
