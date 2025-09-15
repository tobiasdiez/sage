from typing import Any, Optional, Union
from sage.structure.parent_gens import ParentWithGens
from sage.categories.category import Category

class Ring(ParentWithGens):
    def __init__(self, base: Any, names: Optional[Any] = None, normalize: bool = True, category: Optional[Category] = None) -> None:
        ...
    
    def __iter__(self) -> Any:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __xor__(self, n: Any) -> Any:
        ...
    
    def base_extend(self, R: Any) -> Any:
        ...
    
    def category(self) -> Category:
        ...
    
    def __mul__(self, x: Any) -> Any:
        ...
    
    def zero(self) -> Any:
        ...
    
    def one(self) -> Any:
        ...
    
    def order(self) -> Any:
        ...

class CommutativeRing(Ring):
    def __init__(self, base_ring: Any, names: Optional[Any] = None, normalize: bool = True, category: Optional[Category] = None) -> None:
        ...
    
    def fraction_field(self) -> Any:
        ...
    
    def extension(self, poly: Any, name: Optional[str] = None, names: Optional[Any] = None, **kwds: Any) -> Any:
        ...

class IntegralDomain(CommutativeRing):
    def __init__(self, *args: Any, **kwds: Any) -> None:
        ...

class NoetherianRing(CommutativeRing):
    def __init__(self, *args: Any, **kwds: Any) -> None:
        ...

class DedekindDomain(CommutativeRing):
    def __init__(self, *args: Any, **kwds: Any) -> None:
        ...

class PrincipalIdealDomain(CommutativeRing):
    def __init__(self, *args: Any, **kwds: Any) -> None:
        ...

class Field(CommutativeRing):
    pass

class Algebra(Ring):
    def __init__(self, base_ring: Any, *args: Any, **kwds: Any) -> None:
        ...

class CommutativeAlgebra(CommutativeRing):
    def __init__(self, base_ring: Any, *args: Any, **kwds: Any) -> None:
        ...

def is_Ring(x: Any) -> bool:
    ...