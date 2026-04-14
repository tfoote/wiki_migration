## Overview

dlut_pc_odom is a package used for receive laser data from hokuyo,then
process these data and publish pointcloud2 message.

## Usage

Node \"dlut_pc_odom\" can be started by running:
```shell
rosrun dlut_pc_odom dlut_pc_odom
```

## Nodes

```clearsilver
node.0 {
name = dlut_pc_odom
desc = The serial_com node is a base controller node.It must run on a computer attached directly to the motor controller by serial port.

sub {
0{
name = scan
type = sensor_msgs/LaserScan
desc = the laser messages form hokuyo.
}
1{
name = is_run_pch
type = std_msgs/Bool
desc = Subscribe the message whether the holder begin to rotate or not.
}
2{
name = motor_param
type = dlut_motor_hokuyo/motor
desc = Subscribe the param of motor.
}
3{
name = odom
type = nav_msgs/Odometry
desc = Get the odometry value.
}
}
pub {
0{
name = hokuyo_point_cloud2
type = pcl/PointCloud<PointType>
desc = pointcloud2 data.
}
}
param {
0.name = is_first_flag_
0.type = bool
0.desc = Whether the first data after the sick rotated.
0.default = false
1.name = is_first_circle_
1.type = bool
1.desc = Whether the data is belong to the first circle.
1.default = false
}
}
```

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.
