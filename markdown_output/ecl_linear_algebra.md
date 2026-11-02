## Prerequisites

Using ros eigen now, but you can also opt to use the internal
[ecl_eigen](https://index.ros.org/p/ecl_eigen).

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

- [Using Eigen](#using-eigen) -
  there are quite a few tricks you should be aware of when using
  eigen\...
- [Eigen Extensions](#eigen-extensions) -
  some extensions built in and around eigen by the ecl.

## Using Eigen

- **Description:** There are quite a few tricks you should be aware of
  when using eigen\...
- **Keywords:** ecl eigen linear algebra
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Eigen Extensions](#eigen-extensions)

### Using Eigen

#### Documentation

The following are some important links for us back to the eigen
documentation:

- [Documentation Frontend](http://eigen.tuxfamily.org/dox-devel/)
- [Lazy Evaluation](http://eigen.tuxfamily.org/dox-devel/TopicLazyEvaluation.html)
- [Writing Optimised Expressions](http://eigen.tuxfamily.org/dox-devel/TopicWritingEfficientProductExpression.html)
- [Decompositions Overview](http://eigen.tuxfamily.org/dox-devel/TopicLinearAlgebraDecompositions.html)
- [Modifications needed for Classes with Eigen Members](http://eigen.tuxfamily.org/dox-devel/TopicStructHavingEigenMembers.html)
- [Stl containers and eigen](http://eigen.tuxfamily.org/dox-devel/TopicStlContainers.html)

Some important points to note (more detailed notes regarding some eigen
specific issues further below):

- Matrices/Vectors of all types are built from the one base class.
- Typedefs exist for all common forms of matrices and vectors (important
  for vectors as there is no Vector class).

The ecl supplements the eigen library with a few extras features.

### Issues

#### Alignment

You have to be very careful with eigen to make sure alignment works
properly. This is a bit of a pain in the bum, but will result in
hardware speedups. If you see the following error message:



```cplusplus
/opt/ros/ecl/ecl_core/ecl_linear_algebra/include/ecl/Eigen2/src/Core/MatrixStorage.h:44:Eigen::ei_matrix_array<T, Size, MatrixOptions, Align>::ei_matrix_array() [with T = double, int Size = 4, int MatrixOptions = 2, bool Align = true]: Assertion     `(reinterpret_cast<size_t>(array) & 0xf) == 0 && "this assertion is explained here:
http://eigen.tuxfamily.org/dox/UnalignedArrayAssert.html  **** READ THIS WEB PAGE !!! ****"' failed.
```



its probably because you need to fix your storage mechanism for classes
with eigen vectors inside them. See that web page for more detail and/or
run gdb on your program to see where the compile time assert triggered.

Usual scenario - you have used an eigen type of fixed size as a storage
container embeddded inside a class or struct, or inherited a class that
does so.

- only for fixed size eigen types
- fixed size eigen type is inside the class or inside an inherited class

In this situation, you need to add the following macro to the public
section of the class <i>as well as</i> each class that inherits this
class.



```cplusplus
EIGEN_MAKE_ALIGNED_OPERATOR_NEW
```



#### Std Vector

If always calling linear_algebra.hpp to access eigen, it will bring in
Eigen's NewStdVector implementation. This will use it for eigen types
and default to the original std vector for other types, but there's one
caveat. For eigen to distinguish, you need to specify the vector
allocator.



```cplusplus
#include <ecl/linear_algebra.hpp>

int main(int argc, char **argv) {

    std::vector< Eigen::Vector2d, Eigen::aligned_allocator<Eigen::Vector2d> > vv; // eigen's std vector implementation
    std::vector<double> vd; // std's vector implementation

    Eigen::Vector2d v; v << 1,2;
    vv.push_back(v); vv.push_back(v);
    std::cout << vv[0] << std::endl;

    return 0;
}
```



If you do not include it, you will see the usual compile time alignment
warning that Eigen loves.

## Eigen Extensions

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Using Eigen](#using-eigen).
- **Description:** Some extensions the ecl has made in and around eigen.
- **Keywords:** ecl eigen
- **Tutorial Level:** INTERMEDIATE

### Eigen Plugin

The eigen matrixbase class provides a way to extend its api via a
macro-based plugin. The trick is enabled by the following code in
eigen's MatrixBase class:



```cplusplus
class MatrixBase {
    // ...
    #ifdef EIGEN_MATRIXBASE_PLUGIN
      #include EIGEN_MATRIXBASE_PLUGIN
    #endif
};
```



Here we take advantage of it to add the following api:

- conservativeResize(int rows, int cols) : matrix resizing, carrying
  over existing elements
- conservativeResize(int rows) : vector resizing, carrying over existing
  elements

This will be brought in if you do one of the following *before* you
include any eigen headers:



```cplusplus
#define EIGEN_MATRIXBASE_PLUGIN <ecl/linear_algebra/eigen_plugin.hpp>
// OR the ecl bundle
#include <ecl/linear_algebra.hpp>
// OR any one of the ecl-eigen3 modules
#include <ecl/linear_algebra/core.hpp>
```



Note that if you wish to customise the eigen plugin differently, simply
define the macro, pointing it at your own customisation before including
ecl/linear_algebra.hpp. The ecl plugin makes a check and won't override
any existing definitions.

### Formatters

Formatters have been included in the plugin for float and double type
matrices (may expand to integral types later if we need them). This is
achieved by use of the
[ecl_formatters](https://index.ros.org/p/ecl_formatters) framework.

There are several ways you can call these formatters, the most
convenient methods are outlined below:



```cplusplus
#include <linear_algebra.hpp>
Matrix2d m; m << 1.0, 2.0, 3.0, 4.0;
Matrix2d::Formatter formatter(3,6); // prec 3, width 6
formatter.precision(2); formatter.width(5);
std::cout << formatter(m) << std::cout;     // format using the stored settings
std::cout << formatter(m,3,6) << std::cout; // format using one-shot settings
```





```cplusplus
#include <ecl/formatters.hpp>
#include <ecl/linear_algebra.hpp>
Matrix2d m; m << 1.0, 2.0, 3.0, 4.0;
Format<Matrix2d> format(3,6); // prec 3, width 6
format.precision(2); format.width(5);
std::cout << format(m) << std::cout;     // format using the stored settings
std::cout << format(m,3,6) << std::cout; // format using one-shot settings
```

## Tutorials

- [Eigen Extensions](#eigen-extensions):
  Some extensions the ecl has made in and around eigen.
- [Using Eigen](#using-eigen):
  There are quite a few tricks you should be aware of when using
  eigen\...
