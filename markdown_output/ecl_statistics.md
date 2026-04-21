## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/statistics.hpp>

// Statistics Classes
using ecl::CovarianceEllipsoid;
using ecl::CovarianceEllipsoid2f; // also 2d, 3f, 3d typedef variants
```

If outside of ros, you will also need to link to *ecl_statistics*.

## Tutorials

Currently we\'ve only implemented simple, fast algorithms for 2x2, 3x3
covariance matrices.

-   [Covariance Ellipsoids](ecl_statistics/Tutorials/Covariance Ellipsoids) -
    covariances ellipsoids, typically used in slam.
