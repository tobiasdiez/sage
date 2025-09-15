from typing import Any, Optional, Union, Tuple
from sage.structure.element import FiniteRingElement

def Mod(n: Any, m: Any, parent: Optional[Any] = None) -> 'IntegerMod_abstract':
    ...

def IntegerMod(parent: Any, value: Any) -> 'IntegerMod_abstract':
    ...

def is_IntegerMod(x: Any) -> bool:
    ...

class NativeIntStruct:
    """Structure for storing modulus in different representations."""
    pass

class IntegerMod_abstract(FiniteRingElement):
    """Abstract base class for elements of Z/nZ."""
    
    def __init__(self, parent: Any, value: Optional[Any] = None) -> None:
        ...
    
    def __abs__(self) -> 'IntegerMod_abstract':
        ...
    
    def __reduce__(self) -> Tuple[Any, ...]:
        ...
    
    def _im_gens_(self, codomain: Any, im_gens: Any, base_map: Optional[Any] = None) -> Any:
        ...
    
    def __mod__(self, modulus: Any) -> 'IntegerMod_abstract':
        ...
    
    def __int__(self) -> int:
        ...
    
    def __index__(self) -> int:
        ...
    
    def __float__(self) -> float:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __add__(self, other: Any) -> Any:
        ...
    
    def __sub__(self, other: Any) -> Any:
        ...
    
    def __mul__(self, other: Any) -> Any:
        ...
    
    def __truediv__(self, other: Any) -> Any:
        ...
    
    def __pow__(self, other: Any) -> Any:
        ...
    
    def __neg__(self) -> 'IntegerMod_abstract':
        ...
    
    def __pos__(self) -> 'IntegerMod_abstract':
        ...
    
    def __invert__(self) -> 'IntegerMod_abstract':
        ...
    
    def additive_order(self) -> Any:
        ...
    
    def multiplicative_order(self) -> Any:
        ...
    
    def is_square(self) -> bool:
        ...
    
    def sqrt(self, extend: bool = True, all: bool = False) -> Any:
        ...
    
    def square_root(self) -> 'IntegerMod_abstract':
        ...
    
    def is_unit(self) -> bool:
        ...
    
    def inverse(self) -> 'IntegerMod_abstract':
        ...
    
    def gcd(self, other: Any) -> Any:
        ...
    
    def lcm(self, other: Any) -> Any:
        ...
    
    def valuation(self, p: Any) -> int:
        ...
    
    def lift(self) -> Any:
        ...
    
    def centerlift(self) -> Any:
        ...
    
    def log(self, base: Any) -> 'IntegerMod_abstract':
        ...
    
    def nth_root(self, n: int, extend: bool = True, all: bool = False) -> Any:
        ...
    
    def is_primitive_root(self) -> bool:
        ...
    
    def charpoly(self, var: str = 'x') -> Any:
        ...
    
    def minpoly(self, var: str = 'x') -> Any:
        ...

class IntegerMod_gmp(IntegerMod_abstract):
    """Integer modulo n using GMP for arbitrarily large modulus."""
    pass

class IntegerMod_int(IntegerMod_abstract):
    """Integer modulo n using native int for small modulus."""
    pass

class IntegerMod_int64(IntegerMod_abstract):
    """Integer modulo n using native int64 for medium modulus."""
    pass

def square_root_mod_prime_power(a: IntegerMod_abstract, p: Any, e: int) -> IntegerMod_abstract:
    ...

def lucas_q1(mm: Any, P: IntegerMod_abstract) -> Any:
    ...