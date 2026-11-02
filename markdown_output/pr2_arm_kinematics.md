## Overview

The pr2_arm_kinematics package is a PR2 specific package that provides
IK solutions for the PR2 robot arms. The recommended interface is
through ROS. The node provides multiple interfaces (listed in the ROS
API below) and can be used to compute the closest IK solution to an
initial guess. More information on using this package can be found in
the API documentation. Example code for using this package can be found
in the
[ pr2_kinematics tutorials](https://index.ros.org/p/pr2_kinematics).

## ROS API

### API Stability

- ROS API is REVIEWED but UNSTABLE
- C++ API is UNREVIEWED and UNSTABLE

### Services Offered

pr2_arm_kinematics provides services for IK computation. It can be
configured using ROS parameters. The ROS API is explained in greater
detail below. To get a collision free version of this node, check out
the
[pr2_arm_kinematics_constraint_aware package](pr2_arm_kinematics_constraint_aware).



```clearsilver
srv{
    0.name = node_namespace/get_ik
    0.type = kinematics_msgs/GetPositionIK
    0.desc = Compute the IK for a desired end-effector pose. The service call specifies the end-effector link name and a pose for this link. The request also includes a "hint" set of joint values that is used as a seed for the IK search. The returned IK solution is the closest to the seed solution (using an Euclidean metric) among the first set of found solutions. 
    1.name = node_namespace/get_fk
    1.type = kinematics_msgs/GetPositionFK
    1.desc = Compute the forward kinematics for a given set of joint positions.
    3.name = node_namespace/get_ik_solver_info
    3.type = kinematics_msgs/GetKinematicSolverInfo
    3.desc = returns the set of joints that the kinematics node uses for computation. Also returns joint limit information and the set of links that the kinematics node can solve IK for.
    4.name = node_namespace/get_fk_solver_info
    4.type = kinematics_msgs/GetKinematicSolverInfo
    4.desc = returns the set of joints that the kinematics node uses for FK computation. Also returns joint limit information and the set of links that the kinematics node can solve FK for.
}
```



### ROS Parameter Configuration



```clearsilver
param {
  4.name= ~free_angle
  4.default= 2
  4.type= int
  4.desc= The joint number for the free parameter that is required for computing IK (since this is a 7 dof redundant manipulator). The specified value of this angle in the initial guess provided in the IKRequest message is used to seed the search for IK solutions. The current options for this parameter are 0 or 2. It will default to 2 if set to any other value.
  5.name= ~search_discretization
  5.default= 0.01
  5.type= double
  5.desc= The discretization angle (in radians) for the free parameter to be used in the search that the ik node will perform to get back a solution.
  2.name= ~root_name
  2.default= torso_lift_link
  2.type= string
  2.desc= The name of the link that corresponds to the torso lift link. This is the root of the chain for the arm.
  3.name= ~tip_name
  3.default= r_wrist_roll_link
  3.type= string
  3.desc= The name of the tip link for the arm. This is the link that corresponds to the last joint axis of the arm chain (excluding the end-effector).

}
```



## Tutorials

Tutorials for this package can be found in the
[pr2_kinematics stack tutorials](https://index.ros.org/p/pr2_kinematics).
