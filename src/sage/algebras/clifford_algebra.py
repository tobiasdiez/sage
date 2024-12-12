# sage.doctest: needs sage.modules
r"""
Clifford Algebras

AUTHORS:

- Travis Scrimshaw (2013-09-06): Initial version
- Trevor K. Karn (2022-07-27): Rewrite basis indexing using FrozenBitset
"""
# ****************************************************************************
#       Copyright (C) 2013-2022 Travis Scrimshaw <tcscrims at gmail.com>
#                 (C) 2022 Trevor Karn <karnx018 at umn.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************
from sage.misc.cachefunc import cached_method
from sage.structure.unique_representation import UniqueRepresentation
from sage.structure.parent import Parent
from sage.structure.element import Element
from sage.structure.richcmp import (richcmp_method, op_EQ, op_NE,
                                    op_LT, op_GT, op_LE, op_GE, rich_to_bool)
from sage.data_structures.bitset import Bitset, FrozenBitset

from sage.algebras.clifford_algebra_element import CliffordAlgebraElement, ExteriorAlgebraElement
from sage.categories.algebras_with_basis import AlgebrasWithBasis
from sage.categories.hopf_algebras_with_basis import HopfAlgebrasWithBasis
from sage.categories.fields import Fields
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.modules.with_basis.morphism import ModuleMorphismByLinearity
from sage.categories.poor_man_map import PoorManMap
from sage.rings.integer_ring import ZZ
from sage.rings.noncommutative_ideals import Ideal_nc
from sage.modules.free_module import FreeModule, FreeModule_generic
from sage.matrix.constructor import Matrix
from sage.matrix.args import MatrixArgs
from sage.sets.family import Family
from sage.combinat.free_module import CombinatorialFreeModule
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass
from sage.typeset.ascii_art import ascii_art
from sage.typeset.unicode_art import unicode_art
import unicodedata


class CliffordAlgebraIndices(UniqueRepresentation, Parent):
    r"""
    A facade parent for the indices of Clifford algebra.
    Users should not create instances of this class directly.
    """
    def __init__(self, Qdim, degree=None):
        r"""
        Initialize ``self``.

        """
        self._nbits = Qdim
        if degree is None:
            self._cardinality = 2 ** Qdim
        else:
            from sage.arith.misc import binomial
            self._cardinality = binomial(Qdim, degree)
        self._degree = degree
        # the if statement here is in case Qdim is 0.
        category = FiniteEnumeratedSets().Facade()
        Parent.__init__(self, category=category, facade=True)

    def _element_constructor_(self, x):
        r"""
        Construct an element of ``self``.


        """
        if isinstance(x, (list, tuple, set, frozenset)):
            if len(x) > self._nbits:
                raise ValueError(f"{x=} is too long")
            if not x:
                return FrozenBitset()
            return FrozenBitset(x)

        if isinstance(x, int):
            return FrozenBitset((x,))

    def __call__(self, el):
        r"""
        """
        if not isinstance(el, Element):
            return self._element_constructor_(el)
        else:
            return Parent.__call__(self, el)

    def cardinality(self):
        r"""
        Return the cardinality of ``self``.

        """
        return self._cardinality

    __len__ = cardinality

    def _repr_(self):
        r"""
        Return a string representation of ``self``.


        """
        if self._degree is not None:
            extra = f" of size {self._degree}"
        else:
            extra = ""
        if self._nbits == 0:
            return "Subsets of {}" + extra
        if self._nbits == 1:
            return "Subsets of {0}" + extra
        if self._nbits == 2:
            return "Subsets of {0,1}" + extra
        return f"Subsets of {{0,1,...,{self._nbits-1}}}" + extra

    def _latex_(self):
        r"""
        Return a latex representation of ``self``.

        """
        if self._degree is not None:
            extra = f", {self._degree}"
        else:
            extra = ""
        if self._nbits == 0:
            return f"\\mathcal{{P}}(\\emptyset{extra})"
        if self._nbits == 1:
            return f"\\mathcal{{P}}(\\{{0\\}}{extra})"
        if self._nbits == 2:
            return f"\\mathcal{{P}}(\\{{0,1\\}}{extra})"
        return f"\\mathcal{{P}}(\\{{0,1,\\ldots,{self._nbits-1}\\}}{extra})"

    def __iter__(self):
        r"""
        Iterate over ``self``.


        """
        import itertools
        n = self._nbits
        if self._degree is not None:
            if self._degree == 0:  # special corner case
                yield FrozenBitset()
                return
            for C in itertools.combinations(range(n), self._degree):
                yield FrozenBitset(C)
            return

        yield FrozenBitset()
        k = 1
        while k <= n:
            for C in itertools.combinations(range(n), k):
                yield FrozenBitset(C)
            k += 1

    def __contains__(self, elt):
        r"""
        Check containment of ``elt`` in ``self``.


        """
        if isinstance(elt, int):
            if self._degree is not None and sum(ZZ(elt).bits()) != self._degree:
                return False
            return elt < self._cardinality and elt >= 0
        if not isinstance(elt, FrozenBitset):
            return False
        if self._degree is not None and len(elt) != self._degree:
            return False
        return elt.capacity() <= self._nbits

    def _an_element_(self):
        r"""
        Return an element of ``self``.

        """
        if not self._nbits:
            return FrozenBitset()

        if self._degree is not None:
            if self._degree == 0:  # special corner case
                return FrozenBitset()
            return FrozenBitset(range(self._degree))

        from sage.combinat.subset import SubsetsSorted
        X = SubsetsSorted(range(self._nbits))
        return FrozenBitset(X.an_element())


