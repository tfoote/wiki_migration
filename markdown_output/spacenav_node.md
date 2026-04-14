1.  keywords joystick, spacenav
    ![A SpaceNavigator](attachment:spacenav.png)

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
upstream [spacenav](spacenav) package.

## API Stability

This package\'s API is expected to be stable.

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
