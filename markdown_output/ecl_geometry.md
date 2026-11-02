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

- [Cartesian Points](#cartesian-points) -
  simple object representations for cartesian points.
- [Angles](#angles) - convenience
  class for abstractly storing and representing angles.
- [Polynomials](#polynomials) -
  working with polynomials of the n-th degree.
- [Splines](#splines) -
  representations for smooth linear, cubic and tension splines.
- [Pose](#pose) - 2D and 3D
  representations for poses (oft used in robotics).

## External Components

There are quite a few useful tools also in eigen's geometry module. You
can use these directly from eigen or via the
[ecl_linear_algebra](https://index.ros.org/p/ecl_linear_algebra)
package.

- angle-axis pairs
- quaternions
- rotation matrices
- transforms

## Cartesian Points

- **Description:** Simple object representations for cartesian points.
- **Keywords:** ecl points
- **Tutorial Level:** BEGINNER

### Cartesian Point

This is a simple templatised abstraction of a cartesian/euclidean point.
The template arguments are used to define the dimension and the storage
type (`float` or `double` for the point.



```cplusplus

#include <ecl/geometry/cartesian_point.hpp>

using ecl::CartesianPoint;   // the template class
using ecl::CartesianPoint3d; // a typedef

CartesianPoint<3,double> p1; // template instantiation
CarteisanPoint3d p2;         // same thing
```



### Setters



```cplusplus
// Point by point - 2d/3d specialisations only
CartesianPoint3d p1(0.1,0.2,0.3);
// From eigen vector
eigen::Vector3d v; v << 0.1, 0.2, 0.3;
CartesianPoint3d p2(v);
// Comma Initialisation
CartesianPoint3d p3;
p3 << 1.0, 2.0, 3.0;
// From api - 2d/3d specialisations only
CartesianPoint3d p4;
p4.x(1.0); p4.y(2.0); p4.z(3.0);
```



### Accessors



```cplusplus
CartesianPoint3d p;
p << 1.0, 2.0, 3.0;
// From api - 2d/3d specialisations only
double x(p.x()), y(p.y()), z(p.z());
// From vector
eigen::Vector3d v = p.positionVector();
// From operator []
double x(p[0]), y(p[1]), z(p[2]);
```



### Error Handling

The class will throw exceptions in debug mode if ranges are exceeded at
any time (comma initisalisations, `operator \[\]`).

## Angles

- **Description:** Convenience class for abstractly storing and
  representing angles.
- **Keywords:** ecl angles
- **Tutorial Level:** BEGINNER

### Overview

The angle class is a convenience class that automates storage and angle
wrapping for you. It stores the angle in radians (which any good
engineer/mathematician should default to!). Take this into consideration
if using it where speed is of the essence. That is, don't use Angle and
then do *all* your calculations in degrees - there will be alot of
copying and converting.

### Basic Usage

Note that you can templatise the storage as either `float` or
`double`. Using float is sometimes important for low end embedded
boards which have to do *alot* of angle calculations.



```cplusplus
#include <ecl/geometry/angle.hpp>

using ecl::Angle;
using ecl::wrap_angle;

// ...

Angle<double> a(3.33); // automatically wraps on -pi:pi
double degrees = a.degrees();
Angle<double> b = a + 3.24; // again, will automatically wrap the answer.
// RotationMatrix is currently a typedef for a 2d eigen matrix
Angle<double>::RotationMatrix matrix = a.rotationMatrix();
```



### Functions

For those who just wish to use functions rather than objects:



```cplusplus
// wrapping
double angle = wrap_angle(3.33);

// conversions
double rads = radians_to_degrees(1.44);
double degrees = degrees_to_radians(rads);
```

## Polynomials

- **Description:** Working with polynomials of the n-th degree.
- **Keywords:** ecl polynomials
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Splines](#splines)

### The Polynomial Class

Polynomials are a template class where the template argument represents
the degree of the polynomial. The class stores only the co-efficients
for the polynomial and calculates the function and its derivatives on
the fly from these co-efficients. Coefficient storage is based on the
array class in ecl_containers, so comma initialisation can be used to
configure the polynomial appropriately.

The following instantiates an uninitialised polynomial. Use comma
initialisation or blueprints to initialise.



```cplusplus
Polynomial<5> p;
```



### Typedefs

Rather than specifying the degree of the polynomial with a template
argument, a few more convenient typedefs are available:



```cplusplus
typedef Polynomial<1> LinearFunction;
typedef Polynomial<2> QuadraticPolynomial;
typedef Polynomial<3> CubicPolynomial;
typedef Polynomial<5> QuinticPolynomial;
```



### Initialisation

#### Comma Initialisation



```cplusplus
Polynomial<5> p; 
// Comma Initialisation
p.coefficients() = 1,2,3,4,5,6;
cout << p << endl; // 1.00 + 2.00x + 3.00x^2 + 4.00x^3 + 5.00x^4 + 6.00x^5
```



#### BluePrints

There are also some blueprints (quick construction and assignment) for
generating polynomials that interpolate between two end points. These
can be accessed via static methods that are inherited by the
polynomial's class. For example:



```cplusplus
LinearFunction linear = LinearFunction::Interpolation(0.0,0.0,1.0,2.0);                         // x_i, y_i, x_f, y_f
LinearFunction linear = LinearFunction::PointSlopeForm(1.0,2.0,2.0);                            // x_f, y_f, slope
CubicPolynomial cubic;
cubic = CubicPolynomial::DerivativeInterpolation(2.0,0.0,0.0,3.0,1.0,0.0);                      // x_i, y_i, y'_i, x_f, y_f, y'_f
cubic = CubicPolynomial::SecondDerivativeInterpolation(2.0,0.0,0.0,3.0,1.0,0.0);                // x_i, y_i, y''_i, x_f, y_f, y''_f
QuinticPolynomial quintic = QuinticPolynomial::Interpolation(0.0,0.0,0.0,0.0,1.0,2.0,1.0,0.0);  // x_i, y_i, y'_i, y''_i, x_f, y_f, y'_f, y''_f
```



#### Shifting

There is also a method for shifting the polynomial on the horizontal
axis. A negative offset will shift the polynomial to the left, while a
positive offset will shift the polynomial to the right.



```cplusplus
Polynomial<2> quadratic; // x^2
quadratic.shift(2);      // x^2 -> (x-2)^2 (graph shifted right by 2)
```



Later, if there is a need a vertical shift will be added.

### Derivatives



```cplusplus
Polynomial<5> p; 
// Comma Initialisation
p.coefficients() = 1,2,3,4,5,6;
cout << p << endl; // 1.00 + 2.00x + 3.00x^2 + 4.00x^3 + 5.00x^4 + 6.00x^5

// Derivatives
Polynomial<4> pdot = p.derivative();  // the derivative function
double pdot_five = p.derivative(5.0); // value of the derivative
Polynomial<2> pddot = p.dderivative();
double pddot_five = p.dderivative(5.0); // value of the derivative
```



### Polynomial Functions

There also exist various functions that operate on polynomials. These
currently include:

- `ecl::Roots<LinearFunction>`
- `ecl::Intersection<LinearFunction>`
- `ecl::Maximum<LinearFunction>`
- `ecl::Minimum<LinearFunction>`
- `ecl::Division<QuadraticPolynomial>`
- `ecl::Roots<QuadraticPolynomial>`
- `ecl::Division<CubicPolynomial>`
- `ecl::Roots<CubicPolynomial>`
- `ecl::Maximum<CubicPolynomial>`
- `ecl::Minimum<CubicPolynomial>`

They can also be called from the function classes themselves if it is
preferred, e.g.



```cplusplus
double maximum = ecl::Maximum<CubicPolynomial>()(0.0, 0.2, p);
```



OR



```cplusplus
double maximum = ecl::CubicPolynomial::Maximum(0.0, 0.2, p);
```



### Pascal's Triangle

Pascal's triangle is used to calculate the coefficients for polynomial
expansion. The class here accepts a template parameter N and calculates
all the coefficients up to order N (i.e. for polynomial expansion up to
(x+y)\^N).

You can stream the output directly if you just need to view them or you
can use an stl style iterator to traverse the rows diagonally. Simply
call the usual begin function with an integer argument representing the
diagonal you're interested in. The first iterator will traverse from
the top of the triangle to the bottom right. As you increase the index
the diagonals shift down and to the left.

There may be a future addition to allow horizontal row representations.
Also note, specialised (low N) versions of these exist that directly set
coefficients so as to avoid expensive calculations.



```cplusplus
PascalsTriangle<5> pascals_triangle;
cout << pascals_triangle << endl;
cout << "Row iteration [2]: ";
PascalsTriangle<5>::const_iterator row_iter;
for (row_iter = pascals_triangle.begin(2); row_iter != pascals_triangle.end(2); ++row_iter) {
    cout << *row_iter << " ";
}
cout << endl;
```

## Splines

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Polynomials](#polynomials).
- **Description:** Continuously connected functions (splines) and
  interpolation algorithms.
- **Keywords:** ecl splines
- **Tutorial Level:** INTERMEDIATE

### CubicSpline

The `CubicSpline` class has a relatively simple c++ interface.

- Generation of splines via blueprint algorithms.
- Access for any x, the spline value, its derivative or its second
  derivative.
- A streamed (algebraic) representation.

#### BluePrints

The blueprints generate a cubic spline over a data set. Depending on the
input constraints, the spline is generated rather differently. These can
be accessed via static methods in the blueprint factory
(`ecl::BluePrintFactory< CubicSpline >`) inherited by the
CubicSpline class. For example:



```cplusplus
CubicSpline cubic;
cubic = CubicSpline::Natural(x_set, y_set);
cubic = CubicSpline::ContinuousDerivatives(x_set, y_set, ydot_0, ydot_f);
cubic = CubicSpline::DerivativeHeuristic(x_set, y_set, ydot_0, ydot_f);
```



#### Access

Access allows you to calculate the value of the spline at any point on
its domain:



```cplusplus
std::cout << "Value         : " << cubic(3.2) << std::endl;
std::cout << "1st Derivative: " << cubic.derivative(3.2) << std::endl;
std::cout << "2nd Derivative: " << cubic.dderivative(3.2) << std::endl;
```



#### Print Algebraic Form

Streaming will provide an algebraic list of the cubic polynomials
constituting the spline.



```cplusplus
std::cout << cubic << std::endl;
// Typical output
// 1.00 + 2.31x + 3.00x^2 + 1.23x^3
// 0.00 + 1.42x + 5.20x^2 + 1.06x^3
```



### Smooth Linear Spline

The `SmoothLinearSpline` simply linearly connects waypoints and adds a
quintic polynomial curve to smooth the corners between each linear
section. The shape of these corners is parameterised by a maximum
curvature (acceleration) parameter.

#### Construction

Simply pass suitable x and y data sets along with a maximum curvature
constraint parameter to the spline's constructor. Be sure to catch an
exception if the construction should fail (this will occur if the
maximum curvature constraint cannot be met).



```cplusplus
double max_curvature = 5.0;
SmoothLinearSpline spline(x_set, y_set, max_curvature);
```



Access and streaming is similar to that for the cubic spline.

### Tension Splines

A [tension function](#tension-function) is
a hyperbolic function often used in spline interpolations that
parameterises the *tension* of an interpolation between points.

- Low tension : behaves exactly like the cubic spline
- High tension : behaves like a spline composed of piecewise smooth
  linear segments

The `TensionSpline` class is composed of a set of C2 connected
[tension functions](#tension-function).

#### BluePrints

There is currently only one blueprint (though variations are not
difficult to create). It is very similar to the natural cubic spline
(zero value boundary conditions for the second derivatives), the only
difference being the addition of the tension parameter.



```cplusplus
TensionSpline spline = TensionSpline::Natural(tension, x_set, y_set);
```



Access and streaming is similar to that for the cubic spline.

### Illustrations

There are different ways to formulate cubic splines - the following is a
*natural cubic spline* - it assumes zero values for the acceleration at
the boundary points.

![Natural Cubic Spline](doc/natural_cubic_spline.png)

The smooth linear spline is composed of linear segments with quintics
connecting them - these quintics operate at the specified maximum
acceleration (curvature).

![Smooth Linear Spline](doc/smooth_linear_splines.png)

The graphs show tension splines on the same set of waypoints, but for
different tension parameters. At high tension it is like a set of linear
segments (with high accelerations at the joints) and at low tension,
like a cubic.

![Tension Spline](doc/tension_splines.png)

## Pose

- **Description:** 2D and 3D representations for poses.
- **Keywords:** ecl pose
- **Tutorial Level:** INTERMEDIATE

### Overvew

These classes provide convenient interfaces to pose information,
typically used in robotics. The first of these, pose2d is useful for
mobile robotics (`x`, `y`, `yaw`), while pose3d is an
unconstrained representation in six dimensional space.

### Pose2D

Todo: see the class documentation for now.

### Pose3D

Todo: see the class documentation for now.

## Tutorials

- [Angles](#angles): Convenience
  class for abstractly storing and representing angles.
- [Cartesian Points](#cartesian-points):
  Simple object representations for cartesian points.
- [Polynomials](#polynomials):
  Working with polynomials of the n-th degree.
- [Pose](#pose): 2D and 3D
  representations for poses.
- [Splines](#splines):
  Continuously connected functions (splines) and interpolation
  algorithms.

## Tension Function

This is a hyperbolic function often used in spline interpolations that
parameterises the 'tension' of a curve interpolation between points.
At low tension it behaves like a cubic polynomial, while at high
tension, it tends towards a piecewise smooth series of linear functions.

They are derived from the following constraints on an interval `\[x_i,
x_i+1\]`:



```cplusplus
  f'''' - tau^2 f'' = 0
  f(x_i)     = y_i
  f(x_i+1)   = y_i+1
  f''(x_i)   = z_i
  f''(x_i+1) = z_i+1
```



This yields a C2 continuous function with hyperbolic terms (not a
polynomial) that ranges from looking like a cubic interpolation at low
tensions (`tau -> 0`) and a linearly blended interpolation at high
tensions.
