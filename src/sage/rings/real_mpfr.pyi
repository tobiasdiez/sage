from typing import Any, Optional, Union, List, Tuple, Dict
from sage.structure.element import RingElement
from sage.rings.abc import RealField as AbstractRealField

# Type aliases for better type specificity
SageNumber = Union['RealNumber', 'sage.rings.rational.Rational', 
                   'sage.rings.integer.Integer', int, float]
RealFieldType = 'RealField_class'
ComplexField = Any  # Will be refined when complex field .pyi is created

# Module-level functions
def mpfr_prec_min() -> int:
    ...

def mpfr_prec_max() -> int:
    ...

def mpfr_get_exp_min() -> int:
    ...

def mpfr_get_exp_max() -> int:
    ...

def mpfr_set_exp_min(e: int) -> None:
    ...

def mpfr_set_exp_max(e: int) -> None:
    ...

def mpfr_get_exp_min_min() -> int:
    ...

def mpfr_get_exp_max_max() -> int:
    ...

class RealField_class(AbstractRealField):
    """Arbitrary precision real number field using MPFR."""
    
    def __init__(self, prec: int = 53, sci_not: int = 0, rnd: int = 0) -> None:
        ...
    
    def __reduce__(self) -> Tuple[Any, ...]:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __cmp__(self, other: RealFieldType) -> int:
        ...
    
    def __call__(self, x: SageNumber = 0, base: int = 10) -> 'RealNumber':
        ...
    
    def __repr__(self) -> str:
        ...
    
    def _latex_(self) -> str:
        ...
    
    def prec(self) -> int:
        """Return precision in bits."""
        ...
    
    def precision(self) -> int:
        """Return precision in bits."""
        ...
    
    def rounding_mode(self) -> str:
        """Return the rounding mode."""
        ...
    
    def is_exact(self) -> bool:
        """Return False since this is not an exact field."""
        ...
    
    def is_finite(self) -> bool:
        """Return False since this field is infinite."""
        ...
    
    def characteristic(self) -> int:
        """Return 0 since this is a field of characteristic 0."""
        ...
    
    def gen(self, n: int = 0) -> 'RealNumber':
        """Return the generator (which is 1)."""
        ...
    
    def ngens(self) -> int:
        """Return number of generators (which is 1)."""
        ...
    
    def complex_field(self) -> ComplexField:
        """Return corresponding complex field."""
        ...
    
    def pi(self) -> 'RealNumber':
        """Return pi to the precision of this field."""
        ...
    
    def euler_constant(self) -> 'RealNumber':
        """Return Euler's constant gamma."""
        ...
    
    def log2(self) -> 'RealNumber':
        """Return log(2)."""
        ...
    
    def catalan_constant(self) -> 'RealNumber':
        """Return Catalan's constant."""
        ...
    
    def khinchin_constant(self) -> 'RealNumber':
        """Return Khinchin's constant."""
        ...
    
    def glaisher_constant(self) -> 'RealNumber':
        """Return Glaisher's constant."""
        ...
    
    def zeta(self, n: int = 3) -> 'RealNumber':
        """Return Riemann zeta(n)."""
        ...

