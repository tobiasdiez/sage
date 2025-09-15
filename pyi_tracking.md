# Cython Type Stub (.pyi) Generation Tracking

This file tracks the progress of creating Python type stub files (.pyi) for all Cython files (.pyx) in the Sage repository.

## Overview
- **Total .pyx files**: 571
- **Existing .pyi files**: 56  
- **Missing .pyi files**: 527

## Progress by Module

### sage.rings (Priority 1) - 107 missing .pyi files

#### Basic Ring Classes
- [ ] ./src/sage/rings/ring.pyx
- [ ] ./src/sage/rings/rational.pyx
- [x] ./src/sage/rings/real_mpfr.pyx
- [ ] ./src/sage/rings/real_mpfi.pyx
- [ ] ./src/sage/rings/real_double.pyx
- [ ] ./src/sage/rings/real_double_element_gsl.pyx
- [ ] ./src/sage/rings/real_arb.pyx
- [ ] ./src/sage/rings/real_interval_absolute.pyx
- [ ] ./src/sage/rings/real_lazy.pyx
- [x] ./src/sage/rings/fast_arith.pyx (already exists)
- [x] ./src/sage/rings/factorint.pyx (already exists)
- [ ] ./src/sage/rings/factorint_flint.pyx
- [ ] ./src/sage/rings/laurent_series_ring_element.pyx
- [ ] ./src/sage/rings/power_series_ring_element.pyx
- [ ] ./src/sage/rings/power_series_mpoly.pyx
- [ ] ./src/sage/rings/power_series_pari.pyx
- [ ] ./src/sage/rings/power_series_poly.pyx
- [ ] ./src/sage/rings/puiseux_series_ring_element.pyx
- [ ] ./src/sage/rings/sum_of_squares.pyx
- [ ] ./src/sage/rings/noncommutative_ideals.pyx

#### Ring Extensions
- [ ] ./src/sage/rings/ring_extension.pyx
- [ ] ./src/sage/rings/ring_extension_conversion.pyx
- [ ] ./src/sage/rings/ring_extension_element.pyx
- [ ] ./src/sage/rings/ring_extension_morphism.pyx

#### Finite Rings
- [ ] ./src/sage/rings/finite_rings/element_base.pyx
- [ ] ./src/sage/rings/finite_rings/element_givaro.pyx
- [ ] ./src/sage/rings/finite_rings/element_ntl_gf2e.pyx
- [ ] ./src/sage/rings/finite_rings/element_pari_ffelt.pyx
- [ ] ./src/sage/rings/finite_rings/finite_field_base.pyx
- [ ] ./src/sage/rings/finite_rings/hom_finite_field.pyx
- [ ] ./src/sage/rings/finite_rings/hom_finite_field_givaro.pyx
- [ ] ./src/sage/rings/finite_rings/hom_prime_finite_field.pyx
- [x] ./src/sage/rings/finite_rings/integer_mod.pyx
- [ ] ./src/sage/rings/finite_rings/residue_field.pyx
- [ ] ./src/sage/rings/finite_rings/residue_field_givaro.pyx
- [ ] ./src/sage/rings/finite_rings/residue_field_ntl_gf2e.pyx
- [ ] ./src/sage/rings/finite_rings/residue_field_pari_ffelt.pyx

#### Number Fields
- [ ] ./src/sage/rings/number_field/number_field_element.pyx
- [ ] ./src/sage/rings/number_field/number_field_element_base.pyx
- [ ] ./src/sage/rings/number_field/number_field_element_quadratic.pyx
- [ ] ./src/sage/rings/number_field/number_field_morphisms.pyx
- [ ] ./src/sage/rings/number_field/totallyreal.pyx
- [ ] ./src/sage/rings/number_field/totallyreal_data.pyx

