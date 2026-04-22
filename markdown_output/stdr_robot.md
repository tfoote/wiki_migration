## Overview

The `stdr_robot` package implements a simulated robot, all simulated
sensors and its simulated motion controller. Till now the following
sensors are implemented:

-   Laser Range Scanner (LIDAR), provides a
    [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html).
-   Sonar, provides a
    [sensor_msgs/msg/Range](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Range.html).

Available motion controllers:

-   Ideal motion controller.

The robot class is available using the `nodelet` interface, named
`stdr_robot/Robot`. To load a new robot a [STDR Server](stdr_server)
has to be running. New robots/nodelets can be loaded only from
[stdr_server](stdr_server), using either [stdr_gui](stdr_gui) or
command-line tools described below.

A parser for YAML and XML files is also provided, to load or save
robots, sensors etc. More details on how to use YAML and XML files with
stdr_simulator [here](stdr_simulator/Tutorials/Using YAML files).

## Tf frames

A robot provides tf transforms for the pose of itself and its sensors.
All transforms are relative to `map_static` frame. For more details
about map tf frames see [STDR Server tf frames](stdr_server#Tf_frames).
An example with one spawned robot follows (using `rqt_tf_tree`):

![alt text\|width=750](attachment:tf_frames.png)

### Sensor transforms

The `frame_id` for each sensor is defined on loading a robot from GUI
or when using a YAML/XML file to describe a sensor. Each sensor
`frame_id` has to have a unique name per robot. To avoid naming
collisions with other robots it is also (automatically) prefixed with
robot's name. Example: `robot0_laser_1`.

### Robot transform

Each robot provides a tf transform with its current pose. The
`frame_id` is automatically assigned and has the format
`robot<ID>`. Example: `robot2`.

## Topics

All topic names are prefixed with robot name. Example
`robot1/cmd_vel`.

### Subscribed Topics

`cmd_vel`
([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html))
Robot listens for velocity commands

### Published Topics

`<laser_sensor_frame_id>`
([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html))
Publishes laser scan. Example: `robot0/laser_back`

`<sonar_sensor_frame_id>`
([sensor_msgs/msg/Range](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Range.html))
Publishes sonar measurements. Example: `robot0/sonar_2`

## Services

All services are prefixed with the name `robot_manager`. This is the
name of the nodelet manager and should **not** change.

`load_nodelet`
([nodelet/srv/NodeletLoad](https://docs.ros.org/en/rolling/p/nodelet/srv/NodeletLoad.html))
Called to load a new robot.

`unload_nodelet`
([nodelet/srv/NodeletUnload](https://docs.ros.org/en/rolling/p/nodelet/srv/NodeletUnload.html))
Called to unload/delete a robot.

## Command-Line Tools

### robot_handler

With the `robot_handler` command-line tool you can add, delete and
move a robot directly from the terminal. The following sections describe
the available commands.

#### robot_handler add

`add <description.yaml> <x> <y> <theta>` Adds a new robot at
given position (x, y, theta). Needs full path to the description file.
Example: 

```
$ rosrun stdr_robot robot_handler add resources/robots/khepera2.yaml 1.2 2 1.57
```

 NOTE: `robot_handler` does not check
if the pose you provided is valid, so you can spawn a robot on a wall,
or on top of an existing robot. (This will change in future releases)

#### robot_handler delete

`delete <robot_name>` Deletes a robot named <robot_name>. Example:


```
$ rosrun stdr_robot robot_handler delete /robot2
```



#### robot_handler replace

`replace <robot_name> <new_x> <new_y> <new_theta>` Moves a
robot to given pose. Example: 

```
$ rosrun stdr_robot robot_handler replace /robot1 1.2 3 3.14
```

 NOTE:
`robot_handler` does not check if the pose you provided is valid, so
you can move a robot on a wall, or on top of an existing robot. (This
will change in future releases)

## Tutorials

For tutorials see [stdr_simulator/Tutorials](stdr_simulator/Tutorials).
