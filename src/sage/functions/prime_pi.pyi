from typing import Any, Optional
from sage.rings.integer import Integer
from sage.symbolic.function import BuiltinFunction

def legendre_phi(x: Any, a: int) -> Integer:
    ...

class PrimePi(BuiltinFunction):
    def __init__(self) -> None:
        ...
    def __call__(self, x: Any, **kwds: Any) -> Any:
        ...
    def plot(self, xmin: float = 0, xmax: float = 100, vertical_lines: bool = True, **kwds: Any) -> Any:
        ...
