## Description

This code is for those working with the Rover Robotics OpenRover. The
OpenRover communicates via UART, this package abstracts away the UART
communications and allows users to quickly get their robots moving
around and doing cool things! We recommend using an FTDI cable which
will convert the UART to USB for communicating with a computer.

![\|width=\"600px\"](attachment:rover_robotics_all_robots_1080_2.png)

## Running the example

```
roslaunch rr_openrover_driver example.launch
```

## Reading Battery State of Charge

```
rostopic echo /rr_openrover_driver/r_slow_rate_data/reg_robot_rel_soc_a
rostopic echo /rr_openrover_driver/r_slow_rate_data/reg_robot_rel_soc_b
```

## Sending Motors Commands

```
managed_pub = rospy.Publisher('/cmd_vel/managed', TwistStamped, queue_size=1)
managed_control_input.header.stamp = rospy.Time.now()
managed_control_input.header.frame_id = 'none'
managed_control_input.twist.linear.x=0.0
managed_control_input.twist.angular.y=0.0
managed_control_input.twist.angular.z=0.5
managed_pub.publish(managed_control_input)
```

### Fusing Encoders with other sensors

We recommend using the robot_localization to fuse

## Nodes

```clearsilver
node.0{
  name = openrover_driver_node
  desc = This package serves as a ROS driver for a Rover Robotics OpenRover driver which communicates via UART to a host PC running ROS. This package assumes users are using an FTDI cable.
}
sub {
0{
name= /cmd_vel/managed
type= geometry_msgs/Twist
desc= A topic that controls the linear (m/s) and angular (rad/s) velocity of the robot. cmd_vel/managed should come from a package that can manage multiple sources of control (local joystick, remote keyboard, move_base, etc...) like rr_control_manager. If only one source of input is need then this can be remapped to cmd_vel.
}
1{
name= /rr_openrover_driver/fan_speed
type= std_msgs/Int32
desc= Controls the fan speed. It will override the fan speed set in the firmware. Use caution when setting fan speed manually, not having enough fan on time can burn out the motors or over heat the electronics. 
}
2{
name= /rr_openrover_driver/soft_estop/enable
type= std_msgs/Bool
desc= When set True the driver will ignore all input commands until the True message is received on the /rr_openrover_driver/soft_estop/reset topic (even if False is published to this topic). This is very useful to map to a button on a controller. If activated while using the ROS nav stack it acts like a pause button and autonomy can easily be resumed if the estop is reset before your navigation stack timeouts kick in.
}
3{
name= /rr_openrover_driver/soft_estop/reset
type= std_msgs/Bool
desc= Used to reset the soft_estop. This is also useful to map to a button on a controller
}
}
param {
0{
name= ~use_legacy
default=`false`
type= bool
desc= Publish the deprecated state messages raw_fast_rate_data, raw_med_rate_data, and raw_slow_rate_data when set to true.
}
1{
name= ~port
default=`"/dev/ttyUSB0"`
type= string
desc= The port used for UART communication. It is recommended to use an FTDI cable to communicate with the robot. When the FTDI cable is plugged into a linux system it will enumerate as /dev/ttyUSBx, where x is the lowest number not currently in use. This means that if the robot gets uplugged and replugged in this value may change. It is recommended to setup a udev rule for the robot that will always name it something like /dev/rover and to set this parameter to the same thing so that if it gets unplugged and replugged in things will work still.
}
2{
name= ~fast_data_rate
default=`10`
type= int
desc= Rate at which the computer polls the robot for data categorized as fast 
}
3{
name= ~med_data_rate
default=`2`
type= int
desc= Rate at which the computer polls the robot for data categorized as med
}
4{
name= ~slow_data_rate
default=`1`
type= int
desc= Rate at which the computer polls the robot for data categorized as slow
}
5{
name= ~closed_loop_control_on
default = 'False'
type= Bool
desc= Turns on a PID controller to match wheel speeds to commanded values
}
6{
name= ~timeout
default=`0.5`
type= float
desc= If ''enable_timeout'' is set to true ''timeout'' is the amount of time in seconds the driver will wait for data to be published to /cmd_vel/managed before stopping the robot.
}
7{
name= ~total_weight
default=`20.0`
type= float
desc= (Effects accuracy of /rr_openrover_driver/odom_encoder). The total weight of the robot in pounds. 
}
8{
name= ~drive_type
default=`"4wd"`
type= string
desc= (Effects accuracy of /rr_openrover_driver/odom_encoder) Sets the robot's wheel configuration. The three options are flippers, 4wd, and 2wd. This param is important to set properly for the odom to be reported properly.
}
9{
name= ~kp
default=`40`
type= int
desc= proportional gain of PID controller
}
10{
name= ~ki
default=`100`
type= int
desc= integral gain of PID controller
}
11{
name= ~kd
default=`0`
type= int
desc= derivative gain of PID controller
}
12{
name= ~traction_factor
default=`depends on drive type chosen`
type= float
desc= (Effects accuracy of /rr_openrover_driver/odom_encoder). This helps the odometry from encoders be more accurate when using a 4WD of flipper robot. The wheels slip a certain amount, this parameter can be adjusted between 0 and 1 to account for the slippage. Default for 2WD is 0.9877, default for 4WD is 0.610, default for flippers is 0.98. 
}
13{
name= ~odom_covariance_0
default=`0.01`
type= float
desc= The driving straight covariance for the encoder odometry
}
14{
name= ~odom_covariance_35
default=`0.03`
type= float
desc= The turning covariance for the encoder odometry
}
}
pub {
0{
name= /rr_openrover_driver/odom_encoder
type= nav_msgs/Odometry
desc= Encoder-based odometry publishing at 10Hz.
}
1{
name= /rr_openrover_driver/raw_fast_rate_data
type= custom
desc= (DEPRECATED) custom message at 30Hz that contains the encoder values for the following: header, left_motor, right_motor, flipper_motor.
}
2{
name= /rr_openrover_driver/raw_med_rate_data
type= custom
desc= (DEPRECATED) custom message at 2Hz that contains the following data: header, reg_pwr_total_current, reg_motor_fb_rpm_left, reg_motor_fb_right, reg_flipper_fb_position_pot1, reg_flipper_fb_position_pot2, reg_motor_fb_current_left, reg_motor_fb_current_right, reg_motor_charger_state, reg_power_a_current, reg_power_b_current, reg_motor_flipper_angle.
}
3{
name= /rr_openrover_driver/raw_slow_rate_data
type= custom
desc= (DEPRECATED) 1Hz custom message that contains the following data: header, reg_motor_fault_flag_left, reg_motor_temp_left, reg_motor_temp_right, reg_power_bat_voltage_a, reg_power_bat_voltage_b, reg_robot_rel_soc_a, reg_robot_rel_soc_b, buildno.
}
4{
name= /rr_openrover_driver/battery_status_a
type= custom
desc= Status message of Cell A
}
5{
name= /rr_openrover_driver/battery_status_b
type= custom
desc= Status message of Cell B
}
}
1{
name = openrover_diagnostics_node
desc = This node publishes OpenRover data to InOrbit.
sub {
0{
name= /rr_openrover_driver/raw_med_rate_data
type= custom
desc= custom message at 2Hz that contains the following data: header, reg_pwr_total_current, reg_motor_fb_rpm_left, reg_motor_fb_right, reg_flipper_fb_position_pot1, reg_flipper_fb_position_pot2, reg_motor_fb_current_left, reg_motor_fb_current_right, reg_motor_charger_state, reg_power_a_current, reg_power_b_current, reg_motor_flipper_angle.
}
1{name= /raw_slow_rate_data
type= custom
desc= 1Hz custom message that contains the following data: header, reg_motor_fault_flag_left, reg_motor_temp_left, reg_motor_temp_right, reg_power_bat_voltage_a, reg_power_bat_voltage_b, reg_robot_rel_soc_a, reg_robot_rel_soc_b, buildno.
}
2{
name= /rr_openrover_driver/battery_status_a
type= custom
desc= Custom message that contains the following data: header, over_charged_alarm, terminate_charge_alarm, over_temp_alarm, terminate_discharge_alarm, remaining_capacity_alarm, remaining_time_alarm, initialized, discharging, fully_charged, fully_discharged
}
3{
name= /rr_openrover_driver/battery_status_b
type= custom
desc= Custom message that contains the following data: header, over_charged_alarm, terminate_charge_alarm, over_temp_alarm, terminate_discharge_alarm, remaining_capacity_alarm, remaining_time_alarm, initialized, discharging, fully_charged, fully_discharged
}
4{
name= /rr_openrover_driver/charging
type= bool
desc= Charging status of the open rover.
}
}
pub {
0{
name= /inorbit/custom_data/0
type= string
desc= Connects to the InOrbit server to push openrover_driver data.
}
}
```

## Running

Example using rosrun

```
rosrun rr_openrover_driver openrover_driver_node
``` Example launch file

```
<launch>
    <arg name="openrover_node_name" default="rr_openrover_driver"/>

    <!-- OpenRover Driver -->
    <node pkg="rr_openrover_driver" type="openrover_driver_node" name="$(arg openrover_node_name)" respawn="false" output="screen">
        <param name="port" value="/dev/rover" />
        <param name="drive_type" value="4wd" />
        <param name="enable_timeout" type="bool" value="true"/>
        <param name="timeout" type="double" value="0.3"/>
        <param name="total_weight" type="double" value="20.41"/>
        <param name="traction_factor" value="0.610"/>
        <param name="odom_covariance_0" value="0.01"/>
        <param name="odom_covariance_35" value="0.03"/>
    </node>

    <!-- OpenRover Diagnostics -->
    <node pkg="rr_openrover_driver" type="diagnostics.py" name="rr_openrover_diagnostics_node">
        <remap from="/raw_slow_rate_data" to="/$(arg openrover_node_name)/raw_slow_rate_data"/>
    </node>
</launch>slow_rate_pub
```

## Release Notes

This package is currently in pre-release meaning the code has been
tested and is functional, but backwards compatibility is not guaranteed
until v1.0.0, so make note of which version you are using and read the
changelog carefully before updating.
