# Documentation

/!\\ **UNDER CONSTRUCTION** /!\\

## Introduction

**vrep_ros_bridge** is a plugin for V-Rep developed by the Inria
[Lagadic](http://team.inria.fr/lagadic) team located at
[Rennes](http://www.inria.fr/rennes).

Our objective is to create a simulation environment in order to test and
debug our algorithms on the simulated robots. We decided to use V-Rep as
3D simulator and ROS for the communication and its useful tools.

The main application of the plugin is to provide a communication
interface between V-Rep and ROS. The aim is to control the V-Rep
simulation externally using ROS messages and ROS services.

**V-Rep**, developed by
[Coppelia Robotics](http://www.coppeliarobotics.com/), is an open-source
state-of-the-art (and freely available for academic use) 3D physical
simulation engine which is becoming more and more widespread in the
robotics community thanks to its flexibility (possibility to simulate
many different robotic platforms), dynamical engine (it supports ODE,
Bullet and Vortex), and finally customizability (it offers many
different possibilities to include one's own code or to interface it
with the external world).

## Description

This plugin is a shared library that is automatically loaded by V-REP's
main client application at program start-up. Our plugin looks for known
objects in the scene in order to manage them. It creates ROS publishers
to send out simulation data (for example pose and velocity of objects
present in the scene), it receives (ROS subscribers) messages and it
dynamically applies the commands to the object.

Note that vrep_ros_bridge is a meta-package, while vrep_ros_plugin is
the real main package.

ROS V-Rep Bridge uses the [pluginlib](pluginlib) package. Pluginlib is a
C++ library for loading and unloading plugins from within a ROS package.
Plugins are dynamically loadable classes that are loaded from a runtime
library (i.e. shared object, dynamically linked library). In this way
our handlers are actually plugins with some dependencies. If we don't
need a handler or we don't have installed its dependencies we are still
able to build our bridge (that plugin will not be available). For
example, the [quadrotor_tk_handler](quadrotor_tk_handler) needs
[Telekyb](telekyb). If we don't want to install Telekyb we can just add
a file called CATKIN_IGNORE in the quadrotor_tk_handler folder and it
will not be considered. In spite of this the other handlers will be
available.

![alt text\|width=300](attachment:test.png)

This is the list of the objects supported by the plugin:

-   Robots:
-   Manipulators and mobile robots
    ([manipulator_handler](manipulator_handler))
-   Quadrotors ([quadrotor_handler](quadrotor_handler))
-   Sensors:
-   Vision sensor ([camera_handler](camera_handler))
-   IMU sensor ([imu_handler](imu_handler))

and this is the list of the handlers to control and describe the
simulation:

-   Rigid body handler: ([rigid_body_handler](rigid_body_handler))
-   Pose:
-   Set pose
-   Get pose
-   Twist:
-   Set Twist
-   Get Twist

The next section show how to link the plugin with an object in V-REP.

### Handlers

We have an object in the scene (let's say a quadrotor) and we want that
the plugin [vrep_ros_bridge](vrep_ros_bridge) manage it. To do it we
will have to tag the object with a predefined string. If we don't do it
the plugin will not act on the object. We will show how to tag a
quadrotor but the procedure for the other objects will be similar.

Procedure:

-   Right Click on the object you want to add the custom data (on the
    'Scene hierarchy' (on the right) or directly on the scene)
-   Click on 'Add \--> Associated child script \--> Non threated'
-   The general structure of the child script (written in
    [LUA](http://www.lua.org/)) is: ```
if (simGetScriptExecutionCount()==0) then
-- Put your Initialization code, executed only once (at the beginning of the simulation)
end

simHandleChildScript(sim_handle_all_except_explicit)

-- Put your main code here. It will act at each iteration of the simulation.

if (simGetSimulationState()==sim_simulation_advancing_lastbeforestop) then
-- Put some restoration code here
end
```
-   Now we have to add some instructions: ```
quadrotor = simGetObjectAssociatedWithScript(sim_handle_self)
simExtSetFloatCustomDataFromHeader(quadrotor, sim_ext_ros_bridge_quadrotor_data_main, 0.0)
```
    withing the initialization code.

The function 'simExtSetFloatCustomDataFromHeader()' adds a custom data
to the object related to 'sim_ext_ros_bridge_set_obj_twist_data_main'.
As we can see, the function requires a third input. If requested, we can
add a value to our custom data, setting the third input of the function.
In our case, since we don't want to use this additional parameter we
set it to zero (it will be ignored). We can add float and int values. If
you want to add an int value you have to use the function
'simExtSetIntCustomDataFromHeader()'. You can find the list of the
Custom Lua Variables in the description of each handler. Moreover you
will find the complete list in the file
[access.cpp](https://github.com/lagadic/vrep_ros_bridge/blob/master/vrep_ros_plugin/src/access.cpp)
(From line 149). In certain case the third values will be important (for
instance to set the frequency of the camera acquisition). You will find
more information about these commands in each wiki.ros page dedicated to
the packages.

## Installation

You will find a guide for the installation in the
[Github repository](https://github.com/lagadic/vrep_ros_bridge).

### Installation test

If you have completed the previous installation guide without get any
error, we can run V-REP and check if everything is working as expected.

-   Type roscore in a terminal
-   Now run V-Rep via terminal. In the terminal you should see:

```
Add-on script 'vrepAddOnScript-addOnScriptDemo.lua' was loaded.
 Simulator launched.
 (...)
 Plugin 'RosBridge': loading...
 Plugin 'RosBridge': load succeeded.
 (...)
```

-   If an external console will appear with the available plugins the
    plugin is working:
    ![text describing image](attachment:Externalconsole.png)

```{=html}
<!-- -->
```
-   Now we can test the working of the plugin opening a scene with some
    object that it can manage.

```{=html}
<!-- -->
```
-   Open in V-REP the scene called
    "vrep_ros_bridge/SceneVrep/Test.ttt". You will see a quadrotor and
    a six dof manipulator (Viper 850).
-   Run the simulation
-   The external console will show the object found in the scene:

![text describing image](attachment:ExtCnsTest.png)

-   In order to see the ROS computation graph, run in a terminal:
    ```
rqt_graph
```

```{=html}
<!-- -->
```
-   Open a terminal and digit: ```
rostopic list
``` These are the
    topics that the plugin created. In this case you should see:

```
/command/quadrotor_0
 /rosout
 /rosout_agg
 /tf
 /vrep/IMU/quadrotor_0
 /vrep/Vision_sensor_0
 /vrep/Vision_sensor_0/Camerainfo
 /vrep/Vision_sensor_0/compressed
 /vrep/Vision_sensor_0/compressed/parameter_descriptions
 /vrep/Vision_sensor_0/compressed/parameter_updates
 /vrep/Vision_sensor_0/compressedDepth
 /vrep/Vision_sensor_0/compressedDepth/parameter_descriptions
 /vrep/Vision_sensor_0/compressedDepth/parameter_updates
 /vrep/Vision_sensor_0/theora
 /vrep/Vision_sensor_0/theora/parameter_descriptions
 /vrep/Vision_sensor_0/theora/parameter_updates
 /vrep/base/pose
 /vrep/camera_info
 /vrep/end_eff/pose
 /vrep/info
 /vrep/pose/quadrotor_0
 /vrep/twist/quadrotor_0
 /vrep/viper_0/jointCommand
 /vrep/viper_0/jointStatus
```

## Demo

### Control of Robots in V-REP via Matlab/Simulink and ROS

[Youtube](https://www.youtube.com/watch?v=SZxp6BJgBUg)

You can find info about this demo
[here](http://www.irisa.fr/lagadic/demo/demo-vrep/demo-vrep.html).
