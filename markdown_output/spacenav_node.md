1.  keywords joystick, spacenav ![A SpaceNavigator](doc/spacenav.png)

## Installation



```
$ sudo apt install spacenavd
$ sudo apt install ros-indigo-spacenav-node
```



## Usage



```
$ roslaunch spacenav_node classic.launch
```



## Supported Hardware

This package should support any hardware that is supported by the
upstream [spacenav](https://index.ros.org/p/spacenav) package.

## API Stability

This package's API is expected to be stable.

## Nodes



```clearsilver
node {
 0{
 name = spacenav_node
 desc = `spacenav_node` provides output from the [[spacenav]] driver over ROS.
 pub {
  0{
  name= spacenav/offset
  type= geometry_msgs/Vector3
  desc= Publishes the linear component of the joystick's position. Approximately normalized to a range of -1 to 1.
  }
  1{
  name= spacenav/rot_offset
  type= geometry_msgs/Vector3
  desc= Publishes the angular component of the joystick's position. Approximately normalized to a range of -1 to 1.
  }
  2{
  name= spacenav/twist
  type= geometry_msgs/Twist
  desc= Combines `offset` and `rot_offset` into a single message.
  }
  3{
  name= spacenav/joy
  type= sensor_msgs/Joy
  desc= Outputs the spacenav's six degrees of freedom and its buttons as a joystick message.
  }
 }
 }
}
```

## Tutorials

- [How to Use a SpaceNavigator with the spacenav_node](#how-to-use-a-spacenavigator-with-the-spacenav_node):
  This tutorial is an introduction to using the 3DConnexion
  !SpaceNavigator connected to a desktop. After reading this, you should
  be able to bring up the spacenav_node and display the data.
- [Writing a Teleoperation Node for the SpaceNavigator](#writing-a-teleoperation-node-for-the-spacenavigator):
  This tutorial covers how to write a teleoperation node and use it to
  drive the turtle in the
  [turtlesim](https://index.ros.org/p/turtlesim).
  - Create a New Tutorial:\*\*

## Troubleshooting

### Errors when using package

#### Error: Could not open the space navigator device.  Did you remember to run spacenavd (as root)?

**Example:** 

```
blaise@hya: /opt/ros/cturtle/stacks/joystick_drivers/spacenav_node $ ./spacenav_node 
connect failed: No such file or directory
[ERROR] [1288904194.289257379]: Could not open the space navigator device.  Did you remember to run spacenavd (as root)?
[ WARN] [1288904194.289311637]: Publisher on '/spacenav/joy' destroyed immediately after creation.  Did you forget to store the handle?
```



**Solution:**

- Did you run spacenavd? 

```
sudo bash
rosrun spacenav spacenavd
```



<!-- -->

- Did you run spacenavd via sudo? In some conditions, running
  

```
sudo rosrun spacenav spacenavd
```

 does not work. Use the invocation above if
  you run into trouble.

#### Error: failed to grab the spacenav device: Device or resource busy

**Example:** 

```
$ sudo ./spacenavd  -d
Spacenav daemon svn-r87
failed to open config file /etc/spnavrc: No such file or directory. using defaults.
using device: /dev/input/event4
failed to grab the spacenav device: Device or resource busy
device name: 3Dconnexion SpaceNavigator for Notebooks
```

 And spacenav_node publishes
/spacenav/{joy,twist} with value of 0.

**Solution:**

- This seems X server automatically detects space navigator, which
  results in the spacenav not getting USB events as described in
  <http://spacenav.sourceforge.net/faq.html#faq11>. I tried to follow
  the FAQ instruction but it didn't help(if someone know how to igonre
  spacenav mouse from X server, please add instruction). What I tried
  is: 

```
1) connect spacenav ( blue led is on : this means X server found the mouse)
2) run spacenavd
3) unplug and plug spacenav until it did not outputs "fialed to grab..." goto
4) start spacenav node
```

## How to Use a SpaceNavigator with the spacenav_node

### Compiling

Start by getting the dependencies and compiling the driver.



```
$ sudo apt install spacenavd
$ sudo apt install ros-indigo-spacenav-node
```



### Plugged In

Make sure that your
[SpaceNavigator](http://www.3dconnexion.com/3dmouse/spacenavigator.php)
is plugged into the USB port.

### Running the spacenav_node



```
$ roslaunch spacenav_node classic.launch
```



### Viewing the data

The spacenav_node publishes four topics:



```
rostopic list
```

 You will see something similar to:

. 

```
/spacenav/joy
/spacenav/offset
/spacenav/rot_offset
/spacenav/twist
```



- /spacenav/joy - publishes the linear motion on a scale of \[-1, 1\]
- /spacenav/offset - publishes the unscaled linear motion
- /spacenav/rot_offset - publishes the unscaled rotational motion
- /spacenav/twist - publishes a twist of unscaled linear and rotational
  motion

To see that everything is working and data is being published to ROS, in
**a new terminal**:



```
$ rostopic echo /spacenav/joy
```

 You will see something similar to:

. 

```
---
axes: (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
buttons: (0, 0)
---
axes: (-0.021484375, 0.009765625, -0.009765625, 0.0, 0.0, 0.0)
buttons: (0, 0)
---
axes: (-0.005859375, 0.02734375, -0.009765625, 0.0, 0.0, 0.0)
buttons: (0, 0)
---
axes: (-0.005859375, 0.02734375, -0.009765625, -0.0234375, 0.0, 0.0)
buttons: (0, 0)
```



Move the spacenavigator around to see the data change.

------------------------------------------------------------------------

## Writing a Teleoperation Node for the SpaceNavigator

### Workspace Setup

If you have not yet created a workspace in which to complete the
tutorials, <<SeeSaw("EnvironmentSetup", toshow="click here for some
brief instructions")>>.



```
{{{{#!wiki seesaw EnvironmentSetup

<<Version()>>

{{

To overlay on the `ROS` distro you are using:
{{{
rosinstall ~/tutorials /opt/ros/$ROS_DISTRO>> ~/tutorials.rosinstall
```



To use this workspace **whenever** you open a new terminal setup your
ROS environment by typing: 

```
source ~/tutorials/setup.bash
```



Sourcing this file adds `/tutorials/workspace` to your
ROS_PACKAGE_PATH.

Any packages you create in that directory will be found by
[rospack](https://index.ros.org/p/rospack).

An alternative to source your script file is to add it to your
`.bashrc`, but remember that this will persist in your `.bashrc`
into the future, and you can only have one environment setup. For more
on what this is doing see [ this page](rosinstall#Generating_setup.sh)
}}}}}



```
{{#!wiki version groovy_and_newer
Create a [[catkin]] workspace like so:

{{{
$ source /opt/ros/$ROS_DISTRO/setup.bash
$ mkdir -p ~/tutorial_ws/src
$ cd ~/tutorial_ws
$ catkin_init_workspace src
$ catkin_make
```



And now source the setup file from the result-space, so that packages
you add to this workspace's `src` folder will be findable by
[rospack](https://index.ros.org/p/rospack), and the built binaries by
[rosrun](rosrun) and [roslaunch](https://index.ros.org/p/roslaunch):



```
$ source devel/setup.bash
```



}}}}}

}}}}}}}

