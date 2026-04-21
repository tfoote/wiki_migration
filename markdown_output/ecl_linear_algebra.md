## Prerequisites

Using ros eigen now, but you can also opt to use the internal
[ecl_eigen](ecl_eigen).

## Compiling & Linking

```cplusplus
// If you want to use the internal eigen
// #define ECL_EIGEN_IS_INTERNAL

// This brings in the whole eigen library
#include <ecl/linear_algebra.hpp>

// These calls bring in the individual modules
#include <ecl/linear_algebra/core.hpp>
#include <ecl/linear_algebra/cholesky.hpp>
#include <ecl/linear_algebra/dense.hpp>
#include <ecl/linear_algebra/eigenvalues.hpp>
#include <ecl/linear_algebra/geometry.hpp>
#include <ecl/linear_algebra/householder.hpp>
#include <ecl/linear_algebra/jacobi.hpp>
#include <ecl/linear_algebra/lu.hpp>
#include <ecl/linear_algebra/qr.hpp>
#include <ecl/linear_algebra/qtalignedmalloc.hpp>
#include <ecl/linear_algebra/sparse.hpp>
#include <ecl/linear_algebra/stddeque.hpp>
#include <ecl/linear_algebra/stdlist.hpp>
#include <ecl/linear_algebra/stdvector.hpp>
#include <ecl/linear_algebra/svd.hpp>

// There will also be some unsupported modules in ecl/linear_algebra/unsupported.
#include <ecl/linear_algebra/unsupported/nonlinear_optimization.hpp>
#include <ecl/linear_algebra/unsupported/numerical_diff.hpp>

using namespace ecl::linear_algebra
```

Note that the namespace is simply an alias to the Eigen namespace. You
can use either namespace, however the ecl namespace is preferred so its
clear we're using our extended interface (via the eigen plugins).

## Tutorials

-   [Using Eigen](ecl_linear_algebra/Tutorials/Using Eigen) - there are
    quite a few tricks you should be aware of when using eigen\...
-   [Eigen Extensions](ecl_linear_algebra/Tutorials/Eigen Extensions) -
    some extensions built in and around eigen by the ecl.
