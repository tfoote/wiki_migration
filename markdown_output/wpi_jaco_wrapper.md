## About

The `wpi_jaco_wrapper` package contains nodes to interface ROS with
the JACO API. It includes publishing angular and Cartesian commands to
the arm, generating and following trajectories from input such as
MoveIt!, rotational representation conversions between ROS and the JACO
API, and forward kinematics.

## Nodes



```clearsilver
node.0 {
  name = jaco_arm_trajectory_node
  desc = 'jaco_arm_trajectory_node' sends trajectory points to the JACO, JACO2, and MICO arms, and handles smooth trajectory following for complex trajectories.
  sub {
    0.name = jaco_arm/angular_cmd
    0.type = wpi_jaco_msgs/AngularCommand
    0.desc = Send an angular command to the arm.
    1.name = jaco_arm/cartesian_cmd
    1.type = wpi_jaco_msgs/CartesianCommand
    1.desc = Send a Cartesian command to the arm.
  }
  pub {
    0.name = jaco_arm/joint_states
    0.type = sensor_msgs/JointState
    0.desc = Publishes the current state of the arm and finger joints.
    1.name = jaco_arm/angular_cmd
    1.type = wpi_jaco_msgs/AngularCommand
    1.desc = Send a angular command to the arm.
    2.name = jaco_arm/cartesian_cmd
    2.type = wpi_jaco_msgs/CartesianCommand
    2.desc = Send a Cartesian command to the arm.
    3.name = jaco_arm/arm_homed
    3.type = std_msgs/Bool
    3.desc = Publish true once after the jaco completes a home arm action using the Kinova API.
  }
  srv {
    0.name = jaco_arm/get_angular_position
    0.type = wpi_jaco_msgs/GetAngularPosition
    0.desc = Read the angular position from the arm.
    1.name = jaco_arm/get_cartesian_position
    1.type = wpi_jaco_msgs/GetCartesianPosition
    1.desc = Read the Cartesian position from the arm.
    2.name = jaco_arm/software_estop
    2.type = wpi_jaco_msgs/EStop
    2.desc = Enable/disable arm software emergency stop.
    3.name = jaco_arm/erase_trajectories
    3.type = std_srvs/Empty
    3.desc = Cancel trajectories currently running on the arm.
  }
  srv_called {
    0.name = jaco_arm/kinematics/fk
    0.type = wpi_jaco_msgs/JacoFK
    0.desc = JACO arm forward kinematics.
    1.name = jaco_conversions/quaternion_to_euler
    1.type = wpi_jaco_msgs/QuaternionToEuler
    1.desc = Converts 3d rotations from quaternion representation to Euler (xyz convention) representation.
    2.name = jaco_arm/erase_trajectories
    2.type = std_srvs/Empty
    2.desc = Stop any trajectory currently running on the arm.
  }
  goal {
    0.name = jaco_arm/arm_controller/trajectory/goal
    0.type = control_msgs/FollowJointTrajectoryGoal
    0.desc = Point-to-point trajectory execution using the JACO API's angular position controller.
    1.name = jaco_arm/smooth_arm_controller/trajectory/goal
    1.type = control_msgs/FollowJointTrajectoryGoal
    1.desc = Smoothed point-to-point trajectory execution using the JACO API's Cartesian position controller (note that trajectories must avoid the arm's internally defined singularity protection zones).
    2.name = jaco_arm/joint_velocity_controller/trajectory/goal
    2.type = control_msgs/FollowJointTrajectoryGoal
    2.desc = Joint velocity control based smooth trajectory generator and follower, provides smooth trajectory execution for any valid point-to-point trajectory in the arm's workspace.
    3.name = jaco_arm/fingers_controller/gripper/goal
    3.type = control_msgs/GripperCommandGoal
    3.desc = Gripper control using control_msgs.  Only active if kinova_gripper param is true.
    4.name = jaco_arm/fingers_controller_radian/gripper/goal
    4.type = control_msgs/GripperCommandGoal
    4.desc = Gripper control using control_msgs, input in radians corresponding to the joint_state positions of the fingers.  Only active if kinova_gripper param is true.
    5.name = jaco_arm/home_arm/goal
    5.type = wpi_jaco_msgs/HomeArmGoal
    5.desc = Move arm to the home position, or to a defined position via the home position.
  }
  result {
    0.name = jaco_arm/arm_controller/trajectory/result
    0.type = control_msgs/FollowJointTrajectoryResult
    0.desc = Trajectory execution result.
    1.name = jaco_arm/smooth_arm_controller/trajectory/result
    1.type = control_msgs/FollowJointTrajectoryResult
    1.desc = Trajectory execution result.
    2.name = jaco_arm/joint_velocity_controller/trajectory/result
    2.type = control_msgs/FollowJointTrajectoryResult
    2.desc = Trajectory execution result.
    3.name = jaco_arm/fingers_controller/gripper/result
    3.type = control_msgs/GripperCommandResult
    3.desc = Gripper position (in the units of the Kinova API defined for the finger actuators), effort, and status upon completion of a gripper control.  Only active if kinova_gripper param is true.
    4.name = jaco_arm/fingers_controller_radian/gripper/result
    4.type = control_msgs/GripperCommandResult
    4.desc = Gripper position (in radians corresponding to the fingers' joint_state positions), effort, and status upon completion of a gripper goal.  Only active if kinova_gripper param is true.
    5.name = jaco_arm/home_arm/result
    5.type = wpi_jaco_msgs/HomeArmResult
    5.desc = Success/failure of moving the arm to the home position.
  }
  param {
    0.name = wpi_jaco/arm_name
    0.type = string
    0.desc = Name of the arm (currently either "jaco", "jaco2", or "mico").
    0.default = "jaco"
    1.name = wpi_jaco/finger_scale
    1.type = float
    1.desc = Conversion between jaco and mico finger values (normalized to 1.0 for the jaco).
    1.default = 1.0
    2.name = wpi_jaco/finger_error_threshold
    2.type = float
    2.desc = Error threshold for a finger position command to be considered completed successfully (Kinova API finger units).
    2.default = 1.0
    3.name = wpi_jaco/gripper_open
    3.type = float
    3.desc = Finger open position (Kinova API finger units).
    3.default = 0.0
    4.name = wpi_jaco/gripper_closed
    4.type = float
    4.desc = Finger closed position (Kinova API finger units).
    4.default = 65.0
    5.name = wpi_jaco/max_curvature
    5.type = double
    5.desc = Maximum allowed curvature for trajectory generation.
    5.default = 10.0
    6.name = wpi_jaco/max_speed_finger
    6.type = float
    6.desc = Maximum finger speed (Kinova API finger units per second).
    6.default = 30.0
    7.name = wpi_jaco/num_fingers
    7.type = int
    7.desc = Number of fingers (3 for jaco, 2 for mico).
    7.default = 3
    8.name = home_arm_on_init
    8.type = bool
    8.desc = Flag for homing the arm when it's initialized, arm will home if true.
    8.default = true
    9.name = kinova_gripper
    9.type = bool
    9.desc = Whether the arm has an attached Kinova gripper (the two- or three-fingered gripper for use with the jaco, jaco2, or mico).  If false, gripper action servers and finger joint states will not be published.
    9.default = true
  }
}
node.1 {
  name = jaco_manipulation
  desc = 'jaco_manipulation' handles object manipulation actions including grasping and lifting actions.
  sub {
    0.name = jaco_arm/joint_states
    0.type = sensor_msgs/JointState
    0.desc = Subscribes to joint state updates for the arm and finger joints.
  }
  pub {
    0.name = jaco_arm/angular_cmd
    0.type = wpi_jaco_msgs/AngularCommand
    0.desc = Send an angular command to the arm.
    1.name = jaco_arm/cartesian_cmd
    1.type = wpi_jaco_msgs/CartesianCommand
    1.desc = Send a Cartesian command to the arm.
  }
  srv_called {
    0.name = jaco_arm/get_cartesian_position
    0.type = wpi_jaco_msgs/GetCartesianPosition
    0.desc = Read the Cartesian position of the arm's end effector.
  }
  goal {
    0.name = jaco_arm/manipulation/gripper/goal
    0.type = rail_manipulation_msgs/GripperGoal
    0.desc = Execute a grasp or release with the JACO gripper until the fingers can no longer move.  Only active if kinova_gripper param is true.
    1.name = jaco_arm/manipulation/lift/goal
    1.type = rail_manipulation_msgs/LiftGoal
    1.desc = Execute a lift action that lifts the end effector while applying a constant force to close the fingers, preventing objects from slipping.
  }
  result {
    0.name = jaco_arm/manipulation/gripper/result
    0.type = rail_manipulation_msgs/GripperResult
    0.desc = Success or failure of a gripper close/open action.  Only active if kinova_gripper param is true.
    1.name = jaco_arm/manipulation/pickup/result
    1.type = rail_manipulation_msgs/LiftResult
    1.desc = Success or failure of the lift action.
  }
  param {
    0.name = wpi_jaco/arm_name
    0.type = string
    0.desc = Name of the arm (currently either "jaco", "jaco2", or "mico").
    0.default = "jaco"
    1.name = wpi_jaco/gripper_open
    1.type = float
    1.desc = Finger open position (Kinova API finger units).
    1.default = 0.0
    2.name = wpi_jaco/gripper_closed
    2.type = float
    2.desc = Finger closed position (Kinova API finger units).
    2.default = 65.0
    3.name = wpi_jaco/num_fingers
    3.type = int
    3.desc = Number of fingers (3 for jaco, 2 for mico).
    3.default = 3
    4.name = kinova_gripper
    4.type = bool
    4.desc = Whether the arm has an attached Kinova gripper (the two- or three-fingered gripper for use with the jaco, jaco2, or mico).  If false, gripper action servers and finger joint states will not be published.
    4.default = true
  }
}
node.2 {
  name = jaco_conversions
  desc = 'jaco_conversions' provides conversion services between the JACO, JACO2, and MICO arms' internal 3D rotation representation and common 3D rotation representations used in ROS.
  srv {
    0.name = jaco_conversions/euler_to_quaternion
    0.type = wpi_jaco_msgs/EulerToQuaternion
    0.desc = Converts a rotation in the Euler XYZ convention (used by the JACO arm) to quaternion representation.
    1.name = jaco_conversions/quaternion_to_euler
    1.type = wpi_jaco_msgs/QuaternionToEuler
    1.desc = Converts a rotation in quaternion representation to the Euler XYZ convention (used by the JACO arm).
  }
  param {
    0.name = wpi_jaco/arm_name
    0.type = string
    0.desc = Name of the arm (currently either "jaco", "jaco2", or "mico").
    0.default = "jaco"
  }
}
node.3 {
  name = jaco_kinematics
  desc = 'jaco_kinematics' provides kinematics services for the JACO and JACO2 arms.
  srv {
    0.name = jaco_arm/kinematics/fk
    0.type = wpi_jaco_msgs/JacoFK
    0.desc = JACO forward kinematics service.
  }
  param {
    0.name = wpi_jaco/arm_name
    0.type = string
    0.desc = Name of the arm (currently either "jaco", "jaco2", or "mico").
    0.default = "jaco"
  }
}
```



