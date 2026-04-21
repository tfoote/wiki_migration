## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/geometry.hpp>

// Angles
using ecl::Angle;
using ecl::wrap_angle;
using ecl::degrees_to_radians;
using ecl::radians_to_degrees;
// Other Objects
using ecl::CartesianPoint;
using ecl::PascalsTriangle;
// Functionals
using ecl::Minimum;
using ecl::Maximum;
// Functions
using ecl::Polynomial; 
using ecl::LinearFunction;
using ecl::CubicPolynomial;
using ecl::QuadraticPolynomial;
using ecl::TensionFunction;
// Splines
using ecl::SmoothLinearSpline;
using ecl::CubicSpline;
using ecl::TensionSpline;
// Transforms
using ecl::Pose2D;
```

If outside ros, you will also need to link to *ecl_geometry*.

## Tutorials

-   [Cartesian Points](ecl_geometry/Tutorials/Cartesian Points) - simple
    object representations for cartesian points.
-   [Angles](ecl_geometry/Tutorials/Angles) - convenience class for
    abstractly storing and representing angles.
-   [Polynomials](ecl_geometry/Tutorials/Polynomials) - working with
    polynomials of the n-th degree.
-   [Splines](ecl_geometry/Tutorials/Splines) - representations for
    smooth linear, cubic and tension splines.
-   [Pose](ecl_geometry/Tutorials/Pose) - 2D and 3D representations for
    poses (oft used in robotics).

## External Components

There are quite a few useful tools also in eigen's geometry module. You
can use these directly from eigen or via the
[ecl_linear_algebra](ecl_linear_algebra) package.

-   angle-axis pairs
-   quaternions
-   rotation matrices
-   transforms