class CliffordAlgebra(CombinatorialFreeModule):
    r"""
    The Clifford algebra of a quadratic form.

    Let `Q : V \to \mathbf{k}` denote a quadratic form on a vector space `V`
    over a field `\mathbf{k}`. The Clifford algebra `Cl(V, Q)` is defined as
    `T(V) / I_Q` where `T(V)` is the tensor algebra of `V` and `I_Q` is the
    two-sided ideal generated by all elements of the form `v \otimes v - Q(v)`
    for all `v \in V`.

    We abuse notation to denote the projection of a pure tensor
    `x_1 \otimes x_2 \otimes \cdots \otimes x_m \in T(V)` onto
    `T(V) / I_Q = Cl(V, Q)` by `x_1 \wedge x_2 \wedge \cdots \wedge x_m`.
    This is motivated by the fact that `Cl(V, Q)` is the exterior algebra
    `\wedge V` when `Q = 0` (one can also think of a Clifford algebra as
    a quantization of the exterior algebra). See :class:`ExteriorAlgebra`
    for the concept of an exterior algebra.

    From the definition, a basis of `Cl(V, Q)` is given by monomials of
    the form

    .. MATH::

        \{ e_{i_1} \wedge \cdots \wedge e_{i_k} \mid 1 \leq i_1 < \cdots <
        i_k \leq n \},

    where `n = \dim(V)` and where `\{ e_1, e_2, \cdots, e_n \}` is any
    fixed basis of `V`. Hence

    .. MATH::

        \dim(Cl(V, Q)) = \sum_{k=0}^n \binom{n}{k} = 2^n.

    .. NOTE::

        The algebra `Cl(V, Q)` is a `\ZZ / 2\ZZ`-graded algebra, but not
        (in general) `\ZZ`-graded (in a reasonable way).

    This construction satisfies the following universal property. Let
    `i : V \to Cl(V, Q)` denote the natural inclusion (which is an
    embedding). Then for every associative `\mathbf{k}`-algebra `A`
    and any `\mathbf{k}`-linear map `j : V \to A` satisfying

    .. MATH::

        j(v)^2 = Q(v) \cdot 1_A

    for all `v \in V`, there exists a unique `\mathbf{k}`-algebra
    homomorphism `f : Cl(V, Q) \to A` such that `f \circ i = j`.
    This property determines the Clifford algebra uniquely up to
    canonical isomorphism. The inclusion `i` is commonly used to
    identify `V` with a vector subspace of `Cl(V)`.

    The Clifford algebra `Cl(V, Q)` is a `\ZZ_2`-graded algebra
    (where `\ZZ_2 = \ZZ / 2 \ZZ`); this grading is determined by
    placing all elements of `V` in degree `1`. It is also an
    `\NN`-filtered algebra, with the filtration too being defined
    by placing all elements of `V` in degree `1`. The :meth:`degree` gives
    the `\NN`-*filtration* degree, and to get the super degree use instead
    :meth:`~sage.categories.super_modules.SuperModules.ElementMethods.is_even_odd`.

    The Clifford algebra also can be considered as a covariant functor
    from the category of vector spaces equipped with quadratic forms
    to the category of algebras. In fact, if `(V, Q)` and `(W, R)`
    are two vector spaces endowed with quadratic forms, and if
    `g : W \to V` is a linear map preserving the quadratic form,
    then we can define an algebra morphism
    `Cl(g) : Cl(W, R) \to Cl(V, Q)` by requiring that it send every
    `w \in W` to `g(w) \in V`. Since the quadratic form `R` on `W`
    is uniquely determined by the quadratic form `Q` on `V` (due to
    the assumption that `g` preserves the quadratic form), this fact
    can be rewritten as follows: If `(V, Q)` is a vector space with a
    quadratic form, and `W` is another vector space, and
    `\phi : W \to V` is any linear map, then we obtain an algebra
    morphism `Cl(\phi) : Cl(W, \phi(Q)) \to Cl(V, Q)` where
    `\phi(Q) = \phi^T \cdot Q \cdot \phi` (we consider `\phi` as a
    matrix) is the quadratic form `Q` pulled back to `W`. In fact, the
    map `\phi` preserves the quadratic form because of

    .. MATH::

        \phi(Q)(x) = x^T \cdot \phi^T \cdot Q \cdot \phi \cdot x
        = (\phi \cdot x)^T \cdot Q \cdot (\phi \cdot x) = Q(\phi(x)).

    Hence we have `\phi(w)^2 = Q(\phi(w)) = \phi(Q)(w)` for all `w \in W`.

    REFERENCES:

    - :wikipedia:`Clifford_algebra`

    INPUT:

    - ``Q`` -- a quadratic form
    - ``names`` -- (default: ``'e'``) the generator names

    """
    @staticmethod
    def __classcall_private__(cls, Q, names=None):
        """
        Normalize arguments to ensure a unique representation.
        """
        if not isinstance(Q, QuadraticForm):
            raise ValueError("{} is not a quadratic form".format(Q))
        if names is None:
            names = 'e'
        names = tuple(names)
        if len(names) != Q.dim():
            if len(names) == 1:
                names = tuple('{}{}'.format(names[0], i) for i in range(Q.dim()))
            else:
                raise ValueError("the number of variables does not match the number of generators")
        return super().__classcall__(cls, Q, names)

    def __init__(self, Q, names, category=None):
        r"""
        Initialize ``self``.
        """
        self._quadratic_form = Q
        R = Q.base_ring()
        category = AlgebrasWithBasis(R.category()).Super().FiniteDimensional().Filtered().or_subcategory(category)
        indices = CliffordAlgebraIndices(Q.dim())
        CombinatorialFreeModule.__init__(self, R, indices, category=category, sorting_key=tuple)
        self._assign_names(names)

    def _repr_(self):
        r"""
        Return a string representation of ``self``.

        """
        return "The Clifford algebra of the {}".format(self._quadratic_form)

    def _repr_term(self, m):
        """
        Return a string representation of the basis element indexed by ``m``.
        """
        if not m:
            return '1'
        term = ''
        for i in m:
            if term:
                term += '*'
            term += self.variable_names()[i]
        return term

    def _latex_term(self, m):
        r"""
        Return a `\LaTeX` representation of the basis element indexed
        by ``m``.
        """
        if not m:
            return '1'
        term = ''
        for i in m:
            term += ' ' + self.latex_variable_names()[i]
        return term

    def _coerce_map_from_(self, V):
        """
        Return if there is a coerce map from ``V`` into ``self``.

        The things which coerce into ``self`` are:

        - Clifford algebras with the same generator names and an equal
          quadratic form over a ring which coerces into the base
          ring of ``self``.
        - The underlying free module of ``self``.
        - The base ring of ``self``.

        EXAMPLES::

            sage: Qp = QuadraticForm(QQ, 3, [1,2,3,4,5,6])
            sage: Clp = CliffordAlgebra(Qp)
        """
        if isinstance(V, CliffordAlgebra):
            Q = self._quadratic_form
            try:
                return (V.variable_names() == self.variable_names() and
                        V._quadratic_form.change_ring(self.base_ring()) == Q)
            except (TypeError, AttributeError):
                return False

        if self.free_module().has_coerce_map_from(V):
            return True

        return super()._coerce_map_from_(V)

    def _element_constructor_(self, x):
        """
        Construct an element of ``self`` from ``x``.

        """
        # This is the natural lift morphism of the underlying free module
        if x in self.free_module():
            R = self.base_ring()
            if x.parent().base_ring() is R:
                return self.element_class(self, {FrozenBitset((i,)): c for i, c in x.items()})
            # if the base ring is different, attempt to coerce it into R
            return self.element_class(self, {FrozenBitset((i,)): R(c) for i, c in x.items() if R(c) != R.zero()})

        if (isinstance(x, CliffordAlgebraElement)
                and self.has_coerce_map_from(x.parent())):
            R = self.base_ring()
            return self.element_class(self, {i: R(c) for i, c in x if R(c) != R.zero()})

        if isinstance(x, tuple):
            R = self.base_ring()
            return self.element_class(self, {FrozenBitset((i,)): R.one() for i in x})

        try:
            return super()._element_constructor_(x)
        except TypeError:
            raise TypeError(f'do not know how to make {x=} an element of self')

    def _basis_index_function(self, x):
        """
        Given an integer indexing the basis, return the correct
        bitset.

        For backwards compatibility, tuples are also accepted.

        """
        Q = self._quadratic_form
        format_style = f"0{Q.dim()}b"

        # if the input is a tuple, assume that it has
        # entries in {0, ..., 2**Q.dim()-1}
        if isinstance(x, tuple):
            return FrozenBitset(x, capacity=Q.dim())

        # slice the output of format in order to make conventions
        # of format and FrozenBitset agree.
        return FrozenBitset(format(x, format_style)[::-1], capacity=Q.dim())

    def gen(self, i):
        """
        Return the ``i``-th standard generator of the algebra ``self``.

        This is the ``i``-th basis vector of the vector space on which
        the quadratic form defining ``self`` is defined, regarded as an
        element of ``self``.


        """
        return self._from_dict({FrozenBitset((i,)): self.base_ring().one()}, remove_zeros=False)

    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.


        """
        d = {x: self.gen(i) for i, x in enumerate(self.variable_names())}
        return Family(self.variable_names(), lambda x: d[x])

    def gens(self):
        r"""
        Return the generators of ``self`` (as an algebra).

        """
        return tuple(self.algebra_generators())

    @cached_method
    def ngens(self):
        """
        Return the number of algebra generators of ``self``.

        """
        return self._quadratic_form.dim()

    @cached_method
    def one_basis(self):
        """
        Return the basis index of the element ``1``. The element ``1``
        is indexed by the emptyset, which is represented by the
        :class:`sage.data_structures.bitset.Bitset` ``0``.


        """
        return FrozenBitset()

    def is_commutative(self):
        """
        Check if ``self`` is a commutative algebra.

        """
        return self._quadratic_form.dim() < 2

    def quadratic_form(self):
        """
        Return the quadratic form of ``self``.

        This is the quadratic form used to define ``self``. The
        quadratic form on ``self`` is yet to be implemented.

        """
        return self._quadratic_form

    def degree_on_basis(self, m):
        r"""
        Return the degree of the monomial indexed by ``m``.

        We are considering the Clifford algebra to be `\NN`-filtered,
        and the degree of the monomial ``m`` is the length of ``m``.

        """
        return ZZ(len(m))

    def graded_algebra(self):
        """
        Return the associated graded algebra of ``self``.

        """
        return ExteriorAlgebra(self.base_ring(), self.variable_names())

    @cached_method
    def free_module(self):
        """
        Return the underlying free module `V` of ``self``.

        This is the free module on which the quadratic form that was
        used to construct ``self`` is defined.

        """
        return FreeModule(self.base_ring(), self._quadratic_form.dim())

    def dimension(self):
        """
        Return the rank of ``self`` as a free module.

        Let `V` be a free `R`-module of rank `n`; then, `Cl(V, Q)` is a
        free `R`-module of rank `2^n`.


        """
        return ZZ(2)**self._quadratic_form.dim()

    def pseudoscalar(self):
        r"""
        Return the unit pseudoscalar of ``self``.

        Given the basis `e_1, e_2, \ldots, e_n` of the underlying
        `R`-module, the unit pseudoscalar is defined as
        `e_1 \cdot e_2 \cdots e_n`.

        This depends on the choice of basis.

        REFERENCES:

        - :wikipedia:`Classification_of_Clifford_algebras#Unit_pseudoscalar`
        """
        d = self._quadratic_form.dim()
        return self.element_class(self, {tuple(range(d)): self.base_ring().one()})

    def lift_module_morphism(self, m, names=None):
        r"""
        Lift the matrix ``m`` to an algebra morphism of Clifford algebras.

        Given a linear map `m : W \to V` (here represented by a matrix
        acting on column vectors), this method returns the algebra
        morphism `Cl(m) : Cl(W, m(Q)) \to Cl(V, Q)`, where `Cl(V, Q)`
        is the Clifford algebra ``self`` and where `m(Q)` is the pullback
        of the quadratic form `Q` to `W`. See the documentation
        of :class:`CliffordAlgebra` for how this pullback and the
        morphism `Cl(m)` are defined.

        .. NOTE::

            This is a map into ``self``.

        INPUT:

        - ``m`` -- a matrix
        - ``names`` -- (default: ``'e'``) the names of the generators of the
          Clifford algebra of the domain of (the map represented by) ``m``

        OUTPUT: the algebra morphism `Cl(m)` from `Cl(W, m(Q))` to ``self``
        """
        Q = self._quadratic_form(m)
        # If R is a quadratic form and m is a matrix, then R(m) returns
        # the quadratic form m^t R m.

        if Q == self._quadratic_form and names is None:
            Cl = self
        else:
            Cl = CliffordAlgebra(Q, names)

        n = self._quadratic_form.dim()
        f = lambda x: self.prod(self._from_dict({FrozenBitset((j, )): m[j, i] for j in range(n)},
                                remove_zeros=True) for i in x)
        cat = AlgebrasWithBasis(self.category().base_ring()).Super().FiniteDimensional()
        return Cl.module_morphism(on_basis=f, codomain=self, category=cat)

    def lift_isometry(self, m, names=None):
        r"""
        Lift an invertible isometry ``m`` of the quadratic form of
        ``self`` to a Clifford algebra morphism.

        Given an invertible linear map `m : V \to W` (here represented by
        a matrix acting on column vectors), this method returns the
        algebra morphism `Cl(m)` from `Cl(V, Q)` to `Cl(W, m^{-1}(Q))`,
        where `Cl(V, Q)` is the Clifford algebra ``self`` and where
        `m^{-1}(Q)` is the pullback of the quadratic form `Q` to `W` along
        the inverse map `m^{-1} : W \to V`. See the documentation of
        :class:`CliffordAlgebra` for how this pullback and the morphism
        `Cl(m)` are defined.

        INPUT:

        - ``m`` -- an isometry of the quadratic form of ``self``
        - ``names`` -- (default: ``'e'``) the names of the generators of
          the Clifford algebra of the codomain of (the map represented by)
          ``m``

        OUTPUT: the algebra morphism `Cl(m)` from ``self`` to `Cl(W, m^{-1}(Q))`
        """
        MS = m.parent()
        if not m.is_invertible():
            raise ValueError('{} is not invertible')
        Q = self._quadratic_form(MS(m.inverse()))

        if Q == self._quadratic_form and names is None:
            Cl = self
        else:
            if names is None:
                names = 'e'
            Cl = CliffordAlgebra(Q, names)

        n = Q.dim()

        f = lambda x: Cl.prod(Cl._from_dict({FrozenBitset((j, )): m[j, i] for j in range(n)},
                              remove_zeros=True) for i in x)
        cat = AlgebrasWithBasis(self.category().base_ring()).Super().FiniteDimensional()
        return self.module_morphism(on_basis=f, codomain=Cl, category=cat)

    # This is a general method for finite dimensional algebras with bases
    #   and should be moved to the corresponding category once there is
    #   a category level method for getting the indexing set of the basis;
    #   similar to #15289 but on a category level.
    @cached_method
    def center_basis(self):
        """
        Return a list of elements which correspond to a basis for the center
        of ``self``.

        This assumes that the ground ring can be used to compute the
        kernel of a matrix.

        .. SEEALSO::

            :meth:`supercenter_basis`,
            http://math.stackexchange.com/questions/129183/center-of-clifford-algebra-depending-on-the-parity-of-dim-v

        .. TODO::

            Deprecate this in favor of a method called `center()` once
            subalgebras are properly implemented in Sage.

        """
        R = self.base_ring()
        B = self.basis()
        K = list(B.keys())
        k = len(K)
        d = {}
        for a, i in enumerate(K):
            Bi = B[i]
            for b, j in enumerate(K):
                Bj = B[j]
                for m, c in (Bi*Bj - Bj*Bi):
                    d[(a, K.index(m)+k*b)] = c
        m = Matrix(R, d, nrows=k, ncols=k*k, sparse=True)
        from_vector = lambda x: self.sum_of_terms(((K[i], c) for i, c in x.items()),
                                                  distinct=True)
        return tuple(map(from_vector, m.kernel().basis()))

    # Same as center except for superalgebras
    @cached_method
    def supercenter_basis(self):
        """
        Return a list of elements which correspond to a basis for the
        supercenter of ``self``.

        This assumes that the ground ring can be used to compute the
        kernel of a matrix.

        .. SEEALSO::

            :meth:`center_basis`,
            http://math.stackexchange.com/questions/129183/center-of-clifford-algebra-depending-on-the-parity-of-dim-v

        .. TODO::

            Deprecate this in favor of a method called `supercenter()` once
            subalgebras are properly implemented in Sage.
        """
        R = self.base_ring()
        B = self.basis()
        K = list(B.keys())
        k = len(K)
        d = {}
        for a, i in enumerate(K):
            Bi = B[i]
            for b, j in enumerate(K):
                Bj = B[j]
                if len(i) % 2 and len(j) % 2:
                    supercommutator = Bi * Bj + Bj * Bi
                else:
                    supercommutator = Bi * Bj - Bj * Bi
                for m, c in supercommutator:
                    d[(a, K.index(m) + k * b)] = c
        m = Matrix(R, d, nrows=k, ncols=k * k, sparse=True)
        from_vector = lambda x: self.sum_of_terms(((K[i], c) for i, c in x.items()),
                                                  distinct=True)
        return tuple(map(from_vector, m.kernel().basis()))

    Element = CliffordAlgebraElement


class ExteriorAlgebra(CliffordAlgebra):
    r"""
    An exterior algebra of a free module over a commutative ring.

    Let `V` be a module over a commutative ring `R`. The exterior algebra
    (or Grassmann algebra) `\Lambda(V)` of `V` is defined as the quotient
    of the tensor algebra `T(V)` of `V` modulo the two-sided ideal
    generated by all tensors of the form `x \otimes x` with `x \in V`. The
    multiplication on `\Lambda(V)` is denoted by `\wedge` (so
    `v_1 \wedge v_2 \wedge \cdots \wedge v_n` is the projection of
    `v_1 \otimes v_2 \otimes \cdots \otimes v_n` onto `\Lambda(V)`) and
    called the "exterior product" or "wedge product".

    If `V` is a rank-`n` free `R`-module with a basis
    `\{e_1, \ldots, e_n\}`, then `\Lambda(V)` is the `R`-algebra
    noncommutatively generated by the `n` generators `e_1, \ldots, e_n`
    subject to the relations `e_i^2 = 0` for all `i`, and
    `e_i e_j = - e_j e_i` for all `i < j`. As an `R`-module,
    `\Lambda(V)` then has a basis `(\bigwedge_{i \in I} e_i)` with `I`
    ranging over the subsets of `\{1, 2, \ldots, n\}` (where
    `\bigwedge_{i \in I} e_i` is the wedge product of `e_i` for `i`
    running through all elements of `I` from smallest to largest), and
    hence is free of rank `2^n`.

    The exterior algebra of an `R`-module `V` can also be realized
    as the Clifford algebra of `V` for the quadratic form `Q` given by
    `Q(v) = 0` for all vectors `v \in V`. See :class:`CliffordAlgebra`
    for the notion of a Clifford algebra.

    The exterior algebra of an `R`-module `V` is a connected `\ZZ`-graded
    Hopf superalgebra. It is commutative in the super sense (i.e., the
    odd elements anticommute and square to `0`).

    This class implements the exterior algebra `\Lambda(R^n)` for
    `n` a nonnegative integer.

    INPUT:

    - ``R`` -- the base ring, *or* the free module whose exterior algebra
      is to be computed

    - ``names`` -- list of strings to name the generators of the
      exterior algebra; this list can either have one entry only (in which
      case the generators will be called ``e + '0'``, ``e + '1'``, ...,
      ``e + 'n-1'``, with ``e`` being said entry), or have ``n`` entries
      (in which case these entries will be used directly as names for the
      generators)

    - ``n`` -- the number of generators, i.e., the rank of the free
      module whose exterior algebra is to be computed (this doesn't have
      to be provided if it can be inferred from the rest of the input)

    REFERENCES:

    - :wikipedia:`Exterior_algebra`
    """
    @staticmethod
    def __classcall_private__(cls, R, names=None, n=None):
        """
        Normalize arguments to ensure a unique representation.

        """
        if names is None:
            names = 'e'
        elif names in ZZ:
            n = names
            names = 'e'

        if isinstance(R, FreeModule_generic):
            if n is not None and n != R.dimension():
                raise ValueError("the number of variables does not match the dimension")
            n = R.dimension()
            R = R.base_ring()

        names = tuple(names)
        if n is not None and len(names) != n:
            if len(names) == 1:
                names = tuple('{}{}'.format(names[0], i) for i in range(n))
            else:
                raise ValueError("the number of variables does not match the number of generators")
        return super().__classcall__(cls, R, names)

    def __init__(self, R, names):
        """
        Initialize ``self``.


        """
        cat = HopfAlgebrasWithBasis(R).FiniteDimensional().Supercommutative().Supercocommutative()
        CliffordAlgebra.__init__(self, QuadraticForm(R, len(names)), names, category=cat)

    def _repr_(self):
        r"""
        Return a string representation of ``self``.

        """
        return "The exterior algebra of rank {} over {}".format(self.ngens(), self.base_ring())

    def _repr_term(self, m):
        """
        Return a string representation of the basis element indexed by
        ``m``.

        """
        if len(m) == 0:
            return '1'
        term = ''
        for i in m:
            if len(term) != 0:
                term += '*'
            term += self.variable_names()[i]
        return term

    def _ascii_art_term(self, m):
        r"""
        Return ascii art for the basis element indexed by ``m``.

        """
        if len(m) == 0:
            return ascii_art('1')
        wedge = '/\\'
        return ascii_art(*[repr(self.basis()[FrozenBitset((i, ))]) for i in m], sep=wedge)

    def _unicode_art_term(self, m):
        """
        Return unicode art for the basis element indexed by ``m``.

        """
        if len(m) == 0:
            return unicode_art('1')
        wedge = unicodedata.lookup('LOGICAL AND')
        return unicode_art(*[self.variable_names()[i] for i in m], sep=wedge)

    def _latex_term(self, m):
        r"""
        Return a `\LaTeX` representation of the basis element indexed
        by ``m``.

        """
        if len(m) == 0:
            return '1'
        term = ''
        for i in m:
            if len(term) != 0:
                term += ' \\wedge'
            term += ' ' + self.latex_variable_names()[i]
        return term

    def lift_morphism(self, phi, names=None):
        r"""
        Lift the matrix ``m`` to an algebra morphism of exterior algebras.

        Given a linear map `\phi : V \to W` (here represented by a matrix
        acting on column vectors over the base ring of `V`), this method
        returns the algebra morphism
        `\Lambda(\phi) : \Lambda(V) \to \Lambda(W)`. This morphism is defined
        on generators `v_i \in \Lambda(V)` by `v_i \mapsto \phi(v_i)`.

        .. NOTE::

            This is the map going out of ``self`` as opposed to
            :meth:`~sage.algebras.clifford_algebra.CliffordAlgebraElement.lift_module_morphism()`
            for general Clifford algebras.

        INPUT:

        - ``phi`` -- a linear map `\phi` from `V` to `W`, encoded as a
          matrix
        - ``names`` -- (default: ``'e'``) the names of the generators of
          the Clifford algebra of the domain of (the map represented by)
          ``phi``

        OUTPUT: the algebra morphism `\Lambda(\phi)` from ``self`` to
        `\Lambda(W)`

        """
        n = phi.nrows()
        R = self.base_ring()
        E = ExteriorAlgebra(R, names, n)
        f = lambda x: E.prod(E._from_dict({FrozenBitset((j, )): phi[j, i] for j in range(n)},
                             remove_zeros=True) for i in x)
        cat = AlgebrasWithBasis(R).Super().FiniteDimensional()
        return self.module_morphism(on_basis=f, codomain=E, category=cat)

    def volume_form(self):
        r"""
        Return the volume form of ``self``.

        Given the basis `e_1, e_2, \ldots, e_n` of the underlying
        `R`-module, the volume form is defined as `e_1 \wedge e_2
        \wedge \cdots \wedge e_n`.

        This depends on the choice of basis.

        """
        d = self._quadratic_form.dim()
        return self.element_class(self, {tuple(range(d)): self.base_ring().one()})

    def boundary(self, s_coeff):
        r"""
        Return the boundary operator `\partial` defined by the structure
        coefficients ``s_coeff`` of a Lie algebra.

        For more on the boundary operator, see
        :class:`ExteriorAlgebraBoundary`.

        INPUT:

        - ``s_coeff`` -- dictionary whose keys are in `I \times I`, where
          `I` is the index set of the underlying vector space `V`, and whose
          values can be coerced into 1-forms (degree 1 elements) in ``E``
          (usually, these values will just be elements of `V`)

        """
        return ExteriorAlgebraBoundary(self, s_coeff)

    def coboundary(self, s_coeff):
        r"""
        Return the coboundary operator `d` defined by the structure
        coefficients ``s_coeff`` of a Lie algebra.

        For more on the coboundary operator, see
        :class:`ExteriorAlgebraCoboundary`.

        INPUT:

        - ``s_coeff`` -- dictionary whose keys are in `I \times I`, where
          `I` is the index set of the underlying vector space `V`, and whose
          values can be coerced into 1-forms (degree 1 elements) in ``E``
          (usually, these values will just be elements of `V`)

        """
        return ExteriorAlgebraCoboundary(self, s_coeff)

    def degree_on_basis(self, m):
        r"""
        Return the degree of the monomial indexed by ``m``.

        The degree of ``m`` in the `\ZZ`-grading of ``self`` is defined
        to be the length of ``m``.

        """
        return ZZ(len(m))

    def coproduct_on_basis(self, a):
        r"""
        Return the coproduct on the basis element indexed by ``a``.

        The coproduct is defined by

        .. MATH::

            \Delta(e_{i_1} \wedge \cdots \wedge e_{i_m}) = \sum_{k=0}^m
            \sum_{\sigma \in Ush_{k,m-k}} (-1)^{\sigma}
            (e_{i_{\sigma(1)}} \wedge \cdots \wedge e_{i_{\sigma(k)}}) \otimes
            (e_{i_{\sigma(k+1)}} \wedge \cdots \wedge e_{i_{\sigma(m)}}),

        where `Ush_{k,m-k}` denotes the set of all `(k,m-k)`-unshuffles
        (i.e., permutations in `S_m` which are increasing on the interval
        `\{1, 2, \ldots, k\}` and on the interval
        `\{k+1, k+2, \ldots, k+m\}`).

        .. WARNING::

            This coproduct is a homomorphism of superalgebras, not a
            homomorphism of algebras!

        """
        from sage.combinat.combinat import unshuffle_iterator
        one = self.base_ring().one()
        L = unshuffle_iterator(tuple(a), one)
        return self.tensor_square()._from_dict(
            {tuple(FrozenBitset(e) if e else FrozenBitset() for e in t): c for t, c in L if c},
            coerce=False,
            remove_zeros=False)

    def antipode_on_basis(self, m):
        r"""
        Return the antipode on the basis element indexed by ``m``.

        Given a basis element `\omega`, the antipode is defined by
        `S(\omega) = (-1)^{\deg(\omega)} \omega`.

        """
        return self.term(m, (-self.base_ring().one())**len(m))

    def counit(self, x):
        r"""
        Return the counit of ``x``.

        The counit of an element `\omega` of the exterior algebra
        is its constant coefficient.

        """
        return x.constant_coefficient()

    def interior_product_on_basis(self, a, b):
        r"""
        Return the interior product `\iota_b a` of ``a`` with respect to
        ``b``.

        See :meth:`~sage.algebras.clifford_algebra.CliffordAlgebra.Element.interior_product`
        for more information.

        In this method, ``a`` and ``b`` are supposed to be
        basis elements (see
        :meth:`~sage.algebras.clifford_algebra.CliffordAlgebra.Element.interior_product`
        for a method that computes interior product of arbitrary
        elements), and to be input as their keys.

        This depends on the choice of basis of the vector space
        whose exterior algebra is ``self``.

        """
        sgn = True
        t = list(a)
        for i in b:
            if i not in t:
                return self.zero()
            if t.index(i) % 2:
                sgn = not sgn
            t.remove(i)
        R = self.base_ring()
        if not t:  # catch empty sets
            t = None
        return self.term(FrozenBitset(t), (R.one() if sgn else - R.one()))

    def lifted_bilinear_form(self, M):
        r"""
        Return the bilinear form on the exterior algebra ``self``
        `= \Lambda(V)` which is obtained by lifting the bilinear
        form `f` on `V` given by the matrix ``M``.

        Let `V` be a module over a commutative ring `R`, and let
        `f : V \times V \to R` be a bilinear form on `V`. Then,
        a bilinear form `\Lambda(f) : \Lambda(V) \times
        \Lambda(V) \to R` on `\Lambda(V)` can be canonically
        defined as follows: For every `n \in \NN`, `m \in \NN`,
        `v_1, v_2, \ldots, v_n, w_1, w_2, \ldots, w_m \in V`,
        we define

        .. MATH::

            \Lambda(f)
            ( v_1 \wedge v_2 \wedge \cdots \wedge v_n ,
              w_1 \wedge w_2 \wedge \cdots \wedge w_m )
            := \begin{cases}
              0, &\mbox{if } n \neq m ; \\
              \det G, & \mbox{if } n = m \end{cases} ,

        where `G` is the `n \times m`-matrix whose
        `(i, j)`-th entry is `f(v_i, w_j)`. This bilinear form
        `\Lambda(f)` is known as the bilinear form on
        `\Lambda(V)` obtained by lifting the bilinear form `f`.
        Its restriction to the `1`-st homogeneous component
        `V` of `\Lambda(V)` is `f`.

        The bilinear form `\Lambda(f)` is symmetric if `f` is.

        INPUT:

        - ``M`` -- a matrix over the same base ring as ``self``,
          whose `(i, j)`-th entry is `f(e_i, e_j)`, where
          `(e_1, e_2, \ldots, e_N)` is the standard basis of the
          module `V` for which ``self`` `= \Lambda(V)` (so that
          `N = \dim(V)`), and where `f` is the bilinear form
          which is to be lifted.

        OUTPUT:

        A bivariate function which takes two elements `p` and
        `q` of ``self`` to `\Lambda(f)(p, q)`.

        .. NOTE::

            This takes a bilinear form on `V` as matrix, and
            returns a bilinear form on ``self`` as a function in
            two arguments. We do not return the bilinear form as
            a matrix since this matrix can be huge and one often
            needs just a particular value.

        .. TODO::

            Implement a class for bilinear forms and rewrite this
            method to use that class.

        """
        R = self.base_ring()

        def lifted_form(x, y):
            result = R.zero()
            for mx, cx in x:
                for my, cy in y:
                    n = len(mx)
                    m = len(my)
                    if m != n:
                        continue
                    matrix_list = [M[i, j] for i in mx for j in my]
                    MA = MatrixArgs(R, n, matrix_list)
                    del matrix_list
                    result += cx * cy * MA.matrix(False).determinant()
            return result
        from sage.categories.cartesian_product import cartesian_product
        return PoorManMap(lifted_form, domain=cartesian_product([self, self]),
                          codomain=self.base_ring(),
                          name="Bilinear Form")

    def _ideal_class_(self, n=0):
        """
        Return the class that is used to implement ideals of ``self``.

        """
        return ExteriorAlgebraIdeal

    Element = ExteriorAlgebraElement


#####################################################################
# Differentials


class ExteriorAlgebraDifferential(ModuleMorphismByLinearity,
                                  UniqueRepresentation,
                                  metaclass=InheritComparisonClasscallMetaclass):
    r"""
    Internal class to store the data of a boundary or coboundary of
    an exterior algebra `\Lambda(L)` defined by the structure
    coefficients of a Lie algebra `L`.

    See :class:`ExteriorAlgebraBoundary` and
    :class:`ExteriorAlgebraCoboundary` for the actual classes, which
    inherit from this.

    .. WARNING::

        This is not a general class for differentials on the exterior
        algebra.
    """
    @staticmethod
    def __classcall__(cls, E, s_coeff):
        """
        Standardize the structure coefficients to ensure a unique
        representation.

        """
        d = {}

        for k, v in dict(s_coeff).items():
            if not v:  # Strip terms with 0
                continue

            if isinstance(v, dict):
                R = E.base_ring()
                v = E._from_dict({FrozenBitset((i,)): R(c) for i, c in v.items()})
            else:
                # Make sure v is in ``E``
                v = E(v)
                # It's okay if v.degree results in an error
                #   (we'd throw a similar error) unless v == 0 (which
                #   is what v.list() is testing for)
                if v.list() and v.degree() != 1:
                    raise ValueError("elements must be degree 1")

            if k[0] < k[1]:
                d[tuple(k)] = v
            else:
                d[(k[1], k[0])] = -v

        from sage.sets.family import Family
        return super().__classcall__(cls, E, Family(d))

    def __init__(self, E, s_coeff):
        """
        Initialize ``self``.

        """
        self._s_coeff = s_coeff

        # Technically this preserves the grading but with a shift of -1
        cat = AlgebrasWithBasis(E.base_ring()).FiniteDimensional()
        ModuleMorphismByLinearity.__init__(self, domain=E, codomain=E, category=cat)

    def homology(self, deg=None, **kwds):
        """
        Return the homology determined by ``self``.

        """
        return self.chain_complex().homology(deg, **kwds)


class ExteriorAlgebraBoundary(ExteriorAlgebraDifferential):
    r"""
    The boundary `\partial` of an exterior algebra `\Lambda(L)` defined
    by the structure coefficients of `L`.

    Let `L` be a Lie algebra. We give the exterior algebra
    `E = \Lambda(L)` a chain complex structure by considering a
    differential `\partial : \Lambda^{k+1}(L) \to \Lambda^k(L)` defined by

    .. MATH::

        \partial(x_1 \wedge x_2 \wedge \cdots \wedge x_{k+1})
        = \sum_{i < j} (-1)^{i+j+1}
        [x_i, x_j] \wedge x_1 \wedge \cdots \wedge \hat{x}_i \wedge \cdots
        \wedge \hat{x}_j \wedge \cdots \wedge x_{k+1}

    where `\hat{x}_i` denotes a missing index. The corresponding homology is
    the Lie algebra homology.

    INPUT:

    - ``E`` -- an exterior algebra of a vector space `L`
    - ``s_coeff`` -- dictionary whose keys are in `I \times I`, where
      `I` is the index set of the basis of the vector space `L`, and whose
      values can be coerced into 1-forms (degree 1 elements) in ``E``;
      this dictionary will be used to define the Lie algebra structure
      on `L` (indeed, the `i`-th coordinate of the Lie bracket of the
      `j`-th and `k`-th basis vectors of `L` for `j < k` is set to be
      the value at the key `(j, k)` if this key appears in ``s_coeff``,
      or otherwise the negated of the value at the key `(k, j)`)

    .. WARNING::

        The values of ``s_coeff`` are supposed to be coercible into
        1-forms in ``E``; but they can also be dictionaries themselves
        (in which case they are interpreted as giving the coordinates of
        vectors in ``L``). In the interest of speed, these dictionaries
        are not sanitized or checked.

    .. WARNING::

        For any two distinct elements `i` and `j` of `I`, the dictionary
        ``s_coeff`` must have only one of the pairs `(i, j)` and
        `(j, i)` as a key. This is not checked.

    REFERENCES:

    - :wikipedia:`Exterior_algebra#Lie_algebra_homology`
    """
    def _repr_type(self):
        """

        """
        return "Boundary"

    def _on_basis(self, m):
        """
        Return the differential on the basis element indexed by ``m``.

        """
        from itertools import combinations
        E = self.domain()
        sc = self._s_coeff
        keys = sc.keys()

        s = E.zero()

        for b, (i, j) in enumerate(combinations(m, 2)):
            if (i, j) not in keys:
                continue
            t = Bitset(m)
            t.discard(i)
            t.discard(j)
            s += sc[i, j] * E.term(FrozenBitset(t), (-1)**b)

        return s

    @cached_method
    def chain_complex(self, R=None):
        """
        Return the chain complex over ``R`` determined by ``self``.

        INPUT:

        - ``R`` -- the base ring; the default is the base ring of
          the exterior algebra

        """
        from sage.homology.chain_complex import ChainComplex
        from sage.matrix.constructor import Matrix
        E = self.domain()
        n = E.ngens()
        if R is None:
            R = E.base_ring()

        if n == 0:
            # Special case because there are no matrices and thus the
            # ChainComplex constructor needs the dimension of the
            # 0th degree space explicitly given.
            return ChainComplex({1: Matrix(R, [[]])}, degree=-1)
            # If you are reading this because you changed something about
            # the ChainComplex constructor and the doctests are failing:
            # This should return a chain complex with degree -1 and
            # only one nontrivial module, namely a free module of rank 1,
            # situated in degree 0.

        # Group the basis into degrees
        basis_by_deg = {deg: [] for deg in range(n+1)}
        for b in E.basis().keys():
            basis_by_deg[len(b)].append(b)

        # Construct the transition matrices
        data = {}
        prev_basis = basis_by_deg[0]
        for deg in range(1, n+1):
            # Make sure within each basis we're sorted by lex
            basis = sorted(basis_by_deg[deg])
            mat = []
            for b in basis:
                ret = self._on_basis(b)
                mat.append([ret.coefficient(p) for p in prev_basis])
            data[deg] = Matrix(mat).transpose().change_ring(R)
            prev_basis = basis

        return ChainComplex(data, degree=-1)


class ExteriorAlgebraCoboundary(ExteriorAlgebraDifferential):
    r"""
    The coboundary `d` of an exterior algebra `\Lambda(L)` defined
    by the structure coefficients of a Lie algebra `L`.

    Let `L` be a Lie algebra. We endow its exterior algebra
    `E = \Lambda(L)` with a cochain complex structure by considering a
    differential `d : \Lambda^k(L) \to \Lambda^{k+1}(L)` defined by

    .. MATH::

        d x_i = \sum_{j < k} s_{jk}^i x_j x_k,

    where `(x_1, x_2, \ldots, x_n)` is a basis of `L`, and where
    `s_{jk}^i` is the `x_i`-coordinate of the Lie bracket `[x_j, x_k]`.

    The corresponding cohomology is the Lie algebra cohomology of `L`.

    This can also be thought of as the exterior derivative, in which case
    the resulting cohomology is the de Rham cohomology of a manifold whose
    exterior algebra of differential forms is ``E``.

    INPUT:

    - ``E`` -- an exterior algebra of a vector space `L`
    - ``s_coeff`` -- dictionary whose keys are in `I \times I`, where
      `I` is the index set of the basis of the vector space `L`, and whose
      values can be coerced into 1-forms (degree 1 elements) in ``E``;
      this dictionary will be used to define the Lie algebra structure
      on `L` (indeed, the `i`-th coordinate of the Lie bracket of the
      `j`-th and `k`-th basis vectors of `L` for `j < k` is set to be
      the value at the key `(j, k)` if this key appears in ``s_coeff``,
      or otherwise the negated of the value at the key `(k, j)`)

    .. WARNING::

        For any two distinct elements `i` and `j` of `I`, the dictionary
        ``s_coeff`` must have only one of the pairs `(i, j)` and
        `(j, i)` as a key. This is not checked.
    """
    def __init__(self, E, s_coeff):
        """
        Initialize ``self``.
        """
        # Construct the dictionary of costructure coefficients, i.e. given
        # [x_j, x_k] = \sum_i s_{jk}^i x_i, we get x^i |-> \sum_{j<k} s_{jk}^i x^j x^k.
        # This dictionary might contain 0 values and might also be missing
        # some keys (both times meaning that the respective `s_{jk}^i` are
        # zero for all `j` and `k`).
        self._cos_coeff = {}
        zero = E.zero()
        B = E.basis()
        for k, v in dict(s_coeff).items():
            if k[0] > k[1]:  # k will have length 2
                k = sorted(k)
                v = -v

            k = B[FrozenBitset(k)]
            for m, c in v:
                self._cos_coeff[m] = self._cos_coeff.get(m, zero) + c * k
        ExteriorAlgebraDifferential.__init__(self, E, s_coeff)

    def _repr_type(self):
        """

        """
        return "Coboundary"

    def _on_basis(self, m):
        r"""
        Return the differential on the basis element indexed by ``m``.

        """
        E = self.domain()
        cc = self._cos_coeff

        tot = E.zero()

        for sgn, i in enumerate(m):
            k = FrozenBitset((i,))
            if k in cc:
                below = tuple([j for j in m if j < i])
                above = tuple([j for j in m if j > i])

                # a hack to deal with empty bitsets
                if not below:
                    below = E.one()
                else:
                    below = E.monomial(FrozenBitset(below))
                if not above:
                    above = E.one()
                else:
                    above = E.monomial(FrozenBitset(above))

                tot += (-1)**sgn * below * cc[k] * above

        return tot

    @cached_method
    def chain_complex(self, R=None):
        """
        Return the chain complex over ``R`` determined by ``self``.

        INPUT:

        - ``R`` -- the base ring; the default is the base ring of
          the exterior algebra

        """
        from sage.homology.chain_complex import ChainComplex
        from sage.matrix.constructor import Matrix
        E = self.domain()
        n = E.ngens()
        if R is None:
            R = E.base_ring()

        if n == 0:
            # Special case because there are no matrices and thus the
            # ChainComplex constructor needs the dimension of the
            # 0th degree space explicitly given.
            return ChainComplex({-1: Matrix(R, [[]])}, degree=1)
            # If you are reading this because you changed something about
            # the ChainComplex constructor and the doctests are failing:
            # This should return a chain complex with degree 1 and
            # only one nontrivial module, namely a free module of rank 1,
            # situated in degree 0.

        # Group the basis into degrees
        basis_by_deg = {deg: [] for deg in range(n+1)}
        for b in E.basis().keys():
            basis_by_deg[len(b)].append(b)

        # Construct the transition matrices
        data = {}
        basis = basis_by_deg[0]
        for deg in range(n):
            # Make sure within each basis we're sorted by lex
            next_basis = sorted(basis_by_deg[deg+1])
            mat = []
            for b in basis:
                ret = self._on_basis(b)
                try:
                    mat.append([ret.coefficient(p) for p in next_basis])
                except AttributeError:  # if ret is in E.base_ring()
                    mat.append([E.base_ring()(ret)]*len(next_basis))
            data[deg] = Matrix(mat).transpose().change_ring(R)
            basis = next_basis

        return ChainComplex(data, degree=1)


@richcmp_method
class ExteriorAlgebraIdeal(Ideal_nc):
    """
    An ideal of the exterior algebra.

    """
    def __init__(self, ring, gens, coerce=True, side='twosided'):
        """
        Initialize ``self``.

        """
        self._groebner_strategy = None
        self._reduced = False
        self._homogeneous = all(x.is_super_homogeneous() for x in gens if x)
        if self._homogeneous:
            side = "twosided"
        Ideal_nc.__init__(self, ring, gens, coerce, side)

    def reduce(self, f):
        """
        Reduce ``f`` modulo ``self``.

        """
        if self._groebner_strategy is None:
            self.groebner_basis()
        R = self.ring()
        return self._groebner_strategy.reduce(R(f))

    def _contains_(self, f):
        r"""
        Return ``True`` if ``f`` is in this ideal,
        ``False`` otherwise.

        """
        return not self.reduce(f)

    def __richcmp__(self, other, op):
        """
        Compare ``self`` and ``other``.

        """
        if not isinstance(other, ExteriorAlgebraIdeal):
            if op == op_EQ:
                return False
            if op == op_NE:
                return True
            return NotImplemented

        if self is other:
            return rich_to_bool(op, 0)

        # comparison for >= and > : swap the arguments
        if op == op_GE:
            return other.__richcmp__(self, op_LE)
        elif op == op_GT:
            return other.__richcmp__(self, op_LT)

        s_gens = {g for g in self.gens() if g}
        o_gens = {g for g in other.gens() if g}

        if self.side() != other.side():
            if other.side() == "right":
                X = {t * f for t in self.ring().basis() for f in s_gens}
                s_gens.update(X)
            elif other.side() == "left":
                X = {f * t for t in self.ring().basis() for f in s_gens}
                s_gens.update(X)

        if set(s_gens) == set(o_gens):
            return rich_to_bool(op, 0)

        contained = all(f in other for f in s_gens)
        if op == op_LE:
            return contained
        if op == op_NE and not contained:
            return True

        if self.side() != other.side():
            if self.side() == "right":
                X = {t * f for t in self.ring().basis() for f in o_gens}
                s_gens.update(X)
            elif self.side() == "left":
                X = {f * t for t in self.ring().basis() for f in o_gens}
                s_gens.update(X)

        contains = all(f in self for f in o_gens)
        if op == op_EQ:
            return contained and contains
        if op == op_NE:
            return not (contained and contains)
        # remaining case <
        return contained and not contains

    def __mul__(self, other):
        """
        Return the product of ``self`` with ``other``.

        .. WARNING::

            If ``self`` is a right ideal and ``other`` is a left ideal,
            this returns a submodule rather than an ideal.

        """
        if not isinstance(other, ExteriorAlgebraIdeal) or self.ring() != other.ring():
            return super().__mul__(other)

        if self._homogeneous or other._homogeneous or (self.side() == "left" and other.side() == "right"):
            gens = (x * y for x in self.gens() for y in other.gens())
        else:
            gens = (x * t * y for t in self.ring().basis() for x in self.gens() for y in other.gens())
        gens = [z for z in gens if z]

        if self.side() == "right" and other.side() == "left":
            return self.ring().submodule(gens)

        if self.side() == "left" or self.side() == "twosided":
            if other.side() == "right" or other.side() == "twosided":
                return self.ring().ideal(gens, side='twosided')
            return self.ring().ideal(gens, side='left')
        return self.ring().ideal(gens, side='right')

    def groebner_basis(self, term_order=None, reduced=True):
        r"""
        Return the (reduced) Gröbner basis of ``self``.

        INPUT:

        - ``term_order`` -- the term order used to compute the Gröbner basis;
          must be one of the following:

          * ``'neglex'`` -- (default) negative (read right-to-left) lex order
          * ``'degrevlex'`` -- degree reverse lex order
          * ``'deglex'`` -- degree lex order

        - ``reduced`` -- boolean (default: ``True``); whether or not to return
          the reduced Gröbner basis

        """
        if self.ring().base_ring() not in Fields():
            raise NotImplementedError("only implemented over fields")
        if term_order is None:
            if self._groebner_strategy is not None:
                strategy = type(self._groebner_strategy)
            else:
                from sage.algebras.exterior_algebra_groebner import GroebnerStrategyNegLex as strategy
        else:
            if term_order == "neglex":
                from sage.algebras.exterior_algebra_groebner import GroebnerStrategyNegLex as strategy
            elif term_order == "degrevlex":
                from sage.algebras.exterior_algebra_groebner import GroebnerStrategyDegRevLex as strategy
            elif term_order == "deglex":
                from sage.algebras.exterior_algebra_groebner import GroebnerStrategyDegLex as strategy
            else:
                raise ValueError("invalid term order")
        if isinstance(self._groebner_strategy, strategy):
            if self._reduced or not reduced:
                return self._groebner_strategy.groebner_basis
            self._reduced = reduced
            self._groebner_strategy.reduce_computed_gb()
            return self._groebner_strategy.groebner_basis
        self._groebner_strategy = strategy(self)
        self._groebner_strategy.compute_groebner(reduced=reduced)
        self._reduced = reduced
        return self._groebner_strategy.groebner_basis