## Arm Parameters

The `wpi_jaco_wrapper` package uses a configuration file to set most
of the parameters for its nodes. This allows for support of different
types of arms, such as the Jaco, Jaco2, or the Mico. The configuration
files are located within the `config` directory, which includes a
`jaco.yaml` file, `jaco2.yaml` file, and `mico.yaml` file that
define default parameter values for the Jaco, Jaco2, and Mico arms
respectively. The parameters include:

-   arm_name - name of the arm, should be the same as the configuration
    file name
-   finger_scale - difference in units for measuring the finger
    position, normalized to 1 for the Jaco
-   finger_error_threshold - threshold in the Kinova API's finger
    position units to consider a finger position as successfully reached
-   gripper_open - finger position for a fully open gripper
-   gripper_closed - finger position for a fully closed gripper
-   max_curvature - used for calculating splines in the joint trajectory
-   max_speed_finger - maximum finger speed when opening/closing
-   num_fingers - number of fingers

## Trajectory Execution Options

The `jaco_arm_trajectory_node` provides three different options for
trajectory execution, each of which has its own action server and its
own set of advantages and disadvantages. The specifics of each
trajectory follower, how they compare to eachother, and situations where
each one may be applicable are detailed below.

### Point-to-Point

The `jaco_arm/arm_controller` action server provides the simplest
trajectory execution method. This method sends each point to the JACO
arm using the Kinova API, which will then execute the trajectory using
its PID controller to move the arm from point to point. This is the most
accurate and precise trajectory follower for point-to-point motion, but
for complex trajectories with many points, the point-to-point motion
causes the arm to stop at each point resulting in a jerky, uneven
overally motion. As such, this trajectory follower is recommended only
for simple trajectories that are comprised of a small number of points
spaced far apart, such as pre-defined trajectories for basic motions.

