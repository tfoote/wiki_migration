## Caution: This package is an active development project

## Overview

Gazebo plugins to support simulation of Unmanned Surface Vehicles
(USVs).

## Available Plugins



```clearsilver
node.0 {
 name = usv_gazebo_dynamics_plugin
 desc = Generates hydrodynamic forces and torques for a twin-hull catamaran vessel with differential drive. 
 param {
  0.name = waterLevel
  0.type = double
  0.desc = Altitude of the water level used to calculate buoyancy forces.  Positive is up from Z=0.0.  [m]
  0.default = 0.5
  1.name = waterDensity
  1.type = double
  1.desc = Density of the fluid [kg/m^3]
  1.default = 997.8
  2.name = xDotU
  2.type = double
  2.desc = Added mass in the surge direction. [kg]
  2.default = 5.0
  3.name = xDotV
  3.type = double
  3.desc = Added mass in the sway direction. [kg]
  3.default = 5.0
  4.name = nDotR
  4.type = double
  4.desc = Added mass in the yaw direction. [kg m^2]
  4.default = 1.0
  5.name = xU
  5.type = double
  5.desc = Linear drag in the surge direction [N/(m/s)]
  5.default = 20.0
  6.name = xUU
  6.type = double
  6.desc = Quadratic drag in the surge direction [N/(m/s)^2]
  6.default = 0.0
  7.name = yV
  7.type = double
  7.desc = Linear drag in the sway direction [N/(m/s)]
  7.default = 20.0
  8.name = yVV
  8.type = double
  8.desc = Quadratic drag in the sway direction [N/(m/s)^2]
  8.default = 0.0
  9.name = zW
  9.type = double
  9.desc = Linear drag in the heave direction [N/(m/s)]
  9.default = 20.0
  10.name = kP
  10.type = double
  10.desc = Linear drag in the pitch direction [Nm/(rad/s)] 
  10.default = 20.0
  11.name = mQ
  11.type = double
  11.desc = Linear drag in the roll direction [Nm/(rad/s)] 
  11.default = 20.0
  12.name = nR
  12.type = double
  12.desc = Linear drag in the yaw direction [Nm/(rad/s)] 
  12.default = 20.0
  13.name = nRR
  13.type = double
  13.desc = Quadratic drag in the yaw direction [Nm/(rad/s)^2] 
  13.default = 20.0
  14.name = maxCmd
  14.type = double
  14.desc = Assumes that the Drive message (see [[http://wiki.ros.org/kingfisher_msgs]]) is +/-F, where F is the maxCmd.
  14.default = 1.0
  15.name = maxForceFwd
  15.type = double
  15.desc = Maximum forward force for a in the +x thruster [N]
  15.default = 100.0
  16.name = maxForceRev
  16.type = double
  16.desc = Maximum forward force for a in the -x thruster [N]
  16.default = -100.0
  17.name = boatArea
  17.type = double
  17.desc = Horizontal surface area of the boat.  Assumed to be constant with draft and used for buoyancy calculation [m^2]
  17.default = 0.48
  18.name = boatWidth
  18.type = double
  18.desc = Width between the thrusters on the vessel - used for calculating the applied torque [m]
  18.default = 1.0
  19.name = boatLength
  19.type = double
  19.desc = Length of the vessel.  The thrust is applied at the rear of the vessel by taking half of the boat length [m]
  19.default = 1.35
  20.name = thrustOffsetZ
  20.type = double
  20.desc = Offset in the Z direction, relative to CG, for applying the thrust.  Causes thrust to couple with pitch and roll [m].
  20.default = -0.01
  21.name = metacentricLength
  21.type = double
  21.desc = Longitudinal (along x-axis) metacentric height [m].  Results in a stabilizing righting moment in the pitch direction and dictates the natural frequency in pitch.
  21.default = 0.4
  22.name = metcentricWidth
  22.type = double
  22.desc = Transverse (along y-axis) metacentric height [m].  Results in a stabilizing righting moment in the roll direction and dictates the natural frequency in roll.
  22.default = 0.4
```



## Xacro Files

The included `urdf/usv_gazebo_dynamics_plugin.xacro` file sets all of
the parameters for the plugin, intended as a example for customization.

## Examples

-   [ Gazebo Simulation of Kingfisher/Heron USV](https://wiki.nps.edu/pages/viewpage.action?pageId=818282511 )
    Simplest example of using the USV dynamics plugin in an empty Gazebo
    world.
