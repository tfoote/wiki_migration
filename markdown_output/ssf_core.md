## Overview

The single sensor fusion (ssf) part of this stack is divided into the
common Kalman Filter steps *prediction* (or propagation) and *update*
(or measurement). We assume to always have an IMU as propagation sensor
on the vehicle while we can change the update sensors depending on the
users preferences. Hence, the propagation part remains unchanged for
different update sensors. Essentially, for every different update sensor
only the measurement matrix, and the calculation of the residuals
change - the rest of the filter framework remains the same. This
constant, core, part is incorporated in this package
[ ssf_core](../ssf_core )

## Nodes

This package only creates a library used by the
[ ssf_updates](../ssf_updates ) for the different update sensors.

## EKF Core Framework

The idea of having a core framework is to have have all fix parts of an
EKF filter encapsulated in one library. Since we assume to always have
an IMU as core (propagation) sensor we can incorporate the entire EKF
propagation steps in the core framework. This leaves only the
measurements as variable parts. More precisely, only the calculation of
the measurement matrix and the residuals vary between the different
measurement sensor *types*. Their handling is again fix and is
incorporated in this package.

### States

With this framework we aim at a (a) pose estimator (b) for
power-on-and-go systems (c) used in long-term missions.

This requires several states to be estimated: a. position, attitude and
velocity for an underlying pose and velocity controller. For MAV
navigation, we suggest to use
[asctec_mav_framework](asctec_mav_framework) on an
[ AscTec](http://www.asctec.de ) multi-copter with
[ethzasl_ptam](ethzasl_ptam) as update sensor for accurate pose control.

a\. pose and velocity are corrupted by sensor misalignment and biases.
To avoid tedious calibration procedure before each mission on each
vehicle, we estimate these intra- and inter-sensor calibration states.
That is: the acceleration and gyroscope biases as well as the
transformation between an update sensor and the IMU are estimated online
during the mission. This renders the vehicle truly power-on-and-go.

a\. pose and velocity are also corrupted by the drift of a non-global
update sensor (e.g. [ethzasl_ptam](ethzasl_ptam) using a camera). A
misalignment to gravity due to attitude drift of such a sensor results
in fatal consequences for airborne vehicles. Also - if a monocular
update sensor is used - drift in the scaling of the update sensor leads
the underlying position controller to instability. Because of these
issues we estimate these states online during the mission. More
precisely this is the (visual) scaling factor and the update sensor
drift in roll and pitch with respect to the navigation frame. This
ensures metric scaled and gravity aligned position and velocity in
long-term missions.

### Prediction: Internal and External

The computationally costly part in the prediction is the quaternion
integration. Position and velocity are propagated using first order
integration. On the remaining states we apply zero order holds since we
assume zero mean Gaussian white noise as process noises.

The [ ssf_core](../ssf_core ) package has a built-in propagation
procedure. However, you may also use an external state propagation as
provided in the [asctec_mav_framework](asctec_mav_framework):

-   imuCallback() with the *sensor_msg::Imu* message invokes the
    internal state propagation
-   stateCallback() with the custom *ssf_core::ext_ekf* message uses the
    external state propagation. You can still force the internal state
    propagation by setting the fix parameter *data_playback=True*.

### Setting the Noise Values

**Generally the noise values accessible in the dynamic reconfigure GUI
should not be tuning parameters.** Please check the acceleration and
gyroscope noises and their bias noises in the manufacturer's data sheet
of your IMU. Furthermore the noise values of the remaining states should
be kept to zero since they are not temporally drifting. Instead, if you
work with a keyframe based visual odomtery as update sensor you may add
uncertainty to the visual scale and visual drift the moment a new
keyframe is created. This reflects the *spatial* nature of these
state's uncertainty.

### EKF Update

This package only contains the EKF prediction step, a shell for the EKF
update procedure and the error detection described in
[ this paper](http://publications.asl.ethz.ch/files/weiss11real.pdf ).
The actual calculations for the update matrix and residuals are done in
a module of the [ ssf_updates](../ssf_updates ) package.

## Using This Package

Apart of setting the correct noise values, the user should not need to
modify this package since it only contains the core consisting of the
propagation using IMU data and the shell for the EKF update. All update
sensor specific calculations are done in
[ ssf_updates](../ssf_updates ).

## Scripts

There are several scripts to plot the different states.
*plot_\[states\] T* plots the states \[states\] in an rxgraph with a
time history of T seconds (without T the default time history is used).

## Node Information

```clearsilver
node.0{
  name = ssf_core
  desc = main framework for single sensor fusion: library used by [[../ssf_updates | ssf_updates]].

# Autogenerated param section. Do not hand edit.
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~init_filter
0.default= False
0.type= bool
0.desc=call filter init using defined scale 
1.name= ~scale_init
1.default= 1.0
1.type= double
1.desc=value for initial scale Range: 0.001 to 30.0
2.name= ~fixed_scale
2.default= False
2.type= bool
2.desc=fix scale 
3.name= ~fixed_bias
3.default= False
3.type= bool
3.desc=fix biases 
4.name= ~fixed_calib
4.default= False
4.type= bool
4.desc=fix calibration states 
5.name= ~noise_acc
5.default= 0.0083
5.type= double
5.desc=noise accelerations (std. dev) Range: 0.0001 to 0.5
6.name= ~noise_accbias
6.default= 0.00083
6.type= double
6.desc=noise acceleration bias  (std. dev) Range: 1e-07 to 0.1
7.name= ~noise_gyr
7.default= 0.0013
7.type= double
7.desc=noise gyros (std. dev) Range: 0.0001 to 0.5
8.name= ~noise_gyrbias
8.default= 0.00013
8.type= double
8.desc=noise gyro biases  (std. dev) Range: 1e-07 to 0.1
9.name= ~noise_scale
9.default= 0.0
9.type= double
9.desc=noise scale (std. dev) Range: 0.0 to 10.0
10.name= ~noise_qwv
10.default= 0.0
10.type= double
10.desc=noise qwv (std. dev) Range: 0.0 to 10.0
11.name= ~noise_qci
11.default= 0.0
11.type= double
11.desc=noise qci (std. dev) Range: 0.0 to 10.0
12.name= ~noise_pic
12.default= 0.0
12.type= double
12.desc=noise pic (std. dev) Range: 0.0 to 10.0
13.name= ~delay
13.default= 0.03
13.type= double
13.desc=fix delay in seconds Range: -2.0 to 2.0
14.name= ~set_height
14.default= False
14.type= bool
14.desc=call filter init using defined height 
15.name= ~height
15.default= 1.0
15.type= double
15.desc=height in m for init Range: 0.1 to 20.0
16.name= ~meas_noise1
16.default= 0.01
16.type= double
16.desc=noise for measurement sensor (std. dev) Range: 0.0 to 10.0
17.name= ~meas_noise2
17.default= 0.01
17.type= double
17.desc=noise for measurement sensor (std. dev) Range: 0.0 to 10.0
}
group.1{
      name = Static parameters
      desc = parameters that are statically set
0.name= ~data_playback
0.default= False
0.desc= Flag to force internal state propagation even though the custom message ssf_core::ext_ekf is used as propagation sensor input
}
# End of autogenerated section. You may edit below.
```