### Smoothed Point-to-Point

The `jaco_arm/smooth_arm_controller` action server works similarly to
the point-to-point trajectory follower provided by
`jaco_arm/arm_controller`, with the addition of the Kinova API's
trajectory smoothing. This is accomplished through first converting the
trajectory points from joint position points to Cartesian end effector
points. The Kinova API then smooths the trajectory of the end effector.
This has the disadvantage of requiring the full trajectory to avoid the
singularity protection zones defined internally, so this trajectory
follower should only be used for trajectories generated from planners
that are aware of these protection zones, or for pre-defined
trajectories.

### Velocity Control

The `jaco_arm/joint_velocity_controller` action server provides an
alternative to the previous two methods (which rely on trajectory
execution through the Kinova API) by using its own trajectory controller
and trajectory follower based on velocity control. The trajectory points
are used to generate a linear interpolated trajectory with smoothed
corners using the [ecl_geometry](ecl_geometry) package. The trajectory
is then followed using a velocity controller, defined in the
`jaco_arm_trajectory_node.cpp` file, that sends its control inputs as
joint velocity commands through the Kinova API. This controller is the
recommended trajectory follower for execution of complex trajectories
with many points, such as those generated by MoveIt!'s motion planners,
as it uses joint control and is therefore not subject to the singularity
constraints of the smoothed point-to-point trajectory follower.

