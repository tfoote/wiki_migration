\'\'\'NOTE: From [ROS Hydro](hydro) functionality of this package is
migrated into [slam_karto](slam_karto)\'\'\'.

\'\'\' Warning, this documentation is not stable \'\'\'

## Hardware Requirements

To use \`karto\`, you need a mobile robot that provides odometry data
and is equipped with a horizontally-mounted, fixed, laser range-finder.
The \`karto\` node will attempt to transform each incoming scan into the
\`odom\` (odometry) [tf](tf) frame. See the
\"[Required tf transforms](#tf)\" for more on required transforms.

## Building Karto in a stand-alone mode

Karto uses [cmake](http://www.cmake.org/)(like ros) to build itself. To
build Karto: ```
mkdir build
cd build
cmake -G \"Unix Makefiles\" ..
make
```

You should see something like that (short version):

```
[  1%] Building CXX object Karto.cpp.o
[  1%] Building CXX object Mapper.cpp.o
Linking CXX shared library ../lib/libOpenKarto_32.dylib
[  1%] Built target OpenKarto
[ 53%] Built target proj
[ 73%] Built target csparse
[ 74%] Built target spa2d
Linking CXX shared library ../lib/libKarto_32.dylib
[ 98%] Built target Karto
[ 98%] Building CXX object tutorial1.cpp.o
Linking CXX executable ../bin/OpenKarto_Tutorial1
[ 98%] Built target OpenKarto_Tutorial1
[ 98%] Building CXX object tutorial2.cpp.o
[100%] Building CXX object SpaSolver.cpp.o
Linking CXX executable ../bin/OpenKarto_Tutorial2
[100%] Built target OpenKarto_Tutorial2
```

In the bin directory, you should have both tutorials built and in the
lib directory you should have \'\'libOpenKarto_32.so\'\'

## Tutorials

## Nodes
