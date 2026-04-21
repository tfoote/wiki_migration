## About

The `jaco_interaction` package provides interactive marker-based
control of the end effector pose and issuing of manipulation commands
for the JACO and JACO2.

## Nodes



```clearsilver
node.0 {
  name = jaco_interactive_manipulation
  desc = 'jaco_interactive_manipulation' publishes interactive markers that can be used to control the end effector pose and issue manipulation commands.
  sub {
    0.name = jaco_arm/joint_states
    0.type = sensor_msgs/JointState
    0.desc = Updates for arm and finger joint states.
  }
  pub {
    0.name = jaco_arm/cartesian_cmd
    0.type = wpi_jaco_msgs/CartesianCommand
    0.desc = Send Cartesian commands to the arm.
  }
  srv_called {
    0.name = jaco_arm/kinematics/fk
    0.type = wpi_jaco_msgs/JacoFK
    0.desc = Forward kinematics for the arm.
    1.name = jaco_conversions/quaternion_to_euler
    1.type = wpi_jaco_msgs/QuaternionToEuler
    1.desc = Conversion from quaternion to Euler xyz rotation representations.
  }
  act_called {
    0.name = jaco_arm/manipulation/gripper
    0.type = rail_manipulation_msgs/GripperGoal
    0.desc = Call open and close actions for the gripper.
    1.name = jaco_arm/manipulation/lift
    1.type = rail_manipulation_msgs/LiftGoal
    1.desc = Call object lift action for the arm.
  }
  param {
    0.name = wpi_jaco/arm_name
    0.type = string
    0.desc = Name of the arm, either "jaco" or "jaco2"
    0.default = jaco
  }
}
```



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

The interactive markers can be launched using two launch files:
`im_backend.launch` and `im_frontend.launch`. The
`im_backend.launch` file launches all of the necessary ROS nodes to
publish the interactive markers and send commands back to the arm, and
as such it should be launched first on a computer connected directly to
the JACO arm. The `im_frontend.launch` file launches rviz with a
preset configuration to show the arm model and the interactive markers.
This can be launched on any computer capable of displaying a GUI. The
syntax for launching these nodes is as follows:

. 

```
roslaunch jaco_interaction im_backend.launch
```

 . 

```
roslaunch jaco_interaction im_frontend.launch
```


