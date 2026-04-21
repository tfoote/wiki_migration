## Overview

The single sensor fusion (ssf) part of this stack is divided into the
common Kalman Filter steps prediction (or propagation) and update (or
measurement). We assume to always have an IMU as propagation sensor on
the vehicle while we can change the update sensors depending on the
users preferences. Hence, the propagation part remains unchanged for
different update sensors. Essentially, for every different update sensor
only the measurement matrix, and the calculation of the residuals
change - the rest of the filter framework remains the same. This package
contains samples for two different update sensors: a 6DoF pose sensor
and a 3DoF position sensor.

## Nodes

The provided nodes are only examples of update sensor modules. Since
your hardware set-up and transformation conventions may differ from
ours, before you use these examples you *must* check their code and
adjust it to your needs.

**pose_sensor**: sample for a 6DoF pose sensor as update sensor (for
example using Vicon or [ethzasl_ptam](ethzasl_ptam))

**position_sensor**: sample for a 3DoF position sensor as update sensor
(for example using a Leica Totalstation)

## Designing an Update Sensor Module

In the following, we state the conceptual steps to design your own
update sensor module. Please see the [ Tutorials](../Tutorials ) to get
a practical insight to the mentioned steps.

Every update sensor consists of 3 files:

-   \[type\]_sensor.cpp and \[type\]_sensor.h contain the topic
    subscription, dynamic reconfigure calls and - most important - the
    calculation of the measurement matrix and residuals passed to
    [ ssf_core](../ssf_core ).
-   \[type\]_measurements.h contains the initialization values passed
    to the initialization procedure in [ ssf_core](../ssf_core ).

Essentially you can use the example modules *pose_sensor* and
*position_sensor* and adapt them to your needs.

The main.cpp file only provides the wrapper to instantiate a sensor
module.

### Subscribing to the Correct Topics

Each sensor module needs to subscribe to its own information source
(e.g. Vicon bridge or output of [ethzasl_ptam](ethzasl_ptam)). The
subscription to the propagation sensor (IMU) for external or internal
state propagation is done automatically by [ ssf_core](../ssf_core ).

### Registering Dynamic Reconfigure Calls

The dynamic reconfigure part in [ ssf_core](../ssf_core ) contains two
general noise parameters *meas_noise1* and *meas_noise2*. They can be
used as dynamically reconfigurable measurement noise parameters.
However, we suggest to have the measurement noise included in the update
sensor's own information source (e.g. covariance estimate of the visual
odometry's PoseWithCovarianceStamped message).

### Calculating the Measurement Matrix and Residuals

This is the mos crucial part and varies from sensor type to sensor type.
Note that the same module can be used for a 6DoF Vicon information or
for the 6DoF pose information from [ethzasl_ptam](ethzasl_ptam). In the
former information source the "visual" scale estimate should - of
course - result in 1.0. However, attention must be paid to the
definition of the 6DoF pose the information source is providing.