#### p-adic Numbers
- [ ] ./src/sage/rings/padics/common_conversion.pyx
- [ ] ./src/sage/rings/padics/local_generic_element.pyx
- [ ] ./src/sage/rings/padics/morphism.pyx
- [ ] ./src/sage/rings/padics/padic_ZZ_pX_CA_element.pyx
- [ ] ./src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx
- [ ] ./src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx
- [ ] ./src/sage/rings/padics/padic_ZZ_pX_element.pyx
- [ ] ./src/sage/rings/padics/padic_capped_absolute_element.pyx
- [ ] ./src/sage/rings/padics/padic_capped_relative_element.pyx
- [ ] ./src/sage/rings/padics/padic_ext_element.pyx
- [ ] ./src/sage/rings/padics/padic_fixed_mod_element.pyx
- [ ] ./src/sage/rings/padics/padic_floating_point_element.pyx
- [ ] ./src/sage/rings/padics/padic_generic_element.pyx
- [ ] ./src/sage/rings/padics/padic_printing.pyx
- [ ] ./src/sage/rings/padics/padic_relaxed_element.pyx
- [ ] ./src/sage/rings/padics/padic_relaxed_errors.pyx
- [ ] ./src/sage/rings/padics/pow_computer.pyx
- [ ] ./src/sage/rings/padics/pow_computer_ext.pyx
- [ ] ./src/sage/rings/padics/pow_computer_flint.pyx
- [ ] ./src/sage/rings/padics/pow_computer_relative.pyx
- [ ] ./src/sage/rings/padics/qadic_flint_CA.pyx
- [ ] ./src/sage/rings/padics/qadic_flint_CR.pyx
- [ ] ./src/sage/rings/padics/qadic_flint_FM.pyx
- [ ] ./src/sage/rings/padics/qadic_flint_FP.pyx
- [ ] ./src/sage/rings/padics/relative_ramified_CA.pyx
- [ ] ./src/sage/rings/padics/relative_ramified_CR.pyx
- [ ] ./src/sage/rings/padics/relative_ramified_FM.pyx
- [ ] ./src/sage/rings/padics/relative_ramified_FP.pyx

#### Polynomials
- [ ] ./src/sage/rings/polynomial/commutative_polynomial.pyx
- [ ] ./src/sage/rings/polynomial/cyclotomic.pyx
- [ ] ./src/sage/rings/polynomial/evaluation_flint.pyx
- [ ] ./src/sage/rings/polynomial/evaluation_ntl.pyx
- [ ] ./src/sage/rings/polynomial/hilbert.pyx
- [ ] ./src/sage/rings/polynomial/laurent_polynomial.pyx
- [ ] ./src/sage/rings/polynomial/laurent_polynomial_mpair.pyx
- [ ] ./src/sage/rings/polynomial/multi_polynomial.pyx
- [ ] ./src/sage/rings/polynomial/multi_polynomial_ideal_libsingular.pyx
- [ ] ./src/sage/rings/polynomial/multi_polynomial_libsingular.pyx
- [ ] ./src/sage/rings/polynomial/multi_polynomial_ring_base.pyx
- [ ] ./src/sage/rings/polynomial/ore_polynomial_element.pyx
- [ ] ./src/sage/rings/polynomial/pbori/pbori.pyx
- [ ] ./src/sage/rings/polynomial/plural.pyx
- [ ] ./src/sage/rings/polynomial/polydict.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_compiled.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_complex_arb.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_element.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_gf2x.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_integer_dense_flint.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_number_field.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_rational_flint.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_ring_homomorphism.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_zmod_flint.pyx
- [ ] ./src/sage/rings/polynomial/polynomial_zz_pex.pyx
- [ ] ./src/sage/rings/polynomial/real_roots.pyx
- [ ] ./src/sage/rings/polynomial/refine_root.pyx
- [ ] ./src/sage/rings/polynomial/skew_polynomial_element.pyx
- [ ] ./src/sage/rings/polynomial/skew_polynomial_finite_field.pyx
- [ ] ./src/sage/rings/polynomial/skew_polynomial_finite_order.pyx
- [ ] ./src/sage/rings/polynomial/symmetric_reduction.pyx
- [ ] ./src/sage/rings/polynomial/weil/weil_polynomials.pyx

#### Other Rings
- [ ] ./src/sage/rings/convert/mpfi.pyx
- [ ] ./src/sage/rings/function_field/khuri_makdisi.pyx
- [ ] ./src/sage/rings/semirings/tropical_semiring.pyx
- [ ] ./src/sage/rings/tate_algebra_element.pyx
- [ ] ./src/sage/rings/tate_algebra_ideal.pyx

