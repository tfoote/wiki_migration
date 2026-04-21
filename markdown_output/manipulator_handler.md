## Manipulator

The manipulator handler looks for a manipulator tag and it finds all its
joints. After it creates a ROS publisher of
[sensor_msgs/JointState](http://docs.ros.org/api/sensor_msgs/html/msg/JointState.html)
messages:

-   the position of the joints
-   the velocity of the joints
-   the effort that is applied in the joints

In addition it gives us the possibility to control the joints using
commands from ROS in several ways (see
[here](http://www.coppeliarobotics.com/helpFiles/index.html) for more
details):

-   In position (passive mode, no dynamic simulation: the links will be
    static) 

```
sim_ext_ros_bridge_manipulator_ctrl_mode_Passive_mode
```


-   In motion mode (DEPRECATED, not working from V-REP V3.2.2. Please
    use the mode in velocity instead) 

```
sim_ext_ros_bridge_manipulator_ctrl_mode_MOT_velocity
```


-   In velocity (passive mode, no dynamic simulation: the links will be
    static) 

```
sim_ext_ros_bridge_manipulator_ctrl_mode_Passive_mode_velocity
```


-   In torque/force mode (the links will be dynamically simulated, see
    [here](http://www.coppeliarobotics.com/helpFiles/en/designingDynamicSimulations.htm)):
-   Position (PID controller) 

```
sim_ext_ros_bridge_manipulator_ctrl_mode_TF_position
```


-   Velocity 

```
sim_ext_ros_bridge_manipulator_ctrl_mode_TF_velocity
```


-   Force and torque 

```
sim_ext_ros_bridge_manipulator_ctrl_mode_TF_effort
```



You can use the function "simExtSetFloatCustomDataFromHeader()" to set
the control mode you prefer.

-   If you will not set anything the joint will be in controlled in the
    mode "position (fixed joint)" as default.
-   If you set in the child script of the root of the manipulator a
    given control mode, all the joints will be controlled in that way.
-   In addition if you want to control some joints in a different way
    with respect the general mode you have defined, you can do it. Just
    add a child script to the joint and use the function
    "simExtSetFloatCustomDataFromHeader()" to set the control mode you
    prefer.

In the folder *vrep_ros_brigde/SceneVrep* you will find the model of a
manipulator with the joints controlled in velocity:
*ManipulatorViper.ttt*.
