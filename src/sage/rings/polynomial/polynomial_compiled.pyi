from typing import Any

class CompiledPolynomialFunction:
    def __init__(self: Any, coeffs: Any, algorithm: Any = ...) -> Any:
        ...
    def __repr__(self: Any) -> Any:
        ...
    def __call__(self: Any, x: Any) -> Any:
        ...

class generic_pd:
    def __init__(self: Any) -> Any:
        ...

class dummy_pd(generic_pd):
    def __init__(self: Any, label: Any) -> Any:
        ...

class var_pd(generic_pd):
    def __init__(self: Any, index: Any) -> Any:
        ...
    def __repr__(self: Any) -> Any:
        ...

class univar_pd(generic_pd):
    def __init__(self: Any) -> Any:
        ...
    def __repr__(self: Any) -> Any:
        ...

class coeff_pd(generic_pd):
    def __init__(self: Any, index: Any) -> Any:
        ...
    def __repr__(self: Any) -> Any:
        ...

class unary_pd(generic_pd):
    def __init__(self: Any, operand: Any) -> Any:
        ...

class sqr_pd(unary_pd):
    def __repr__(self: Any) -> Any:
        ...

class pow_pd(unary_pd):
    def __init__(self: Any, base: Any, exponent: Any) -> Any:
        ...
    def __repr__(self: Any) -> Any:
        ...

class binary_pd(generic_pd):
    def __init__(self: Any, left: Any, right: Any) -> Any:
        ...

class add_pd(binary_pd):
    def __repr__(self: Any) -> Any:
        ...

class mul_pd(binary_pd):
    def __repr__(self: Any) -> Any:
        ...

class abc_pd(binary_pd):
    def __init__(self: Any, left: Any, right: Any, index: Any) -> Any:
        ...
    def __repr__(self: Any) -> Any:
        ...