### Other Sage Modules (Remaining 420 files)

#### Algebras
- [ ] ./src/sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra_element.pyx
- [ ] ./src/sage/algebras/fusion_rings/fast_parallel_fmats_methods.pyx
- [ ] ./src/sage/algebras/fusion_rings/fast_parallel_fusion_ring_braid_repn.pyx
- [ ] ./src/sage/algebras/fusion_rings/poly_tup_engine.pyx
- [ ] ./src/sage/algebras/fusion_rings/shm_managers.pyx
- [ ] ./src/sage/algebras/letterplace/free_algebra_element_letterplace.pyx
- [ ] ./src/sage/algebras/letterplace/free_algebra_letterplace.pyx
- [ ] ./src/sage/algebras/letterplace/letterplace_ideal.pyx
- [ ] ./src/sage/algebras/lie_algebras/lie_algebra_element.pyx
- [ ] ./src/sage/algebras/octonion_algebra.pyx
- [ ] ./src/sage/algebras/quatalg/quaternion_algebra_element.pyx
- [ ] ./src/sage/algebras/spinor_gens.pyx
- [ ] ./src/sage/algebras/steenrod/steenrod_algebra_mult.pyx

#### Categories  
- [ ] ./src/sage/categories/action.pyx
- [ ] ./src/sage/categories/algebra_functor.pyx
- [ ] ./src/sage/categories/cartesian_product.pyx
- [ ] ./src/sage/categories/category.pyx
- [ ] ./src/sage/categories/covariant_functorial_construction.pyx
- [ ] ./src/sage/categories/functor.pyx
- [ ] ./src/sage/categories/homset.pyx
- [ ] ./src/sage/categories/map.pyx
- [ ] ./src/sage/categories/morphism.pyx
- [ ] ./src/sage/categories/pushout.pyx

#### Coding Theory
- [ ] ./src/sage/coding/ag_code.pyx
- [ ] ./src/sage/coding/ag_code_decoders.pyx
- [ ] ./src/sage/coding/binary_code.pyx
- [ ] ./src/sage/coding/bounds.pyx
- [ ] ./src/sage/coding/codecan/autgroup_can_label.pyx
- [ ] ./src/sage/coding/codecan/codecan.pyx
- [ ] ./src/sage/coding/guruswami_sudan/gs_decoder.pyx
- [ ] ./src/sage/coding/guruswami_sudan/interpolation.pyx
- [ ] ./src/sage/coding/guruswami_sudan/utils.pyx

#### Combinatorics
- [ ] ./src/sage/combinat/cluster_algebra_quiver/path_string.pyx
- [ ] ./src/sage/combinat/cluster_algebra_quiver/quiver.pyx
- [ ] ./src/sage/combinat/combinat_cython.pyx
- [ ] ./src/sage/combinat/crystals/fast_crystals.pyx
- [ ] ./src/sage/combinat/designs/ext_rep.pyx
- [ ] ./src/sage/combinat/designs/incidence_structures.pyx
- [ ] ./src/sage/combinat/free_module.pyx
- [ ] ./src/sage/combinat/integer_lists/base.pyx
- [ ] ./src/sage/combinat/integer_lists/invlex.pyx
- [ ] ./src/sage/combinat/integer_vectors.pyx
- [ ] ./src/sage/combinat/matrices/dancing_links.pyx
- [ ] ./src/sage/combinat/matrices/dlxcpp.pyx
- [ ] ./src/sage/combinat/partitions.pyx
- [ ] ./src/sage/combinat/q_analogues.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_abstract_class.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_infinity.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_type_A.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_type_A2_dual.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_type_A2_even.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_type_A2_odd.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_type_B.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_type_C.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_type_D.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_type_D_tri.pyx
- [ ] ./src/sage/combinat/rigged_configurations/bij_type_D_twisted.pyx
- [ ] ./src/sage/combinat/rigged_configurations/rigged_configuration_element.pyx
- [ ] ./src/sage/combinat/rigged_configurations/rigged_configurations.pyx
- [ ] ./src/sage/combinat/rigged_configurations/rigged_partition.pyx
- [ ] ./src/sage/combinat/rigged_configurations/tensor_product_kr_tableaux.pyx
- [ ] ./src/sage/combinat/rigged_configurations/tensor_product_kr_tableaux_element.pyx
- [ ] ./src/sage/combinat/symmetric_group_algebra.pyx
- [ ] ./src/sage/combinat/symmetric_group_representations.pyx
- [ ] ./src/sage/combinat/tableau.pyx
- [ ] ./src/sage/combinat/words/finite_word.pyx

