"""
Common type aliases for Sage mathematical objects.

This module provides type aliases that can be used across multiple .pyi files
to ensure consistency in type annotations for Cython modules.
"""

from typing import Any, TypeVar, Union, TYPE_CHECKING

if TYPE_CHECKING:
    # Import the actual classes when type checking
    from sage.rings.integer import Integer as IntegerClass
    from sage.rings.rational import Rational as RationalClass
    from sage.rings.real_mpfr import RealNumber as RealNumberClass
    from sage.rings.complex_mpfr import ComplexNumber as ComplexNumberClass
    from sage.matrix.matrix import Matrix as MatrixClass
    from sage.modules.vector_space_element import Vector as VectorClass
    from sage.structure.element import Element as ElementClass
    from sage.structure.element import RingElement as RingElementClass
    from sage.structure.element import ModuleElement as ModuleElementClass
    from sage.structure.element import AlgebraElement as AlgebraElementClass
    from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElementClass
    from sage.structure.parent import Parent as ParentClass
    from sage.rings.ring import Ring as RingClass
    from sage.rings.field import Field as FieldClass
    from sage.libs.gap.element import GapElement as GapElementClass
else:
    # Use Any during runtime to avoid import issues
    IntegerClass = Any
    RationalClass = Any
    RealNumberClass = Any
    ComplexNumberClass = Any
    MatrixClass = Any
    VectorClass = Any
    ElementClass = Any
    RingElementClass = Any
    ModuleElementClass = Any
    AlgebraElementClass = Any
    MultiplicativeGroupElementClass = Any
    ParentClass = Any
    RingClass = Any
    FieldClass = Any
    GapElementClass = Any

# Common Sage types
Integer = IntegerClass
Rational = RationalClass
RealNumber = RealNumberClass
ComplexNumber = ComplexNumberClass
Matrix = MatrixClass
Vector = VectorClass
Element = ElementClass
RingElement = RingElementClass
ModuleElement = ModuleElementClass
AlgebraElement = AlgebraElementClass
MultiplicativeGroupElement = MultiplicativeGroupElementClass
Parent = ParentClass
Ring = RingClass
Field = FieldClass
GapElement = GapElementClass

# Generic type variables for mathematical structures
T = TypeVar('T')
ElementType = TypeVar('ElementType', bound=Element)
RingElementType = TypeVar('RingElementType', bound=RingElement)
ModuleElementType = TypeVar('ModuleElementType', bound=ModuleElement)

# Common mathematical types
Number = Union[int, float, Integer, Rational, RealNumber, ComplexNumber]
RingLike = Union[Ring, Field]