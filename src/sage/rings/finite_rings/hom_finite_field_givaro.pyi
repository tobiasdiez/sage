from typing import Any

class SectionFiniteFieldHomomorphism_givaro(SectionFiniteFieldHomomorphism_generic):
    def __init__(self: Any, inverse: Any) -> Any:
        ...

class FiniteFieldHomomorphism_givaro(FiniteFieldHomomorphism_generic):
    def __init__(self: Any, parent: Any, im_gens: Any = ..., check: Any = ...) -> Any:
        ...

class FrobeniusEndomorphism_givaro(FrobeniusEndomorphism_finite_field):
    def __init__(self: Any, domain: Any, power: Any = ...) -> Any:
        ...
    def fixed_field(self: Any) -> Any:
        ...