#### Crypto
- [ ] ./src/sage/crypto/block_cipher/des.pyx
- [ ] ./src/sage/crypto/block_cipher/present.pyx
- [ ] ./src/sage/crypto/block_cipher/sdes.pyx
- [ ] ./src/sage/crypto/lwe.pyx
- [ ] ./src/sage/crypto/mq/mpolynomialsystem.pyx
- [ ] ./src/sage/crypto/sbox.pyx
- [ ] ./src/sage/crypto/stream_cipher.pyx

#### Data Structures
- [ ] ./src/sage/data_structures/bitset.pyx
- [ ] ./src/sage/data_structures/stream.pyx

#### Dynamics
- [ ] ./src/sage/dynamics/arithmetic_dynamics/projective_ds_helper.pyx
- [ ] ./src/sage/dynamics/complex_dynamics/mandel_julia_helper.pyx

#### Geometry
- [ ] ./src/sage/geometry/cone.pyx
- [ ] ./src/sage/geometry/fan.pyx
- [ ] ./src/sage/geometry/fan_morphism.pyx
- [ ] ./src/sage/geometry/integral_points.pyx
- [ ] ./src/sage/geometry/lattice_polytope.pyx
- [ ] ./src/sage/geometry/linear_expression.pyx
- [ ] ./src/sage/geometry/point_collection.pyx
- [ ] ./src/sage/geometry/polyhedron/base.pyx
- [ ] ./src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx
- [ ] ./src/sage/geometry/polyhedron/combinatorial_polyhedron/combinatorial_face.pyx
- [ ] ./src/sage/geometry/polyhedron/combinatorial_polyhedron/conversions.pyx
- [ ] ./src/sage/geometry/polyhedron/combinatorial_polyhedron/face_data_structure.pyx
- [ ] ./src/sage/geometry/polyhedron/combinatorial_polyhedron/face_iterator.pyx
- [ ] ./src/sage/geometry/polyhedron/combinatorial_polyhedron/list_of_faces.pyx
- [ ] ./src/sage/geometry/polyhedron/combinatorial_polyhedron/polyhedron_face_lattice.pyx
- [ ] ./src/sage/geometry/polyhedron/face.pyx
- [ ] ./src/sage/geometry/polyhedron/ppl_lattice_polytope.pyx
- [ ] ./src/sage/geometry/polyhedron/representation.pyx
- [ ] ./src/sage/geometry/toric_lattice.pyx
- [ ] ./src/sage/geometry/toric_lattice_element.pyx
- [ ] ./src/sage/geometry/triangulation/base.pyx
- [ ] ./src/sage/geometry/triangulation/element.pyx

