## Introduction

This package contains relevant files for running Svenzva robots in 3D
simulations. Currently supported simulations are through Gazebo,
MoveIt!, or both Gazebo and Moveit!.

For control of robot arms in simulation we use \`ros_control\` plugins
for Gazebo. This provides software level controllers for each joint
which likely will not translate 1-1 on the real robot.

Tips on tuning PID parameters for \`ros_control\` can be found on
Gazebo\'s \`ros_control\` plugin page (located
[ here](http://gazebosim.org/tutorials/?tut=ros_control#UseRQTToSendCommands))
under the section \"Tuning PID Parameters\".

### Supported Version

Simulations have been run in both ROS Indigo (Gazebo 2) and ROS Kinetic
(Gazebo 7).

## Tutorials

For software guides and tutorials we use the Wiki on our main Github
repository.

The tutorial for 3D simulations using Gazebo and/or MoveIt can be found
at
<https://github.com/SvenzvaRobotics/svenzva_ros/wiki/Simulation-with-Gazebo-and-MoveIt!>

## Nodes

```clearsilver
node.0 {
name = /revel/revel_trajectory_controller
desc = The `ros_control` interface for trajectory execution. Run when executing Gazebo and Moveit, as it allows MoveIt trajectories to be played back and realized in the Gazebo environment.
sub { 
0.name = /revel/effort_joint_trajectory_controller/follow_joint_trajectory/goal
0.type = control_msgs/FollowJointTrajectoryActionGoal
0.desc = Trajectory action interface goal subscription.
1.name = /revel/effort_joint_trajectory_controller/gains/joint_1/parameter_descriptions
1.type = dynamic_reconfigure/ConfigDescription
1.desc = Dynamic reconfigure linked topic for configuring controller gains.

2.name = /revel/effort_joint_trajectory_controller/gains/joint_2/parameter_descriptions
2.type = dynamic_reconfigure/ConfigDescription
2.desc = Dynamic reconfigure linked topic for configuring controller gains.

3.name = /revel/effort_joint_trajectory_controller/gains/joint_3/parameter_descriptions
3.type = dynamic_reconfigure/ConfigDescription
3.desc = Dynamic reconfigure linked topic for configuring controller gains.

4.name = /revel/effort_joint_trajectory_controller/gains/joint_4/parameter_descriptions
4.type = dynamic_reconfigure/ConfigDescription
4.desc = Dynamic reconfigure linked topic for configuring controller gains.

5.name = /revel/effort_joint_trajectory_controller/gains/joint_5/parameter_descriptions
5.type = dynamic_reconfigure/ConfigDescription
5.desc = Dynamic reconfigure linked topic for configuring controller gains.

6.name = /revel/effort_joint_trajectory_controller/gains/joint_6/parameter_descriptions
6.type = dynamic_reconfigure/ConfigDescription
6.desc = Dynamic reconfigure linked topic for configuring controller gains.
}
pub {
1.name = /revel/effort_joint_trajectory_controller/follow_joint_trajectory/feedback
1.type = control_msgs/FollowJointTrajectoryActionFeedback
1.desc = Trajectory action interface feedback topic.
2.name = /revel/effort_joint_trajectory_controller/follow_joint_trajectory/result
2.type = control_msgs/FollowJointTrajectoryActionResult
2.desc = Trajectory action interface result topic.
}

}
```

```clearsilver
node.0 {
name = /revel/controller
desc = Spawns and runs a PID controller for each joint outside of a trajectory controller, making it useful for standalone Gazebo simulations. Each motor has its own command and state expositions.
sub {
0.name = /svenzva_controllers/joint_1/command
0.type = std_msgs/Float64
0.desc = Position command to set the set-point for this joint controller.
1.name = /svenzva_controllers/joint_1/pid/parameter_descriptions
1.type = dynamic_reconfigure/ConfigDescription
1.desc = Dynamic Reconfigure configuration topic for changing controller gains.
2.name = /svenzva_controllers/joint_2/command
2.type = std_msgs/Float64
2.desc = Position command to set the set-point for this joint controller.
3.name = /svenzva_controllers/joint_2/pid/parameter_descriptions
3.type = dynamic_reconfigure/ConfigDescription
3.desc = Dynamic Reconfigure configuration topic for changing controller gains.

4.name = /svenzva_controllers/joint_3/command
4.type = std_msgs/Float64
4.desc = Position command to set the set-point for this joint controller.
5.name = /svenzva_controllers/joint_3/pid/parameter_descriptions
5.type = dynamic_reconfigure/ConfigDescription
5.desc = Dynamic Reconfigure configuration topic for changing controller gains.

6.name = /svenzva_controllers/joint_4/command
6.type = std_msgs/Float64
6.desc = Position command to set the set-point for this joint controller.
7.name = /svenzva_controllers/joint_4/pid/parameter_descriptions
7.type = dynamic_reconfigure/ConfigDescription
7.desc = Dynamic Reconfigure configuration topic for changing controller gains.

8.name = /svenzva_controllers/joint_5/command
8.type = std_msgs/Float64
8.desc = Position command to set the set-point for this joint controller.
9.name = /svenzva_controllers/joint_5/pid/parameter_descriptions
9.type = dynamic_reconfigure/ConfigDescription
9.desc = Dynamic Reconfigure configuration topic for changing controller gains.

10.name = /svenzva_controllers/joint_6/command
10.type = std_msgs/Float64
10.desc = Position command to set the set-point for this joint controller.
11.name = /svenzva_controllers/joint_6/pid/parameter_descriptions
11.type = dynamic_reconfigure/ConfigDescription
11.desc = Dynamic Reconfigure configuration topic for changing controller gains.
}
pub {
0.name = /svenzva_controllers/joint_1/state
0.type = control_msgs/JointControllerState
0.desc = Controller and joint state information for this joint.
1.name = /svenzva_controllers/joint_2/state
1.type = control_msgs/JointControllerState
1.desc = Controller and joint state information for this joint.
2.name = /svenzva_controllers/joint_3/state
2.type = control_msgs/JointControllerState
2.desc = Controller and joint state information for this joint.
3.name = /svenzva_controllers/joint_4/state
3.type = control_msgs/JointControllerState
3.desc = Controller and joint state information for this joint.
4.name = /svenzva_controllers/joint_5/state
4.type = control_msgs/JointControllerState
4.desc = Controller and joint state information for this joint.
5.name = /svenzva_controllers/joint_6/state
5.type = control_msgs/JointControllerState
5.desc = Controller and joint state information for this joint.
}

}
```
