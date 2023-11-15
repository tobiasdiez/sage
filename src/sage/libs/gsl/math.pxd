# distutils: libraries = GSL_LIBRARIES
# distutils: library_dirs = GSL_LIBDIR
# distutils: include_dirs = GSL_INCDIR
from sage.libs.gsl.types cimport *

cdef extern from "gsl/gsl_math.h":
    bint gsl_isnan(double x)
    bint gsl_isinf(double x)
    bint gsl_finite(double x)
    double gsl_log1p(double x)
    double gsl_expm1(double x)
    double gsl_hypot(double x, double y)
    double gsl_acosh(double x)
    double gsl_asinh(double x)
    double gsl_atanh(double x)
    double gsl_ldexp(double x, int e)
    double gsl_frexp(double x, int * e)
    double gsl_pow_int(double x, int n)
    double gsl_pow_2(double x)
    double gsl_pow_3(double x)
    double gsl_pow_4(double x)
    double gsl_pow_5(double x)
    double gsl_pow_6(double x)
    double gsl_pow_7(double x)
    double gsl_pow_8(double x)
    double gsl_pow_9(double x)
    int GSL_SIGN(double x)
    bint GSL_IS_ODD(int n)
    bint GSL_IS_EVEN(int n)
    double GSL_MAX(double a, double b)
    double GSL_MIN(double a, double b)
    double GSL_MAX_DBL(double a, double b)
    double GSL_MIN_DBL(double a, double b)
    int GSL_MAX_INT(int a, int b)
    int GSL_MIN_INT(int a, int b)
    long double GSL_MAX_LDBL(long double a, long double b)
    long double GSL_MIN_LDBL(long double a, long double b)
    int gsl_fcmp(double x, double y, double epsilon)
    double GSL_FN_EVAL(gsl_function * F, double x)
    double GSL_FN_FDF_EVAL_F(gsl_function_fdf * FDF, double x)
    GSL_FN_FDF_EVAL_DF(gsl_function_fdf * FDF, double x)
    GSL_FN_FDF_EVAL_F_DF(gsl_function_fdf * FDF, double x, double y, double dy)
