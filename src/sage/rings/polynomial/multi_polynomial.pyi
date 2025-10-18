from typing import Any, List, Dict, Tuple, Optional, Union, Iterator
from sage.rings.polynomial.commutative_polynomial import CommutativePolynomial

# Type aliases for better specificity
SageInteger = Union['sage.rings.integer.Integer', int]
SageNumber = Union['sage.rings.rational.Rational', SageInteger, 'sage.structure.element.RingElement']
PolynomialRing = Any  # Will be refined when polynomial_ring.pyi is created
Variable = Any
Ideal = Any
ETuple = Tuple[int, ...]

def is_MPolynomial(x: Any) -> bool:
    ...

class MPolynomial(CommutativePolynomial):
    """Base class for multivariate polynomials."""
    
    def _scalar_conversion(self, R: Any) -> SageNumber:
        ...
    
    def args(self) -> Tuple[Variable, ...]:
        """Return variables as arguments."""
        ...
    
    def variables(self) -> Tuple[Variable, ...]:
        """Return tuple of variables."""
        ...
    
    def variable(self, i: int) -> Variable:
        """Return i-th variable."""
        ...
    
    def nvariables(self) -> int:
        """Return number of variables."""
        ...
    
    def parent(self) -> PolynomialRing:
        """Return parent polynomial ring."""
        ...
    
    def is_univariate(self) -> bool:
        """Test if polynomial is univariate."""
        ...
    
    def is_multivariate(self) -> bool:
        """Test if polynomial is multivariate."""
        ...
    
    def is_constant(self) -> bool:
        """Test if polynomial is constant."""
        ...
    
    def is_monomial(self) -> bool:
        """Test if polynomial is a monomial."""
        ...
    
    def is_term(self) -> bool:
        """Test if polynomial is a term."""
        ...
    
    def is_homogeneous(self) -> bool:
        """Test if polynomial is homogeneous."""
        ...
    
    def total_degree(self) -> int:
        """Return total degree."""
        ...
    
    def degree(self, x: Optional[Variable] = None) -> Union[int, Dict[Variable, int]]:
        """Return degree in variable x or all variables."""
        ...
    
    def degrees(self) -> Tuple[int, ...]:
        """Return degrees in all variables."""
        ...
    
    def monomial_coefficient(self, mon: 'MPolynomial') -> SageNumber:
        """Return coefficient of given monomial."""
        ...
    
    def coefficient(self, degrees: Union[ETuple, Dict[Variable, int]]) -> SageNumber:
        """Return coefficient of monomial with given degrees."""
        ...
    
    def coefficients(self) -> List[SageNumber]:
        """Return list of coefficients."""
        ...
    
    def monomials(self) -> List['MPolynomial']:
        """Return list of monomials."""
        ...
    
    def exponents(self) -> List[ETuple]:
        """Return list of exponent tuples."""
        ...
    
    def terms(self) -> List['MPolynomial']:
        """Return list of terms."""
        ...
    
    def iterator_exp_coeff(self, as_ETuples: bool = True) -> Iterator[Tuple[ETuple, SageNumber]]:
        """Iterate over (exponent, coefficient) pairs."""
        ...
    
    def dict(self) -> Dict[ETuple, SageNumber]:
        """Return dictionary representation."""
        ...
    
    def leading_monomial(self, order: Optional[str] = None) -> 'MPolynomial':
        """Return leading monomial."""
        ...
    
    def leading_coefficient(self, order: Optional[str] = None) -> SageNumber:
        """Return leading coefficient."""
        ...
    
    def leading_term(self, order: Optional[str] = None) -> 'MPolynomial':
        """Return leading term."""
        ...
    
    def lm(self) -> 'MPolynomial':
        """Return leading monomial."""
        ...
    
    def lc(self) -> SageNumber:
        """Return leading coefficient."""
        ...
    
    def lt(self) -> 'MPolynomial':
        """Return leading term."""
        ...
    
    def derivative(self, *args: Variable) -> 'MPolynomial':
        """Return partial derivative."""
        ...
    
    def integral(self, var: Variable) -> 'MPolynomial':
        """Return integral with respect to variable."""
        ...
    
    def subs(self, fixed: Optional[Dict[Variable, SageNumber]] = None, **kwds: SageNumber) -> 'MPolynomial':
        """Substitute variables."""
        ...
    
    def substitute(self, *args: Any, **kwds: SageNumber) -> 'MPolynomial':
        """Substitute variables."""
        ...
    
    def __call__(self, *args: SageNumber, **kwds: SageNumber) -> SageNumber:
        """Evaluate polynomial."""
        ...
    
    def reduce(self, I: Ideal) -> 'MPolynomial':
        """Reduce modulo ideal."""
        ...
    
    def lift(self, I: Ideal) -> List['MPolynomial']:
        """Lift from quotient ring."""
        ...
    
    def gcd(self, other: 'MPolynomial') -> 'MPolynomial':
        """Return greatest common divisor."""
        ...
    
    def lcm(self, other: 'MPolynomial') -> 'MPolynomial':
        """Return least common multiple."""
        ...
    
    def quo_rem(self, other: 'MPolynomial') -> Tuple['MPolynomial', 'MPolynomial']:
        """Return quotient and remainder."""
        ...
    
    def resultant(self, other: 'MPolynomial', variable: Variable) -> 'MPolynomial':
        """Return resultant."""
        ...
    
    def sylvester_matrix(self, other: 'MPolynomial', variable: Variable) -> Any:
        """Return Sylvester matrix."""
        ...
    
    def factor(self, proof: Optional[bool] = None) -> Any:
        """Return factorization."""
        ...
    
    def content(self) -> SageNumber:
        """Return content."""
        ...
    
    def primitive_part(self) -> 'MPolynomial':
        """Return primitive part."""
        ...
    
    def is_squarefree(self) -> bool:
        """Test if polynomial is squarefree."""
        ...
    
    def squarefree_decomposition(self) -> Any:
        """Return squarefree decomposition."""
        ...
    
    def newton_polytope(self) -> Any:
        """Return Newton polytope."""
        ...

class MPolynomial_libsingular(MPolynomial):
    """Multivariate polynomial implemented via libSINGULAR."""
    pass

def _is_M_convex_(points: List[ETuple]) -> bool:
    """Test if points form M-convex set."""
    ...