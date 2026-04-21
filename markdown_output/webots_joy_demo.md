**`'[[kaist_webots]]:`**' *[webots_run](webots_run) \| webots_joy_demo
\| [webots_controllers](webots_controllers)*

This is an example of a Webots Controller written in C++, running as a
ROS Node. It demonstrates how to build a ROS package linked against the
Webots CppLibrary, control a robot using ROS messages, and start the
simulation from a single launch file. This package is based on
[webots_joystick](webots_joystick), which uses the C API and a different
launching method.

The 'joy' node from the 'joystick_drivers' stack receives input from
a USB joystick and publishes the state of the buttons and axes on the
'/joy' topic. This node uses that input to drive a simple simulated
robot in Webots. Speed commands are sent to the differential drive model
using the Webots C++ API.

Tested with Webots 6.4.4 and ROS Fuerte.

-   Author: David Butterworth. Based on work by Andreas Breitenser and
    Olivier Michel.
-   License: BSD
-   Repository: [kaist-ros-pkg](kaist-ros-pkg)
-   Source:
    <http://kaist-ros-pkg.googlecode.com/svn/trunk/kaist_webots/webots_joy_demo/>

\

## Installation

Follow [these instructions](kaist_webots) to install the
`kaist_webots` stack.

\

## Usage

Plug-in your USB joystick. This joystick controller has been tested with
the Microsoft Xbox-360 USB joystick.

You can test the joystick by running: 

```
$ cat /dev/input/js0
```

 (you
should see strange characters when you press the buttons)

You can edit the joystick path in the launch file.

Run the demo: 

```
$ roslaunch webots_joy_demo run.launch
```



The Webots simulator should load, as shown:

![](http://img.acianetmedia.com/i/WieQo.jpg)

If the controller loads successfully, there should be no error messages
in the Webots console:

![](http://img.acianetmedia.com/i/0odiy.jpg)

You can control the simulated robot using the USB joystick.\
For the Xbox-360 joystick, the controls are as follows:

![](http://img.acianetmedia.com/i/vTWs.jpg)

\

## Controlling your own Webots mobile robot

-   Create a new Webots world with a differential drive robot

```{=html}
<!-- -->
```
-   Ceate a new ROS package e.g. `myrobot_sim_webots`. See
    [Creating a ROS Package](ROS/Tutorials/CreatingPackage)

```{=html}
<!-- -->
```
-   Add the Webots .wbt world file to your package, in the `/world`
    directory

```{=html}
<!-- -->
```
-   Copy the `webots_joy_demo` source to the `/src` directory

```{=html}
<!-- -->
```
-   Edit `CMakeLists.txt`, using this package as an example. Note how
    the destination of the compiled binary is in the
    `controllers/binary_name` directory to suit Webots requirements,
    not the default ROS directory `/bin`

```{=html}
<!-- -->
```
-   Edit your Webots world file and specify the name of the controller
    binary file

```{=html}
<!-- -->
```
-   Create a launch file in the `/launch` directory, using this
    package as an example. The Webots world file is specified as an
    argument to the `webots_run` node

```{=html}
<!-- -->
```
-   Build your package: `rosmake myrobot_sim_webots`

For an example of a joint position controller, see the
[webots_controllers](webots_controllers) package.

\
