This package is barely usable alone since it provides only the common
features to be exploited and expanded in the derived packages (cf.
[qb_hand](https://index.ros.org/p/qb_hand) and
[qb_move](https://index.ros.org/p/qb_move)).

## Launch files

<a id="controllers_bringup"></a>


```clearsilver
name = spawner_template
desc = This launch file loads the controller parameters (i.e. the given yaml file) to the Parameter Server and spawns them in the [[controller_manager]]. If specified, starts the [[rqt_joint_trajectory_controller]] GUI.
param {
  0.name = controllers
  0.type = string
  0.desc = The list of names of the controllers to be spawned (e.g. `*_trajectory_controller`)
  1.name = namespace
  1.type = string
  1.desc = The namespace prefix (without "_controllers.yaml") of the controller configuration file, necessary with many devices (e.g. `my_device` if it is `my_device_controllers.yaml`). The file must be located in the `config/` subdirectory of the selected `_control` package. In addition, the joint names inside should be consistent with the ones specified in the description bringup, usually the share the same namespace.
  2.name = package_prefix
  2.type = string
  2.desc = The base package name prefix (without "_control") where controller settings are stored (e.g. `qb_device` if it is `qb_device_control`).
  3.name = use_controller_gui
  3.type = bool
  3.desc = Selects whether to load joint trajectory controller GUI.
  3.default = false
}
```



## API



```clearsilver
name = qb_device_control
desc = This device-independent library provides all the common structures to control both the [[qb_hand]] and the [[qb_move]] devices. It exploits the [[qb_device_hardware_interface]] and thus requires all the ROS resources related to it.
act_called {
  0.name = ~<namespaced_action_type>_trajectory_controller/follow_joint_trajectory
  0.type = control_msgs/FollowJointTrajectory
  0.desc = The control action advertised by the [[controller_manager]] relative to the controller in use.
}
param {
  0.name = ~namespaced_action_type
  0.type = string
  0.desc = The namespaced type of the control action advertised by the [[controller_manager]] without the "_trajectory_controller/follow_joint_trajectory" suffix (e.g. `device_foo` if it is `device_foo_trajectory_controller/follow_joint_trajectory`).
  1.name = ~control_duration
  1.type = double
  1.desc = The duration of the control loop, in [s].
  1.default = 0.01
  2.name = ~waypoints
  2.type = list of maps
  2.desc = The list of waypoint. Each contains a `time` array, which can be either a single value or an interval for which all the specified `joint_positions` hold, and a `joint_positions` map, which pairs contain the device namespace (i.e. the map key) associated with the relative joint positions array. If a namespace used before is not specified for a given waypoint, it is assumed that it does not change the device configuration. Nonetheless for critical applications it is recommended to specify every namespaces to avoid interpolation approximations.
}
srv_called {
  0.name = /communication_handler/sync_nodes
  0.type = qb_device_srvs/Trigger
  0.desc = Checks if all the already registered devices are completely initialized and ready for the control application; a device node is considered ready if it has requested this service at least once. The response `success` variable is set to `true` if all the control nodes are ready.
}
```

## Tutorials

- [Basics](#basics): Basic
  knowledge of the qbrobotics control Nodes
- [Details](#details):
  Details on the qbrobotics control Nodes
- [Communication Handler](#communication-handler):
  Details on the Communication Handler Node
- [Control](#control):
  Details on the control Node

## Basics

As shown in the following picture there are two distinct configurations
to control several *qbrobotics®* devices connected to the system:

- The first (and recommended) groups all the Hardware Interfaces
  together (thanks to the
  [combined_robot_hw](https://index.ros.org/p/combined_robot_hw)) and
  exploits them as a unique robot system. We have called it
  *"synchronous"* just to point out that every sequence of reads and
  writes is always done in the same predefined order.
- The second mode threats every device as an independent Hardware
  Interface with its dedicated ROS Node which executes the control loop
  independently w.r.t. the rest of the system, i.e.
  *"asynchronously"*.

Mixed configurations can be also achieved through a proper setup. In
such a case we can think of synchronous sub-systems which execute
asynchronously w.r.t. each other.

*Note that in a single-device system the synchronous mode is a
nonsense.*

![overview_setup\|width=755](https://bitbucket.org/qbrobotics/qbhand-ros/raw/ddbccc369d6846549e9b03c9dce0c2dc6c1115e1/qb_hand_media/overview_setup.svg)

*Note that in the previous picture are shown qbmoves, but the same
concept applies to any other qbrobotics device.*

In both cases there is always one central Node which manages the shared
resources for the serial communication (e.g. one or many USB ports) and
which provides several ROS services to whom wants to interact with the
connected devices. This Node is called *Communication Handler* and it is
usually started in a separate terminal.



```wiki
Please remember that in a multi-device configuration, each ''qbrobotics®'' device connected to your system '''must have a unique ID'''.
```

## Details

To understand what is hiding under the hood, have a look at the C++
classes overview which sums up all the main concepts of our ROS
packages:

![overview_classes\|width=755](https://bitbucket.org/qbrobotics/qbhand-ros/raw/ddbccc369d6846549e9b03c9dce0c2dc6c1115e1/qb_hand_media/overview_classes.svg)

## Communication Handler

The Communication Handler Node has no parameters to be set, therefore it
is always launched like this: 

```
roslaunch qb_device_driver communication_handler.launch
```



On start, it scans the serial communication resources connected to you
system and shows a list of the devices it has found. By default it never
scans again for new devices, apart from asking it explicitly during the
initialization of a control Node.

This is a simple example when starting the Communication Handler with
two *qbrobotics®* devices connected on two distinct USB ports:


```
[ INFO] [1524044523.511369300]: [CommunicationHandler] handles [/dev/ttyUSB1].
[ INFO] [1524044524.426984697]: [CommunicationHandler] handles [/dev/ttyUSB0].
[ INFO] [1524044525.218613760]: [CommunicationHandler] has found [2] devices connected:
[ INFO] [1524044525.218696997]:                        - device [1] connected through [/dev/ttyUSB0]
[ INFO] [1524044525.218736612]:                        - device [2] connected through [/dev/ttyUSB1]
```



When the Communication Handler is on, it provides all the Services
required to interact with the connected devices: e.g. *get info or
measurements, activate or deactivate motors, set commands*, and even
more\... A detailed description of the services can be found in the
[qb_device_driver](https://index.ros.org/p/qb_device_driver) package
wiki.

## Control

As shown in
[Details](#details) the
control Node exploits the
[ros_control](https://index.ros.org/p/ros_control) Controller Manager
which loads and runs the device controllers. Each controller provides an
Action Server that, together with the Hardware Interface structure,
allows the user to send commands to the relative device and get its
measurements.

From an API point of view, it is implemented an Action Client which
matches the relative trajectory controller and provides a method to send
Goals, i.e. command references, directly to the given device.
Additionally the Action Client is subscribed to a Topic
(`\*_controller/command`) that can be used to send reference commands
from outside the code, e.g. asynchronously from the command line, or
from a higher level control Node, e.g. as a result of a planning
algorithm.



```wiki
It is recommended not to mix these two control modes: choose either to control the device directly from the code by extending our API or through this command Topic.
```



Regardless the control mode chosen for the given application, and apart
form a customization of the API, the following launch file templates can
be used respectively to control several devices or a single one:

![overview_launch\|width=755](https://bitbucket.org/qbrobotics/qbhand-ros/raw/ddbccc369d6846549e9b03c9dce0c2dc6c1115e1/qb_hand_media/overview_launch.svg)
