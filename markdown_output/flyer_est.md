## ROS API

```clearsilver
name=estimator
desc=Node for producing state estimates from observed measurements. Position/attitude are essentially passed-through from the source data (i.e. Vicon measurements) and linear/angular velocity are simply derived by finite differencing with filtering.

pub{
0.name=~output
0.type=nav_msgs/Odometry
0.desc=State (position, orientation, linear velocity and angular velocity) estimate of the vehicle (`/<vehiclename>/flyer_imu` frame, expressed in `/ned` frame).

}
sub{
0.name=`<transform_topic>`
0.type=geometry_msgs/TransformStamped
0.desc=Input data from Vicon (vicon_mocap/vicon_recv_direct). Actual topic name is specified by the `~transform_topic` parameter.

}

param {
group.0 {
0.name= ~transform_topic
0.default= `"vicon_recv_direct/output"`
0.type= str
0.desc= Topic to listen to for Vicon output.

1.name= ~freq
1.default= `50`
1.type= int
1.desc= Rate in Hz at which to publish state estimates.

2.name= ~xy_vel_filt_a
2.default= 0.9
2.type= float
2.desc= Coefficient for linear velocity filter (x and y components).

3.name= ~xy_vel_filt_b
3.default= 0.1
3.type= float
3.desc= Coefficient for linear velocity filter (x and y components).

4.name= ~z_vel_filt_a
4.default= 0.9
4.type= float
4.desc= Coefficient for linear velocity filter (z component).

5.name= ~z_vel_filt_b
5.default= 0.1
5.type= float
5.desc= Coefficient for linear velocity filter (z component).

6.name= ~ang_vel_filt_a
6.default= 0.9
6.type= float
6.desc= Coefficient for angular velocity filter.

7.name= ~ang_vel_filt_b
7.default= 0.1
7.type= float
7.desc= Coefficient for angular velocity filter.
}
}
req_tf {
  0.from = `/<vehiclename>/flyer_vicon`
  0.to   = `/<vehiclename>/flyer_imu`
  0.desc = Transform from vehicle's Vicon frame (segment) to flyer_imu frame. The flyer_imu frame should be at the center of the vehicle, in the plane of the IMU, with X pointing towards the forward (orange tape) prop, Y pointing starboard and Z pointing down. This transform is only looked up once at startup time and then subsequently used to transform incoming Vicon data on the vehicle's pose (which is expected to be /enu -> /<vehiclename>/flyer_vicon) to a preferable transform (/ned -> /<vehiclename>/flyer_imu).
}
```