#### Graphs
- [ ] ./src/sage/graphs/base/boost_graph.pyx
- [ ] ./src/sage/graphs/base/c_graph.pyx
- [ ] ./src/sage/graphs/base/dense_graph.pyx
- [ ] ./src/sage/graphs/base/sparse_graph.pyx
- [ ] ./src/sage/graphs/base/static_dense_graph.pyx
- [ ] ./src/sage/graphs/base/static_sparse_graph.pyx
- [ ] ./src/sage/graphs/chrompoly.pyx
- [ ] ./src/sage/graphs/connectivity.pyx
- [ ] ./src/sage/graphs/convexity_properties.pyx
- [ ] ./src/sage/graphs/distances_all_pairs.pyx
- [ ] ./src/sage/graphs/domination.pyx
- [ ] ./src/sage/graphs/generic_graph_pyx.pyx
- [ ] ./src/sage/graphs/graph_coloring.pyx
- [ ] ./src/sage/graphs/graph_decompositions/bandwidth.pyx
- [ ] ./src/sage/graphs/graph_decompositions/cutwidth.pyx
- [ ] ./src/sage/graphs/graph_decompositions/fast_digraph.pyx
- [ ] ./src/sage/graphs/graph_decompositions/graph_products.pyx
- [ ] ./src/sage/graphs/graph_decompositions/modular_decomposition.pyx
- [ ] ./src/sage/graphs/graph_decompositions/rankwidth.pyx
- [ ] ./src/sage/graphs/graph_decompositions/tree_decomposition.pyx
- [ ] ./src/sage/graphs/graph_decompositions/vertex_separation.pyx
- [ ] ./src/sage/graphs/graph_generators.pyx
- [ ] ./src/sage/graphs/hyperbolicity.pyx
- [ ] ./src/sage/graphs/independent_sets.pyx
- [ ] ./src/sage/graphs/lineargraph.pyx
- [ ] ./src/sage/graphs/matchpoly.pyx
- [ ] ./src/sage/graphs/path_enumeration.pyx
- [ ] ./src/sage/graphs/planarity.pyx
- [ ] ./src/sage/graphs/schnyder.pyx
- [ ] ./src/sage/graphs/spanning_tree.pyx
- [ ] ./src/sage/graphs/trees.pyx
- [ ] ./src/sage/graphs/tutte_polynomial.pyx
- [ ] ./src/sage/graphs/weakly_chordal.pyx

#### Groups
- [ ] ./src/sage/groups/matrix_gps/group_element.pyx
- [ ] ./src/sage/groups/matrix_gps/group_element_gap.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref/automorphism_group_canonical_label.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref/canonical_augmentation.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref/double_coset.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref/refinement_lists.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref/refinement_python.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref/refinement_sets.pyx
- [ ] ./src/sage/groups/perm_gps/partn_ref2/refinement_generic.pyx
- [ ] ./src/sage/groups/perm_gps/permgroup_element.pyx

#### Knots
- [ ] ./src/sage/knots/pd_code.pyx

