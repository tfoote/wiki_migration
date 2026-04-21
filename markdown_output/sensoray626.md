This package provides a ROS wrapper for the Sensoray Model 626 analog
and digital I/O card drivers. This multifunctional board features analog
to digital (ADC), digital to analog (DAC), and counters for motor
encoders. For further technical specifications please visit the
[product website](http://www.sensoray.com/products/626.htm).

## Driver Installation

*This installation is generally untested, but works on my machine with
64-bit Ubuntu 10.04 machine and Diamondback.*

First, check out the sensoray626 package from the repository.

```
svn co https://mediabox.grasp.upenn.edu/svn/penn-ros-pkgs/penn_lightweight_teleop/trunk/sensoray626 sensoray626
```

Within the repository is a folder named ``s626-1.0.1``, which
contains the Sensoray's Linux SDK files (v1.0.1) that are also
available on the
[product website](http://www.sensoray.com/products/626.htm ). The README
file in this folder has instructions for building and installing the
kernel level driver for the 626. For simplicity (and because it seems
that these drivers must be reinstalled every time the computer is
restarted), I wrote a script to automate the build and install process.
This script must be run as sudo.

```
roscd sensoray626
sudo ./setup626.py
```

One important thing to note is that this script disables *comedi*. The
[comedi driver](http://www.comedi.org/doc/x1781.html#AEN4530) does not
support analog i/o functionality and conflicts with the manufacturer's
driver.

Now we can make the package, which should build the core&mod library as
*lib/libsensoray626.so* and a demo program as *bin/demo_cpp*. Run the
demo program to verify successful installation of the driver.

```
make
rosrun sensoray626 demo_cpp
```

## Using Sensoray 626 in your node.

Add the following line to *CMakeLists.txt* in your package to link to
the library in the sensoray626 package. ```
target_link_libraries(YOUR_EXECUTABLE_NAME_HERE sensoray626)
```

## External API Documentation

Sensoray provides documentation for the API as part of their
[Windows SDK](http://www.sensoray.com/downloads/sdk626.zip), or for
convenience you can download just the document
[here](https://mediabox.grasp.upenn.edu/svn/penn-ros-pkgs/penn_lightweight_teleop/trunk/sensoray626/626%20DLL%20Manual.pdf).
