A Catkin-friendly package for utilizing the C++ API of Tensorflow.

Get Tensorflow C++ API into ROS as easy as

```
find_package(catkin REQUIRED COMPONENTS
  ... your other packages ...
  tensorflow_ros_cpp
)
``` See the usage example at
<https://github.com/tradr-project/tensorflow_ros_test> .

```wiki
Starting with ROS Kinetic, the supported Ubuntu versions started to use C++11 ABI for building system packages. This makes problems when using the pip-installed Tensorflow (as described further). See section ''C++ ABI difference problems'' for hints on how to overcome this limitation.
``` \'\'Note: If you only intend to use Tensorflow
from Python nodes, you don\'t need this package. Just add
`<run_depend>python-tensorflow-pip</run_depend>` to your package.xml and
that\'s it.\'\'

## Multiple Tensorflow installation options

This package allows its users to \"provide\" Tensorflow in several ways,
and the developer doesn\'t have to care about which option the user
chooses:

-   \'\'\'As a pip (Python) package:\'\'\' The easiest way on Ubuntu
    14.04 / ROS Indigo. Just pip install tensorflow and that\'s it. GPU
    version supported! Can be used on newer Ubuntu versions, but with
    important limitations (see below).
-   \'\'\'Using
    [tensorflow_catkin](https://github.com/Skydes/tensorflow_catkin)
    package:\'\'\' Easily compile Tensorflow for your platform. A
    convenient way on newer systems. Supports GPU version.
-   \'\'\'Using a custom build of Tensorflow built by bazel:\'\'\' The
    least comfortable, yet most powerful way.
    [Compile Tensorflow yourself using bazel](https://www.tensorflow.org/install/install_sources)
    and tell this package where to find it.

A comprehensive list of compatible options for various OSes and ROS
distros is available
[in the package README](https://github.com/tradr-project/tensorflow_ros_cpp#tested-compatible-versions).

[Detailed configuration options](https://github.com/tradr-project/tensorflow_ros_cpp#pip-installation)
are available for each of the options.

## Note for rosdep users

If you\'re managing dependencies via rosdep, it is likely that you do
not want it to try to install the optional dependencies (currently
python-tensorflow-pip and tensorflow_catkin). In such case, add the
following to the rosdep call:

```
rosdep install ... --skip-keys=tensorflow_catkin --skip-keys=python-tensorflow-pip
```

## C++ ABI difference problems

Ubuntu systems starting with 16.04 (Xenial) are using the new C++11 ABI
for all system libraries. Until
[pip bug 1707002](https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1707002)
gets resolved (if ever!), the pip-distributed Tensorflow is built
againts an older C++ ABI, which is incompatible with the C++11 ABI. This
means linking to the Tensorflow library will fail on such systems and
there\'s no way around it.

The only \"workaround\" is to wrap all tensorflow code into a library
that exposes its functions using C API (so no std::strings, std::vectors
or Eigen types) and which does not link to any system library with a C++
API. Such library can then be built separately with
-D_GLIBCXX_USE_CXX11_ABI=0. Then you can freely link the rest of your
code using ROS, Eigen and so on to this library.

An example of this approach can be found at
[kinetic-devel branch of tensorflow_ros_test](https://github.com/tradr-project/tensorflow_ros_test/tree/kinetic-devel).

A library created this way is \"backwards compatible\" with older
systems, so it can be used everywhere. However, separating all
Tensorflow code can be tiresome, so we only suggest it as a last resort
option. This is why searching for the pip-installed Tensorflow is
disabled by default on systems using the new C++11 ABI (you can force it
using -DFORCE_TF_PIP_SEARCH=ON).
