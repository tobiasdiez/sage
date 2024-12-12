# sage.doctest: needs sage.modules
r"""
Associated Graded Algebras To Filtered Algebras

AUTHORS:

- Travis Scrimshaw (2014-10-08): Initial version
"""

#*****************************************************************************
#  Copyright (C) 2014 Travis Scrimshaw <tscrim at ucdavis.edu>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.misc.cachefunc import cached_method
from copy import copy

from sage.sets.family import Family
from sage.combinat.free_module import CombinatorialFreeModule


class AssociatedGradedAlgebra(CombinatorialFreeModule):
    r"""
    The associated graded algebra/module `\operatorname{gr} A`
    of a filtered algebra/module with basis `A`.

    Let `A` be a filtered module over a commutative ring `R`.
    Let `(F_i)_{i \in I}` be the filtration of `A`, with `I` being
    a totally ordered set. Define

    .. MATH::

        G_i = F_i / \sum_{j < i} F_j

    for every `i \in I`, and then

    .. MATH::

        \operatorname{gr} A = \bigoplus_{i \in I} G_i.

    There are canonical projections `p_i : F_i \to G_i` for
    every `i \in I`. Moreover `\operatorname{gr} A` is naturally a
    graded `R`-module with `G_i` being the `i`-th graded component.
    This graded `R`-module is known as the *associated graded module*
    (or, for short, just *graded module*) of `A`.

    Now, assume that `A` (endowed with the filtration
    `(F_i)_{i \in I}`) is not just a filtered `R`-module, but also
    a filtered `R`-algebra.
    Let `u \in G_i` and `v \in G_j`, and let `u' \in F_i` and
    `v' \in F_j` be lifts of `u` and `v`, respectively (so that
    `u = p_i(u')` and `v = p_j(v')`). Then, we define a
    multiplication `*` on `\operatorname{gr} A` (not to be mistaken
    for the multiplication of the original algebra `A`) by

    .. MATH::

        u * v = p_{i+j} (u' v').

    The *associated graded algebra* (or, for short, just
    *graded algebra*) of `A` is the graded algebra
    `\operatorname{gr} A` (endowed with this multiplication).

    Now, assume that `A` is a filtered `R`-algebra with basis.
    Let `(b_x)_{x \in X}` be the basis of `A`,
    and consider the partition `X = \bigsqcup_{i \in I} X_i` of
    the set `X`, which is part of the data of a filtered
    algebra with basis. We know (see
    :class:`~sage.categories.filtered_modules_with_basis.FilteredModulesWithBasis`)
    that `A` (being a filtered `R`-module with basis) is canonically
    (when the basis is considered to be part of the data)
    isomorphic to `\operatorname{gr} A` as an `R`-module. Therefore
    the `k`-th graded component `G_k` can be identified with
    the span of `(b_x)_{x \in X_k}`, or equivalently the
    `k`-th homogeneous component of `A`. Suppose
    that `u' v' = \sum_{k \leq i+j} m_k` where `m_k \in G_k` (which
    has been identified with the `k`-th homogeneous component of `A`).
    Then `u * v = m_{i+j}`. We also note that the choice of
    identification of `G_k` with the `k`-th homogeneous component
    of `A` depends on the given basis.

    The basis `(b_x)_{x \in X}` of `A` gives rise to a basis
    of `\operatorname{gr} A`. This latter basis is still indexed
    by the elements of `X`, and consists of the images of the
    `b_x` under the `R`-module isomorphism from `A` to
    `\operatorname{gr} A`. It makes `\operatorname{gr} A` into
    a graded `R`-algebra with basis.

    In this class, the `R`-module isomorphism from `A` to
    `\operatorname{gr} A` is implemented as
    :meth:`to_graded_conversion` and also as the default
    conversion from `A` to `\operatorname{gr} A`. Its
    inverse map is implemented as
    :meth:`from_graded_conversion`.
    The projection `p_i : F_i \to G_i` is implemented as
    :meth:`projection` ``(i)``.

    INPUT:

    - ``A`` -- a filtered module (or algebra) with basis

    OUTPUT:

    The associated graded module of `A`, if `A` is just a filtered
    `R`-module.
    The associated graded algebra of `A`, if `A` is a filtered
    `R`-algebra.

    """
    def __init__(self, A, category=None):
        """
        Initialize ``self``.

        """
        if A not in ModulesWithBasis(A.base_ring().category()).Filtered():
            raise ValueError("the base algebra must be filtered and with basis")
        self._A = A

        base_ring = A.base_ring()
        base_one = base_ring.one()

        category = A.category().Graded().or_subcategory(category)
        try:
            opts = copy(A.print_options())
            if not opts['prefix'] and not opts['bracket']:
                opts['bracket'] = '('
            opts['prefix'] = opts['prefix'] + 'bar'
        except AttributeError:
            opts = {'prefix': 'Abar'}

        CombinatorialFreeModule.__init__(self, base_ring, A.basis().keys(),
                                         category=category, **opts)

        # Setup the conversion back
        phi = self.module_morphism(diagonal=lambda x: base_one, codomain=A)
        self._A.register_conversion(phi)

    def _repr_(self):
        """
        Return a string representation of ``self``.

        """
        from sage.categories.algebras_with_basis import AlgebrasWithBasis
        if self in AlgebrasWithBasis:
            return "Graded Algebra of {}".format(self._A)
        return "Graded Module of {}".format(self._A)

    def _latex_(self):
        r"""
        Return a latex representation of ``self``.

        """
        from sage.misc.latex import latex
        return "\\operatorname{gr} " + latex(self._A)

    def _element_constructor_(self, x):
        r"""
        Construct an element of ``self`` from ``x``.

        If ``self`` `= \operatorname{gr} A` for a filtered algebra
        `A` with basis, and if ``x`` is an element of `A`, then
        this returns the image of `x` under the canonical `R`-module
        isomorphism `A \to \operatorname{gr} A`. (In this case,
        this is equivalent to calling
        ``self.to_graded_conversion()(x)``.)

        EXAMPLES::

            sage: A = Algebras(QQ).WithBasis().Filtered()
        """
        if isinstance(x, CombinatorialFreeModule.Element):
            if x.parent() is self._A:
                return self._from_dict(dict(x))
        return super()._element_constructor_(x)

    def gen(self, *args, **kwds):
        """
        Return a generator of ``self``.
        """
        try:
            x = self._A.gen(*args, **kwds)
        except AttributeError:
            x = self._A.algebra_generators()[args[0]]
        return self(x)

    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        This assumes that the algebra generators of `A` provided by
        its ``algebra_generators`` method are homogeneous.
        """
        G = self._A.algebra_generators()
        return Family(G.keys(), lambda x: self(G[x]), name='generator')

    def degree_on_basis(self, x):
        """
        Return the degree of the basis element indexed by ``x``.
        """
        return self._A.degree_on_basis(x)

    @cached_method
    def one_basis(self):
        r"""
        Return the basis index of the element `1` of
        `\operatorname{gr} A`.

        This assumes that the unity `1` of `A` belongs to `F_0`.
        """
        return self._A.one_basis()

    def product_on_basis(self, x, y):
        """
        Return the product on basis elements given by the
        indices ``x`` and ``y``.
        """
        ret = self._A.product_on_basis(x, y)
        deg = self._A.degree_on_basis(x) + self._A.degree_on_basis(y)
        return self.sum_of_terms([(i,c) for i,c in ret
                                     if self._A.degree_on_basis(i) == deg],
                                 distinct=True)