class RealNumber(RingElement):
    """An arbitrary precision real number using MPFR."""
    
    def __cinit__(self, parent: RealFieldType, x: SageNumber = None, base: Optional[int] = None) -> None:
        ...
    
    def __init__(self, parent: RealFieldType, x: SageNumber = 0, base: int = 10) -> None:
        ...
    
    def _magma_init_(self, magma: Any) -> str:
        ...
    
    def __array_interface__(self) -> Dict[str, Any]:
        ...
    
    def __reduce__(self) -> Tuple[Any, ...]:
        ...
    
    def __dealloc__(self) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __format__(self, format_spec: str) -> str:
        ...
    
    def _latex_(self) -> str:
        ...
    
    def _interface_init_(self, I: Optional[Any] = None) -> str:
        ...
    
    def _mathematica_init_(self) -> str:
        ...
    
    def _sage_input_(self, sib: Any, coerced: bool) -> Any:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def _im_gens_(self, codomain: Any, im_gens: Any, base_map: Optional[Any] = None) -> Any:
        ...
    
    def real(self) -> 'RealNumber':
        """Return real part (which is self)."""
        ...
    
    def imag(self) -> 'RealNumber':
        """Return imaginary part (which is 0)."""
        ...
    
    def str(self, base: int = 10, digits: int = 0, no_sci: Optional[bool] = None, 
           e: Optional[str] = None, truncate: bool = True, skip_zeroes: bool = False) -> str:
        """Return string representation."""
        ...
    
    def hex(self) -> str:
        """Return hexadecimal representation."""
        ...
    
    def exact_rational(self) -> 'sage.rings.rational.Rational':
        """Return exact rational representation."""
        ...
    
    def simplest_rational(self) -> 'sage.rings.rational.Rational':
        """Return simplest rational approximation."""
        ...
    
    def nearby_rational(self, max_error: Optional[SageNumber] = None, 
                       max_denominator: Optional[int] = None) -> 'sage.rings.rational.Rational':
        """Return nearby rational approximation."""
        ...
    
    def fp_rank(self) -> int:
        """Return floating point rank."""
        ...
    
    def ulp(self) -> 'RealNumber':
        """Return unit in last place."""
        ...
    
    def epsilon(self, field: Optional[RealFieldType] = None) -> 'RealNumber':
        """Return machine epsilon."""
        ...
    
    def algebraic_degree(self) -> int:
        """Return algebraic degree."""
        ...
    
    def prec(self) -> int:
        """Return precision in bits."""
        ...
    
    def precision(self) -> int:
        """Return precision in bits."""
        ...
    
    def parent(self) -> RealFieldType:
        """Return parent field."""
        ...
    
    def nexttoward(self, other: 'RealNumber') -> 'RealNumber':
        """Return next representable value toward other."""
        ...
    
    def nextabove(self) -> 'RealNumber':
        """Return next representable value above."""
        ...
    
    def nextbelow(self) -> 'RealNumber':
        """Return next representable value below."""
        ...
    
    def is_zero(self) -> bool:
        """Test if this is zero."""
        ...
    
    def is_one(self) -> bool:
        """Test if this is one."""
        ...
    
    def is_negative(self) -> bool:
        """Test if this is negative."""
        ...
    
    def is_positive(self) -> bool:
        """Test if this is positive."""
        ...
    
    def is_infinity(self) -> bool:
        """Test if this is infinity."""
        ...
    
    def is_NaN(self) -> bool:
        """Test if this is NaN."""
        ...
    
    def is_finite(self) -> bool:
        """Test if this is finite."""
        ...
    
    def is_real(self) -> bool:
        """Test if this is real (always True)."""
        ...
    
    def is_square(self) -> bool:
        """Test if this is a perfect square."""
        ...
    
    def is_integer(self) -> bool:
        """Test if this is an integer."""
        ...
    
    def sign(self) -> int:
        """Return sign (-1, 0, or 1)."""
        ...
    
    def round(self) -> 'sage.rings.integer.Integer':
        """Return rounded value."""
        ...
    
    def floor(self) -> 'sage.rings.integer.Integer':
        """Return floor."""
        ...
    
    def ceil(self) -> 'sage.rings.integer.Integer':
        """Return ceiling."""
        ...
    
    def ceiling(self) -> 'sage.rings.integer.Integer':
        """Return ceiling."""
        ...
    
    def trunc(self) -> 'sage.rings.integer.Integer':
        """Return truncation toward zero."""
        ...
    
    def frac(self) -> 'RealNumber':
        """Return fractional part."""
        ...
    
    def __int__(self) -> int:
        ...
    
    def __float__(self) -> float:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    def __add__(self, other: SageNumber) -> Union['RealNumber', Any]:
        ...
    
    def __sub__(self, other: SageNumber) -> Union['RealNumber', Any]:
        ...
    
    def __mul__(self, other: SageNumber) -> Union['RealNumber', Any]:
        ...
    
    def __truediv__(self, other: SageNumber) -> Union['RealNumber', Any]:
        ...
    
    def __pow__(self, other: SageNumber) -> Union['RealNumber', Any]:
        ...
    
    def __neg__(self) -> 'RealNumber':
        ...
    
    def __pos__(self) -> 'RealNumber':
        ...
    
    def __abs__(self) -> 'RealNumber':
        ...
    
    def sqrt(self) -> 'RealNumber':
        """Return square root."""
        ...
    
    def nth_root(self, n: int) -> 'RealNumber':
        """Return n-th root."""
        ...
    
    def is_nth_power(self, n: int) -> bool:
        """Test if this is an n-th power."""
        ...
    
    def log(self, base: Optional[SageNumber] = None) -> 'RealNumber':
        """Return logarithm."""
        ...
    
    def log2(self) -> 'RealNumber':
        """Return base-2 logarithm."""
        ...
    
    def log10(self) -> 'RealNumber':
        """Return base-10 logarithm."""
        ...
    
    def log1p(self) -> 'RealNumber':
        """Return log(1+self)."""
        ...
    
    def exp(self) -> 'RealNumber':
        """Return exponential."""
        ...
    
    def exp2(self) -> 'RealNumber':
        """Return 2^self."""
        ...
    
    def exp10(self) -> 'RealNumber':
        """Return 10^self."""
        ...
    
    def expm1(self) -> 'RealNumber':
        """Return exp(self)-1."""
        ...
    
    def sin(self) -> 'RealNumber':
        """Return sine."""
        ...
    
    def cos(self) -> 'RealNumber':
        """Return cosine."""
        ...
    
    def tan(self) -> 'RealNumber':
        """Return tangent."""
        ...
    
    def sec(self) -> 'RealNumber':
        """Return secant."""
        ...
    
    def csc(self) -> 'RealNumber':
        """Return cosecant."""
        ...
    
    def cot(self) -> 'RealNumber':
        """Return cotangent."""
        ...
    
    def arcsin(self) -> 'RealNumber':
        """Return arcsine."""
        ...
    
    def arccos(self) -> 'RealNumber':
        """Return arccosine."""
        ...
    
    def arctan(self) -> 'RealNumber':
        """Return arctangent."""
        ...
    
    def arctan2(self, x: 'RealNumber') -> 'RealNumber':
        """Return atan2(self, x)."""
        ...
    
    def sinh(self) -> 'RealNumber':
        """Return hyperbolic sine."""
        ...
    
    def cosh(self) -> 'RealNumber':
        """Return hyperbolic cosine."""
        ...
    
    def tanh(self) -> 'RealNumber':
        """Return hyperbolic tangent."""
        ...
    
    def sech(self) -> 'RealNumber':
        """Return hyperbolic secant."""
        ...
    
    def csch(self) -> 'RealNumber':
        """Return hyperbolic cosecant."""
        ...
    
    def coth(self) -> 'RealNumber':
        """Return hyperbolic cotangent."""
        ...
    
    def arcsinh(self) -> 'RealNumber':
        """Return inverse hyperbolic sine."""
        ...
    
    def arccosh(self) -> 'RealNumber':
        """Return inverse hyperbolic cosine."""
        ...
    
    def arctanh(self) -> 'RealNumber':
        """Return inverse hyperbolic tangent."""
        ...
    
    def gamma(self) -> 'RealNumber':
        """Return gamma function."""
        ...
    
    def log_gamma(self) -> 'RealNumber':
        """Return log of gamma function."""
        ...
    
    def factorial(self) -> 'RealNumber':
        """Return factorial."""
        ...
    
    def zeta(self) -> 'RealNumber':
        """Return Riemann zeta function."""
        ...
    
    def erf(self) -> 'RealNumber':
        """Return error function."""
        ...
    
    def erfc(self) -> 'RealNumber':
        """Return complementary error function."""
        ...
    
    def j0(self) -> 'RealNumber':
        """Return Bessel function J_0."""
        ...
    
    def j1(self) -> 'RealNumber':
        """Return Bessel function J_1."""
        ...
    
    def jn(self, n: int) -> 'RealNumber':
        """Return Bessel function J_n."""
        ...
    
    def y0(self) -> 'RealNumber':
        """Return Bessel function Y_0."""
        ...
    
    def y1(self) -> 'RealNumber':
        """Return Bessel function Y_1."""
        ...
    
    def yn(self, n: int) -> 'RealNumber':
        """Return Bessel function Y_n."""
        ...
    
    def agm(self, other: 'RealNumber') -> 'RealNumber':
        """Return arithmetic-geometric mean."""
        ...
    
    def min(self, other: 'RealNumber') -> 'RealNumber':
        """Return minimum."""
        ...
    
    def max(self, other: 'RealNumber') -> 'RealNumber':
        """Return maximum."""
        ...

class RealLiteral(RealNumber):
    """A real number literal with automatic parent determination."""
    pass

# Type aliases
RealField = RealField_class

def RealField(prec: int = 53, sci_not: int = 0, rnd: int = 0) -> RealField_class:
    """Construct a real field with given precision and rounding mode."""
    ...