## Description

ROS package that will automatically dock and undock Rover Robotics
rovers. The node use a front mounted camera to detect a specified Aruco
Marker, center itself, and proceed towards the dock.

[Youtube](https://www.youtube.com/watch?v=ZsJTrespOgE)

## Running auto dock

To run the auto-docking code add the below line to your launch file.


```
<node pkg="aruco_detect" name="aruco_detect" type="aruco_detect" output="screen" respawn="false">
      <param name="image_transport" value="$(arg transport)"/>
      <param name="publish_images" value="true" />
      <param name="fiducial_len" value="$(arg fiducial_len)"/>
      <param name="dictionary" value="$(arg dictionary)"/>
      <param name="do_pose_estimation" value="$(arg do_pose_estimation)"/>
      <param name="ignore_fiducials" value="$(arg ignore_fiducials)"/>
      <param name="fiducial_len_override" value="$(arg fiducial_len_override)"/>
      <remap from="/camera/compressed"
          to="$(arg camera)/$(arg image)/$(arg transport)"/>
      <remap from="/camera_info" to="/camera/color/camera_info"/>
    </node>

    <node pkg="rr_auto_dock" type="auto_dock.py" name="auto_dock_node">
      <param name="dock_aruco_number" value="102"/>
      <param name="cmd_vel_angular_rate" value="0.8" />
      <param name="cmd_search_angular_rate" value="0.4" />
      <param name="motor_response_delay" value="0.50" />
      <param name="search_turn_amount" value="0.8" />
    </node>
```



To start the undocking procedure publish a True std_msgs/Bool value to
"/auto_dock/undock". 

```
rostopic pub /auto_dock/undock std_msgs/Bool "true"
```



To start the docking procedure publish a True std_msgs/Bool value to
"/auto_dock/dock". 

```
rostopic pub /auto_dock/dock std_msgs/Bool "true"
```



## Nodes



```clearsilver
node.0{
name= auto_detect_node
desc= This node is a state machine that includes all docking and undocking behavior.  It rotates by small angles until it detects a  specific Aruco marker and then proceeds towards the marker until it detects that the rover is charging.
}
sub {
0{
name= fiducial_transforms
type= fiducial_msgs/FiducialTransformArray
desc= Topic that published array of transform information for detected Aruco markers from fiducials aruco_detect node.
}
1{
name= rr_openrover_driver/charging
type= std_msgs/Bool
desc= Publishes charging state of the rover. `True` if charging.
}
2{
name= /auto_dock/undock
type= std_msgs/Bool
desc= When a True message is received begin undocking routine.
}
3{
name= /auto_dock/dock
type= std_msgs/Bool
desc= When a True message is received begin docking routine.
}
4{
name= /auto_dock/cancel
type= std_msgs/Bool
desc= When a True message is received cancel current routine.
}
}
pub {
0{
name= /cmd_vel/auto_dock
type= geometry_msgs/TwistStamped
desc= Publishes the the command velocities.  Remap to target desired endpoint.
}
1{
name= /auto_dock/state
type= std_msgs/String
desc= Publishes the current mode state of the auto-docking state machine. . All mode states: 'undocked', 'searching', 'centering', 'approach', 'final_approach', 'final_wiggle', 'docking_failed', 'docked', 'undock'.
}
2{
name= /auto_dock/action_state
type= std_msgs/String
desc= Publishes the action state of the state machine. Actions states represent the behavior of the robot such as moving forward, counting markers, or turning.  All action states: 'turning', 'count_aruco_callbacks', 'jogging', 'stopping'.
}
}
param {
0{
name= ~dock_aruco_number
default= 0
type= int
desc= The ID code for the Aruco marker attached to the charging dock.
}
1{
name= ~search_turn_amount
default= -0.8
type= float
desc= The number of radians to turn while searching for the charging dock's Aruco marker. While in search mode the robot makes incremental turns and stops.  This behavior reduces the noise in Aruco detection and allows them to be detected from much further away.
}
2{
name= ~undock_distance
default= 1.0
type= float
desc= The distance in meters the robot reverses while undocking.
}
3{
name= ~undock_turn_amount
default= 3.1415
type= float
desc= The angle, in radians, to turn after reversing while undocking.  The node is naive and does not account for feed back while moving, and instead is timer based.  This means that depending on PID tuning, the robot may not turn to the exact angle specified. 
}
4{
name= ~start_delay
default= 2.0
type= float
desc= The number of seconds to wait before beginning the Docking routine.
}
5{
name= ~cmd_vel_linear_rate
default= 0.25
type= float
desc= The linear speed, in meters per second, at which the robot moves during reversal or forward motion.
}
6{
name= ~cmd_vel_angular_rate
default= 0.3
type= float
desc= The speed, in radians per second, the robot turns while searching or centering.  For the 4 wheel drive due to the increased friction it may be advisable to increase this value.
}
7{
name= ~motor_response_delay
default= 0.05 
type= float
desc= This increases the duration of the turn timer to compensate for the response delay of the PID.  For the 2 wheel drive robot this may be negligible.  For the 4 wheel drive robot due to friction, this may be quite a bit higher for lower speeds.  0.25 is recommended for 4 wheel drive configurations. 
}
8{
name= ~action_delay
default= 0.3
type= float
desc= The number of seconds before the Aruco detection counter begins accepting detection again after the previous action. 
}
}
```


