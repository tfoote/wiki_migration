## Introduction

Light Detection and Ranging, or LiDAR, depends on data from one or more
laser range finders. While some laser range finders are now available
that create 3D scans, such as the Velodyne Puck, there are still gaps in
the data, and 2D laser range finders provide even less data. By
connecting a 2D sensor to a servo, the amount of data acquired can be
significantly increased and improve the robot's perception of its
environment. This package includes the code to operate such a setup and
generates a point cloud that then be visualized in rviz or used to
create an OctoMap.

## Hardware

The hardware used for developing this package were based on the setup
detailed in this
[capstone report](https://github.com/gcc-robotics/3d_photobooth/blob/master/CapstoneFinalReport_VisionTeam.pdf)
from Glendale Community College.

-   UTM-30LX Hokuyo 2D laser scanner
-   MX-28 Dynamixel servo
-   Power adaptor and USB serial for servo
-   custom designed, 3D printed gimbal and mount

While this code is specifically designed to operate with the Hokuyo
laser and Dynamixel servo, any laser range finder and servo that provide
identical or similar data could be used with the proper modification of
the code. The part files for the gimbal and mount used in this project
are currently unavailable, but the original gimbal used in the capstone
report can be found
[here](https://grabcad.com/library/hokuyo-utm-30lx-lidar-to-dynamixel-servo-gimbal-2-1).

## Tutorial

This example walks through using this package and corresponding hardware
for the first time. For additional information on the code, please see
Nodes section below.

1\. ```
sudo apt-get install ros-indigo-spin-hokuyo
``` 1. In the tutorials/launch folder, update
the dynamixel_servos.yaml file to match the information for your servo.
In particular, make sure the id number matches that of your servo. 1. In
the tutorials/launch folder, update the basic_motors.launch file, go to
line 12. These parameters are used to set up the dynamixel_motor
package. In particular, make sure the port_name and baud_rate match your
servo. Also, check that your motor id falls within the inclusive range
from min_motor_id to max_motor_id. 1. Save and compile changes (if
applicable). 1. ```
roslaunch spin_hokuyo basic_motors.launch
``` 1. In a new terminal, open the
rostopics list. There should be two new commands:
/tilt_controller/command and /tilt_controller/state. /command will issue
new positions to the motor via Float64 (try this using rostopic pub).
/state will list various pieces of information about the motor (rostopic
echo). 1. If this is fully functional, kill the node and run the
following command. This should cause the motor to regularly sweep from
90 to -90 and generate a point cloud and occupancy map. Be sure to
update the dynamixel_servos_tilting.yaml for position, speed, etc. 1.
```
roslaunch spin_hokuyo tilting_lidar_continuous.launch
```

## Nodes

```clearsilver
node.0{
name = tilt_motor
desc = Controls the motion of the servo, causing it to continuously sweep from -90 to +90 to -90.
sub {
  0.name = tilt_controller/state
  0.type = dynamixel_msgs/JointState
  0.desc = provides information on the position of the servo 
}
pub {
  0.name = tilt_controller/command
  0.type = std_msgs/Float64
  0.desc = tells servo new position (in radians) to move to

  1.name = time/start_time
  1.type = std_msgs/Time
  1.desc = time that the servo begins a sweep

  2.name = time/end_time
  2.type = std_msgs/Time
  2.desc = time that servo ends a sweep
}
param {
  0.name = ~maximum
  0.type = integer
  0.desc = maximum angle, in degrees, servo can turn to
  0.default = 92

  1.name = ~minimum
  1.type = integer
  1.desc = minimum angle, in degrees, servo can turn to
  1.default = -92

  2.name = ~pause
  2.type = float
  2.desc = pause time between sending new commands to the servo, prevents grinding
  2.default = 0.1
}
}

node.1{
name = tilt_motor_subscriber
desc = Controls the motion of the servo, causing it to sweep from -90 to +90 to -90 when sent an empty message.
sub {
  0.name = tilt_controller/state
  0.type = dynamixel_msgs/JointState
  0.desc = provides information on the position of the servo 

  1.name = perform_sweep
  1.type = std_msgs/Empty
  1.desc = initializes a sweep
}
pub {
  0.name = tilt_controller/command
  0.type = std_msgs/Float64
  0.desc = tells servo new position (in radians) to move to

  1.name = time/start_time
  1.type = std_msgs/Time
  1.desc = time that the servo begins a sweep

  2.name = time/end_time
  2.type = std_msgs/Time
  2.desc = time that servo ends a sweep
}
param {
  0.name = ~maximum
  0.type = integer
  0.desc = maximum angle, in degrees, servo can turn to
  0.default = 92

  1.name = ~minimum
  1.type = integer
  1.desc = minimum angle, in degrees, servo can turn to
  1.default = -92

  2.name = ~pause
  2.type = float
  2.desc = pause time between sending new commands to the servo, prevents grinding
  2.default = 0.1
}
}

node.2{
name = tilt_transform
desc = Publishes the transforms between the laser scan and the servo.
sub {
  0.name = tilt_controller/State
  0.type = dynamixel_msgs/JointState
  0.desc = provides information on the position of the servo 
}
prov_tf {
  0.from = servo
  0.to   = laser
  0.desc = Aligns the laser scan in accordance with the angle of the servo at the time of the scan
}
}

node.3{
name = hokuyo_robot_filter
desc = Along with slightly limiting the angle of the Hokuyo, removes the robot from the scan data
sub {
  0.name = scan
  0.type = sensor_msgs/LaserScan
  0.desc = scan data collected by the Hokuyo
}
pub {
  0.name = hokuyo_filtered
  0.type = sensor_msgs/LaserScan
  0.desc = scan data with points corresponding to robot removed
}
}

node.4{
name = scan_to_pcl
desc = Converts Hokuyo laser scan data to point cloud
sub {
  0.name = hokuyo_filtered
  0.type = sensor_msgs/LaserScan
  0.desc = scan data with points corresponding to robot removed
}
pub {
  0.name = hokuyo_points
  0.type = PointCloud
  0.desc = Hokuyo data without robot converted to point cloud
}
}

node.5{
name = pcl_assembler_client
desc = makes the service call to compile all transformed point clouds into one point cloud
sub {
  0.name = time/start_time
  0.type = std_msgs/Time
  0.desc = time that the servo begins a sweep

  1.name = time/end_time
  1.type = std_msgs/Time
  1.desc = time that the servo ends a sweep
}
pub {
  0.name = assembled_cloud
  0.type = std_msgs/PointCloud2
  0.desc = compiled cloud of all points from a single sweep
}
srv_called {
  0.name = assemble_scans2
  0.type = laser_assembler/AssembleScans2
  0.desc = When an assembler receives an assemble_scans request, it searches its rolling buffer for clouds that occur in the requested interval (begin to end). These clouds are then assembled into a larger cloud, in the frame specified by the ~fixed_frame parameter, and sent to to the caller in the service response. This is a non-blocking operation and will return an empty cloud if no scans are received in the requested interval. The resulting cloud will have channels named intensities, index, distances, and stamps as defined by the laser_geometry::LaserProjection library. It returns a sensor_msgs/PointCloud2.
}
param {
  0.name = ~assembled_cloud_mode
  0.type = string
  0.desc = sets node to either subscriber or time and causes node to either subscribe to specific sweep start and end times or compiles all scans in a particular amount of time
  0.default = subscriber

  1.name = ~scan_time
  1.type = double
  1.desc = time interval from which scans are obtained to compile
  1.default = 5
}
}
```

## Acknowledgements

This package was created as part of the Pinnacle Scholar program at
Stevens Institute of Technology in the Robust Field Autonomy Laboratory.
We would like to thank Prof. Brendan Englot and PhD students Shi Bai and
Tixiao Shan for their assistance.
