## End of Life

The pi_tracker package was created a long time ago as an entry for the
early ROS 3D contest and I don\'t have plans to develop it in the
future.

Note that the pi_tracker package depends on either the openni_tracker
package or the skeleton_markers package. Under ROS Indigo, I have only
had success using a Microsoft Kinect with these package. It seems the
Asus Xtion Pro Live can be difficult to get working with skeleton
tracking on newer USB 3.0 machines and Ubuntu 14.04.

## Overview

The pi_tracker package uses four interrelated but independent ROS nodes
that communicate over ROS topics and services:

-   \`skeleton_tracker\` (from the [skeleton_markers](skeleton_markers)
    package) for talking to the OpenNI skeleton tracking API and
    publishing the joint configuration and tf frames. Publishes joints
    names, positions, orientations and confidence values to the
    \`/skeleton\` topic.
-   \`tracker_command\` for detecting gesture commands and connecting to
    services that control the robot. Subscribes to the \`/skeleton\`
    topic and makes calls to services on other nodes. New gestures and
    commands can be added easily by defining simple functions over the
    joint configurations.
-   \`tracker_base_controller\` for controlling the movements of a
    differential drive (either holonomic or non-holonomic) mobile base.
    Subscribes to \`/skeleton\` and publishes to \`/cmd_vel\`.
-   \`tracker_joint_controller\` for teleoperating the joints of the
    robot including arms, torso and head. Subscribes to \`/skeleton\`
    and publishes to \`/cmd_joints\`.

## Skeleton Tracker Node (from the skeleton_markers package)

```clearsilver
node.0 {
name = skeleton_tracker
desc = (This description is copied from the [[skeleton_markers]] package.) A ROS node written in C++ for talking to the OpenNI skeleton tracking API and publishing the joint configuration and tf frames.  Based on Taylor Veltrop's teleop_kinect.cpp source at [[veltrobot_teleop]].
}

pub {
  0.name = /skeleton
  0.type = pi_tracker/Skeleton
  0.desc = Joint names, positions, orientations and confidence values.
}

param {
  0.name = ~tracking_rate
  0.type = int
  0.desc = Rate to publish skeleton data.
  0.default = 1

  1.name = ~fixed_frame
  1.type = string
  1.desc = The fixed reference frame when computing the joint frame transforms.
  1.default = "openni_depth"
}

