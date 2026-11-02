## What is PR2 Controller Manager?

### Hard realtime control loop

The `pr2_controller_manager` provides a
**[hard realtime](http://www.oit.uci.edu/dcslib/digital_unix/digital-v40d/APS33DTE/TITLE.HTM)**
loop to control the robot mechanism. The robot mechanism is represented
by a set of effort controlled joints (see
[pr2_mechanism_model](https://index.ros.org/p/pr2_mechanism_model) for
details). For the PR2 robot, we run the control loop at 1000 Hz. The
controller manager provides the infrastructure to load your own realtime
controller into its control loop. Every controller that is loaded into
the controller manager will get triggered once every mili-second. To
find out how to write your own hard realtime controller, take a look at
[this tutorial](https://index.ros.org/p/pr2_mechanism).

### Safety limits

The controller manager ensures that none of the loaded controllers can
command a joint past its
[safety limits](#safety_limits). If
necessary, the controller manager reduces the commanded joint effort, or
even applies an effort in the opposite direction. For more details, take
a look at the
[safety limits](#safety_limits)
page.

### Joint State Publishing

The controller manager publishes the state of all joints over ROS, as
[sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)
messages. These messages appear on the `joint_state` topic, at 100 Hz.
You can change this publishing frequency by setting the
`joint_state_publish_rate` parameter.

### Tools for running controllers

![width="400px"](doc/controller_state.png)

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

## safety_limits

### Joint Safety Limits Explained

The effort limit is an attribute of the limit tag. In this case, a
controller cannot command an effort of more than 30 N (N-m for revolute)
nor less than -30 N (N-m for revolute) on the joint. If the controller
tries to command an effort beyond the effort limit, the magnitude of the
effort is truncated.

The velocity limit specifies the bounds on the magnitude of the joint
velocity (m/s for prismatic, rad/s for revolute). The velocity limit is
enforced by bounding the commanded effort such that no effort can be
applied to push the joint beyond the velocity limit, and a damping
effort is applied if the joint is moving at a velocity beyond the limit.
The k_velocity term determines the scale of the effort bound.

For a velocity v, a velocity limit of v\^+\^ and a k_velocity of k,,v,,
the upper bound on effort is -k,,v,, \* (v - v\^+\^)
![attachment:k_velocity.png](doc/k_velocity.png)

The safety_length_min and safety_length_max determine the locations of
the software joint limits (the "soft" limits). The upper soft limit is
the upper hardware limit minus the safety_length_max and the lower soft
limit is the lower hardware limit plus safety_length_min. When the joint
is near the soft limits, the possible velocities are bounded to keep the
position from crossing the soft limits. The k_position term determines
the scale of the bound on velocity.

For position x, soft upper limit x\^+\^ and a k_position of k,,x,, the
upper bound on velocity is -k,,x,,\*(x - x\^+\^), see figures below:
![attachment:k_position.png](doc/k_position.png)

These bounds on velocity are taken into account when determining the
bounds on effort.

## Troubleshooting

Many things can cause problems when interacting with controllers. Always
**check the PR2 dashboard** first, every failure should print one or
more error messages that give very useful information about the problem.

### Understanding error messages

- **A controller named xxx was already loaded inside the controller
  manager** You are trying to load a controller with a name that matches
  one of the controllers already loaded inside the controller manager.
  This is not allowed since every controller needs to have a unique
  name. To get a list of all controllers that are loaded, type:
  

```
$ rosrun pr2_controller_manager pr2_controller_manager list
```



<!-- -->

- **Could not load controller xxx because the type was not specified.
  Did you load the controller configuration on the parameter server?**
  In order to spawn a controller, you need to load the controller
  configuration on the parameter server first. One of these parameters
  is the controller type. This parameter should be specified as
  parameter 'xxx/type'. However, you did not specify this parameter on
  the parameter server. For information on how to load this parameter on
  the parameter server, take a look at the instructions for spawning a
  controller.

<!-- -->

- **Could not spawn controller xxx because controller type yyy does not
  exist** or **Could not load class yyy** The controller manager does
  not know about a controller type named 'yyy'. To list the controller
  types known to the controller manager, type: 

```
$ rosrun pr2_controller_manager pr2_controller_manager list-types
```



<!-- -->

- **Initializing controller xxx failed** The controller manager tried to
  initialize the controller, but the controller itself returned an
  error. Check the controller specific documentation to find out how to
  solve this problem.

<!-- -->

- **Scheduling controller xxx failed** When two controllers directly
  communicate with each other, one controller will depend on the other
  to function. This type of dependencies specify the order in which
  controllers are executed. However, when e.g. a circular dependency
  exists between controllers, the scheduling of the execution order will
  fail. To fix this problem, read the controller specific documentation
  to find out which controllers depend on which controllers.

<!-- -->

- **Cannot unload controller xxx because controller yyy still depends on
  it** When two controllers directly communicate with each other, one
  controller will depend on the other to function. This type of
  dependencies specify the order in which controllers are executed. When
  controller yyy depends on controller xxx, it is not possible to unload
  controller xxx. First unload controller yyy, and then unload
  controller xxx.

<!-- -->

- **Could not unload/start/stop controller with name xxx because no
  controller with this name exists** You tried to unload/start/stop a
  controller that is not loaded inside the controller manager. To get a
  list of all controllers that are loaded, type:
  

```
$ rosrun pr2_controller_manager pr2_controller_manager list
```



<!-- -->

- **Could not unload controller with name xxx because it is still
  running** A controller can only be unloaded when it is in a stopped
  state. To unload a running controller, first stop it.

### NaN Values in Joint States

If `pr2_controller_manager` ever calculates a NaN or Inf value for a
joint state\--position, velocity, effort, etc\--then
pr2_controller_manager will be unable to control the mechanism. A
restart of pr2_controller_manager is the only way to revert this
condition.

This condition usually means there is a serious hardware or software
problem, and should be reported immediately.
