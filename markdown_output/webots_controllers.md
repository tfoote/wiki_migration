***[kaist_webots](kaist_webots):*** *[webots_run](webots_run) \|
[webots_joy_demo](webots_joy_demo) \| webots_controllers*

The idea behind this package was to create a controller manager for
Webots, similar to GazeboRosControllerManager. This would enable users
to easily test different position, velocity, or force controllers with
their simulation.

The launch file loads the \'webots_run\' node which opens the specified
world file in the Webots simulator, which in turn executes the
controller binary.

At present, only a simple stand-alone P-controller has been implemented:
joint_position_controller. The controller can be easily configured for
new Webots worlds, allowing users to quickly test their model.

Tested with Webots 6.4.4 and ROS Fuerte.

-   Author: David Butterworth.
-   License: BSD
-   Repository: [kaist-ros-pkg](kaist-ros-pkg)
-   Source:
    <http://kaist-ros-pkg.googlecode.com/svn/trunk/kaist_webots/webots_controllers/>

\

## Joint Position Controller

A joint position controller for Webots, utilising the C++ API and simple
P-control.

The controller configuration is defined in a yaml file, which includes
the ROS topic for subscribing to commands for each joint, the joint\'s
servo name in Webots, and the value of the P constant.\
The \`webots_controllers_to_load\` parameter in the launch file
specifies which controllers from the yaml file should be loaded.

Position commands are received on a ROS topic for each joint.\
Current position and calculated velocity values are published on the
\`/joint_states\` topic.\
Force information is not checked due to a bug with Webots 6.4.4

\

## Installation

Follow [these instructions](kaist_webots) to install the
\`kaist_webots\` stack.

\

## Usage

A demo of the joint position controller is included, using ROS messages
to control a simulated Puma 560 manipulator in Webots.

Run the demo: ```
$ roslaunch webots_controllers joint_position_controller_demo.launch
```

The Webots simulator should load with the Puma 560 in the home position.

If everything is working correctly, the following messages will be
printed in the Webots console:
![](http://img.acianetmedia.com/i/9pT7C.jpg)

List the available joint controllers by opening a new shell console and
running: `$ rostopic list`

To move one of the joints, you need to publish the desired position to
the\
\`/Puma560/SimController/\<joint name\>/command\`\
topic.

For example, the base rotation joint is called \'waist\'. To move that
joint, run the command: ```
$ rostopic pub -1 /Puma560/SimController/waist/command std_msgs/Float64 -- 1.5
``` The joint will rotate
1.5 radians in the positive direction.\
This command publishes one message to the ROS topic and the \"\`\--\`\"
indiciates that the next input is a number.

![](http://img.acianetmedia.com/i/D9Umb.jpg)

\

## Controlling your own Webots robot arm

-   Create a new Webots world and robot arm model. Assign each joint
    servo with a unique name.

```{=html}
<!-- -->
```
-   Ceate a new ROS package e.g. \`myrobot_sim_webots\`. See
    [Creating a ROS Package](ROS/Tutorials/CreatingPackage)

```{=html}
<!-- -->
```
-   Add the Webots .wbt world file to your package, in the \`/world\`
    directory

```{=html}
<!-- -->
```
-   Copy the \`webots_controllers\` source to the \`/src\` directory

```{=html}
<!-- -->
```
-   Edit \`CMakeLists.txt\`, using this package as an example. Note how
    the destination of the compiled binary is in the
    \`controllers/binary_name\` directory to suit Webots requirements,
    not the default ROS directory \`/bin\`

```{=html}
<!-- -->
```
-   Edit your Webots world file and specify the name of the controller
    binary file

```{=html}
<!-- -->
```
-   Create a new .yaml file in the \`/config\` directory, using this
    package as an example. This contains the name of the ROS topic for
    joint commands, the servo names from the Webots model, and the P
    constant for the position controller.

```{=html}
<!-- -->
```
-   Create a launch file in the \`/launch\` directory, using this
    package as an example. The \`webots_controllers_to_load\` parameter
    contains the controller names from the yaml file. The Webots world
    file is specified as an argument to the \`webots_run\` node

```{=html}
<!-- -->
```
-   Build your package: \`rosmake myrobot_sim_webots\`

\
