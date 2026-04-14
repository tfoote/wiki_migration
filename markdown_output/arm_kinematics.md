## Overview

This package is intended to be a generic version of
[pr2_kinematics](pr2_kinematics). The main purpose is to do solid arm
kinematics for ANY robot.

```clearsilver
name = arm_kinematics
desc = Forward and backward kinematics for a solid arm
srv {
0.name = ~get_ik
0.type = kinematics_msgs/GetPositionIK
0.desc = Get the inverse kinematics
1.name = ~get_ik_solver_info
1.type = kinematics_msgs/GetKinematicSolverInfo
1.desc = Get the inverse kinematics solver info
2.name = ~get_fk
2.type = kinematics_msgs/GetPositionFK
2.desc = Get the forward kinematics
3.name = ~get_fk_solver_info
3.type = kinematics_msgs/GetKinematicSolverInfo
3.desc = Get the forward kinematics solver info

}
param {
0.name = urdf_xml
0.type = String
0.desc = Parameter name for where the URDF xml is located.
0.default = robot_description
1.name = [robot_description]
1.type = String
1.desc = Contents of the URDF xml
2.name = root_name
2.type = String
2.desc = URDF Link name specifying the first element of the kinematic chain
3.name = tip_name
3.type = String
3.desc = URDF Link name specifying the last element of the kinematic chain
4.name = maxIterations
4.type = Integer
4.desc = Maximum number of iterations to use when calculating inverse kinematics
4.default = 1000
5.name = epsilon
5.type = Float
5.desc = Epsilon used in inverse kinematics calculations
5.default = 1e-2
}
```
