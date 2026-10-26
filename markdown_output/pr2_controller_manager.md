## What is PR2 Controller Manager?

### Hard realtime control loop

The `pr2_controller_manager` provides a
**[hard realtime](http://www.oit.uci.edu/dcslib/digital_unix/digital-v40d/APS33DTE/TITLE.HTM)**
loop to control the robot mechanism. The robot mechanism is represented
by a set of effort controlled joints (see
[pr2_mechanism_model](pr2_mechanism_model) for details). For the PR2
robot, we run the control loop at 1000 Hz. The controller manager
provides the infrastructure to load your own realtime controller into
its control loop. Every controller that is loaded into the controller
manager will get triggered once every mili-second. To find out how to
write your own hard realtime controller, take a look at
[this tutorial](pr2_mechanism/Tutorials/Writing a realtime joint controller).

### Safety limits

The controller manager ensures that none of the loaded controllers can
command a joint past its
[safety limits](pr2_controller_manager/safety_limits). If necessary, the
controller manager reduces the commanded joint effort, or even applies
an effort in the opposite direction. For more details, take a look at
the [safety limits](pr2_controller_manager/safety_limits) page.

### Joint State Publishing

The controller manager publishes the state of all joints over ROS, as
[sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)
messages. These messages appear on the `joint_state` topic, at 100 Hz.
You can change this publishing frequency by setting the
`joint_state_publish_rate` parameter.

### Tools for running controllers

![\|width="400px"](attachment:controller state.png)

The controller manager provides the infrastructure to interact with
controllers. Depending on if you're running controllers form a launch
file, from the command line or from a ROS node, the controller manager
provides different tools to run controllers.

## Command-line tools

### pr2_controller_manager

To interact with controllers from the command line, use the
`pr2_controller_manager` tool. To interact with a specific controller,
use:



```
$ rosrun pr2_controller_manager pr2_controller_manager <command> <controller_name>
```

 The following commands are available:

- `load`: load a controller (construct and initialize)
- `unload`: unload a controller (destruct)
- `start`: start a controller
- `stop`: stop a controller
- `spawn`: load and start a controller
- `kill`: stop and unload a controller

To get the state of the controllers, use:



```
$ rosrun pr2_controller_manager pr2_controller_manager <command>
```

 The following commands are available:

- `list`: list all the controllers in the order they are executed, and
  give the state of each controller
- `list-types`: list all the controller types the controller manager
  knows about. If your controller is not in this list, you won't be
  able to spawn it.
- `list-joints`: lists all the joint and actuator names that are used
  by the controller manager.
- `reload-libraries`: Reloads all the controller libraries that are
  available as plugins. This is convenient when you are developing a
  controller and you want to test your new controller code, without
  restarting the robot every time. This does not restart controllers
  which were running before.
- `reload-libraries \--restore`: Reloads all the controller libraries
  that are available as plugins and restores all controllers to their
  original state.

### spawner

To automatically load and start a set of controllers at once, and
automatically stop and unload those same controllers at once, use the
`spawner` tool: 

```
$ rosrun pr2_controller_manager spawner [--stopped] name1 name2 name3
```

 When you run spawner, the
listed controllers will get loaded and started (unless you specify
\--stopped). Spawner will keep running while the controllers are up.
When you kill spawner (ctrl-c) it will automatically stop and unload all
controllers it initially started.

### unspawner

To automatically stop a set of controllers, and restart them later, you
can use the `unspawner` tool: 

```
$ rosrun pr2_controller_manager unspawner name1 name2 name3
```

 The listed
controllers will be *stopped*, but not unloaded. Once spawner is shut
down, the controllers will be restarted.

## Creating launch files

You could run `pr2_controller_manager` to start controllers from
within a launch file. However, the controller would then stay up even
after the launch file is taken down. Instead, use the `spawner `tool
to automatically load, start, stop and unload a controller from within a
launch file. When you start `spawner`, it will load and start the
controller. When you stop `spawner` (when the launch file is taken
down) it will stop and unload the controller. Your launch file would
look something like this:



```
<launch>
   <node pkg="pr2_controller_manager" 
         type="spawner" 
         args="controller_name1 controller_name2" />
 </launch>
```



or, if you just want to load the controller, but not start it yet:


```
<launch>
   <node pkg="pr2_controller_manager" 
         type="spawner" 
         args="--stopped controller_name1 controller_name2" />
 </launch>
```



## ROS API

To interact with controllers form another ROS node, the controller
manager provides five service calls:



```clearsilver
node.0 {
  name = pr2_controller_manager
  pub {
    0.name = joint_states
    0.type = sensor_msgs/JointState
    0.desc = the measured position, velocity and effort of each joint
    1.name = mechanism_statistics
    1.type = pr2_mechanism_msgs/MechanismStatistics
    1.desc = this message contains statistics about the joints, the controllers and the actuators.
  }
  srv {
    0.name = pr2_controller_manager/load_controller
    0.type = pr2_mechanism_msgs/LoadController
    0.desc = the service request contains the name of the controller to load, and the response contains a boolean indicating success or failure.
    1.name = pr2_controller_manager/unload_controller
    1.type = pr2_mechanism_msgs/UnloadController
    1.desc = the service request contains the name of the controller to unload, and the response contains a boolean indicating success or failure. A controller can only be unloaded when it is in the stopped state.
    2.name = pr2_controller_manager/switch_controller
    2.type = pr2_mechanism_msgs/SwitchController
    2.desc = the service request contains a list of controller names to start, a list of controller names to stop and an int to indicate the strictness (`BEST_EFFORT` or `STRICT`). `STRICT` means that switching will fail if anything goes wrong (an invalid controller name, a controller that failed to start, etc. ). `BEST_EFFORT` means that even when something goes wrong with on controller, the service will still try to start/stop the remaining controllers. The service response contains a boolean indicating success or failure.  The list of controllers to stop or start can be an empty list, if you are only stopping or only starting controllers.
    3.name = pr2_controller_manager/list_controllers
    3.type = pr2_mechanism_msgs/ListControllers
    3.desc = the service returns all the controller names that are loaded in pr2_controller_manager at that time. Also, the service returns the state of each controller: running or stopped.
    4.name = pr2_controller_manager/list_controller_types
    4.type = pr2_mechanism_msgs/ListControllerTypes
    4.desc = the service returns all the controller types that are known to pr2_controller_manager. Only the controller types that are known can be constructed. To let pr2_controller_manager know about your own controller type, use the [[pluginlib]] as explained in [[pr2_mechanism/Tutorials/Writing a realtime joint controller|this tutorial]].
    5.name = pr2_controller_manager/reload_controller_libraries
    5.type = pr2_mechanism_msgs/ReloadControllerLibraries
    5.desc = the service reloads all the controller libraries that are available as plugins. This is convenient when you are developing a controller, and you want to test your new controller code without restarting the robot every time. This service only works when there are NO controller loaded. 
  }
  param {
    0.name = pr2_controller_manager/joint_state_publish_rate
    0.type = double
    0.desc = the publish frequency of messages on the joint_states topic
    0.default = 100.0
    1.name = pr2_controller_manager/mechanism_statistics_publish_rate
    1.type = double
    1.desc = the publish frequency of messages on the mechanism_statistics topic
    1.default = 1.0

  }
}
```


