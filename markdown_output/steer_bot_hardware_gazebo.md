An example of usage of this plugin can be seen in
[Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03), especially in
[cirkit_unit03_gazebo](cirkit_unit03_gazebo).

## About

This package provides 4-wheel car-like robot model with steer mechanism
for Gazebo simulation, by using \`gazebo_ros_control\` plugin.

\`steer_bot_hardware_gazebo::SteerBotHardwareGazebo\` inherits
\`gazebo_ros_control::RobotHWSim\` so that the plugin is integrated to
\`Gazebo\`.

We developed this plugins assuming that
[steer_drive_controller](steer_drive_controller) is selected as the
driving controller.

## Joint configuration of steer_bot_hardware_gazebo

### Review about steer_drive_controller

[steer_drive_controller](steer_drive_controller) is designed to have two
joint interfaces, one is velocity_joint_interface for the single rear
wheel joint and the other is position_joint_interface for the single
front steer joint. This concept keeps the controller\'s abstraction to
be applied in various types of configuration by converting the joint
interfaces in the controller to ones on an actual robot via \`RobotHW\`
or \`RobotHWSim\`.

### Converting cmd_vel command to Gazebo joint command

Now we need to do it for a Gazebo model too, which is the main role of
this plugin. The following figure shows how a velocity command of
\`geometry_msgs::Twist\` converted to a joint command to \`Gazebo\` via
[steer_drive_controller](steer_drive_controller).

![steerbot_steer_drive_controller_integrate_01\|width=\"700\"](attachment:steerbot_steer_drive_controller_integrate_01.png)

Each type of joint interface on
[steer_drive_controller](steer_drive_controller) is split into two
interface for right and left. This is because \`URDF\` doesn\'t support
closed links (e.g. parallel link or Ackermann link), which means we need
to virtually imitate such links by software.

### Registering joint interfaces in URDF model

In order to achieve the conversion mentioned above, you need to register
joint interfaces for both
[steer_drive_controller](steer_drive_controller) and \`Gazebo\` in
\`steer_bot_hardware_gazebo\`.

![register_joint_interfaces\|width=\"700\"](attachment:register_joint_interfaces.png)

For \`steer_drive_controller\`, it\'s simple to just register two joint
interface for a rear wheel and a front steer as mentioned previously.

For \`Gazebo\`, 4 more velocity joint interfaces for wheels and 2 more
position joint interface for front steers (in total 2 + 4 + 2 = 8 joint
interface are registered in this plugin).

-   The 2 rear wheel velocity joint interfaces are used as command
    interface for controlling linear drive on \`Gazebo\`.
-   The other 2 front wheel joints just grabs current angle to update
    joint_states, namely [tf](tf).
-   The front 2 steer joints virtually behave like parallel link or
    Ackermann link as you configure in a ROS parameter.

These joint interfaces are mapped with joints shown in the sub section
2.

![Registering joint \_nterfaces_in_URDF_model\|width=\"700\"](attachment:Registering joint _nterfaces_in_URDF_model.png)

An example of registering such joint interfaces can be seen in
[cirkit_unit03_gazebo](cirkit_unit03_gazebo).

## Usage

### URDF

In \`URDF\` in your robot, add the following tag to apply
[steer_bot_hardware_gazebo](steer_bot_hardware_gazebo).

```
<!-- Gazebo plugin for ROS Control -->
  <gazebo>
    <plugin name="gazebo_ros_control" filename="libgazebo_ros_control.so">
      <robotNamespace>/</robotNamespace>
      <robotSimType>steer_bot_hardware_gazebo/SteerBotHardwareGazebo</robotSimType>
    </plugin>
  </gazebo>
```

An example of a xacro is \`description.gazebo.xacro\` in
[steer_bot_hardware_gazebo](steer_bot_hardware_gazebo).

### Paremters

You need to register ROS parameter to apply the plugin to your original
robot.

#### Joint Parameters

```clearsilver
param{
  no_header=True
  0.name=rear_wheel
  0.type=string
  0.desc=The rear wheel joint name to receive a linear drive command from [[steer_drive_controller]].
  1.name=front_steer
  1.type=string
  1.desc=The front steer joint name to receive a angular drive command from [[steer_drive_controller]].
  2.name=virtual_rear_wheels
  2.type=string [2]
  2.desc=Virtual rear wheel joint names to send a velocity command to the correspondent wheel joints in `Gazebo`.
  3.name=virtual_front_wheels
  3.type=string [2]
  3.desc=Virtual front wheel joint names to grab current angle of the correspondent wheel joints in `Gazebo`.
  4.name=virtual_front_steers
  4.type=string [2]
  4.desc=Virtual front steer joint names to send a position command to the correspondent steer joints in `Gazebo`.
}
```

#### Virtual Ackermann link mechanism related parameters

```clearsilver
param{
  no_header=True
  0.name=enable_ackermann_link
  0.type=bool
  0.desc=If it is true, enable virtual ackerman link mechanism. Otherwise, paralell link mechanism is enabled.
  1.name=wheel_separation_w
  1.type=double
  1.desc=Wheel separation length between the left side and the right side, which is used for calculating steer angle of Ackermann link mechanism.
  2.name=wheel_separation_h
  2.type=double
  2.desc=Wheel separation length between the front side and the rear side, which is used for calculating steer angle of Ackermann link mechanism.
}
```

#### PID parameters to send velocity to the rear wheel joints in Gazebo

```
gains:
  base_to_right_rear_wheel  :  {p: 100000.0, d: 10.0, i: 0.50, i_clamp: 3.0}
  base_to_left_rear_wheel   :  {p: 100000.0, d: 10.0, i: 0.50, i_clamp: 3.0}
```

[cirkit_unit03_simulator](cirkit_unit03_simulator) has an example launch
file to spawn [Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03) with
[steer_bot_hardware_gazebo](steer_bot_hardware_gazebo) named
\`cirkit_unit03_world.launch\`.
