## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/math.hpp>

// constants
using ecl::pi; // also pi_2, pi_4

// simple functions
using ecl::EuclideanNorm;
using ecl::isApprox;
using ecl::isApproxOrLessThan;
using ecl::sign; // also psign
using ecl::cube_root; // only for real numbers/solutions
```



## Tutorial

-   [Simple Math](ecl_math/Tutorials/Simple Math) - simple math
    constants and functions.