prov_tf {
  0.from = fixed_frame
  0.to   = head
  0.desc = Head transform

  1.from = fixed_frame
  1.to   = neck
  1.desc = Neck transform

  2.from = fixed_frame
  2.to   = torso
  2.desc = Torso transform

  3.from = fixed_frame
  3.to   = left_shoulder
  3.desc = Left shoulder transform

  4.from = fixed_frame
  4.to   = left_elbow
  4.desc = Left elbow transform

  5.from = fixed_frame
  5.to   = left_hand
  5.desc = Left hand transform

  6.from = fixed_frame
  6.to   = right_shoulder
  6.desc = Right shoulder transform

  7.from = fixed_frame
  7.to   = right elbow
  7.desc = Right elbow transform

  8.from = fixed_frame
  8.to   = right_hand
  8.desc = Right hand transform

  9.from = fixed_frame
  9.to   = left_hip
  9.desc = Left hip transform

  10.from = fixed_frame
  10.to   = left_knee
  10.desc = Left knee transform

  11.from = fixed_frame
  11.to   = left_foot
  11.desc = Left foot transform

  12.from = fixed_frame
  12.to   = right_hip
  12.desc = Right hip transform

  13.from = fixed_frame
  13.to   = right_knee
  13.desc = Right knee transform

  14.from = fixed_frame
  14.to   = right_foot
  14.desc = Right foot transform
}
```

## Tracker Command Node

```clearsilver
node.1 {
name = tracker_command
desc = A ROS node written in Python for detecting gesture commands and connecting to services that control the robot.  New gestures and commands can be easily added by defining simple functions over the joint configurations.

sub {
  0.name = /skeleton
  0.type = pi_tracker/Skeleton
  0.desc = Joint names, positions, orientations and confidence values.
}

param {
  0.name = ~command_rate
  0.type = int
  0.desc = Rate to compute gestures from the skeleton tracker data.
  0.default = 1
}
```

### Tracker Command Required Services

Tracker command requires one or more services from each node it
commands. In its current form, the tracker command node sends simple
string commands to control nodes via their \`set_command\` service. For
example, sending the command \"STOP\" to the \`tracker_base_controller\`
node (see below) tells the base to stop moving.

## Tracker Base Controller Node

```clearsilver
node.2 {
name = tracker_base_controller
desc = A ROS node written in Python for controlling the movements of a wheeled robot (holonomic or non-holonomic) using either the hands or the feet.

pub {
  0.name = /cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Command the robot base to move forward/backward or rotate in place.  For a holonomic robot, both x and y linear components of the velocity are available.
}

sub {
  0.name = /skeleton
  0.type = pi_tracker/Skeleton
  0.desc = Joint names, positions, orientations and confidence values.
}

srv {
  0.name = ~set_command
  0.type = pi_tracker/SetCommand
  0.desc = Set the mode command to control the base.  Commands include: "STOP", "DRIVE_BASE_HANDS" or "DRIVE_BASE_FEET"
}

param {
  0.name = ~base_controller_rate
  0.type = int
  0.desc = Rate to send motion commands to the base.
  0.default = 1

  1.name = ~max_drive_speed
  1.type = double
  1.desc = Maximum forward/backward speed allowed.
  1.default = 0.3

  2.name = ~maximum_rotation_speed
  2.type = double
  2.desc = Maximum rotation speed allowed.
  2.default = 0.5

  3.name = ~base_control_side
  3.type = string
  3.desc = Are you left handed/legged or right?
  3.default = "right"

  4.name = ~scale_drive_speed
  4.type = double
  4.desc = Some robot drivers may require a scale factor to get speed in m/s
  4.default = 1.0

  5.name = ~scale_rotation_speed
  5.type = double
  5.desc = Some robot drivers may require a scale factor to get angular speed in rad/s
  5.default = 1.0

  6.name = ~reverse_rotation
  6.type = boolean
  6.desc = Some robot drivers may require use a left-handed coordinate system
  6.default = False

  6.name = ~holonomic
  6.type = boolean
  6.desc = The `tracker_base_controller` will send separate `x` and `y` components in the `Twist` message for holonomic robots.
  6.default = False

}
```

## Tracker Joint Controller Node

```clearsilver
node.2 {
name = tracker_joint_controller
desc =  A ROS node written in Python for teleoperating the joints of a multi-jointed robot, typically humanoid in form with arms, torso and a pan and tilt head.

pub {
  0.name = /cmd_joints
  0.type = sensor_msgs/JointState
  0.desc = Command the robot's joints to move to goal positions at a designated speed.
}

sub {
  0.name = /skeleton
  0.type = pi_tracker/Skeleton
  0.desc = Joint names, positions, orientations and confidence values.
}

srv {
  0.name = ~set_command
  0.type = pi_tracker/SetCommand
  0.desc = Set the mode command to control the joints.  Commands include: "STOP", "TELEOP_JOINTS"
}

param {
  0.name = ~joint_controller_rate
  0.type = int
  0.desc = Rate to publish the joint updates.
  0.default = 5

  1.name = ~default_joint_speed
  1.type = double
  1.desc = Default movement speed for the joints in rad/s.
  1.default = 0.5

  2.name = ~use_real_robot
  2.type = boolean
  2.desc = Whether or not there is a real robot on the other end.  Otherwise, the joint commands are published on the `/joint_state` topic so the result can be viewed in RViz.
  2.default = True

  3.name = ~skel_to_joint_map
  3.type = dict
  3.desc = A dictionary mapping skeleton frames to joint names for the given robot.
  3.default = Based on URDF for Pi Robot.  Adjust for your robot!
}
```

### Example Launch File

It is recommended to split the launch process into two launch files. The
first launch file brings up the Kinect, robot state publisher and
skeleton publisher. The second launch file fires up the various tracker
nodes. This way you can play with variations on the tracker nodes
without having to disconnect and reconnect to the Kinect camera. Also,
note that neither launch file brings up a real joint controller or base
controller since these will depend on your hardware.

Sample Skeleton/Kinect Launch File: ```
<launch>
  <arg name="fixed_frame" value="camera_depth_frame" />
 
  <param name="/use_sim_time" value="False" />
 

  <arg name="debug" value="False" />
  <arg name="launch_prefix" value="xterm -e gdb --args" />
 
  <param name="robot_description" command="$(find xacro)/xacro.py '$(find pi_tracker)/urdf/pi_robot/pi_robot_with_two_arms.xacro'" />
 
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="state_publisher">
    <param name="publish_frequency" value="20.0"/>
  </node>
    
  <include file="$(find rgbd_launch)/launch/kinect_frames.launch" />

  <group if="$(arg debug)">
    <node launch-prefix="$(arg launch_prefix)" pkg="skeleton_markers" name="skeleton_tracker" type="skeleton_tracker" output="screen"    >
      <param name="fixed_frame" value="$(arg fixed_frame)" />
      <param name="load_filepath" value="$(find pi_tracker)/params/SamplesConfigNewOpenNI.xml" />
    </node>
  </group>
  <group unless="$(arg debug)">
    <node name="skeleton_tracker" pkg="skeleton_markers" type="skeleton_tracker">
      <param name="fixed_frame" value="$(arg fixed_frame)" />
      <param name="load_filepath" value="$(find pi_tracker)/params/SamplesConfigNewOpenNI.xml" />
    </node>
  </group>
</launch>
```

Sample Tracker Nodes Launch File: ```
<launch>
    <node name="tracker_command" pkg="pi_tracker" type="tracker_command.py" output="screen">
        <rosparam command="load" file="$(find pi_tracker)/params/tracker_params.yaml" />
    </node>
    <node name="tracker_base_controller" pkg="pi_tracker" type="tracker_base_controller.py" output="screen">
        <rosparam command="load" file="$(find pi_tracker)/params/tracker_params.yaml" />
    </node>
    <node name="tracker_joint_controller" pkg="pi_tracker" type="tracker_joint_controller.py" output="screen">
        <rosparam command="load" file="$(find pi_tracker)/params/tracker_params.yaml" />
    </node>
</launch>
```

### Example YAML File

```
command_rate: 2
tracking_rate: 2
base_controller_rate: 2
joint_controller_rate: 2
default_joint_speed: 0.6
max_drive_speed: 0.3
max_rotation_speed: 0.3
base_control_side: right

use_real_robot: True

# Use these values for a typical non-holonomic robot.
scale_drive_speed: 1.0
scale_rotation_speed: 1.0
reverse_rotation: False
holonomic: False

# Use the following scale factors for the Rovio.
#scale_drive_speed: 4.0
#scale_rotation_speed: 0.4
#reverse_rotation: True
#holonomic: True

fixed_frame: openni_depth

skel_to_joint_map: {
   head: head_pan_joint,
   neck: head_tilt_joint,
   torso: torso_joint,
   left_shoulder: left_shoulder_lift_joint,
   left_elbow: left_elbow_joint,
   left_hand: left_hand_joint,
   right_shoulder: right_shoulder_joint,
   right_elbow: right_elbow_joint,
   right_hand: right_hand_joint,
   left_hip: no_joint,
   left_knee: no_joint,
   left_foot: no_joint,
   right_hip: no_joint,
   right_knee: no_joint,
   right_foot: no_joint
}
```
