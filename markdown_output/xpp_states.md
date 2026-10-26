\
![\|width="170"](https://i.imgur.com/ct8e7T4.png)

## State Representations

This package provides two ways to describe an articulated robot state,
one in cartesian (=task) space, the other in joint (=configuration)
space. Each of these states has a corresponding ROS message
[xpp_msgs](xpp_msgs), where conversion function are provided in
`convert.h`.

### Cartesian Representation

In this representation
([robot_state_cartesian.h](http://docs.ros.org/api/xpp_states/html/robot__state__cartesian_8h_source.html)),
the robot is described by the position, velocity and acceleration of
it's endeffectors and the Cartesian force they exert.


```cplusplus
class RobotStateCartesian {
public:
  State3d base_;
  EndeffectorsMotion ee_motion_;
  Endeffectors<Vector3d> ee_forces_;
  EndeffectorsContact ee_contact_;
  double t_global_;
};
```



### Joint Representation

In this representation
([robot_state_joint.h](http://docs.ros.org/api/xpp_states/html/robot__state__joint_8h_source.html))
the endeffector state is only indirectly given through the joint values.
Instead of forces acting on the endeffectors, this state equivalently
represents this as torques acting on the joints.


```cplusplus
class RobotStateJoint {
public:
  State3d base_;
  Joints q_, qd_, qdd_;
  Joints torques_;
  EndeffectorsContact ee_contact_;
  double t_global_;
};
```



## Endeffectors

The core difference between the above representations is how the
articulated limbs and the force they exert are described (task or joint
space). In order to make these states most interchangeable, we create a
class
([endeffectors.h](http://docs.ros.org/api/xpp_states/html/endeffectors_8h_source.html))
that parameterizes each endeffector. This can be done in two ways:

- using Cartesian xyz values for position velocity and acceleration for
  each endeffector.
- using joint position, velocity and acceleration of every joint of the
  limb.

## Feedback

Please let us know your improvement suggestions, bugs or any other
issues [here](https://github.com/leggedrobotics/xpp/issues).
