## Documentation

Note that the node for teleoperation (gamepad control) of Nao is now in
its own package at [nao_teleop](nao_teleop).

### Visualization in RViz

![](attachment:nao_rviz.png)

When the remote nodes for Nao are up and running, you can visualize the
following topics in [rviz](rviz) (set fixed and target frame to /odom):

-   **Robot Model**: Basic visualization of Nao\'s joint state (from
    [nao_description](nao_description) through
    [robot_state_publisher](robot_state_publisher)), topic
    \"robot_description\"
-   **TF**: full transforms to all joints and cameras (from
    [nao_description](nao_description) through
    [robot_state_publisher](robot_state_publisher))
-   **Odometry**: topic \"/odom\"

## Nodes

```clearsilver
node.0 {
 name = remap_odometry
 desc = Creates proper ROS odometry from the RAW odometry originating from Nao
 sub{
  0.name = torso_odometry
  0.type = nao_ctrl/TorsoOdometry
  0.desc = Basic odometry of Nao's torso
  1.name = torso_imu
  1.type = nao_ctrl/TorsoIMU
  1.desc = Data from Nao's internal IMU
 }
 pub{
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = ROS style odometry (only the Pose is set at the moment)
 }
param {
  0.name = ~odom_frame_id
  0.type = String
  0.desc = tf Frame ID of odometry frame
  0.default = odom

  1.name = ~base_frame_id
  1.type = String
  1.desc = tf Frame ID of Nao's base (torso) link
  1.default = base_link

  2.name = ~use_imu_angles
  2.type = bool
  2.desc = If true, roll and pitch of the odometry pose will be continuously copied from the IMU
  2.default = false

  3.name = ~init_from_imu
  3.type = bool
  3.desc = If true, roll and pitch of the odometry pose will be initialized using the IMU angles during initialization and when `resume_odometry` service is called
  3.default = false

  4.name = ~init_from_odometry
  4.type = bool
  4.desc = If true, roll and pitch of the odometry pose will be initialized using the kinematic chain during initialization and when `resume_odometry` service is called
  4.default = false

  5.name = ~imu_topic
  5.type = String
  5.desc = Topic name of IMU messages to be used when `use_imu_angles`, `init_from_imu` or `reset_orientation_after_resume` is true
  5.default = torso_imu
}

prov_tf {
  0.from = odom
  0.to   = base_link
  0.desc = Odometry transform from odom frame to Nao's torso. The name of the frames can be adjusted with the parameters above.
  1.from = base_link
  1.to   = base_footprint
  1.desc = Computed footprint of the robot on the ground (z=0). This pose is always between the two feet with the orientation (yaw) of the torso.
}

req_tf {
  0.from = base_link
  0.to   = {L,R}Foot_link
  0.desc = Requires the transforms to the feet (from robot_state_publisher) to compute the base_footprint frame
}
}

node.1 {
 name = pose_manager
 desc = Creates whole-body poses and motions from joint trajectories stored on the param server
 sub{
 }
 pub{
 }
}
```