#### Libs
- [ ] ./src/sage/libs/coxeter3/coxeter.pyx
- [ ] ./src/sage/libs/ecl.pyx
- [ ] ./src/sage/libs/flint/arith.pyx
- [ ] ./src/sage/libs/flint/fmpq_poly.pyx
- [ ] ./src/sage/libs/flint/fmpz_poly.pyx
- [ ] ./src/sage/libs/flint/fmpz_vec.pyx
- [ ] ./src/sage/libs/gap/element.pyx
- [ ] ./src/sage/libs/gap/libgap.pyx
- [ ] ./src/sage/libs/gap/util.pyx
- [ ] ./src/sage/libs/giac/giac.pyx
- [ ] ./src/sage/libs/linbox/conversion.pyx
- [ ] ./src/sage/libs/linbox/fflas.pyx
- [ ] ./src/sage/libs/linbox/linbox.pyx
- [ ] ./src/sage/libs/m4ri.pyx
- [ ] ./src/sage/libs/m4rie.pyx
- [ ] ./src/sage/libs/mpmath/utils.pyx
- [ ] ./src/sage/libs/ntl/convert.pyx
- [ ] ./src/sage/libs/ntl/error.pyx
- [ ] ./src/sage/libs/ntl/ntl_GF2.pyx
- [ ] ./src/sage/libs/ntl/ntl_GF2E.pyx
- [ ] ./src/sage/libs/ntl/ntl_GF2EContext.pyx
- [ ] ./src/sage/libs/ntl/ntl_GF2EX.pyx
- [ ] ./src/sage/libs/ntl/ntl_GF2X.pyx
- [ ] ./src/sage/libs/ntl/ntl_lzz_p.pyx
- [ ] ./src/sage/libs/ntl/ntl_lzz_pContext.pyx
- [ ] ./src/sage/libs/ntl/ntl_lzz_pE.pyx
- [ ] ./src/sage/libs/ntl/ntl_lzz_pEContext.pyx
- [ ] ./src/sage/libs/ntl/ntl_lzz_pEX.pyx
- [ ] ./src/sage/libs/ntl/ntl_lzz_pX.pyx
- [ ] ./src/sage/libs/ntl/ntl_mat_GF2.pyx
- [ ] ./src/sage/libs/ntl/ntl_mat_GF2E.pyx
- [ ] ./src/sage/libs/ntl/ntl_mat_ZZ.pyx
- [ ] ./src/sage/libs/ntl/ntl_ZZ.pyx
- [ ] ./src/sage/libs/ntl/ntl_ZZX.pyx
- [ ] ./src/sage/libs/ntl/ntl_ZZ_p.pyx
- [ ] ./src/sage/libs/ntl/ntl_ZZ_pContext.pyx
- [ ] ./src/sage/libs/ntl/ntl_ZZ_pE.pyx
- [ ] ./src/sage/libs/ntl/ntl_ZZ_pEContext.pyx
- [ ] ./src/sage/libs/ntl/ntl_ZZ_pEX.pyx
- [ ] ./src/sage/libs/ntl/ntl_ZZ_pX.pyx
- [ ] ./src/sage/libs/ntl/vec_GF2.pyx
- [ ] ./src/sage/libs/ntl/vec_GF2E.pyx
- [ ] ./src/sage/libs/ntl/vec_ZZ_p.pyx
- [ ] ./src/sage/libs/ntl/vec_lzz_p.pyx
- [ ] ./src/sage/libs/pari/convert_flint.pyx
- [ ] ./src/sage/libs/pari/convert_gmp.pyx
- [ ] ./src/sage/libs/pari/convert_sage.pyx
- [ ] ./src/sage/libs/pari/convert_sage_complex_double.pyx
- [ ] ./src/sage/libs/pari/convert_sage_int.pyx
- [ ] ./src/sage/libs/pari/convert_sage_matrix.pyx
- [ ] ./src/sage/libs/pari/convert_sage_real_double.pyx
- [ ] ./src/sage/libs/pari/convert_sage_real_mpfr.pyx
- [ ] ./src/sage/libs/singular/decl.pyx
- [ ] ./src/sage/libs/singular/function.pyx
- [ ] ./src/sage/libs/singular/groebner_strategy.pyx
- [ ] ./src/sage/libs/singular/option.pyx
- [ ] ./src/sage/libs/singular/polynomial.pyx
- [ ] ./src/sage/libs/singular/ring.pyx
- [ ] ./src/sage/libs/singular/singular.pyx

#### Matrix
- [ ] ./src/sage/matrix/action.pyx
- [ ] ./src/sage/matrix/berlekamp_massey.pyx
- [ ] ./src/sage/matrix/change_ring.pyx
- [ ] ./src/sage/matrix/constructor.pyx
- [ ] ./src/sage/matrix/matrix.pyx
- [ ] ./src/sage/matrix/matrix0.pyx
- [ ] ./src/sage/matrix/matrix1.pyx
- [ ] ./src/sage/matrix/matrix2.pyx
- [ ] ./src/sage/matrix/matrix_complex_ball_dense.pyx
- [ ] ./src/sage/matrix/matrix_complex_double_dense.pyx
- [ ] ./src/sage/matrix/matrix_cyclo_dense.pyx
- [ ] ./src/sage/matrix/matrix_dense.pyx
- [ ] ./src/sage/matrix/matrix_double_dense.pyx
- [ ] ./src/sage/matrix/matrix_gap.pyx
- [ ] ./src/sage/matrix/matrix_gf2e_dense.pyx
- [ ] ./src/sage/matrix/matrix_gfpn_dense.pyx
- [ ] ./src/sage/matrix/matrix_integer_dense.pyx
- [ ] ./src/sage/matrix/matrix_integer_sparse.pyx
- [ ] ./src/sage/matrix/matrix_mod2_dense.pyx
- [ ] ./src/sage/matrix/matrix_modn_dense_double.pyx
- [ ] ./src/sage/matrix/matrix_modn_dense_float.pyx
- [ ] ./src/sage/matrix/matrix_modn_sparse.pyx
- [ ] ./src/sage/matrix/matrix_rational_dense.pyx
- [ ] ./src/sage/matrix/matrix_rational_sparse.pyx
- [ ] ./src/sage/matrix/matrix_real_double_dense.pyx
- [ ] ./src/sage/matrix/matrix_sparse.pyx
- [ ] ./src/sage/matrix/misc.pyx
- [ ] ./src/sage/matrix/strassen.pyx