To calculate the measurement matrix and residuals one generally tries to
express the measurements aid of the states. Please see the following
papers to get some insights to this:
[ pdf1 ](http://PhDThsis_ToAppear ),
[ pdf2](http://publications.asl.ethz.ch/files/weiss11real.pdf ),
[ pdf3](http://publications.asl.ethz.ch/files/weiss12realtime.pdf )

The code examples in *pose_sensor* and *position_sensor* already cover
the two most important *types* of sensors and may be adapted to your
needs.

### Designing the Initialization

The correct initialization of the states is crucial since EKF frameworks
may get stuck in local minima. We provide
[ here](http://PhDThsis_ToAppear ) a detailed overview on which states
are more sensitive to correct initializations. The most delicate state
is the position scaling factor (not more than 5% off the true value),
hence we suggest to provide this via dynamic reconfigure GUI upon filter
initialization. Using the first update sensor measurements together with
this scaling factors some other states can be calculated. The remaining
states are not very sensitive to correct initialization - an "eye
based" initial value may be sufficient.

## Node Information

```clearsilver
node.0{
  name = pose_sensor
  desc = example of a 6DoF pose sensor with scaled position measurement (e.g. [[ethzasl_ptam]])
  sub{
  0.name = pose_measurement
  0.type = geometry_msgs/PoseWithCovarianceStamped
  0.desc = the sensor's information source
  1.name = imu_state_input
  1.type = sensor_msgs/Imu
  1.desc = propagation sensor input for internal state propagation
  2.name = hl_state_input
  2.type = sensor_fusion_comm/ExtEkf
  2.desc = input from external state propagation (e.g. [[asctec_mav_framework]])
}
  pub{
  0.name = state_out
  0.type = sensor_fusion_comm/DoubleArrayStamped
  0.desc = all state information
  1.name = correction
  1.type = sensor_fusion_comm/ExtEkf
  1.desc = correction for external state propagation (e.g. [[asctec_mav_framework]])
  2.name = pose
  2.type = geometry_msgs/PoseWithCovarianceStamped
  2.desc = 6DoF pose for underlying pose controller (e.g. [[asctec_mav_framework]])
  3.name = ext_state
  3.type = sensor_fusion_comm/ExtState
  3.desc = 6DoF pose and velocity for underlying pose and velocity controller (e.g. [[asctec_mav_framework]])
}
param {
group.0{
      name = Static parameters
      desc = parameters that are statically set
0.name= ~init/q_ci/w
0.default= 1.0
0.desc= Initial value for the real part of the quaternion describing the rotation of the sensor (camera) w.r.t. the IMU, i.e. q_ci brings camera coordinates to IMU coordinates.
1.name= ~init/q_ci/x
1.default= 0.0
1.desc= see above, imaginary part x
2.name= ~init/q_ci/y
2.default= 0.0
2.desc= see above, imaginary part y
3.name= ~init/q_ci/z
3.default= 0.0
3.desc= see above, imaginary part z

4.name= ~init/p_ci/x
4.default= 0.0
4.desc= Initial value of the translation of the sensor (camera) w.r.t. the IMU, i.e. p_ci brings camera coordinates to IMU coordinates.
5.name= ~init/p_ci/y
5.default= 0.0
5.desc= y
6.name= ~init/p_ci/z
6.default= 0.0
6.desc= z

7.name= ~use_fixed_covariance
7.default= false
7.desc= selects if covariance reported by the sensor is used or if fixed values from the reconfigure guy from [[ssf_core]] should be taken (meas_noise1 for position, meas_noise2 for attitude)  
8.name= ~measurement_world_sensor
8.default= true
8.desc= selects if sensor measures its position w.r.t. world (true, e.g. Vicon) or the position of the world coordinate system w.r.t. the sensor (false, e.g. [[ethzasl_ptam]])

}
# End of autogenerated section. You may edit below.
}

}
node.1{
  name = position_sensor
  desc = example of a 3DoF position sensor with scaled position measurement
  sub{
  0.name = position_measurement
  0.type = ssf_updates/PositionWithCovarianceStamped
  0.desc = the sensor's information source
  1.name = imu_state_input
  1.type = sensor_msgs/Imu
  1.desc = propagation sensor input for internal state propagation
  2.name = hl_state_input
  2.type = sensor_fusion_comm/ExtEkf
  2.desc = input from external state propagation (e.g. [[asctec_mav_framework]])
}
  pub{
  0.name = state_out
  0.type = ssf_core/DoubleArrayStamped
  0.desc = all state information
  1.name = correction
  1.type = sensor_fusion_comm/ExtEkf
  1.desc = correction for external state propagation (e.g. [[asctec_mav_framework]])
  2.name = pose
  2.type = geometry_msgs/PoseWithCovarianceStamped
  2.desc = 6DoF pose for underlying pose controller (e.g. [[asctec_mav_framework]])
  3.name = ext_state
  3.type = sensor_fusion_comm/ExtState
  3.desc = 6DoF pose and velocity for underlying pose and velocity controller (e.g. [[asctec_mav_framework]])
}
}
```
