from typing import Any, Optional, Union, Tuple, List
from sage.structure.element import FiniteRingElement

# Type aliases for better specificity
SageInteger = Union['sage.rings.integer.Integer', int]
SageRational = Union['sage.rings.rational.Rational', SageInteger]
SageNumber = Union[SageRational, 'IntegerMod_abstract']
ModulusRing = Any  # Will be refined when integer_mod_ring.pyi is created
Factorization = Any
Polynomial = Any

def Mod(n: SageNumber, m: SageInteger, parent: Optional[ModulusRing] = None) -> 'IntegerMod_abstract':
    """Create element n modulo m."""
    ...

def IntegerMod(parent: ModulusRing, value: SageNumber) -> 'IntegerMod_abstract':
    """Create integer modulo element with given parent and value."""
    ...

def is_IntegerMod(x: Any) -> bool:
    """Test if x is an integer modulo n."""
    ...

class NativeIntStruct:
    """Structure for storing modulus in different representations."""
    pass

class IntegerMod_abstract(FiniteRingElement):
    """Abstract base class for elements of Z/nZ."""
    
    def __init__(self, parent: ModulusRing, value: Optional[SageNumber] = None) -> None:
        ...
    
    def __abs__(self) -> 'IntegerMod_abstract':
        """Return absolute value."""
        ...
    
    def __reduce__(self) -> Tuple[Any, ...]:
        ...
    
    def _im_gens_(self, codomain: Any, im_gens: List[Any], base_map: Optional[Any] = None) -> Any:
        ...
    
    def __mod__(self, modulus: SageInteger) -> 'IntegerMod_abstract':
        """Return self modulo given modulus."""
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
    
    def __add__(self, other: SageNumber) -> Union['IntegerMod_abstract', Any]:
        ...
    
    def __sub__(self, other: SageNumber) -> Union['IntegerMod_abstract', Any]:
        ...
    
    def __mul__(self, other: SageNumber) -> Union['IntegerMod_abstract', Any]:
        ...
    
    def __truediv__(self, other: SageNumber) -> Union['IntegerMod_abstract', Any]:
        ...
    
    def __pow__(self, other: SageInteger) -> Union['IntegerMod_abstract', Any]:
        ...
    
    def __neg__(self) -> 'IntegerMod_abstract':
        ...
    
    def __pos__(self) -> 'IntegerMod_abstract':
        ...
    
    def __invert__(self) -> 'IntegerMod_abstract':
        """Return multiplicative inverse."""
        ...
    
    def additive_order(self) -> SageInteger:
        """Return additive order."""
        ...
    
    def multiplicative_order(self) -> SageInteger:
        """Return multiplicative order."""
        ...
    
    def is_square(self) -> bool:
        """Test if this is a quadratic residue."""
        ...
    
    def sqrt(self, extend: bool = True, all: bool = False) -> Union['IntegerMod_abstract', List['IntegerMod_abstract']]:
        """Return square root(s)."""
        ...
    
    def square_root(self) -> 'IntegerMod_abstract':
        """Return a square root."""
        ...
    
    def is_unit(self) -> bool:
        """Test if this is a unit (invertible)."""
        ...
    
    def inverse(self) -> 'IntegerMod_abstract':
        """Return multiplicative inverse."""
        ...
    
    def gcd(self, other: SageNumber) -> SageInteger:
        """Return gcd with other."""
        ...
    
    def lcm(self, other: SageNumber) -> SageInteger:
        """Return lcm with other."""
        ...
    
    def valuation(self, p: SageInteger) -> int:
        """Return p-adic valuation."""
        ...
    
    def lift(self) -> SageInteger:
        """Return canonical lift to the integers."""
        ...
    
    def centerlift(self) -> SageInteger:
        """Return centered lift to the integers."""
        ...
    
    def log(self, base: SageNumber) -> 'IntegerMod_abstract':
        """Return discrete logarithm."""
        ...
    
    def nth_root(self, n: int, extend: bool = True, all: bool = False) -> Union['IntegerMod_abstract', List['IntegerMod_abstract']]:
        """Return n-th root(s)."""
        ...
    
    def is_primitive_root(self) -> bool:
        """Test if this is a primitive root."""
        ...
    
    def charpoly(self, var: str = 'x') -> Polynomial:
        """Return characteristic polynomial."""
        ...
    
    def minpoly(self, var: str = 'x') -> Polynomial:
        """Return minimal polynomial."""
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

def square_root_mod_prime_power(a: IntegerMod_abstract, p: SageInteger, e: int) -> IntegerMod_abstract:
    """Compute square root modulo prime power."""
    ...

def lucas_q1(mm: SageInteger, P: IntegerMod_abstract) -> SageInteger:
    """Lucas sequence computation."""
    ...