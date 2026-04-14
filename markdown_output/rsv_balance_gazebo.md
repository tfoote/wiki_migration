## Description

This package provides all the necessary URDF model extensions, worlds
and launch files for successfully simulating RoboSavvy\'s self-balance
platform.

On `rsv_balance_gazebo` package we have available 3 worlds: 1.
`empty.world` - Empty world with only the robot.
```
roslaunch rsv_balance_gazebo simulation_empty.launch
``` 2. `ramp.world` - Robot on inclined, flat
terrain. ```
roslaunch rsv_balance_gazebo simulation_ramp.launch
``` 3. `terrain.world` - Robot on bumpy
terrain. ```
roslaunch rsv_balance_gazebo simulation_terrain.launch
```

As you can understand from the spawned robot, the demo model includes a
dummy, spherical, 5kg load at about 1m height from the center of the
platform.

![\|width=100%](attachment:simulation_tutorial1.png)

It also provides RVIZ configured launchfile: ```
roslaunch rsv_balance_gazebo view.launch
```

## Gazebo plugin node

The Gazebo model plugin was developed to expose the same ROS interface
of topics and services as the real platform.

```clearsilver
name=libgazebo_rsv_balance.so
desc=Gazebo plugin for RoboSavvy's self-balance platform
pub {
  0.name = /odom
  0.type = nav_msgs/Odometry
  0.desc = Publishes vehicle odometry
  1.name = /state
  1.type = rsv_balance_msgs/State
  1.desc = Publishes self-balance control state
  2.name = /joint_states
  2.type = sensor_msgs/JointState
  2.desc = Outputs wheel joint states if desired.
  3.name = /tf
  3.type = tf2_msgs/TFMessage
  3.desc = Outputs odom and wheel transforms if desired
}
sub {
  0.name = /cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Velocity command input for differential drive type vehicle.
  1.name = /tilt_equilibrium
  1.type = std_msgs/Float64
  1.desc = Equilibrium point for the current state of the vehicle
}
srv_called {
  0.name = /set_mode
  0.type = rsv_balance_msgs/SetMode
  0.desc = Service to set platform's operation mode.
  1.name = /set_input
  1.type = rsv_balance_msgs/SetInput
  1.desc = Service to set which input commands the vehicle. Not used in simulation.
  2.name = /reset_odom
  2.type = std_srvs/Empty
  2.desc = Service to reset odometry.
  3.name = /reset_override
  3.type = std_srvs/Empty
  3.desc = Service to disable RC override. Not used in simulation.
}
}
```

### Plugin parameters

Example configuration to include in your URDF model.

```xml
<plugin name="rsv_balance_controller" filename="libgazebo_rsv_balance.so">
  <rosDebugLevel>Debug</rosDebugLevel>
  <!--<robotNamespace></robotNamespace>-->
  <commandTopic>cmd_vel</commandTopic>
  <baseFrameId>base_link</baseFrameId>
  <publishOdomTF>true</publishOdomTF>
  <odomFrameId>odom</odomFrameId>
  <odomSource>world</odomSource>
  <odomTopic>odom</odomTopic>
  <publishWheelJointState>true</publishWheelJointState>
  <!-- Platform specific configurations -->
  <startMode>balance</startMode>
  <publishState>true</publishState>
  <publishStateRate>1</publishStateRate>
  <publishDiagnosticsRate>1</publishDiagnosticsRate>
  <wheelSeparation>${base_width+2.*wheel_width/2.}</wheelSeparation>
  <wheelRadius>${wheel_radius}</wheelRadius>
  <leftJoint>base_to_left_wheel</leftJoint>
  <rightJoint>base_to_right_wheel</rightJoint>   
  <!-- Control specific configurations -->
  <updateRate>100</updateRate>
</plugin>
```

```clearsilver
param {
  0.name = robotNamespace
  0.type = str
  0.desc = Robot's namespace
  0.default = ""
  1.name = commandTopic
  1.type = str
  1.desc = Name for the velocity command topic
  1.default = "cmd_vel"
  2.name = publishOdomTF
  2.type = bool
  2.desc = Does the node publish odom tf?
  2.default = false
  3.name = baseFrameId
  3.type = str
  3.desc = Base frame ID.
  3.default = "base_link"
  4.name = odomFrameId
  4.type = str
  4.desc = Odometry frame ID.
  4.default = "odom"
  5.name = odomSource
  5.type = str
  5.desc = Odometry source. Odometry is computed from ''encoders'' or taken directly from ''world''.
  5.default = "world"
  6.name = odomTopic
  6.type = str
  6.desc = Name for the odometry topic
  6.default = "odom"
  7.name = publishWheelJointState
  7.type = bool
  7.desc = Does the node publish wheel joint state?
  7.default = false
  8.name = startMode
  8.type = str
  8.desc = Starting operation mode. 
  8.default = "balance"
  9.name = publishState
  9.type = bool
  9.desc = Does the node publish self-balance control state?
  9.default = false
  10.name = publishStateRate
  10.type = int
  10.desc = Rate for publishing self-balance control state.
  10.default = 1
  11.name = updateRate
  11.type = int
  11.desc = Rate for self-balance control loop.
  11.default = 50
}
```
