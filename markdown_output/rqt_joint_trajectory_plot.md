# Introduction

This package is to plot JointTrajectory message and JointTrajectoryGoal
action in real time.

Example in UR5:

Launch fake joint driver for UR5.

\` \$ roslaunch fake_joint_launch ur5.launch \`

Then launch MoveIt!

\` \$ roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch
sim:=true \`

Now you can control the UR5 using MoveIt.

Then run rqt and add JointTrajectoryPlot plugin. Choose the trajectory
topic.

\` \$ rqt \`

Then you can plot each joint position, velocity and acceleration.