## Alternative End-Effectors

This package is designed to work with the 2- or 3-fingered gripper
included with the JACO, JACO2, and MICO. With it's default behavior,
the wrapper node will publish joint states for the fingers, and includes
gripper control action servers. If you are using an alternative
end-effector for your arm, setting the kinova_gripper argument in the
`arm.launch` file will disable the finger joint state publishing and
the gripper action servers.

## Notes about the JACO2

This package has been updated to work with the new JACO2. There is one
important difference to note when using this package with the JACO2
instead of the JACO or the MICO. For the JACO and MICO, the joint state
names are published as `\[arm_name\]_joint_\[joint_number\]`. The
JACO2 publishes joint state names under a different set of names for
compatibility with a new arm urdf. The joint names, in order from the
base to the end-effector, are: \[`jaco_shoulder_pan_joint`,
`jaco_shoulder_lift_joint`, `jaco_elbow_joint`,
`jaco_wrist_1_joint`, `jaco_wrist_2_joint`, `jaco_wrist_3_joint`\]

See the metapackage, [wpi_jaco](wpi_jaco), for any other limitations of
using this package with the JACO2.

## Installation

To install the `wpi_jaco` package, you can install from source with
the following commands: . 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/RIVeR-Lab/wpi_jaco.git
cd ..
catkin_make
catkin_make install
```



## Startup

The `wpi_jaco_wrapper` package contains the launch file `arm.launch`
which will launch all of the nodes required to send trajectories and
manipulation commands to the JACO arm. Note that the launch file will
remap some of the topic names for the trajectory execution actions (this
is done for easier MoveIt! integration), but these can be changed if
desired by editing the launch file. This can be launched with the
following command:

. 

```
roslaunch wpi_jaco_wrapper arm.launch
```


