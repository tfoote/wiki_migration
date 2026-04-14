This package uses Bosch MEMS sensors to estimate the pose of the PR2\'s
arm. The cost of accelerometers and gyroscopes has dropped to a point
where they have become ubiquitous sensors, as seen by their presence in
mobile phones and video game controllers. It is possible to use these
sensors to estimate the joint positions of a robotic manipulator. This
allows the joint angle sensor to be decoupled from the physical joint
axis or actuator axis. In turn, this allows for a truly redundant
measurement mechanism for safety as well as for new, lower-cost
manipulator designs.

Currently only the left arm is supported, and the sensors must be placed
in specific locations and orientations.

![Sensor Placement\|width=768](attachment:PR2_Arm_State_Estimation_Sensor_Placement.jpg)
This image shows how the sensors are mounted on the Bosch PR2.
Instructions on how to place the sensors is forthcoming.

## Sensors

This package requires one Bosch BMA180 accelerometer per joint axis. It
is optional to include Bosch SMI540 gyroscopes.

## Background

The state of a three-dimensional robotic manipulator considered here is
the joint angles and velocities. By incorporating a gyroscope on each
link, the joint velocities can be directly and accurately measured.
Joint acceleration is not considered. Using \'\'a priori\'\' knowledge
of the manipulator kinematics and the corresponding accelerometer
mounting, a unified state estimate for the joint angles can be obtained
using an Extended Kalman Filter. A critical requirement for the proposed
approach is the accelerometer must be able to sense the acceleration due
to gravity at all times. Our approach utilizes the gravity component of
the acceleration while ignoring the centripetal and centrifugal
components. The robot moves slowly to be safe around humans, and the
movements are slow enough to justify this assumption. However, any high
frequency motions of the manipulator arm may result in unstable readings
from the accelerometers, thereby introducing offsets which cannot be
compensated.

When the joint axis is not parallel to the gravity vector, the joint
angle is estimated using accelerometer measurements and compensated
using gyroscope measurements. Mounting one accelerometer on every link
reduces the calculation of the joint angle between the link pairs to the
difference between the gravity vectors measured by consecutive
accelerometers. The gravity vector provides an orientation for each
accelerometer. X-Y-Z Euler angles are used to relate the accelerometer
orientations between consecutive links. A quaternion based solution is
not necessary because the joints connecting the manipulator links have
only one degree of freedom.

Intelligent placement of the accelerometers can simplify the fixed
rotation, and a calibration routine can be run to find the remaining
values. When a joint axis is parallel to the gravity vector, the
accelerometer measurements provide no useful information for determining
the joint angle. An angular rate gyroscope mounted such that measurement
axis is parallel to the axis of rotation of the joint can easily
eliminate this restriction. In this singularity condition, the gyroscope
measurements are integrated at each time step to provide the joint angle
estimate. There is the potential for large errors to accumulate due to
gyroscope drift.

## ROS API

```clearsilver
node.0 {
  name = pr2_arm_state_estimation
  desc = Estimates PR2 manipulator joint angles in rad.
  pub {
    0.name = pr2_arm_state_data
    0.type = pr2_arm_state_estimation/pr2_arm_state_data
    0.desc << EOM
 * `float64[] Theta` is the joint angle estimated by the MEMS sensors
 * `float64[] Accel` is the output from the MEMS accelerometers
 * `string[] JointName` contains the PR2 names for the joints whose position is estimated
 * `float64[] JointAngle` is the joint angle read from the optical encoders.
EOM
  }
}
```
