from typing import Any, List, Optional, Tuple, Union, Dict, Iterator
from sage.structure.element import FieldElement

# Type aliases for better specificity
SageInteger = Union['sage.rings.integer.Integer', int]
SageRational = Union['Rational', SageInteger]
SageNumber = Union[SageRational, float, complex]
Polynomial = Any  # Will be refined when polynomial.pyi is improved
ContinuedFraction = Any
NumberField = Any
Factorization = Any

def is_Rational(x: Any) -> bool:
    """Test if x is a rational number."""
    ...

class Rational(FieldElement):
    """Rational number using GNU Multi-Precision library."""
    
    def __cinit__(self) -> None:
        ...
    
    def __init__(self, x: Any = None, base: int = 0) -> None:
        ...
    
    def __reduce__(self) -> Tuple[Any, ...]:
        ...
    
    def __index__(self) -> int:
        ...
    
    def list(self) -> List[SageInteger]:
        """Return [numerator, denominator]."""
        ...
    
    def continued_fraction_list(self, type: str = 'std') -> List[SageInteger]:
        """Return continued fraction expansion as a list."""
        ...
    
    def continued_fraction(self) -> ContinuedFraction:
        """Return continued fraction expansion."""
        ...
    
    def __copy__(self) -> 'Rational':
        ...
    
    def __deepcopy__(self, memo: Dict[int, Any]) -> 'Rational':
        ...
    
    def __dealloc__(self) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def _latex_(self) -> str:
        ...
    
    def _symbolic_(self, sring: Any) -> Any:
        ...
    
    def _sympy_(self) -> Any:
        ...
    
    def __mpz__(self) -> Any:
        """Convert to PARI mpz."""
        ...
    
    def __mpq__(self) -> Any:
        """Convert to PARI mpq."""
        ...
    
    def _magma_init_(self, magma: Any) -> str:
        ...
    
    def _regina_(self, regina: Any) -> Any:
        ...
    
    def __array_interface__(self) -> Dict[str, Any]:
        ...
    
    def _mathml_(self) -> str:
        ...
    
    def _im_gens_(self, codomain: Any, im_gens: Any, base_map: Optional[Any] = None) -> Any:
        ...
    
    def content(self, other: 'Rational') -> 'Rational':
        """Return the content of self and other."""
        ...
    
    def valuation(self, p: SageInteger) -> SageInteger:
        """Return the p-adic valuation."""
        ...
    
    def local_height(self, p: SageInteger, prec: Optional[int] = None) -> SageNumber:
        """Return the local height at prime p."""
        ...
    
    def local_height_arch(self, prec: Optional[int] = None) -> SageNumber:
        """Return the archimedean local height."""
        ...
    
    def global_height_non_arch(self, prec: Optional[int] = None) -> SageNumber:
        """Return the non-archimedean global height."""
        ...
    
    def global_height_arch(self, prec: Optional[int] = None) -> SageNumber:
        """Return the archimedean global height."""
        ...
    
    def global_height(self, prec: Optional[int] = None) -> SageNumber:
        """Return the global height."""
        ...
    
    def is_square(self) -> bool:
        """Test if this rational is a perfect square."""
        ...
    
    def is_norm(self, L: NumberField, element: bool = False, proof: bool = True) -> Union[bool, Tuple[bool, Any]]:
        """Test if this rational is a norm from the number field L."""
        ...
    
    def _bnfisnorm(self, L: NumberField, proof: bool = True) -> Tuple[bool, Any]:
        ...
    
    def is_perfect_power(self, expected_n: Optional[int] = None) -> Union[bool, Tuple['Rational', int]]:
        """Test if this rational is a perfect power."""
        ...
    
    def squarefree_part(self) -> 'Rational':
        """Return the squarefree part."""
        ...
    
    def is_padic_square(self, p: SageInteger, check_validity: bool = True) -> bool:
        """Test if this rational is a p-adic square."""
        ...
    
    def val_unit(self, p: SageInteger) -> Tuple[SageInteger, 'Rational']:
        """Return valuation and unit part."""
        ...
    
    def prime_to_S_part(self, S: List[SageInteger] = None) -> 'Rational':
        """Return the S-integral part."""
        ...
    
    def sqrt(self, prec: Optional[int] = None, extend: bool = True, all: bool = False) -> Union['Rational', Any]:
        """Return square root."""
        ...
    
    def period(self) -> List[SageInteger]:
        """Return period of decimal expansion."""
        ...
    
    def nth_root(self, n: int, truncate_mode: int = 0) -> Union['Rational', Any]:
        """Return n-th root."""
        ...
    
    def is_nth_power(self, n: int) -> bool:
        """Test if this rational is an n-th power."""
        ...
    
    def str(self, base: int = 10) -> str:
        """Return string representation in given base."""
        ...
    
    def __float__(self) -> float:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __getitem__(self, n: int) -> SageInteger:
        """Return n-th coefficient in base representation."""
        ...
    
    def __add__(self, other: SageNumber) -> Union['Rational', Any]:
        ...
    
    def __sub__(self, other: SageNumber) -> Union['Rational', Any]:
        ...
    
    def __mul__(self, other: SageNumber) -> Union['Rational', Any]:
        ...
    
    def __truediv__(self, other: SageNumber) -> Union['Rational', Any]:
        ...
    
    def __invert__(self) -> 'Rational':
        ...
    
    def __pos__(self) -> 'Rational':
        ...
    
    def __neg__(self) -> 'Rational':
        ...
    
    def __abs__(self) -> 'Rational':
        ...
    
    def __int__(self) -> int:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    def __pow__(self, n: Union[SageInteger, 'Rational'], modulus: Optional[SageInteger] = None) -> Union['Rational', Any]:
        ...
    
    def _pari_(self) -> Any:
        ...
    
    def _interface_init_(self, I: Optional[Any] = None) -> str:
        ...
    
    def additive_order(self) -> SageInteger:
        """Return additive order (infinity unless self is 0)."""
        ...
    
    def multiplicative_order(self) -> SageInteger:
        """Return multiplicative order."""
        ...
    
    def sign(self) -> int:
        """Return sign (-1, 0, or 1)."""
        ...
    
    def ceil(self) -> SageInteger:
        """Return ceiling."""
        ...
    
    def floor(self) -> SageInteger:
        """Return floor."""
        ...
    
    def trunc(self) -> SageInteger:
        """Return truncation toward zero."""
        ...
    
    def round(self, mode: str = "away") -> SageInteger:
        """Return rounded value."""
        ...
    
    def frac(self) -> 'Rational':
        """Return fractional part."""
        ...
    
    def numerator(self) -> SageInteger:
        """Return numerator."""
        ...
    
    def denominator(self) -> SageInteger:
        """Return denominator."""
        ...
    
    def factor(self) -> Factorization:
        """Return factorization."""
        ...
    
    def support(self) -> List[SageInteger]:
        """Return list of prime divisors."""
        ...
    
    def lcm(self, other: 'Rational') -> 'Rational':
        """Return least common multiple."""
        ...
    
    def gcd(self, other: 'Rational') -> 'Rational':
        """Return greatest common divisor."""
        ...
    
    def rational_reconstruction(self, m: SageInteger) -> 'Rational':
        """Rational reconstruction modulo m."""
        ...
    
    def mod(self, other: SageInteger) -> 'Rational':
        """Return self modulo other."""
        ...
    
    def _lcm(self, other: 'Rational') -> 'Rational':
        ...
    
    def _gcd(self, other: 'Rational') -> 'Rational':
        ...
    
    def real(self) -> 'Rational':
        """Return real part (which is self)."""
        ...
    
    def imag(self) -> 'Rational':
        """Return imaginary part (which is 0)."""
        ...
    
    def conjugate(self) -> 'Rational':
        """Return complex conjugate (which is self)."""
        ...
    
    def is_one(self) -> bool:
        """Test if self equals 1."""
        ...
    
    def is_integral(self) -> bool:
        """Test if self is an integer."""
        ...
    
    def is_rational(self) -> bool:
        """Test if self is rational (always True)."""
        ...
    
    def is_S_integral(self, S: List[SageInteger] = None) -> bool:
        """Test if self is S-integral."""
        ...
    
    def is_S_unit(self, S: Optional[List[SageInteger]] = None) -> bool:
        """Test if self is an S-unit."""
        ...
    
    def __lshift__(self, y: int) -> 'Rational':
        """Left shift (multiply by power of 2)."""
        ...
    
    def __rshift__(self, y: int) -> 'Rational':
        """Right shift (divide by power of 2)."""
        ...
    
    def height(self) -> SageNumber:
        """Return logarithmic height."""
        ...

# Additional module-level functions
def rational_power_parts(a: 'Rational', b: 'Rational', factor_limit: int = 100000) -> Tuple[Any, bool]:
    """Compute power decomposition of rational numbers."""
    ...

def make_rational(s: str) -> 'Rational':
    """Create rational from string representation."""
    ...