#### Create a Scratch Package

Before starting this tutorial, take the time to create a scratch package
to work in and manipulate the example code. See
[creating a ROS package](ROS/Tutorials/CreatingPackage) to learn more
about creating a package. Create a learning_spacenav package with the
following dependencies: 

```
$ roscd tutorials
$ roscreate-pkg learning_spacenav roscpp turtlesim spacenav_node
```



Uncomment the genmsg() line in the CMakeLists.txt file of the
learning_spacenav package and run
[rosmake](https://index.ros.org/p/rosmake).

#### Writing a Simple Teleoperation Node

First, create learning_spacenav/src/teleop_turtle_spacenav.cpp in your
favorite editor, and place the following inside of it:

##### The Code

Source:
[teleop_turtle_joy.cpp](https://github.com/ros-drivers/joystick_drivers_tutorials/blob/master/turtle_teleop/src/teleop_turtle_joy.cpp)



```cpp
#include <ros/ros.h>
#include <turtlesim/Velocity.h>
#include <sensor_msgs/Joy.h>
class TeleopTurtle
{
public:
  TeleopTurtle();

private:
  void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);
  
  ros::NodeHandle nh_;

  int linear_, angular_;
  double l_scale_, a_scale_;
  ros::Publisher vel_pub_;
  ros::Subscriber joy_sub_;
  
};
TeleopTurtle::TeleopTurtle():
  linear_(1),
  angular_(2)
{

  nh_.param("axis_linear", linear_, linear_);
  nh_.param("axis_angular", angular_, angular_);
  nh_.param("scale_angular", a_scale_, a_scale_);
  nh_.param("scale_linear", l_scale_, l_scale_);
  vel_pub_ = nh_.advertise<turtlesim::Velocity>("turtle1/command_velocity", 1);
  joy_sub_ = nh_.subscribe<sensor_msgs::Joy>("joy", 10, &TeleopTurtle::joyCallback, this);
}
void TeleopTurtle::joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
  turtlesim::Velocity vel;
  vel.angular = a_scale_*joy->axes[angular_];
  vel.linear = l_scale_*joy->axes[linear_];
  vel_pub_.publish(vel);
}
int main(int argc, char** argv)
{
  ros::init(argc, argv, "teleop_turtle");
  TeleopTurtle teleop_turtle;

  ros::spin();
}
```



##### The Code Explained

Now, let's break down the code piece by piece.



```cpp
#include <ros/ros.h>
#include <turtlesim/Velocity.h>
#include <sensor_msgs/Joy.h>
```



- turtlesim/Velocity.h includes the turtle velocity msg so that we can
  publish velocity commands to the turtle
- joy/Joy.h includes the joystick msg so that we can listen to the joy
  topic



```cpp
class TeleopTurtle
{
public:
  TeleopTurtle();

private:
  void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);
  
  ros::NodeHandle nh_;

  int linear_, angular_;
  double l_scale_, a_scale_;
  ros::Publisher vel_pub_;
  ros::Subscriber joy_sub_;
  
};
```

 Here we create the !TeleopTurtle class and
define the joyCallback function that will take a joy msg. We also create
a node handle, publisher, and subscriber for later use.



```cpp
TeleopTurtle::TeleopTurtle():
  linear_(1),
  angular_(2)
{

  nh_.param("axis_linear", linear_, linear_);
  nh_.param("axis_angular", angular_, angular_);
  nh_.param("scale_angular", a_scale_, a_scale_);
  nh_.param("scale_linear", l_scale_, l_scale_);
```

 Here we initialize some parameters: the
linear_ and angular_ variables are used to define which axes of the
joystick will control our turtle. We also check the parameter server for
new scalar values for driving the turtle.



```cpp
  vel_pub_ = nh_.advertise<turtlesim::Velocity>("turtle1/command_velocity", 1);
```

 Here we create a publisher that will advertise
on the command_velocity topic of the turtle.



```cpp
  joy_sub_ = nh_.subscribe<sensor_msgs::Joy>("joy", 10, &TeleopTurtle::joyCallback, this);
```

 Here we subscribe to the joystick topic for
the input to drive the turtle. If our node is slow in processing
incoming messages on the joystick topic, up to 10 messages will be
buffered before any are lost.



```cpp
void TeleopTurtle::joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
  turtlesim::Velocity vel;
  vel.angular = a_scale_*joy->axes[angular_];
  vel.linear = l_scale_*joy->axes[linear_];
  vel_pub_.publish(vel);
}
```

 Here we take the data from the joystick and
manipulate it by scaling it and using independent axes to control the
linear and angular velocities of the turtle. Finally we publish the
prepared message.



```cpp
int main(int argc, char** argv)
{
  ros::init(argc, argv, "teleop_turtle");
  TeleopTurtle teleop_turtle;

  ros::spin();
}
```

 Lastly we initialize our ROS node, create a
teleop_turtle, and spin our node until `Ctrl-C` is pressed.

#### Compiling and Running Turtle Teleop

Add the following line to your CMakeLists.txt file:



```
rosbuild_add_executable(turtle_teleop_spacenav src/turtle_teleop_spacenav.cpp)
```



#### Setting up the SpaceNavigator

Before we can run the !SpaceNavigator and teleop together, we need to
make the !SpaceNavigator accessible. Connect your !SpaceNavigator as we
did in the
[previous tutorial](#how-to-use-a-spacenavigator-with-the-spacenav_node).



```
$ roscd /spacenav/spacenav_svn/spacenavd
$ sudo ./spacenavd -d
```



#### Writing a Launch File to Start all of the Nodes

Now let's make a launch file to start all of the nodes we need. See
[Roslaunch XML Reference](https://index.ros.org/p/roslaunch) for
[roslaunch](https://index.ros.org/p/roslaunch) syntax. Create the file
launch/turtle_spacenav.launch and paste the following:

(See
[turtle_spacenav.launch](https://code.ros.org/svn/ros-pkg/stacks/joystick_drivers_tutorials/trunk/turtle_teleop/launch/turtle_spacenav.launch))

Now you can start the nodes to drive your turtle around:



```
roslaunch learning_spacenav turtle_spacenav.launch
```
