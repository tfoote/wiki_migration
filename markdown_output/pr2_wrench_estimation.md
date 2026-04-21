## Overview

This package estimates the wrenches exerted at the tip of the PR2 arms
through two methods.

The first approach uses the joint efforts as input and propagates them
forward using the inverse of the transposed jacobian.

The second approach takes the joint velocity errors as inputs and
propagates the error forward through the jacobian to obtain the error in
the twist of the tip of the arm. This error in the twist is a measure of
the wrench up to a scale factor.

Filtered versions of the calculated signals through a Butterworth 2nd
order LPF are also available.

The first method takes the joint efforts from the /joint_states topic,
while the second needs to have joint velocity controllers loaded.

The configuration of the root and tip links of each arm are in the yaml
files located in the config/ directory.

-   **Authors:** Francisco Viña and Alexis Maldonado
-   **License:** BSD
-   **Repository:** <https://github.com/fevb/pr2_wrench_estimation.git>

## ROS API



```clearsilver
 name = l_arm_wrench_estimation/r_arm_wrench_estimation

sub{
0.name = /joint_states
  0.type = sensor_msgs/JointState
  0.desc = Joint state information of the robot. From this topic the /field is used for 
 1.name = /l_arm_vel/state or /r_arm_vel/state
 1.type = pr2_controllers_msgs/JointTrajectoryControllerState
 1.desc = Receives joint positions and velocity error from the joint velocity controllers. Used for the second method described above.
}

pub{
  0.name = /l_arm_wrench_estimation/estimated_wrench
  0.type = geometry_msgs/WrenchStamped
  0.desc = estimated wrench from the joint efforts.
  1.name = /l_arm_wrench_estimation/filtered_wrench
  1.type = geometry_msgs/WrenchStamped
  1.desc = low pass filtered estimated wrench from joint efforts.
  2.name = /l_arm_wrench_estimation/twist_error
  2.type = geometry_msgs/TwistStamped
  2.desc = error in the twist at the tip of the PR2 arm, calculated from the velocity error of the PR2's velocity controllers.
  3.name = /l_arm_wrench_estimation/filtered_twist_error
  3.type = geometry_msgs/TwistStamped
  3.desc = low pass filtered estimated twist error at the tip of the PR2 arm.
}

param{
 0.name = chain_tip_frame
 0.type = string
 0.default = "l_gripper_tool_frame"
 0.desc = Specifies the tip frame of the PR2 arm chain.
 1.name = chain_root_frame
 1.type = string
 1.default = "torso_lift_link"
 1.desc = Specifies the root frame of the PR2 arm chain.
 2.name = filter_coeff_b_effort
 2.type = list of doubles
 2.default = Required
 2.desc = 3 element array specifying the 'b' coefficients of the LPF for the joint effort based wrench estimator.
 3.name = filter_coeff_a_effort
 3.type = list of doubles
 3.default = Required
 3.desc = 3 element array specifying the 'a' coefficients of the LPF for the joint effort based wrench estimator. The first element should be '1'.
 4.name = filter_coeff_b_vel
 4.type = list of doubles
 4.default = Required
 4.desc = 3 element array specifying the 'b' coefficients of the LPF for the joint velocity error based wrench estimator.
 5.name = filter_coeff_a_vel
 5.type = list of doubles
 5.default = Required
 5.desc = 3 element array specifying the 'a' coefficients of the LPF for the joint velocity error based wrench estimator. The first element should be '1'.
}

req_tf{
}

prov_tf{
}
```


