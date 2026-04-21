**`'[[kaist_webots]]:`**' *webots_run \|
[webots_joy_demo](webots_joy_demo) \|
[webots_controllers](webots_controllers)*

Starts the [Webots](http://www.cyberbotics.com) simulator using a
system() call, so Webots can be run directly from a roslaunch file.\
The Webots world file is specified as an argument in the launch file.

Tested with Webots 6.4.4 and ROS Fuerte.

-   Author: David Butterworth
-   License: BSD
-   Repository: [kaist-ros-pkg](kaist-ros-pkg)
-   Source:
    <http://kaist-ros-pkg.googlecode.com/svn/trunk/kaist_webots/webots_run/>

\

## Installation

Follow [these instructions](kaist_webots) to install the
`kaist_webots` stack.

\

## Usage

To test the node, run: ```
$ roslaunch webots_run test_world.launch
``` This will start the
Webots simulator, which should look something like this:

![](http://img.acianetmedia.com/i/j5mWB.jpg)

This is just an empty world with no controller specified. If the
graphics quality is poor, then you may need to enable your 3D graphics
card. See the stack [installation instructions](kaist_webots) for more
information.

To use ROS with your own Webots model, you need to create a new package
e.g. `myrobot_sim_webots` containing the Webots .wbt world file and a
controller. The launch file loads the `webots_run` node with the world
file specified as an argument.\

For more information and examples, see the
[webots_joy_demo](webots_joy_demo) and
[webots_controllers](webots_controllers) packages.

\
