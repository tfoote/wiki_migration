A simple Cartesian trajectory controller that uses the new Cartesian
trajectory definition.

## Rationale

This controller shall get you started with executing Cartesian
trajectories on your robot. It implements a simple action server for
FollowCartesianTrajectory. There are currently two ways of execution,
depending on the interface provided by the robot.

The table below highlights possible applications.

  -- ---------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     **Hardware interface**          **Primary application**                                                                                                                                                                                                                                                    
     `PoseCommandInterface`        You want spline interpolation in ROS but the OEMs driver to take care of inverse kinematics (IK). This variant requires the new Cartesian interfaces.                                                                                                                      
     `PositionJointInterface`      You want spline interpolation in ROS and implement your own IK solver. The provided example uses the established Weighted Levenberg-Marquardt solver form KDL. This variant is compatible with current ROS-control so that you need not change your RobotHW abstraction.   
  -- ---------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## Further information

For further information, especially how to integrate this into a RobotHW
interface, see the
[Documentation on GitHub](https://github.com/UniversalRobots/Universal_Robots_ROS_controllers_cartesian/blob/main/cartesian_trajectory_controller/README.md)
