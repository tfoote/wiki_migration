# Algorithm

RF2O is a fast and precise method to estimate the planar motion of a
lidar from consecutive range scans. For every scanned point we formulate
the range flow constraint equation in terms of the sensor velocity, and
minimize a robust function of the resulting geometric constraints to
obtain the motion estimate. Conversely to traditional approaches, this
method does not search for correspondences but performs dense scan
alignment based on the scan gradients, in the fashion of dense 3D visual
odometry. The minimization problem is solved in a coarse-to-fine scheme
to cope with large displacements, and a smooth filter based on the
covariance of the estimate is employed to handle uncertainty in
unconstraint scenarios (e.g. corridors).

The user is advised to check the related papers
([see here](http://mapir.isa.uma.es/mapirwebsite/index.php/mapir-downloads/papers/217))
for a more detailed description of the method.

# Demo Video

[Youtube](https://www.youtube.com/watch?v=eGDoVk93otY)

# Nodes



```clearsilver
 name = rf2o_laser_odometry
 desc = The `rf2o_laser_odometry` node publishes planar odometry estimations for a mobile robot from scan lasers of an onboard 2D lidar. It initially estimates the odometry of the lidar device, and then calculates the robot base odometry by using `tf` transforms.

sub {
  0.name = laser_scan
  0.type = sensor_msgs/LaserScan
  0.desc = Laser scans to process. (This topic can be remapped via the ~laser_scan_topic parameter)
}

sub {
  1.name = tf
  1.type = tf/tfMessage
  1.desc = Transforms
}

pub {
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = Odometry estimations as a ROS topic. (This topic can be remapped via the ~odom_frame_id parameter)
}

pub {
  1.name = tf
  1.type = tf/tfMessage
  1.desc = Publishes the transform from the \base_link (which can be remapped via the ~base_frame_id parameter) to \odom (which can be remapped via the ~odom_frame_id parameter).
}

param {
  0.name = ~laser_scan_topic
  0.type = string
  0.default = /laser_scan
  0.desc = Topic name where lidar scans are being published.  
}

param {
  1.name = ~base_frame_id
  1.type = string
  1.default = /base_link
  1.desc = TF frame name of the mobile robot base. A `tf` transform from the `laser_frame` to the `base_frame` should exist. 
}

param {
  2.name = ~odom_frame_id
  2.type = string
  2.default = /odom
  2.desc = TF frame name for published odometry estimations. This same parameter is used to publish odometry as a topic.
}

param {
  3.name = ~freq
  3.type = double
  3.default = 10.0
  3.desc = Odometry publication rate (Hz).  
}
```


