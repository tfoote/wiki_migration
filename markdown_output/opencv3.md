## Status

### Indigo and Jade

Since Indigo, there is a package for OpenCV3. It contains the
\'\'opencv\'\' and \'\'opencv_contrib\'\' repos from
<https://github.com/Itseez>. Some modules might not get included because
the dependencies are hard to package for all platforms (e.g. the optical
character recognition module that needs tesseract).

### Kinetic and above

Since Kinetic, OpenCV3 is the default. Discussion happened on
<https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!msg/ros-sig-perception/K5__71SX7eU/mxWwn3AeAwAJ>.

The reasons to choose OpenCV3 are:

-   OpenCV3 brings optimizations and many new features useful to
    robotics (calibration, object recognition \...)
-   the OpenCV2 version in Debian got rid of contribution modules and
    things like SIFT got lost

The reasons to package it ourselves are:

-   OpenCV3 is not packaged in Debian/Ubuntu yet
-   packaging opencv_contrib is difficult as it needs to be compiled
    with OpenCV sources. OpenCV 3.2.0 should allow to build
    opencv_contrib with an installed OpenCV.

## Usage

You would use OpenCV3 as you would usually outside of ROS but let\'s
explain a few corner cases:

-   if you have OpenCV2 and OpenCV3 installed,
    \'\'find_package(OpenCV)\'\' in CMake will first find OpenCV3. If
    you want to explicitly link to OpenCV2, use \'\'find_package(OpenCV
    2)\'\'
-   if you have OpenCV2 and OpenCV3 installed, OpenCV3 is not on your
    path: libraries and headers are renamed to only be visible through
    CMake. Python is the only exception but you can use the guide below
    to get your code to work with both.
-   just like with any library, you have to be careful that your binary
    does not link/includes directly or indirectly (through a dependency)
    to both OpenCV2 and OpenCV3.

A consequence of all that is that you have OpenCV3 installed in Indigo
or Jade and compile from source, you need to have any OpenCV dependent
package be part of your source workspace.

## Migration

Switching code to OpenCV3 can be done following the official guide at
<http://docs.opencv.org/master/db/dfa/tutorial_transition_guide.html>.

The rosdep key is \'\'opencv3\'\'.

## Dual Compatibility

Now, as a maintainer, you might want to not duplicate branches and keep
you code compatibility with OpenCV2. It is actually easy to write code
compatible with OpenCV 2.4.9+ and 3+.

### Python

```python
import cv2
from distutils.version import LooseVersion
if LooseVersion(cv2.__version__).version[0] == 2:
    # Whatever OpenCV2 code
else:
    # Whatever OpenCV3 code
```

### C++

```cpp
#include "opencv2/core/version.hpp"
#if CV_MAJOR_VERSION == 2
// do opencv 2 code
#elif CV_MAJOR_VERSION == 3
// do opencv 3 code
#endif
```

Also, if you write OpenCV3 code, chances are high that it will also
compile with OpenCV 2.4.9+. E.g., in color conversion, when replacing
\'\'CV_BGR2GRAY\'\' by \'\'cv::COLOR_RGB2GRAY\'\', your code will also
compile in OpenCV2 as this API has been backported (and not documented
\...).

### CMake

```cmake
if(OpenCV_VERSION VERSION_LESS "3.0")
# use 2.4 modules
else()
# use 3.x modules
endif()
```

### package.xml

Instead of depending on \'\'\'opencv3\'\'\', you should depend on
\'\'\'cv_bridge\'\'\' or \'\'\'image_geometry\'\'\'. Depending on one of
those two keys transitively makes you depend on
\'\'\'libopencv-dev\'\'\' on Jade and below, or \'\'\'opencv3\'\'\' on
Kinetic and above.

\'\'\'image_pipeline\'\'\' will only pull in \'\'\'sensor_msgs\'\'\' as
an extra dependency while \'\'\'cv_bridge\'\'\' will also pull in
\'\'\'boost\'\'\', \'\'\'python\'\'\' and \'\'\'rosconsole\'\'\' so it
depends on whether you go for something small or something you need.

## Building the Package

