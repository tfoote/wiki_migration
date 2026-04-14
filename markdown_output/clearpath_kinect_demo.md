## Nodes

```clearsilver
node {
  no_header=True
  0 {
      name=ClearpathDemoExplore 
      desc= `ClearpathDemoExplore` is a ROS node that reads a frame from the Kinect PointCloud and generates a motion output that drives it towards empty space.
  }
}
```

```clearsilver
sub {
  0 {
    name= idfloor_in(~in)
    type= sensor_msgs/PointCloud2
    desc= Get the Kinect Point cloud as a pcl::PointCloud<pcl::PointXYZRGB>.
  }
}
pub {
  0 {
    name= idfloor_out(~out)
    type= sensor_msgs/PointCloud2
    desc= A pcl::PointCloud<pcl::PointXYZRGB> that can be used for visualization.
  }
  1 {
    name= idfloor_out_vel(~out_vel)
    type= geometry_msgs/Twist
    desc= Publish the commanded velocity.
  }
}
param{
    1 {
        name = ~in
        type = string
        default = `"idfloor_in"`
        desc = Name of the topic your XYZRGB Point Cloud is on.
    }
    2 {
        name = ~out
        type = string
        default = `"idfloor_out"`
        desc = Name of the topic your display XYZRGB Point Cloud is put out on.
    }
    3 {
        name = ~out_vel
        type = string
        default = `"idfloor_out_vel"`
        desc = Name of the topic your cmd_vel should go out on.
    }
    4 {
        name = ~angular_vel_correction
        type = double
        default = `1.0`
        desc = A gain applied to the commanded angular velocity during turns.
    }
    5 {
        name = ~lin_speed
        type = double
        default = `0.3`
        desc = The linear speed in m/s the robot should move during operation.
    }
    6 {
        name = ~ang_speed
        type = double
        default = `0.3`
        desc = The angular speed that the robot should moving during turns, rad/s.
    }
    7 {
        name = ~cam_height
        type = double
        default = `0.55`
        desc = The height of the Kinect from the ground
    }
    8 {
        name = ~cam_z_trans
        type = double
        default = `0.0`
        desc = Displacement of the camera from the center of the robot.
    }
    9 {
        name = ~wall_buffer
        type = double
        default = `0.6`
        desc = Amount of "buffer" to add to obstacles (treating the robot as a point)
    }
    10 {
        name = ~publish_visualization
        type = int
        default = `1`
        desc = A flag to turn on/off visualization publishing on the 'out' channel
    }
}
```

```clearsilver
node {
  no_header=True
  0 {
      name=ClearpathDemoTrack
      desc= `ClearpathDemoTrack` is a ROS node that reads a frame from the Kinect PointCloud and generates a motion output that drives it towards a tracked object (person).
  }
}
```

```clearsilver
sub {
  0 {
    name= idfloor_in(~in)
    type= sensor_msgs/PointCloud2
    desc= Get the Kinect Point cloud as a pcl::PointCloud<pcl::PointXYZRGB>.
  }
}
pub {
  0 {
    name= idfloor_out(~out)
    type= sensor_msgs/PointCloud2
    desc= A pcl::PointCloud<pcl::PointXYZRGB> that can be used for visualization.
  }
  1 {
    name= idfloor_out_vel(~out_vel)
    type= geometry_msgs/Twist
    desc= Publish the commanded velocity.
  }
}
param{
    1 {
        name = ~in
        type = string
        default = `"idfloor_in"`
        desc = Name of the topic your XYZRGB Point Cloud is on.
    }
    2 {
        name = ~out
        type = string
        default = `"idfloor_out"`
        desc = Name of the topic your display XYZRGB Point Cloud is put out on.
    }
    3 {
        name = ~out_vel
        type = string
        default = `"idfloor_out_vel"`
        desc = Name of the topic your cmd_vel should go out on.
    }
    4 {
        name = ~angular_vel_correction
        type = double
        default = `1.0`
        desc = A gain applied to the commanded angular velocity during turns.
    }
    5 {
        name = ~lin_speed
        type = double
        default = `0.3`
        desc = The linear speed in m/s the robot should move during operation.
    }
    6 {
        name = ~ang_speed
        type = double
        default = `0.3`
        desc = The angular speed that the robot should moving during turns, rad/s.
    }
    7 {
        name = ~cam_height
        type = double
        default = `0.55`
        desc = The height of the Kinect from the ground
    }
    8 {
        name = ~cam_z_trans
        type = double
        default = `0.0`
        desc = Displacement of the camera from the center of the robot.
    }
    9 {
        name = ~window_size
        type = double
        default = `0.5`
        desc = Distance in meters that is searched from the previous object location.
    }
    10 {
        name = ~publish_visualization
        type = int
        default = `1`
        desc = A flag to turn on/off visualization publishing on the 'out' channel
    }
}
```