#### Matroids
- [ ] ./src/sage/matroids/basis_exchange_matroid.pyx
- [ ] ./src/sage/matroids/circuits_matroid.pyx
- [ ] ./src/sage/matroids/graphic_matroid.pyx
- [ ] ./src/sage/matroids/lean_matrix.pyx
- [ ] ./src/sage/matroids/linear_matroid.pyx
- [ ] ./src/sage/matroids/set_system.pyx
- [ ] ./src/sage/matroids/unpickling.pyx

#### Misc
- [ ] ./src/sage/misc/bitset.pyx
- [ ] ./src/sage/misc/edit_module.pyx
- [ ] ./src/sage/misc/fast_methods.pyx
- [ ] ./src/sage/misc/fpickle.pyx
- [ ] ./src/sage/misc/function_mangling.pyx
- [ ] ./src/sage/misc/inherit_comparison.pyx
- [ ] ./src/sage/misc/persist.pyx
- [ ] ./src/sage/misc/prandom.pyx
- [ ] ./src/sage/misc/sageinspect.pyx
- [ ] ./src/sage/misc/search.pyx

#### Modular
- [ ] ./src/sage/modular/abvar/finite_subgroup.pyx
- [ ] ./src/sage/modular/arithgroup/arithgroup_element.pyx
- [ ] ./src/sage/modular/arithgroup/farey_symbol.pyx
- [ ] ./src/sage/modular/hecke/ambient_module.pyx
- [ ] ./src/sage/modular/hecke/hecke_operator.pyx
- [ ] ./src/sage/modular/hecke/module.pyx
- [ ] ./src/sage/modular/hecke/submodule.pyx
- [ ] ./src/sage/modular/modsym/ambient.pyx
- [ ] ./src/sage/modular/modsym/boundary.pyx
- [ ] ./src/sage/modular/modsym/element.pyx
- [ ] ./src/sage/modular/modsym/heilbronn.pyx
- [ ] ./src/sage/modular/modsym/hecke_operator.pyx
- [ ] ./src/sage/modular/modsym/manin_symbol.pyx
- [ ] ./src/sage/modular/modsym/manin_symbols.pyx
- [ ] ./src/sage/modular/modsym/p1list.pyx
- [ ] ./src/sage/modular/modsym/relation_matrix.pyx
- [ ] ./src/sage/modular/modsym/subspace.pyx
- [ ] ./src/sage/modular/overconvergent/hecke_series.pyx
- [ ] ./src/sage/modular/pollack_stevens/dist.pyx
- [ ] ./src/sage/modular/pollack_stevens/distributions.pyx
- [ ] ./src/sage/modular/pollack_stevens/fund_domain_element.pyx
- [ ] ./src/sage/modular/pollack_stevens/manin_map.pyx
- [ ] ./src/sage/modular/pollack_stevens/sigma0.pyx
- [ ] ./src/sage/modular/quasimodform/element.pyx
- [ ] ./src/sage/modular/quasimodform/ring.pyx

#### Modules
- [ ] ./src/sage/modules/diagonal_matrix.pyx
- [ ] ./src/sage/modules/fg_pid/fgp_element.pyx
- [ ] ./src/sage/modules/fg_pid/fgp_module.pyx
- [ ] ./src/sage/modules/finite_submodule_iter.pyx
- [ ] ./src/sage/modules/free_module_element.pyx
- [ ] ./src/sage/modules/free_module_homspace.pyx
- [ ] ./src/sage/modules/free_module_morphism.pyx
- [ ] ./src/sage/modules/matrix_morphism.pyx
- [ ] ./src/sage/modules/module.pyx
- [ ] ./src/sage/modules/quotient_module.pyx
- [ ] ./src/sage/modules/submodule.pyx
- [ ] ./src/sage/modules/torsion_quadratic_module.pyx
- [ ] ./src/sage/modules/vector_complex_double_dense.pyx
- [ ] ./src/sage/modules/vector_double_dense.pyx
- [ ] ./src/sage/modules/vector_integer_dense.pyx
- [ ] ./src/sage/modules/vector_mod2_dense.pyx
- [ ] ./src/sage/modules/vector_modn_dense.pyx
- [ ] ./src/sage/modules/vector_rational_dense.pyx
- [ ] ./src/sage/modules/vector_real_double_dense.pyx
- [ ] ./src/sage/modules/vector_space_homspace.pyx
- [ ] ./src/sage/modules/vector_space_morphism.pyx
- [ ] ./src/sage/modules/with_basis/cell_module.pyx
- [ ] ./src/sage/modules/with_basis/representation.pyx