The package is slightly patched from upstream to not build certain
things like tests and examples. It is released through bloom using a tar
file as source. In case you ever need to build your own package, this
tar file is obtained with the following: ```highlight
#!/bin/bash
mkdir tmp
cd tmp
# the two lines below will fail in case it's not the first time we clone
git clone https://github.com/Itseez/opencv.git
git clone https://github.com/Itseez/opencv_contrib.git

# revert the main CMakeLists.txt file in case it's not the first time
cd opencv
git reset --hard HEAD
git checkout master
git clean -dxf
git reset --hard HEAD
git pull --rebase
# Use that date because of: https://github.com/ros-perception/vision_opencv/issues/170
git checkout `git rev-list -n 1 --before="2017-04-01 00:00" master`
#git checkout 3.2.0

cd ../opencv_contrib
git checkout master
git reset --hard HEAD
git pull --rebase
git checkout `git rev-list -n 1 --before="2017-04-01 00:00" master`                                                                  
#git checkout 3.2.0                                                                                                                  
cd ../                                                                                                                               
                                                                                                                                     
cp -fr ./opencv_contrib/modules ./opencv/opencv_contrib                                                                              
                                                                                                                                     
# revert the main CMakeLists.txt file in case it's not the first time                                                                
cd opencv                                                                                                                            
# Disable dnn for now.                                                                                                               
rm -fr ./opencv_contrib/dnn                                                                                                          
git checkout CMakeLists.txt                                                                                                          
sed -i 's/set(OPENCV_EXTRA_MODULES_PATH "" CACHE PATH "Where to look for additional OpenCV modules")/set(OPENCV_EXTRA_MODULES_PATH "${CMAKE_CURRENT_SOURCE_DIR}\/opencv_contrib\/" CACHE PATH "Where to look for additional OpenCV modules")/' ./CMakeLists.txt           
# Disable tests                                                                                                                      
sed -i 's/OCV_OPTION(BUILD_PERF_TESTS         "Build performance tests"                     ON  IF (NOT APPLE_FRAMEWORK) )/OCV_OPTION(BUILD_PERF_TESTS         "Build performance tests"                     OFF)/' ./CMakeLists.txt                                      
sed -i 's/OCV_OPTION(BUILD_TESTS              "Build accuracy \& regression tests"           ON  IF (NOT APPLE_FRAMEWORK) )/OCV_OPTION(BUILD_TESTS              "Build accuracy \& regression tests"           OFF)/' ./CMakeLists.txt                                    
# Enable Qt                                                                                                                          
sed -i 's/OCV_OPTION(WITH_QT             "Build with Qt Backend support"               OFF  IF (NOT ANDROID AND NOT IOS AND NOT WINRT) )/OCV_OPTION(WITH_QT             "Build with Qt Backend support"               ON  IF (NOT ANDROID AND NOT IOS AND NOT WINRT) )/' ./CMakeLists.txt                                                                                                                      
# Enable mangled path to have two OpenCV installable side by side                                                                    
sed -i 's/OCV_OPTION(INSTALL_TO_MANGLED_PATHS "Enables mangled install paths, that help with side by side installs." OFF IF (UNIX AND NOT ANDROID AND NOT APPLE_FRAMEWORK AND BUILD_SHARED_LIBS) )/OCV_OPTION(INSTALL_TO_MANGLED_PATHS "Enables mangled install paths, that help with side by side installs." ON)/' ./CMakeLists.txt                                                                           
#sed -i 's/OCV_OPTION(WITH_IPP            "Include Intel IPP support"                   NOT MINGW IF (X86_64 OR X86) AND NOT WINRT )/OCV_OPTION(WITH_IPP            "Include Intel IPP support"                   OFF)/' ./CMakeLists.txt                                 
sed -i 's/set(OPENCV_DLLVERSION "")/set(OPENCV_DLLVERSION "3")/' ./CMakeLists.txt                                                    
echo "install(FILES package.xml DESTINATION share/opencv3)" >> ./CMakeLists.txt                                                      
                                                                                                                                     
cd ../                                                                                                                               
                                                                                                                                     
# when configuring bloom the first time, use the tar file created above                                                              
rm ./opencv.tar.gz                                                                                                                   
tar --exclude-vcs -zcf ./opencv.tar.gz ./opencv/*
```

We need to use a .tar archive and not an upstream repo because we are
packaging opencv_contrib too and it cannot be packaged independently:
the official way of compiling it is by incorporating it into the OpenCV
sources.

Then, just download the opencv3-release repo at
<https://github.com/ros-gbp/opencv3-release> and:
```
git-bloom-release kinetic
```

## Future

OpenCV3 still evolves a lot, though the API is stable. You can expect
more GSOC projects to be integrated and more CMake modularity.
