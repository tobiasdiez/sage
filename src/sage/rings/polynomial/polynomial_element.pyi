from typing import Any, List, Optional, Union, Dict, Tuple
from sage.rings.polynomial.commutative_polynomial import CommutativePolynomial
from sage.structure.element import RingElement
from sage.categories.morphism import Morphism
from sage.categories.map import Map

class Polynomial(CommutativePolynomial):
    """Generic polynomial over any ring."""
    
    def __init__(self, parent: Any, is_gen: bool = False, construct: bool = False) -> None:
        ...
    
    def plot(self, xmin: Optional[Any] = None, xmax: Optional[Any] = None, *args: Any, **kwds: Any) -> Any:
        ...
    
    def subs(self, in_dict: Optional[Dict[Any, Any]] = None, *args: Any, **kwds: Any) -> 'Polynomial':
        ...
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        ...
    
    def substitute(self, *args: Any, **kwds: Any) -> 'Polynomial':
        ...
    
    def compose(self, other: 'Polynomial') -> 'Polynomial':
        ...
    
    def derivative(self, *args: Any) -> 'Polynomial':
        ...
    
    def integral(self, var: Optional[Any] = None) -> 'Polynomial':
        ...
    
    def degree(self) -> int:
        ...
    
    def leading_coefficient(self) -> Any:
        ...
    
    def constant_coefficient(self) -> Any:
        ...
    
    def coefficients(self, sparse: bool = True) -> List[Any]:
        ...
    
    def exponents(self) -> List[int]:
        ...
    
    def monomials(self) -> List['Polynomial']:
        ...
    
    def dict(self) -> Dict[int, Any]:
        ...
    
    def list(self, copy: bool = True) -> List[Any]:
        ...
    
    def roots(self, ring: Optional[Any] = None, multiplicities: bool = True, algorithm: Optional[str] = None) -> List[Any]:
        ...
    
    def factor(self, **kwds: Any) -> Any:
        ...
    
    def is_irreducible(self) -> bool:
        ...
    
    def is_squarefree(self) -> bool:
        ...
    
    def squarefree_decomposition(self) -> Any:
        ...
    
    def gcd(self, other: 'Polynomial') -> 'Polynomial':
        ...
    
    def lcm(self, other: 'Polynomial') -> 'Polynomial':
        ...
    
    def resultant(self, other: 'Polynomial', variable: Optional[Any] = None) -> Any:
        ...
    
    def discriminant(self) -> Any:
        ...
    
    def sylvester_matrix(self, other: 'Polynomial', variable: Optional[Any] = None) -> Any:
        ...
    
    def quo_rem(self, other: 'Polynomial') -> Tuple['Polynomial', 'Polynomial']:
        ...
    
    def __divmod__(self, other: 'Polynomial') -> Tuple['Polynomial', 'Polynomial']:
        ...
    
    def __floordiv__(self, other: 'Polynomial') -> 'Polynomial':
        ...
    
    def __mod__(self, other: 'Polynomial') -> 'Polynomial':
        ...
    
    def reverse(self, degree: Optional[int] = None) -> 'Polynomial':
        ...
    
    def revert_series(self, n: int) -> 'Polynomial':
        ...
    
    def valuation(self, p: Optional[Any] = None) -> int:
        ...
    
    def newton_slopes(self, p: Any) -> List[Any]:
        ...
    
    def hensel_lift(self, p: Any, alpha: Any) -> Any:
        ...
    
    def rational_reconstruction(self, m: 'Polynomial', n_deg: Optional[int] = None, d_deg: Optional[int] = None) -> Tuple['Polynomial', 'Polynomial']:
        ...
    
    def rational_reconstruct(self, m: 'Polynomial', n_deg: Optional[int] = None, d_deg: Optional[int] = None) -> Any:
        ...
    
    def norm(self, p: Optional[Any] = None) -> Any:
        ...
    
    def trace(self) -> Any:
        ...
    
    def is_weil_polynomial(self, return_q: bool = False) -> Union[bool, Tuple[bool, Any]]:
        ...
    
    def count_real_roots(self, a: Optional[Any] = None, b: Optional[Any] = None) -> int:
        ...

class Polynomial_generic_dense(Polynomial):
    """Dense polynomial implementation."""
    
    def __init__(self, parent: Any, x: Optional[Any] = None, check: bool = True, is_gen: bool = False, construct: bool = False) -> None:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def _cache_key(self) -> Any:
        ...
    
    def __getitem__(self, i: int) -> Any:
        ...
    
    def __setitem__(self, i: int, value: Any) -> None:
        ...
    
    def __iter__(self) -> Any:
        ...

class Polynomial_generic_dense_inexact(Polynomial_generic_dense):
    """Dense polynomial over inexact ring."""
    pass

class ConstantPolynomialSection(Map):
    """Section of constant polynomial map."""
    
    def __init__(self, R: Any) -> None:
        ...
    
    def _call_(self, x: Any) -> Any:
        ...

class PolynomialBaseringInjection(Morphism):
    """Injection from base ring to polynomial ring."""
    
    def __init__(self, domain: Any, codomain: Any) -> None:
        ...
    
    def _call_(self, x: Any) -> 'Polynomial':
        ...
    
    def _repr_type(self) -> str:
        ...
    
    def section(self) -> ConstantPolynomialSection:
        ...

def make_generic_polynomial(parent: Any, coeffs: List[Any]) -> Polynomial_generic_dense:
    ...

def universal_discriminant(n: int) -> 'Polynomial':
    ...