#### Number Theory
- [ ] ./src/sage/quadratic_forms/binary_qf.pyx
- [ ] ./src/sage/quadratic_forms/count_local_2.pyx
- [ ] ./src/sage/quadratic_forms/extras.pyx
- [ ] ./src/sage/quadratic_forms/genera/genus.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__automorphisms.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__equivalence_testing.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__evaluate.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__local_density_congruence.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__local_field_invariants.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__local_normal_form.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__local_representation_conditions.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__mass.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__mass__Siegel_densities.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__neighbors.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__reduction_theory.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__represent.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__split_local_covering.pyx
- [ ] ./src/sage/quadratic_forms/quadratic_form__theta.pyx
- [ ] ./src/sage/quadratic_forms/ternary.pyx
- [ ] ./src/sage/quadratic_forms/ternary_qf.pyx

#### Schemes
- [ ] ./src/sage/schemes/elliptic_curves/descent_two_isogeny.pyx
- [ ] ./src/sage/schemes/elliptic_curves/mod_sym_num.pyx
- [ ] ./src/sage/schemes/elliptic_curves/period_lattice_region.pyx
- [ ] ./src/sage/schemes/hyperelliptic_curves/hypellfrob.pyx
- [ ] ./src/sage/schemes/toric/divisor_class.pyx

#### Sets
- [ ] ./src/sage/sets/disjoint_union_enumerated_sets.pyx
- [ ] ./src/sage/sets/finite_set_map_cy.pyx
- [ ] ./src/sage/sets/pythonclass.pyx

#### Stats
- [ ] ./src/sage/stats/distributions/discrete_gaussian_integer.pyx
- [ ] ./src/sage/stats/distributions/discrete_gaussian_lattice.pyx
- [ ] ./src/sage/stats/hmm/chmm.pyx
- [ ] ./src/sage/stats/hmm/util.pyx

#### Structure
- [ ] ./src/sage/structure/category_object.pyx
- [ ] ./src/sage/structure/coerce.pyx
- [ ] ./src/sage/structure/coerce_dict.pyx
- [ ] ./src/sage/structure/element.pyx
- [ ] ./src/sage/structure/factory.pyx
- [ ] ./src/sage/structure/list_clone.pyx
- [ ] ./src/sage/structure/parent.pyx
- [ ] ./src/sage/structure/proof.pyx
- [ ] ./src/sage/structure/richcmp.pyx
- [ ] ./src/sage/structure/sage_object.pyx

#### Symbolic
- [ ] ./src/sage/symbolic/ginac/ex.pyx
- [ ] ./src/sage/symbolic/ginac/function.pyx
- [ ] ./src/sage/symbolic/ginac/numeric.pyx
- [ ] ./src/sage/symbolic/ginac/py_funcs.pyx
- [ ] ./src/sage/symbolic/ginac/registrar.pyx
- [ ] ./src/sage/symbolic/ginac/relational.pyx
- [ ] ./src/sage/symbolic/ginac/symbol.pyx

## Typing Conventions and Patterns

### Import Statements
Standard typing imports used across .pyi files:
```python
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
```

### Common Type Aliases
- `Element` for ring/field elements  
- `Parent` for algebraic structures
- `Integer` for Sage integers
- `RealNumber` for real number types

### Function Signatures
- Use `Any` for complex Sage objects without specific typing
- Use `...` as function body for all stub functions
- Include `self` parameter for methods
- Use Union types for multiple possible return types

### Class Definitions
- Include all public methods and properties
- Use inheritance when clear from .pyx file
- Add `__init__` methods with appropriate parameters
- Include special methods (`__call__`, `__repr__`, etc.)