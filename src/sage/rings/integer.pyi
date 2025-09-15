from typing import Any, List, Optional, Tuple, Union, Iterator
from sage.libs.gmp.types import __mpz_struct, mpz_t, mpz_ptr
from sage.libs.gmp.mpz import mpz_set

from sage.structure.element import EuclideanDomainElement, RingElement
from sage.categories.morphism import Morphism

class Integer(EuclideanDomainElement):
    value: __mpz_struct[1]

    def set_from_mpz(self, value: mpz_t) -> None:
        ...

    def hash_c(self) -> int:
        ...

    def __pari__(self) -> object:
        ...

    def _shift_helper(self, y: object, sign: int) -> object:
        ...

    def _add_(self, other: 'Integer') -> 'Integer':
        ...

    def _mul_(self, other: 'Integer') -> 'Integer':
        ...

    def _pow_(self, other: 'Integer') -> 'Integer':
        ...

    def _and(self, other: 'Integer') -> 'Integer':
        ...

    def _or(self, other: 'Integer') -> 'Integer':
        ...

    def _xor(self, other: 'Integer') -> 'Integer':
        ...

    def _exact_log_log2_iter(self, m: 'Integer') -> int:
        ...

    def _exact_log_mpfi_log(self, m: object) -> int:
        ...

    def _valuation(self, p: 'Integer') -> RingElement:
        ...

    def _val_unit(self, p: 'Integer') -> object:
        ...

    def _divide_knowing_divisible_by(self, right: 'Integer') -> 'Integer':
        ...

    def _is_power_of(self, n: 'Integer') -> bool:
        ...

    def _pseudoprime_is_prime(self, proof: bool = True) -> bool:
        ...

    # Public methods
    def list(self) -> List['Integer']:
        ...

    def str(self, base: int = 10) -> str:
        ...

    def ordinal_str(self) -> str:
        ...

    def hex(self) -> str:
        ...

    def oct(self) -> str:
        ...

    def binary(self) -> str:
        ...

    def bits(self) -> List[int]:
        ...

    def bit_length(self) -> int:
        ...

    def nbits(self) -> int:
        ...

    def trailing_zero_bits(self) -> int:
        ...

    def digits(self, base: int = 10, digits: Optional[Any] = None, padto: int = 0) -> List[int]:
        ...

    def balanced_digits(self, base: int = 10, positive_shift: bool = True) -> List[int]:
        ...

    def ndigits(self, base: int = 10) -> int:
        ...

    def nth_root(self, n: int, truncate_mode: bool = False) -> 'Integer':
        ...

    def exact_log(self, m: 'Integer') -> int:
        ...

    def log(self, m: Optional['Integer'] = None, prec: Optional[int] = None) -> Any:
        ...

    def exp(self, prec: Optional[int] = None) -> Any:
        ...

    def prime_to_m_part(self, m: 'Integer') -> 'Integer':
        ...

    def prime_divisors(self) -> List['Integer']:
        ...

    def divisors(self, method: Optional[str] = None) -> List['Integer']:
        ...

    def factor(self, proof: Optional[bool] = None, limit: Optional[int] = None, int_: bool = False, trial_division: bool = True, watch: Optional[Any] = None, **kwds: Any) -> Any:
        ...

    def gcd(self, other: 'Integer') -> 'Integer':
        ...

    def lcm(self, other: 'Integer') -> 'Integer':
        ...

    def is_prime(self, proof: bool = True) -> bool:
        ...

    def is_power(self, n: Optional[int] = None, proof: bool = True) -> Union[bool, Tuple['Integer', int]]:
        ...

    def is_perfect_power(self) -> bool:
        ...

    def is_square(self) -> bool:
        ...

    def sqrt(self, prec: Optional[int] = None, extend: bool = True, all: bool = False) -> Any:
        ...

    def isqrt(self) -> 'Integer':
        ...

    def abs(self) -> 'Integer':
        ...

def mpz_set_str_python(z: mpz_ptr, s: str, base: int) -> int:
    ...

def smallInteger(value: int) -> 'Integer':
    ...

_small_primes_table: list[bool]

def _Integer_from_mpz(e: mpz_t) -> 'Integer':
    z = Integer.__new__(Integer)
    mpz_set(z.value, e)
    return z
